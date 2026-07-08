const express = require('express');
const router = express.Router();
const multer = require('multer');
const path = require('path');
const fileController = require('../controllers/fileController');

// Konfigurasi Penyimpanan Multer
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/');
    },
    filename: (req, file, cb) => {
        const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
        cb(null, uniqueSuffix + path.extname(file.originalname));
    }
});

const upload = multer({ storage: storage });

// Routes Endpoints
router.get('/files', fileController.getDashboardData);
router.post('/upload', upload.single('file_cloud'), fileController.uploadSingleFile);
router.get('/files/download/:id', fileController.downloadFile);
router.delete('/files/:id', fileController.deleteFile);

module.exports = router;

