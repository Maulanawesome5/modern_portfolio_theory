USE saham_indonesia;

CREATE TABLE sektorKesehatan(
	id INT NOT NULL AUTO_INCREMENT,
	kodeSaham VARCHAR(4) NOT NULL,
    namaEmiten VARCHAR(100),
    tglListing VARCHAR(100),
    jumlahSaham BIGINT,
    papanBursa VARCHAR(20),
    PRIMARY KEY (id)
) ENGINE = InnoDB;

SELECT * FROM sektorKesehatan;

INSERT INTO sektorKesehatan(kodeSaham, namaEmiten, tglListing, jumlahSaham, papanBursa) VALUES
('BMHS',	'Bundamedik Tbk.',  '2021-07-06', 	   8603416176,	'Utama'),
('CARE',	'Metro Healthcare Indonesia Tbk.',  '2020-03-13', 	  33250000000,	'Pengembangan'),
('DGNS',	'Diagnos Laboratorium Utama Tbk.',  '2021-01-15', 	   1250000000,	'Pengembangan'),
('DVLA',	'Darya-Varia Laboratoria Tbk.',  '1994-11-11', 	   1120000000,	'Utama'),
('HEAL',	'Medikaloka Hermina Tbk.',  '2018-05-16', 	  14890000000,	'Utama'),
('INAF',	'Indofarma Tbk.',  '2001-04-17', 	   3099267500,	'Utama'),
('IRRA',	'Itama Ranoraya Tbk.',  '2019-10-15', 	   1600000000,	'Pengembangan'),
('KAEF',	'Kimia Farma Tbk.',  '2001-07-04', 	   5554000000,	'Utama'),
('KLBF',	'Kalbe Farma Tbk.',  '1991-07-30', 	  46875122110,	'Utama'),
('MERK',	'Merck Tbk.',  '1981-07-23', 	    448000000,	'PENGEMBANGAN'),
('MIKA',	'Mitra Keluarga Karyasehat Tbk.',  '2015-03-24', 	  14246349500,	'Utama'),
('PEHA',	'Phapros Tbk.',  '2018-12-26', 	    840000000,	'Utama'),
('PRDA',	'Prodia Widyahusada Tbk.',  '2016-12-07', 	    937500000,	'Utama'),
('PRIM',	'Royal Prima Tbk.',  '2018-05-15', 	   3393434905,	'Pengembangan'),
('PYFA',	'Pyridam Farma Tbk.',  '2001-10-16', 	    535080000,	'Pengembangan'),
('RSGK',	'Kedoya Adyaraya Tbk.',  '2021-09-08', 	    929675000,	'Utama'),
('SAME',	'Sarana Meditama Metropolitan Tbk.',  '2013-01-11', 	  17113987263,	'Pengembangan'),
('SCPI',	'Organon Pharma Indonesia Tbk.',  '1990-06-08', 	      3600000,	'PENGEMBANGAN'),
('SIDO',	'Industri Jamu dan Farmasi Sidomuncul Tbk',  '2013-12-18', 	  30000000000,	'Utama'),
('SILO',	'Siloam International Hospitals Tbk.',  '2013-09-12', 	   1625765625,	'Utama'),
('SOHO',	'Soho Global Health Tbk.',  '2020-09-08', 	   1269168239,	'Utama'),
('SRAJ',	'Sejahteraraya Anugrahjaya Tbk.',  '2011-04-11', 	  12000705445,	'Utama'),
('TSPC',	'Tempo Scan Pacific Tbk.',  '1994-06-17', 	   4509864300,	'Utama')
;

-- Membuat foreign key
ALTER TABLE sektorKesehatan
ADD COLUMN kode_sektor VARCHAR(10) AFTER id;
ALTER TABLE sektorKesehatan
	ADD CONSTRAINT fk_kode_sektor_kesehatan
		FOREIGN KEY (kode_sektor) REFERENCES daftar_sektor (kode_sektor);
-- Memasukkan data foreign key --> kode sektor
UPDATE sektorKesehatan SET kode_sektor = 'IDX:F' WHERE id < 30;

ALTER TABLE sektorKesehatan
ADD COLUMN sektor_usaha VARCHAR(100) AFTER kode_sektor;
UPDATE sektorKesehatan SET sektor_usaha = 'Kesehatan' WHERE kode_sektor = 'IDX:F'; -- Data akan direplace semua karena foreign key sama

SELECT * FROM sektorKesehatan;