// Kunci Rahasia Brankas Anda (Bisa Anda ganti dengan kata sandi apapun)
const KUNCI_BRANKAS = "cloud-pribadi-2026";

const verifikasiPIN = (req, res, next) => {
    // Kita akan meminta kunci ini diletakkan di bagian 'Header' setiap request
    const kunciKlien = req.headers['x-api-key'];

    if (kunciKlien === KUNCI_BRANKAS) {
        // Kunci benar, silakan masuk ke kontroler (manajer gudang)
        next();
    } else {
        // Kunci salah atau tidak ada, berikan respons humanis
        res.status(401).json({
            success: false,
            message: "Halo! Maaf ya, brankas ini terkunci. Pastikan Anda memiliki kunci akses yang benar."
        });
    }
};

module.exports = verifikasiPIN;

