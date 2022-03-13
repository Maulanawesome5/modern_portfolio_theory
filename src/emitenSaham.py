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

    kursor.execute(daftar_saham)
    data = kursor.fetchall()

    koneksi.commit() # Commit segala query yang di eksekusi
    koneksi.close() # Menutup commit setelah query di eksekusi

except:
    koneksi.rollback() # Jika gagal terhubung
    print("Database tidak terhubung bro !")


