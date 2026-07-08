const API_URL = 'https://grid-removed-toolbar-railroad.trycloudflare.com/api/v1';
let accessToken = null;

/* =========================================
   UI Controllers (Toasts & Modals)
========================================= */
function showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    
    // Konfigurasi warna berdasarkan tipe
    const bgColors = {
        success: 'bg-emerald-600',
        error: 'bg-red-600',
        info: 'bg-blue-600'
    };
    const icon = type === 'success' ? 'fa-check' : (type === 'error' ? 'fa-triangle-exclamation' : 'fa-info');

    toast.className = `${bgColors[type]} text-white px-5 py-3 rounded-lg shadow-lg flex items-center gap-3 fade-in`;
    toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${message}</span>`;
    
    container.appendChild(toast);
    
    // Hapus otomatis setelah 3 detik
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function formatBytes(bytes, decimals = 2) {
    if (!+bytes) return '0 Bytes';
    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`;
}

/* =========================================
   Authentication Module
========================================= */
async function authenticate() {
    const input = document.getElementById('apiTokenInput').value;
    const statusEl = document.getElementById('authStatus');
    
    if (!input) {
        statusEl.innerText = "Token cannot be empty.";
        statusEl.classList.remove('hidden');
        return;
    }

    // Uji koneksi ping ke server untuk memvalidasi token
    try {
        const response = await fetch(`${API_URL}/files`, {
            headers: { 'x-api-key': input }
        });

        if (response.status === 401) {
            statusEl.innerText = "Invalid Access Token. Connection Refused.";
            statusEl.classList.remove('hidden');
            return;
        }

        // Token Valid, Transisi UI
        accessToken = input;
        document.getElementById('authModal').classList.add('hidden');
        const main = document.getElementById('mainDashboard');
        main.classList.remove('opacity-0', 'pointer-events-none');
        
        showToast('Connection established successfully', 'success');
        fetchDirectoryData();
    } catch (error) {
        statusEl.innerText = "Network error. Server might be down.";
        statusEl.classList.remove('hidden');
    }
}

function logout() {
    accessToken = null;
    document.getElementById('apiTokenInput').value = '';
    document.getElementById('mainDashboard').classList.add('opacity-0', 'pointer-events-none');
    document.getElementById('authModal').classList.remove('hidden');
    showToast('Disconnected from server', 'info');
}

/* =========================================
   Data Fetching & Rendering
========================================= */
async function fetchDirectoryData() {
    if (!accessToken) return;

    try {
        const response = await fetch(`${API_URL}/files`, {
            headers: { 'x-api-key': accessToken }
        });
        
        const result = await response.json();
        const tbody = document.getElementById('fileTableBody');
        tbody.innerHTML = ''; 

        if (result.data.length === 0) {
            tbody.innerHTML = `<tr><td colspan="4" class="px-6 py-8 text-center text-slate-500">Directory is empty. Upload files to begin.</td></tr>`;
            document.getElementById('statTotalFiles').innerText = "0";
            document.getElementById('statTotalSize').innerText = "0 B";
            return;
        }

        let totalSizeBytes = 0;

        result.data.forEach(file => {
            totalSizeBytes += file.size;
            
            // Render Ekstensi Ikon
            const ext = file.filename.split('.').pop().toLowerCase();
            let icon = 'fa-file';
            if (['jpg', 'jpeg', 'png', 'gif'].includes(ext)) icon = 'fa-file-image text-blue-500';
            else if (['pdf'].includes(ext)) icon = 'fa-file-pdf text-red-500';
            else if (['txt', 'md'].includes(ext)) icon = 'fa-file-lines text-slate-500';
            else if (['zip', 'rar'].includes(ext)) icon = 'fa-file-zipper text-amber-500';

            const tr = document.createElement('tr');
            tr.className = "hover:bg-slate-50 transition-colors group";
            tr.innerHTML = `
                <td class="px-6 py-4 flex items-center gap-3">
                    <i class="fa-solid ${icon} text-xl w-6 text-center"></i>
                    <span class="font-medium text-slate-700">${file.filename}</span>
                </td>
                <td class="px-6 py-4 text-slate-500 text-sm">${formatBytes(file.size)}</td>
                <td class="px-6 py-4 text-slate-500 text-sm">${new Date(file.uploaded_at).toLocaleString('en-US', { hour12: false })}</td>
                <td class="px-6 py-4 text-right">
                    <div class="flex justify-end gap-2">
                        <button onclick="downloadFile(${file.id}, '${file.filename}')" class="p-2 text-blue-600 hover:bg-blue-100 rounded-md transition-colors" title="Download">
                            <i class="fa-solid fa-download"></i>
                       </button>
                       <button onclick="deleteFile(${file.id})" class="p-2 text-red-600 hover:bg-red-100 rounded-md transition-colors" title="Delete">
                            <i class="fa-solid fa-trash-can"></i>
                      </button>
                  </div>
                </td>
            `;
            tbody.appendChild(tr);
        });

        // Update Dashboard Metrics
        document.getElementById('statTotalFiles').innerText = result.data.length;
        document.getElementById('statTotalSize').innerText = formatBytes(totalSizeBytes);

    } catch (error) {
        showToast('Failed to retrieve directory data', 'error');
    }
}

/* =========================================
   Upload Controllers (Drag & Drop + Input)
========================================= */
const dropZone = document.getElementById('dropZone');

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('bg-blue-100', 'border-blue-500');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('bg-blue-100', 'border-blue-500');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('bg-blue-100', 'border-blue-500');
    if (e.dataTransfer.files.length) {
        processUpload(e.dataTransfer.files[0]);
    }
});

function handleFileSelect(event) {
    if (event.target.files.length) {
        processUpload(event.target.files[0]);
    }
}

async function processUpload(file) {
    if (!accessToken) return;

    const formData = new FormData();
    formData.append('file_cloud', file);

    showToast(`Uploading ${file.name}...`, 'info');

    try {
        const response = await fetch(`${API_URL}/upload`, {
            method: 'POST',
            headers: { 'x-api-key': accessToken },
            body: formData
        });
        
        if (response.status === 401) return logout();
        
        const result = await response.json();
        
        if (result.success) {
            showToast('File uploaded successfully', 'success');
            document.getElementById('fileUploadInput').value = ''; 
            fetchDirectoryData(); 
        }
    } catch (error) {
        showToast('Network error during upload', 'error');
    }
}

/* =========================================
   File Operations (Download & Delete)
========================================= */
async function deleteFile(id) {
    if (!confirm('Are you sure you want to permanently delete this file?')) return;

    try {
        const response = await fetch(`${API_URL}/files/${id}`, { 
            method: 'DELETE',
            headers: { 'x-api-key': accessToken }
        });
        
        if (response.status === 401) return logout();
        
        showToast('File deleted', 'success');
        fetchDirectoryData();
    } catch (error) {
        showToast('Failed to delete file', 'error');
    }
}

async function downloadFile(id, filename) {
    showToast(`Preparing download for ${filename}...`, 'info');
    try {
        const response = await fetch(`${API_URL}/files/download/${id}`, {
            headers: { 'x-api-key': accessToken }
        });
        
        if (response.status === 401) return logout();

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
    } catch (error) {
        showToast('Download failed', 'error');
    }
}

