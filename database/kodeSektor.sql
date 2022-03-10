USE saham_indonesia;
SHOW TABLES;
DESCRIBE daftar_sektor;
SELECT * FROM daftar_sektor; -- Menampilkan tabel beserta semua nilainya
DROP TABLE sektor_emiten; -- Menghapus tabel

-- Membuat tabel
CREATE TABLE daftar_sektor(
	kode_sektor VARCHAR(10) PRIMARY KEY NOT NULL,
    nama_sektor VARCHAR(100) NOT NULL,
    bursa VARCHAR(10) NOT NULL
)ENGINE = InnoDB;

-- Menambahkan data
INSERT INTO daftar_sektor(kode_sektor, nama_sektor, bursa)
VALUES ("IDX:A", "Energi", "IDX"), ("IDX:B", "Barang Baku", "IDX"), ("IDX:C", "Perindustrian", "IDX"), ("IDX:D", "Barang Konsumen Primer", "IDX"),
("IDX:E", "Barang Konsumen Non-Primer", "IDX"), ("IDX:F", "Kesehatan", "IDX"), ("IDX:G", "Keuangan", "IDX"), ("IDX:H", "Properti & Real Estate", "IDX"),
("IDX:I", "Teknologi", "IDX"), ("IDX:J", "Infrastruktur", "IDX"), ("IDX:K", "Transportasi & Logistik", "IDX"), ("IDX:Z", "Produk Investasi Tercatat", "IDX");

-- Selection query
SELECT * FROM daftar_sektor;


