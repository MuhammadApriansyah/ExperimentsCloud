const FileModel = require('../models/fileModel');
const fs = require('fs');
const path = require('path');

const fileController = {
    // 1. Fitur Read: Menampilkan Dashboard
    getDashboardData: (req, res) => {
        FileModel.getAll((err, rows) => {
            if (err) return res.status(500).json({ success: false, error: err.message });
            res.json({
                success: true,
                architecture: "Clean Layered Architecture",
                total_files: rows.length,
                data: rows
            });
        });
    },

    // 2. Fitur Create: Menangani Upload
    uploadSingleFile: (req, res) => {
        if (!req.file) {
            return res.status(400).json({ success: false, message: "Tidak ada file yang diunggah" });
        }

        const { originalname, path: filePath, size } = req.file;

        FileModel.create(originalname, filePath, size, (err, lastId) => {
            if (err) return res.status(500).json({ success: false, error: err.message });

            res.status(201).json({
                success: true,
                message: "File berhasil disimpan di Cloud Pribadi!",
                file_info: {
                    id: lastId,
                    filename: originalname,
                    storage_path: filePath,
                    size_bytes: size
                }
            });
        });
    },

    // 3. Fitur Read Stream: Menangani Download
    downloadFile: (req, res) => {
        const fileId = req.params.id;

        FileModel.getById(fileId, (err, row) => {
            if (err) return res.status(500).json({ success: false, error: err.message });
            if (!row) return res.status(404).json({ success: false, message: "File tidak ditemukan di database" });

            const absolutePath = path.resolve(row.filepath);

            if (!fs.existsSync(absolutePath)) {
                return res.status(404).json({ success: false, message: "File fisik hilang dari storage" });
            }

            res.download(absolutePath, row.filename);
        });
    },

    // FITUR BARU: Menghapus file fisik dan metadata
    deleteFile: (req, res) => {
        const fileId = req.params.id;

        // 1. Cari file dulu untuk mendapatkan path fisiknya
        FileModel.getById(fileId, (err, row) => {
            if (err) return res.status(500).json({ success: false, error: err.message });
            if (!row) return res.status(404).json({ success: false, message: "File tidak ditemukan di database" });

            const absolutePath = path.resolve(row.filepath);

            // 2. Hapus catatan dari database SQLite
            FileModel.deleteById(fileId, (deleteErr) => {
                if (deleteErr) return res.status(500).json({ success: false, error: deleteErr.message });

                // 3. Hapus file fisik dari storage ponsel (jika masih ada)
                if (fs.existsSync(absolutePath)) {
                    fs.unlinkSync(absolutePath);
                }

                res.json({
                    success: true,
                    message: `File ${row.filename} berhasil dihapus permanen dari sistem.`
                });
            });
        });
    }

};

module.exports = fileController;

