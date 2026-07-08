const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const dbPath = path.resolve(__dirname, '../cloud_pribadi.db');
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) console.error('Database Error:', err.message);
    else console.log('✔ Connected to Enterprise SQLite Cluster');
});

module.exports = db;

