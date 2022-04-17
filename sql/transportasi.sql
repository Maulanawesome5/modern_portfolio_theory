USE saham_indonesia;
SHOW TABLES;
DESC sektorTeknologi;
DROP TABLE sektorTransportasi;

CREATE TABLE sektorTransportasi(
	id INT NOT NULL AUTO_INCREMENT,
	kodeSaham VARCHAR(4) NOT NULL,
    namaEmiten VARCHAR(100),
    tglListing VARCHAR(100),
    jumlahSaham BIGINT,
    papanBursa VARCHAR(20),
    PRIMARY KEY (id)
) ENGINE = InnoDB;

-- Tambah kolom
ALTER TABLE sektorTransportasi
ADD COLUMN kode_sektor VARCHAR(10) AFTER id;
ALTER TABLE sektorTransportasi
ADD COLUMN sektor_usaha VARCHAR(100) AFTER kode_sektor;

-- Membuat foreign key
ALTER TABLE sektorTransportasi
	ADD CONSTRAINT fk_kode_sektor_transportasi
		FOREIGN KEY (kode_sektor) REFERENCES daftar_sektor (kode_sektor);

-- Memasukkan data foreign key --> kode ekskul
UPDATE sektorTransportasi SET kode_sektor = 'IDX:K' WHERE id < 30;
UPDATE sektorTransportasi SET sektor_usaha = 'Transportasi & Logistik' WHERE kode_sektor = 'IDX:K'; -- Data akan direplace semua karena foreign key sama



SELECT * FROM sektorTransportasi; -- Menampilkan kolom beserta isinya
TRUNCATE sektorTransportasi; -- Menghapus seluruh data yang sudah ada didalam kolom
DESCRIBE sektorTransportasi; -- Menampilkan pengaturan tabel