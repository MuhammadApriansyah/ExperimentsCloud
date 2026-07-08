const db = require('../config/db');

db.serialize(() => {
    db.run(`
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            filepath TEXT NOT NULL,
            size INTEGER,
            uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    `);
});

const FileModel = {
    getAll: (callback) => {
        db.all("SELECT * FROM files ORDER BY uploaded_at DESC", [], callback);
    },

    create: (filename, filepath, size, callback) => {
        const query = `INSERT INTO files (filename, filepath, size) VALUES (?, ?, ?)`;
        db.run(query, [filename, filepath, size], function(err) {
            callback(err, this.lastID);
        });
    },

    // FITUR BARU: Cari detail file berdasarkan ID untuk download
    getById: (id, callback) => {
        db.get("SELECT * FROM files WHERE id = ?", [id], callback);
    },

    // FITUR BARU: Hapus catatan dari database
    deleteById: (id, callback) => {
        db.run("DELETE FROM files WHERE id = ?", [id], callback);
    }
};


module.exports = FileModel;

