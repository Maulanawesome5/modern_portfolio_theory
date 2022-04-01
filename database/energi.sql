USE saham_indonesia;
SHOW TABLES;
DESC sektorEnergi;
DROP TABLE sektorEnergi;

CREATE TABLE sektorEnergi(
	id INT NOT NULL AUTO_INCREMENT,
	kodeSaham VARCHAR(4) NOT NULL,
    namaEmiten VARCHAR(100),
    tglListing VARCHAR(100),
    jumlahSaham BIGINT,
    papanBursa VARCHAR(100),
    PRIMARY KEY (id)
) ENGINE = InnoDB;

SELECT * FROM sektorEnergi; -- Menampilkan kolom beserta isinya
TRUNCATE sektorEnergi; -- Menghapus seluruh data yang sudah ada didalam kolom
DESCRIBE sektorEnergi; -- Menampilkan pengaturan tabel

-- Tambah kolom
ALTER TABLE sektorEnergi
ADD COLUMN kode_sektor VARCHAR(10) AFTER id;
ALTER TABLE sektorEnergi
ADD COLUMN sektor_usaha VARCHAR(100) AFTER kode_sektor;

-- Membuat foreign key
ALTER TABLE sektorEnergi
	ADD CONSTRAINT fk_kode_sektor
		FOREIGN KEY (kode_sektor) REFERENCES daftar_sektor (kode_sektor);

-- Memasukkan data foreign key --> kode ekskul
UPDATE sektorEnergi SET kode_sektor = 'IDX:A' WHERE id < 74; -- Data akan direplace semua karena jumlahnya kurang dari 74
UPDATE sektorEnergi SET sektor_usaha = 'Energi' WHERE kode_sektor = 'IDX:A'; -- Data akan direplace semua karena foreign key sama




SELECT * FROM sektorEnergi; -- Menampilkan kolom beserta isinya
TRUNCATE sektorEnergi; -- Menghapus seluruh data yang sudah ada didalam kolom
DESCRIBE sektorEnergi; -- Menampilkan pengaturan tabel