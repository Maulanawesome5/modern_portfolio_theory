from pymysql.connections import Connection
from pymysql import *

# sintaks SQL
add_sektor_teknologi = """INSERT INTO sektorTeknologi(kodeSaham, namaEmiten, tglListing, jumlahSaham, papanBursa) VALUES
('ATIC',	    'Anabatic Technologies Tbk.',     '2015 Jul 08',	      2315361355,	'Utama'),
('BUKA',	    'Bukalapak.com Tbk.',     '2021 Aug 06',	    103062019354,	'Pengembangan'),
('CASH',	    'Cashlez Worldwide Indonesia Tbk.',     '2020 May 04',	      1431125517,	'Akselerasi'),
('DCII',	    'DCI Indonesia Tbk.',     '2021 Jan 06',	      2383745900,	'Pengembangan'),
('DIVA',	    'Distribusi Voucher Nusantara Tbk.',     '2018 Nov 27',	      1428571400,	'Pengembangan'),
('DMMX',	    'Digital Mediatama Maxima Tbk.',     '2019 Oct 21',	      7692307700,	'Pengembangan'),
('EDGE',	    'Indointernet Tbk.',     '2021 Feb 08',	       404050000,	'Pengembangan'),
('EMTK',	    'Elang Mahkota Teknologi Tbk.',     '2010 Jan 12',	     61241751483,	'Utama'),
('ENVY',	    'Envy Technologies Indonesia Tbk.',     '2019 Jul 08',	      1800000000,	'Pengembangan'),
('GLVA',	    'Galva Technologies Tbk.',     '2019 Dec 23',	      1500000000,	'Pengembangan'),
('HDIT',	    'Hensel Davest Indonesia Tbk.',     '2019 Jul 12',	      1524680000,	'Utama'),
('KIOS',	    'Kioson Komersial Indonesia Tbk.',     '2017 Oct 05',	       717239900,	'Pengembangan'),
('KREN',	    'Kresna Graha Investama Tbk.',     '2002 Jun 28',	     18208470100,	'Utama'),
('LMAS',	    'Limas Indonesia Makmur Tbk.',     '2001 Dec 28',	       787851525,	'Pengembangan'),
('LUCK',	    'Sentral Mitra Informatika Tbk.',     '2018 Nov 28',	       715749640,	'Pengembangan'),
('MCAS',	    'M Cash Integrasi Tbk.',     '2017 Nov 01',	       867933300,	'Pengembangan'),
('MLPT',	    'Multipolar Technology Tbk.',     '2013 Jul 08',	      1875000000,	'Utama'),
('MTDL',	    'Metrodata Electronics Tbk.',     '1990 Apr 09',	     12276884585,	'Utama'),
('NFCX',	    'NFC Indonesia Tbk.',     '2018 Jul 12',	       666667500,	'Pengembangan'),
('PGJO',	    'Tourindo Guide Indonesia Tbk.',     '2020 Jan 08',	       723859095,	'Akselerasi'),
('PTSN',	    'Sat Nusapersada Tbk',     '2007 Nov 08',	      5314344000,	'Utama'),
('RUNS',	    'Global Sukses Solusi Tbk.',     '2021 Sep 08',	       983557875,	'Akselerasi'),
('SKYB',	    'Northcliff Citranusa Indonesia Tbk.',     '2010 Jul 07',	       585000000,	'PENGEMBANGAN'),
('TECH',	    'Indosterling Technomedia Tbk.',     '2020 Jun 04',	      1256300000,	'Pengembangan'),
('TFAS',	    'Telefast Indonesia Tbk.',     '2019 Sep 17',	      1666666500,	'Pengembangan'),
('UVCR',	    'Trimegah Karya Pratama Tbk.',     '2021 Jul 27',	      2000072603,	'Akselerasi'),
('WGSH',	    'Wira Global Solusi Tbk.',     '2021 Dec 06',	      1042500000,	'Akselerasi'),
('ZYRX',	    'Zyrexindo Mandiri Buana Tbk.',     '2021 Mar 30',	      1333333300,	'Pengembangan')
;"""

add_sektor_transportasi = """INSERT INTO sektorTransportasi(kodeSaham, namaEmiten, tglListing, jumlahSaham, papanBursa) VALUES
('AKSI',	'Mineral Sumberdaya Mandiri Tbk.',  '2001 Jul 13',	      720000000,	    'Pengembangan'),
('ASSA',	'Adi Sarana Armada Tbk.',  '2012 Nov 12',	     3565496148,	    'Utama'),
('BIRD',	'Blue Bird Tbk.',  '2014 Nov 05',	     2502100000,	    'UTAMA'),
('BLTA',	'Berlian Laju Tanker Tbk.',  '1990 Mar 26',	    25940187103,	    'Utama'),
('BPTR',	'Batavia Prosperindo Trans Tbk.',  '2018 Jul 09',	     1550000000,	    'Utama'),
('CMPP',	'AirAsia Indonesia Tbk.',  '1994 Dec 08',	    10685124441,	    'Pengembangan'),
('DEAL',	'Dewata Freightinternational Tbk.',  '2018 Nov 11',	     1146170959,	    'Pengembangan'),
('GIAA',	'Garuda Indonesia (Persero) Tbk.',  '2011 Feb 11',	    25886576254,	    'Utama'),
('HAIS',	'Hasnur Internasional Shipping Tbk.',  '2021 Sep 01',	     2626250000,	    'Utama'),
('HELI',	'Jaya Trishindo Tbk.',  '2018 Mar 27',	      832862387,	    'Pengembangan'),
('IATA',	'Indonesia Transport & Infrastructure Tbk.',  '2006 Sep 13',	    11415812114,	    'Pengembangan'),
('JAYA',	'Armada Berjaya Trans Tbk.',  '2019 Feb 21',	      750000210,	    'Pengembangan'),
('KJEN',	'Krida Jaringan Nusantara Tbk.',  '2019 Jul 01',	      500000000,	    'Pengembangan'),
('LRNA',	'Eka Sari Lorena Transport Tbk.',  '2014 Apr 15',	      350000022,	    'Pengembangan'),
('MIRA',	'Mitra International Resources Tbk.',  '1997 Jan 30',	     3961452039,	    'Pengembangan'),
('NELY',	'Pelayaran Nelly Dwi Putri Tbk.',  '2012 Oct 11',	     2350000000,	    'Pengembangan'),
('PPGL',	'Prima Globalindo Logistik Tbk.',  '2020 Jul 20',	      750021341,	    'Akselerasi'),
('PURA',	'Putra Rajawali Kencana Tbk.',  '2020 Jan 22',	     5941264082,	    'Pengembangan'),
('SAFE',	'Steady Safe Tbk.',  '1994 Aug 15',	      615145012,	    'PENGEMBANGAN'),
('SAPX',	'Satria Antaran Prima Tbk.',  '2018 Oct 03',	      833333300,	    'Pengembangan'),
('SDMU',	'Sidomulyo Selaras Tbk.',  '2011 Jul 12',	     1135225000,	    'Pengembangan'),
('SMDR',	'Samudera Indonesia Tbk.',  '1999 Jul 05',	     3275120000,	    'Utama'),
('TAXI',	'Express Transindo Utama Tbk.',  '2012 Nov 02',	    10223647156,	    'Utama'),
('TMAS',	'Temas Tbk.',  '2003 Jul 09',	     5705150000,	    'Utama'),
('TNCA',	'Trimuda Nuansa Citra Tbk.',  '2018 Jun 28',	      421640000,	    'Pengembangan'),
('TRJA',	'Transkon Jaya Tbk.',  '2020 Aug 27',	     1510200000,	    'Pengembangan'),
('TRUK',	'Guna Timur Raya Tbk.',  '2018 May 23',	      435000000,	    'PENGEMBANGAN'),
('WEHA',	'WEHA Transportasi Indonesia Tbk.',  '2007 May 31',	      886411265,	    'Utama')
;"""

# Menambahkan sektor baru kedalam dbms
daftar_saham = """INSERT INTO daftar_saham_indonesia(kode_sektor, kodeSaham, namaEmiten, tglListing, papanBursa) VALUES
('IDX:K',  'AKSI',	'Mineral Sumberdaya Mandiri Tbk.',            '2001 Jul 13',	  'Pengembangan'),
('IDX:K',  'ASSA',	'Adi Sarana Armada Tbk.',                     '2012 Nov 12',	  'Utama'),
('IDX:K',  'BIRD',	'Blue Bird Tbk.',                             '2014 Nov 05',	  'UTAMA'),
('IDX:K',  'BLTA',	'Berlian Laju Tanker Tbk.',                   '1990 Mar 26',	  'Utama'),
('IDX:K',  'BPTR',	'Batavia Prosperindo Trans Tbk.',             '2018 Jul 09',	  'Utama'),
('IDX:K',  'CMPP',	'AirAsia Indonesia Tbk.',                     '1994 Dec 08',	  'Pengembangan'),
('IDX:K',  'DEAL',	'Dewata Freightinternational Tbk.',           '2018 Nov 11',	  'Pengembangan'),
('IDX:K',  'GIAA',	'Garuda Indonesia (Persero) Tbk.',            '2011 Feb 11',	  'Utama'),
('IDX:K',  'HAIS',	'Hasnur Internasional Shipping Tbk.',         '2021 Sep 01',	  'Utama'),
('IDX:K',  'HELI',	'Jaya Trishindo Tbk.',                        '2018 Mar 27',	  'Pengembangan'),
('IDX:K',  'IATA',	'Indonesia Transport & Infrastructure Tbk.',  '2006 Sep 13',	  'Pengembangan'),
('IDX:K',  'JAYA',	'Armada Berjaya Trans Tbk.',                  '2019 Feb 21',	  'Pengembangan'),
('IDX:K',  'KJEN',	'Krida Jaringan Nusantara Tbk.',              '2019 Jul 01',	  'Pengembangan'),
('IDX:K',  'LRNA',	'Eka Sari Lorena Transport Tbk.',             '2014 Apr 15',	  'Pengembangan'),
('IDX:K',  'MIRA',	'Mitra International Resources Tbk.',         '1997 Jan 30',	  'Pengembangan'),
('IDX:K',  'NELY',	'Pelayaran Nelly Dwi Putri Tbk.',             '2012 Oct 11',	  'Pengembangan'),
('IDX:K',  'PPGL',	'Prima Globalindo Logistik Tbk.',             '2020 Jul 20',	  'Akselerasi'),
('IDX:K',  'PURA',	'Putra Rajawali Kencana Tbk.',                '2020 Jan 22',	  'Pengembangan'),
('IDX:K',  'SAFE',	'Steady Safe Tbk.',                           '1994 Aug 15',	  'PENGEMBANGAN'),
('IDX:K',  'SAPX',	'Satria Antaran Prima Tbk.',                  '2018 Oct 03',	  'Pengembangan'),
('IDX:K',  'SDMU',	'Sidomulyo Selaras Tbk.',                     '2011 Jul 12',	  'Pengembangan'),
('IDX:K',  'SMDR',	'Samudera Indonesia Tbk.',                    '1999 Jul 05',	  'Utama'),
('IDX:K',  'TAXI',	'Express Transindo Utama Tbk.',               '2012 Nov 02',	  'Utama'),
('IDX:K',  'TMAS',	'Temas Tbk.',                                 '2003 Jul 09',	  'Utama'),
('IDX:K',  'TNCA',	'Trimuda Nuansa Citra Tbk.',                  '2018 Jun 28',	  'Pengembangan'),
('IDX:K',  'TRJA',	'Transkon Jaya Tbk.',                         '2020 Aug 27',	  'Pengembangan'),
('IDX:K',  'TRUK',	'Guna Timur Raya Tbk.',                       '2018 May 23',	  'PENGEMBANGAN'),
('IDX:K',  'WEHA',	'WEHA Transportasi Indonesia Tbk.',           '2007 May 31',	  'Utama')
;"""

add_kesehatan = """INSERT INTO daftar_saham_indonesia(kode_sektor, kodeSaham, namaEmiten, tglListing, papanBursa) VALUES
('IDX:F', 'BMHS',	'Bundamedik Tbk.',                           '2021-07-06', 	'Utama'),
('IDX:F', 'CARE',	'Metro Healthcare Indonesia Tbk.',           '2020-03-13', 	'Pengembangan'),
('IDX:F', 'DGNS',	'Diagnos Laboratorium Utama Tbk.',           '2021-01-15', 	'Pengembangan'),
('IDX:F', 'DVLA',	'Darya-Varia Laboratoria Tbk.',              '1994-11-11', 	'Utama'),
('IDX:F', 'HEAL',	'Medikaloka Hermina Tbk.',                   '2018-05-16', 	'Utama'),
('IDX:F', 'INAF',	'Indofarma Tbk.',                            '2001-04-17', 	'Utama'),
('IDX:F', 'IRRA',	'Itama Ranoraya Tbk.',                       '2019-10-15', 	'Pengembangan'),
('IDX:F', 'KAEF',	'Kimia Farma Tbk.',                          '2001-07-04', 	'Utama'),
('IDX:F', 'KLBF',	'Kalbe Farma Tbk.',                          '1991-07-30', 	'Utama'),
('IDX:F', 'MERK',	'Merck Tbk.',                                '1981-07-23', 	'PENGEMBANGAN'),
('IDX:F', 'MIKA',	'Mitra Keluarga Karyasehat Tbk.',            '2015-03-24', 	'Utama'),
('IDX:F', 'PEHA',	'Phapros Tbk.',                              '2018-12-26', 	'Utama'),
('IDX:F', 'PRDA',	'Prodia Widyahusada Tbk.',                   '2016-12-07', 	'Utama'),
('IDX:F', 'PRIM',	'Royal Prima Tbk.',                          '2018-05-15', 	'Pengembangan'),
('IDX:F', 'PYFA',	'Pyridam Farma Tbk.',                        '2001-10-16', 	'Pengembangan'),
('IDX:F', 'RSGK',	'Kedoya Adyaraya Tbk.',                      '2021-09-08', 	'Utama'),
('IDX:F', 'SAME',	'Sarana Meditama Metropolitan Tbk.',         '2013-01-11', 	'Pengembangan'),
('IDX:F', 'SCPI',	'Organon Pharma Indonesia Tbk.',             '1990-06-08', 	'PENGEMBANGAN'),
('IDX:F', 'SIDO',	'Industri Jamu dan Farmasi Sidomuncul Tbk',  '2013-12-18', 	'Utama'),
('IDX:F', 'SILO',	'Siloam International Hospitals Tbk.',       '2013-09-12', 	'Utama'),
('IDX:F', 'SOHO',	'Soho Global Health Tbk.',                   '2020-09-08', 	'Utama'),
('IDX:F', 'SRAJ',	'Sejahteraraya Anugrahjaya Tbk.',            '2011-04-11', 	'Utama'),
('IDX:F', 'TSPC',	'Tempo Scan Pacific Tbk.',                   '1994-06-17', 	'Utama')
;"""

add_infrastruktur = """INSERT INTO daftar_saham_indonesia(kode_sektor, kodeSaham, namaEmiten, tglListing, papanBursa) VALUES
('IDX:J', 'ACST',	'Acset Indonusa Tbk.',                          '2013-06-24',	          'Utama'),
('IDX:J', 'ADHI',	'Adhi Karya (Persero) Tbk.',                    '2004-03-18',	           'Utama'),
('IDX:J', 'BALI',	'Bali Towerindo Sentra Tbk.',                   '2014-03-13',	           'Utama'),
('IDX:J', 'BTEL',	'Bakrie Telecom Tbk.',                          '2006-02-03',	          'Utama'),
('IDX:J', 'BUKK',	'Bukaka Teknik Utama Tbk.',                     '2015-06-29',	           'Pengembangan'),
('IDX:J', 'CASS',	'Cardig Aero Services Tbk.',                    '2011-12-05',	           'Pengembangan'),
('IDX:J', 'CENT',	'Centratama Telekomunikasi Indonesia Tbk',      '2001-11-01',	          'Pengembangan'),
('IDX:J', 'CMNP',	'Citra Marga Nusaphala Persada Tbk.',           '1995-01-10',	           'Utama'),
('IDX:J', 'DGIK',	'Nusa Konstruksi Enjiniring Tbk.',              '2007-12-19',	           'Utama'),
('IDX:J', 'EXCL',	'XL Axiata Tbk.',                               '2005-09-29',	          'Utama'),
('IDX:J', 'FIMP',	'Fimperkasa Utama Tbk.',                        '2021-04-09',	            'Akselerasi'),
('IDX:J', 'FREN',	'Smartfren Telecom Tbk.',                       '2006-11-29',	         'Utama'),
('IDX:J', 'GHON',	'Gihon Telekomunikasi Indonesia Tbk.',          '2018-04-09',	            'Utama'),
('IDX:J', 'GMFI',	'Garuda Maintenance Facility Aero Asia Tbk',    '2017-10-10',	          'Utama'),
('IDX:J', 'GOLD',	'Visi Telekomunikasi Infrastruktur Tbk.',       '2010-07-07',	           'PENGEMBANGAN'),
('IDX:J', 'HADE',	'Himalaya Energi Perkasa Tbk.',                 '2004-04-12',	           'PENGEMBANGAN'),
('IDX:J', 'IBST',	'Inti Bangun Sejahtera Tbk.',                   '2012-08-31',	           'Utama'),
('IDX:J', 'IDPR',	'Indonesia Pondasi Raya Tbk.',                  '2015-12-10',	           'Utama'),
('IDX:J', 'IPCC',	'Indonesia Kendaraan Terminal Tbk.',            '2018-07-09',	           'Utama'),
('IDX:J', 'IPCM',	'Jasa Armada Indonesia Tbk.',                   '2017-12-22',	           'Utama'),
('IDX:J', 'ISAT',	'Indosat Tbk.',                                 '1994-10-19',	           'Utama'),
('IDX:J', 'JAST',	'Jasnita Telekomindo Tbk.',                     '2019-05-16',	            'Pengembangan'),
('IDX:J', 'JKON',	'Jaya Konstruksi Manggala Pratama Tbk.',        '2007-12-04',	          'Utama'),
('IDX:J', 'JSMR',	'Jasa Marga (Persero) Tbk.',                    '2007-11-12',	           'Utama'),
('IDX:J', 'KARW',	'ICTSI Jasa Prima Tbk.',                        '1994-12-20',	            'Pengembangan'),
('IDX:J', 'KBLV',	'First Media Tbk.',                             '2000-02-25',	           'Pengembangan'),
('IDX:J', 'KEEN',	'Kencana Energi Lestari Tbk.',                  '2019-09-02',	           'Utama'),
('IDX:J', 'LAPD',	'Leyand International Tbk.',                    '2001-07-17',	           'Pengembangan'),
('IDX:J', 'LCKM',	'LCK Global Kedaton Tbk.',                      '2018-01-16',	           'Pengembangan'),
('IDX:J', 'LINK',	'Link Net Tbk.',                                '2014-06-02',	           'Utama'),
('IDX:J', 'META',	'Nusantara Infrastructure Tbk.',                '2001-07-18',	          'Utama'),
('IDX:J', 'MPOW',	'Megapower Makmur Tbk.',                        '2017-07-05',	            'Pengembangan'),
('IDX:J', 'MTEL',	'Dayamitra Telekomunikasi Tbk.',                '2021-11-22',	          'Utama'),
('IDX:J', 'MTPS',	'Meta Epsi Tbk.',                               '2019-04-10',	           'PENGEMBANGAN'),
('IDX:J', 'MTRA',	'Mitra Pemuda Tbk.',                            '2016-02-10',	            'Pengembangan'),
('IDX:J', 'NRCA',	'Nusa Raya Cipta Tbk.',                         '2013-06-27',	           'UTAMA'),
('IDX:J', 'OASA',	'Protech Mitra Perkasa Tbk.',                   '2016-07-18',	            'Pengembangan'),
('IDX:J', 'PBSA',	'Paramita Bangun Sarana Tbk.',                  '2016-09-28',	           'Utama'),
('IDX:J', 'PORT',	'Nusantara Pelabuhan Handal Tbk.',              '2017-03-16',	           'Pengembangan'),
('IDX:J', 'POWR',	'Cikarang Listrindo Tbk.',                      '2016-06-14',	          'Pengembangan'),
('IDX:J', 'PPRE',	'PP Presisi Tbk.',                              '2017-11-24',	          'Utama'),
('IDX:J', 'PTDU',	'Djasa Ubersakti Tbk.',                         '2020-12-08',	           'Pengembangan'),
('IDX:J', 'PTPP',	'PP (Persero) Tbk.',                            '2010-02-09',	           'Utama'),
('IDX:J', 'PTPW',	'Pratama Widya Tbk.',                           '2020-02-07',	            'Pengembangan'),
('IDX:J', 'RONY',	'Aesler Grup Internasional Tbk.',               '2020-04-09',	           'Pengembangan'),
('IDX:J', 'SMKM',	'Sumber Mas Konstruksi Tbk.',                   '2022-03-09',	           'Akselerasi'),
('IDX:J', 'SSIA',	'Surya Semesta Internusa Tbk.',                 '1997-03-27',	           'Utama'),
('IDX:J', 'SUPR',	'Solusi Tunas Pratama Tbk.',                    '2011-10-11',	           'Pengembangan'),
('IDX:J', 'TAMA',	'Lancartama Sejati Tbk.',                       '2020-02-10',	           'Pengembangan'),
('IDX:J', 'TBIG',	'Tower Bersama Infrastructure Tbk.',            '2010-10-26',	          'Utama'),
('IDX:J', 'TGRA',	'Terregra Asia Energy Tbk.',                    '2017-05-16',	           'UTAMA'),
('IDX:J', 'TLKM',	'Telkom Indonesia (Persero) Tbk.',              '1995-11-14',	          'Utama'),
('IDX:J', 'TOPS',	'Totalindo Eka Persada Tbk.',                   '2017-06-16',	          'Utama'),
('IDX:J', 'TOTL',	'Total Bangun Persada Tbk.',                    '2006-07-25',	           'Utama'),
('IDX:J', 'TOWR',	'Sarana Menara Nusantara Tbk.',                 '2010-03-08',	          'Utama'),
('IDX:J', 'WEGE',	'Wijaya Karya Bangunan Gedung Tbk.',            '2017-11-30',	           'Utama'),
('IDX:J', 'WIKA',	'Wijaya Karya (Persero) Tbk.',                  '2007-10-29',	           'Utama'),
('IDX:J', 'WSKT',	'Waskita Karya (Persero) Tbk.',                 '2012-12-19',	          'Utama')
;"""

try:
    # membuat koneksi ke MySQL
    # karena saya menggunakan panel XAMPP, maka tinggal menyambungkan saja
    # Membuat koneksi ke database yang ada
    koneksi = Connection(
        host="localhost",
        user="root",
        password="",
        database="saham_indonesia",
        port=3306
    )
    kursor = koneksi.cursor() # Membuat kursor untuk mengeksekusi program
    
    # execute SQL query using execute() method.
    # kursor.execute("SELECT VERSION()")

    # # Fetch a single row using fetchone() method.
    # data = kursor.fetchone()

    # print("Database version : %s " %data)

    kursor.execute(add_infrastruktur)
    data = kursor.fetchall()

    koneksi.commit() # Commit segala query yang di eksekusi
    koneksi.close() # Menutup commit setelah query di eksekusi

except:
    koneksi.rollback() # Jika gagal terhubung
    print("Database tidak terhubung bro !")


