USE saham_indonesia;
SHOW TABLES; -- Menampilkan tabel yang tersedia didalam database
DESCRIBE daftar_saham_indonesia; -- Mendeskripsi struktur tabel
SELECT * FROM daftar_saham_indonesia; -- Menampilkan tabel beserta semua nilainya
DROP TABLE daftar_saham_indonesia; -- Menghapus tabel

CREATE TABLE daftar_saham_indonesia(
	id INT NOT NULL AUTO_INCREMENT,
    kode_sektor VARCHAR(10),
    sektor_usaha VARCHAR(100),
	kodeSaham VARCHAR(4),
    namaEmiten VARCHAR(100),
    tglListing VARCHAR(100),
    papanBursa VARCHAR(20),
    PRIMARY KEY (id)
) ENGINE = InnoDB;

-- Membuat foreign key
ALTER TABLE daftar_saham_indonesia
	ADD CONSTRAINT fk_kode_sektor_emiten
		FOREIGN KEY (kode_sektor) REFERENCES daftar_sektor (kode_sektor);

-- Memasukkan data foreign key --> kode ekskul
UPDATE daftar_saham_indonesia
SET sektor_usaha = 'Energi'
WHERE kode_sektor = 'IDX:A';

UPDATE daftar_saham_indonesia
SET sektor_usaha = 'Properti & Real Estate'
WHERE kode_sektor = 'IDX:H';

-- Membuat UNIQUE KEY terhadap kode saham agar tidak ada ticker yang kembar
ALTER TABLE daftar_saham_indonesia
	ADD CONSTRAINT uk_kode_saham UNIQUE (kodeSaham);




SELECT * FROM daftar_saham_indonesia WHERE kode_sektor = 'IDX:H';
SELECT kode_sektor, sektor_usaha, kodeSaham, namaEmiten FROM daftar_saham_indonesia;
SELECT kode_sektor, sektor_usaha, kodeSaham, namaEmiten
FROM daftar_saham_indonesia;

DESCRIBE daftar_saham_indonesia; -- Mendeskripsi struktur tabel
SELECT * FROM daftar_saham_indonesia; -- Menampilkan tabel beserta semua nilainya
DROP TABLE daftar_saham_indonesia; -- Menghapus tabel