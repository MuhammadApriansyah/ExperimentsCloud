const express = require('express');
const cors = require('cors');
const apiRoutes = require('./routes/api');
const verifikasiPIN = require('./middleware/auth'); // Memanggil Sang Penjaga

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

// Menyuruh server melayani folder 'public' sebagai tampilan web utama (Lobi)
app.use(express.static('public'));

// FITUR BARU: Memasang gembok pada semua rute API
// Hanya orang yang lolos verifikasiPIN yang bisa mengakses rute di dalamnya
app.use('/api/v1', verifikasiPIN, apiRoutes);

app.get('/health', (req, res) => {
    res.json({ status: "Sehat", pesan: "Mesin brankas berjalan optimal." });
});

app.listen(PORT, () => {
    console.log(`🚀 Production Server berjalan dengan keamanan gembok di port ${PORT}`);
});

