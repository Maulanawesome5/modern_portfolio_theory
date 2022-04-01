USE saham_indonesia;
SHOW TABLES;
DESC sektorProperti;
DROP TABLE sektorProperti;

CREATE TABLE sektorProperti(
	id INT NOT NULL AUTO_INCREMENT,
	kodeSaham VARCHAR(4) NOT NULL,
    namaEmiten VARCHAR(100),
    tglListing DATE,
    jumlahSaham BIGINT,
    papanBursa VARCHAR(20),
    PRIMARY KEY (id)
) ENGINE = InnoDB;

SELECT * FROM sektorProperti; -- Menampilkan kolom beserta isinya
TRUNCATE sektorProperti; -- Menghapus seluruh data yang sudah ada didalam kolom
DESCRIBE sektorProperti; -- Menampilkan pengaturan tabel

-- Tambah kolom
ALTER TABLE sektorProperti
ADD COLUMN kode_sektor VARCHAR(10) AFTER id;
ALTER TABLE sektorProperti
ADD COLUMN sektor_usaha VARCHAR(100) AFTER kode_sektor;

-- Membuat foreign key
ALTER TABLE sektorProperti
	ADD CONSTRAINT fk_kode_sektor_properti
		FOREIGN KEY (kode_sektor) REFERENCES daftar_sektor (kode_sektor);

-- Memasukkan data foreign key --> kode ekskul
UPDATE sektorProperti SET kode_sektor = 'IDX:H' WHERE id < 81; -- Data akan direplace semua karena jumlahnya kurang dari 74
UPDATE sektorProperti SET sektor_usaha = 'Properti & Real Estate' WHERE kode_sektor = 'IDX:H'; -- Data akan direplace semua karena foreign key sama




SELECT * FROM sektorProperti; -- Menampilkan kolom beserta isinya
TRUNCATE sektorProperti; -- Menghapus seluruh data yang sudah ada didalam kolom
DESCRIBE sektorProperti; -- Menampilkan pengaturan tabel