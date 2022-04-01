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

UPDATE daftar_saham_indonesia
SET sektor_usaha = 'Kesehatan'
WHERE kode_sektor = 'IDX:F';

-- Membuat UNIQUE KEY terhadap kode saham agar tidak ada ticker yang kembar
ALTER TABLE daftar_saham_indonesia
	ADD CONSTRAINT uk_kode_saham UNIQUE (kodeSaham);

-- Memasukkan data foreign key
-- UPDATE daftar_saham_indonesia SET kode_sektor = 'IDX:K' WHERE id < 30;
UPDATE daftar_saham_indonesia SET sektor_usaha = 'Teknologi' WHERE kode_sektor = 'IDX:I'; -- Data akan direplace semua karena foreign key sama
UPDATE daftar_saham_indonesia SET sektor_usaha = 'Transportasi & Logistik' WHERE kode_sektor = 'IDX:K'; -- Data akan direplace semua karena foreign key sama
UPDATE daftar_saham_indonesia SET sektor_usaha = 'Infrastruktur' WHERE kode_sektor = 'IDX:J';


-- Metode untuk selection
SELECT id, kode_sektor, kodeSaham, tglListing FROM daftar_saham_indonesia WHERE kode_sektor = 'IDX:H';
SELECT kode_sektor, sektor_usaha, kodeSaham, namaEmiten FROM daftar_saham_indonesia;
SELECT kode_sektor, sektor_usaha, kodeSaham, namaEmiten FROM daftar_saham_indonesia;
SELECT kodeSaham, namaEmiten, sektor_usaha FROM daftar_saham_indonesia ORDER BY kodeSaham;
SELECT kodeSaham, namaEmiten, tglListing FROM daftar_saham_indonesia;
SELECT DISTINCT kode_sektor FROM daftar_saham_indonesia;


-- Coba membuat dummy record
INSERT INTO daftar_saham_indonesia (kodeSaham, namaEmiten, tglListing)
VALUES ('HRUM', 'Harum Wangi', '1999-06-30'); -- Error, karena kode saham HRUM sudah ada, keuntungan menggunakan 'unique key'
INSERT INTO daftar_saham_indonesia (kode_sektor, kodeSaham, namaEmiten, tglListing)
VALUES ('IDX:Y', 'PWON', 'Pawon Dapur', '2001-06-30'); -- Error, karena foreign key 'IDX:Y' tidak ada di tabel reference
INSERT INTO daftar_saham_indonesia (kodeSaham, namaEmiten, tglListing)
VALUES ('KAEF', 'Kimia Farmasi', '2100-01-30'); -- Error, karena kode saham KAEF sudah ada, keuntungan menggunakan 'unique key'
INSERT INTO daftar_saham_indonesia (kode_sektor, kodeSaham, namaEmiten, tglListing)
VALUES ('IDX:F', 'BMHS', 'Bunda Memang Menggoda', '2001-06-30'); -- Error, meskipun Foreign Key benar, karena BMHS sudah ada maka tidak bisa dimasukkan


DESCRIBE daftar_saham_indonesia; -- Mendeskripsi struktur tabel
SELECT * FROM daftar_saham_indonesia; -- Menampilkan tabel beserta semua nilainya
DROP TABLE daftar_saham_indonesia; -- Menghapus tabel