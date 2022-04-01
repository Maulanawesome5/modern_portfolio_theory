from tkinter import *
from pymysql import *

# Database connection
koneksi = Connection(
    host="localhost",
    user="root",
    database="saham_indonesia",
    port=3306
)

kursor = koneksi.cursor() # cursor untuk eksekusi query

# GUI apps
root = Tk()
root.title("Optimasi Portofolio Saham")
root.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")
root.geometry("400x400")

def testConnection():
    koneksi = Connection(
        host="localhost",
        user="root",
        database="saham_indonesia",
        port=3306
    )

    kursor = koneksi.cursor() # cursor untuk eksekusi query

    kursor.execute("SELECT VERSION();")

    sql = kursor.fetchone() # fetch data

    myLabel = Label(master=root, text="DBMS Version: %s" % sql)
    myLabel.pack()

    # commit eksekusi query dan menutup koneksi
    koneksi.commit()
    koneksi.close()


myButton = Button(master=root, text="Test Connect to DBMS", command=testConnection)
myButton.pack()



# commit eksekusi query dan menutup koneksi
koneksi.commit()
koneksi.close()
# menyalakan loop GUI
root.mainloop()


add_energi = """INSERT INTO daftar_saham_indonesia(kode_sektor, kodeSaham, namaEmiten, tglListing, papanBursa) VALUES
('IDX:A', 'ADMR',  'Adaro Minerals Indonesia Tbk.', '2022 Jan 03',  'Pengembangan'),
('IDX:A', 'ADRO',  'Adaro Energy Tbk.', '2008 Jul 16',  'Utama'),
('IDX:A', 'AIMS',  'Akbar Indo Makmur Stimec Tbk.', '2001 Jul 20',  'Pengembangan'),
('IDX:A', 'AKRA',  'AKR Corporindo Tbk.', '1994 Oct 03',  'Utama'),
('IDX:A', 'APEX',  'Apexindo Pratama Duta Tbk.', '2013 Jun 05',  'Pengembangan'),
('IDX:A', 'ARII',  'Atlas Resources Tbk.', '2011 Nov 08',  'Pengembangan'),
('IDX:A', 'ARTI',  'Ratu Prabu Energi Tbk.', '2003 Apr 30',  'Utama'),
('IDX:A', 'ABRM',  'Pelayaran Nasional Bina Buana Raya Tbk', '2013 Jan 09',  'Utama'),
('IDX:A', 'AESS',  'Batulicin Nusantara Maritim Tbk.', '2020 Mar 09',  'Pengembangan'),
('IDX:A', 'BIPI',  'Astrindo Nusantara infrastruktur Tbk', '2010 Feb 11',  'Pengembangan'),
('IDX:A', 'BOSS',  'Borneo Olah Sarana Sukses Tbk.', '2018 Feb 15',  'Pengembangan'),
('IDX:A', 'BSML',  'Bintang Samudera Mandiri Lines Tbk.', '2021 Dec 16',  'Pengembangan'),
('IDX:A', 'BSSR',  'Baramulti Suksessarana Tbk.', '2012 Nov 08',  'Pengembangan'),
('IDX:A', 'BULL',  'Buana Lintas Lautan Tbk.', '2011 May 23',  'Utama'),
('IDX:A', 'BUMI',  'Bumi Resources Tbk.', '1990 Jul 30',  'Pengembangan'),
('IDX:A', 'BYAN',  'Bayan Resources Tbk.', '2008 Ags 12',  'Utama'),
('IDX:A', 'CANI',  'Capitol Nusantara Indonesia Tbk.', '2014 Jan 16',  'Pengembangan'),
('IDX:A', 'CNKO',  'Exploitasi Energi Indonesia Tbk.', '2001 Nov 20',  'Utama'),
('IDX:A', 'DEWA',  'Darma Henwa Tbk.', '2007 Sep 26',  'Utama'),
('IDX:A', 'DOID',  'Delta Dunia Makmur Tbk.', '2001 Jun 15',  'Utama'),
('IDX:A', 'DSSA',  'Dian Swastatika Sentosa Tbk.', '2009 Dec 10',  'Utama'),
('IDX:A', 'DWGL',  'Dwi Guna Laksana Tbk.', '2017 Dec 13',  'Pengembangan'),
('IDX:A', 'ELSA',  'Elnusa Tbk.', '2008 Feb 06',  'Utama'),
('IDX:A', 'ENRG',  'Energi Mega Persada Tbk.', '2004 Jun 07',  'Pengembangan'),
('IDX:A', 'ETWA',  'Eterindo Wahanatama Tbk', '1997 May 16',  'Utama'),
('IDX:A', 'FIRE',  'Alfa Energi Investama Tbk.', '2017 Jun 09',  'Pengembangan'),
('IDX:A', 'GEMS',  'Golden Energy Mines Tbk.', '2011 Nov 17',  'Utama'),
('IDX:A', 'GTBO',  'Garda Tujuh Buana Tbk', '2009 Jul 09',  'Pengembangan'),
('IDX:A', 'GTSI',  'GTS Internasional Tbk.', '2021 Sep 08',  'Utama'),
('IDX:A', 'HITS',  'Humpuss Intermoda Transportasi Tbk.', '1997 Dec 15',  'Utama'),
('IDX:A', 'HRUM',  'Harum Energy Tbk.', '2010 Oct 06',  'Utama'),
('IDX:A', 'INDY',  'Indika Energy Tbk.', '2008 Jun 11',  'Utama'),
('IDX:A', 'INPS',  'Indah Prakasa Sentosa Tbk.', '2018 Apr 06',  'Pengembangan'),
('IDX:A', 'ITMA',  'Sumber Energi Andalan Tbk.', '1990 Dec 10',  'Pengembangan'),
('IDX:A', 'ITMG',  'Indo Tambangraya Megah Tbk.', '2007 Dec 18',  'Utama'),
('IDX:A', 'JSKY',  'Sky Energy Indonesia Tbk.', '2018 Mar 28',  'Utama'),
('IDX:A', 'KKGI',  'Resource Alam Indonesia Tbk.', '1991 Jul 01',  'Utama'),
('IDX:A', 'KOPI',  'Mitra Energi Persada Tbk.', '2015 May 04',  'PENGEMBANGAN'),
('IDX:A', 'LEAD',  'Logindo Samudramakmur Tbk.', '2013 Dec 11',  'UTAMA'),
('IDX:A', 'MBAP',  'Mitrabara Adiperdana Tbk.', '2014 Jul 10',  'Pengembangan'),
('IDX:A', 'MBSS',  'Mitrabahtera Segara Sejati Tbk', '2011 Apr 06',  'Utama'),
('IDX:A', 'MCOL',  'Prima Andalan Mandiri Tbk.', '2021 Sep 07',  'Utama'),
('IDX:A', 'MEDC',  'Medco Energi Internasional Tbk.', '1994 Oct 12',  'Utama'),
('IDX:A', 'MITI',  'Mitra Investindo Tbk.', '1997 Jul 16',  'Pengembangan'),
('IDX:A', 'MTFN',  'Capitalinc Investment Tbk.', '1990 Apr 16',  'Pengembangan'),
('IDX:A', 'MYOH',  'Samindo Resources Tbk.', '2000 Jul 27',  'Utama'),
('IDX:A', 'PGAS',  'Perusahaan Gas Negara Tbk.', '2003 Dec 15',  'Utama'),
('IDX:A', 'PKPK',  'Perdana Karya Perkasa Tbk.', '2007 Jul 11',  'Pengembangan'),
('IDX:A', 'PSSI',  'Pelita Samudera Shipping Tbk.', '2017 Dec 05',  'Utama'),
('IDX:A', 'PTBA',  'Bukit Asam Tbk.', '2002 Dec 23',  'Utama'),
('IDX:A', 'PTIS',  'Indo Straits Tbk.', '2011 Jul 12',  'Utama'),
('IDX:A', 'PTRO',  'Petrosea Tbk.', '1990 May 21',  'Utama'),
('IDX:A', 'RAJA',  'Rukun Raharja Tbk.', '2006 Apr 19',  'Utama'),
('IDX:A', 'RIGS',  'Rig Tenders Indonesia Tbk.', '1990 Mar 05',  'Pengembangan'),
('IDX:A', 'RMKE',  'RMK Energy Tbk.', '2021 Dec 07',  'Utama'),
('IDX:A', 'RUIS',  'Radiant Utama Interinsco Tbk.', '2006 Jul 12',  'Pengembangan'),
('IDX:A', 'SEMA',  'Semacom Integrated Tbk.', '2022 Jan 10',  'Pengembangan'),
('IDX:A', 'SGER',  'Sumber Global Energy Tbk.', '2020 Ags 10',  'Pengembangan'),
('IDX:A', 'SHIP',  'Sillo Maritime Perdana Tbk.', '2016 Jun 16',  'Pengembangan'),
('IDX:A', 'SMMT',  'Golden Eagle Energy Tbk.', '1997 Dec 01',  'PENGEMBANGAN'),
('IDX:A', 'SMRU',  'SMR Utama Tbk.', '2011 Oct 10',  'Pengembangan'),
('IDX:A', 'SOCI',  'Soechi Lines Tbk.', '2014 Dec 03',  'Utama'),
('IDX:A', 'SUGI',  'Sugih Energy Tbk.', '2002 Jun 19',  'PENGEMBANGAN'),
('IDX:A', 'SURE',  'Super Energy Tbk.', '2018 Oct 05',  'PENGEMBANGAN'),
('IDX:A', 'TAMU',  'Pelayaran Tamarin Samudra Tbk.', '2017 May 10',  'Pengembangan'),
('IDX:A', 'TCPI',  'Transcoal Pacific Tbk.', '2018 Jul 06',  'Pengembangan'),
('IDX:A', 'TEBE',  'Dana Brata Luhur Tbk.', '2019 Nov 18',  'PENGEMBANGAN'),
('IDX:A', 'TOBA',  'TBS Energi Utama Tbk.', '2012 Jul 06',  'Utama'),
('IDX:A', 'TPMA',  'Trans Power Marine Tbk.', '2013 Feb 20',  'Pengembangan'),
('IDX:A', 'TRAM',  'Trada Alam Minera Tbk.', '2008 Sep 10',  'Utama'),
('IDX:A', 'UNIQ',  'Ulima Nitra Tbk.', '2021 Mar 08',  'Utama'),
('IDX:A', 'WINS',  'Wintermar Offshore Marine Tbk.', '2010 Nov 29',  'Utama'),
('IDX:A', 'WOWS',  'Ginting Jaya Energi Tbk.', '2019 Nov 08',  'Pengembangan')
;"""

add_properti = """INSERT INTO daftar_saham_indonesia(kode_sektor, kodeSaham, namaEmiten, tglListing, papanBursa) VALUES
('IDX:H', 'ADCP',	'Adhi Commuter Properti Tbk.', '21 Mei 2021', 'Utama'),
('IDX:H', 'AMAN',	'Makmur Berkah Amanda Tbk.', '13 Mar 2020', 'Utama'),
('IDX:H', 'APLN',	'Agung Podomoro Land Tbk.', '11 Nov 2010', 'Utama'),
('IDX:H', 'ARMY',	'Armidian Karyatama Tbk.', '21 Jun 2017', 'Pengembangan'),
('IDX:H', 'ASPI',	'Andalan Sakti Primaindo Tbk.', '17 Feb 2020', 'Pengembangan'),
('IDX:H', 'ASRI',	'Alam Sutera Realty Tbk.', '18 Des 2007', 'Utama'),
('IDX:H', 'ATAP',	'Trimitra Prawara Goldland Tbk.', '11 Des 2020', 'Pengembangan'),
('IDX:H', 'BAPA',	'Bekasi Asri Pemula Tbk.', '14 Jan 2008', 'Utama'),
('IDX:H', 'BAPI',	'Bhakti Agung Propertindo Tbk.', '16 Sep 2019', 'Pengembangan'),
('IDX:H', 'BBSS',	'Bumi Benowo Sukses Sejahtera Tbk.', '15 Apr 2020', 'Pengembangan'),
('IDX:H', 'BCIP',	'Bumi Citra Permai Tbk.', '11 Des 2009', 'Pengembangan'),
('IDX:H', 'BEST',	'Bekasi Fajar Industrial Estate Tbk.', '10 Apr 2012', 'Utama'),
('IDX:H', 'BIKA',	'Binakarya Jaya Abadi Tbk.', '14 Jul 2015', 'Pengembangan'),
('IDX:H', 'BIPP',	'Bhuwanatala Indah Permai Tbk.', '23 Okt 1995', 'Pengembangan'),
('IDX:H', 'BKDP',	'Bukit Darmo Property Tbk.', '15 Jun 2007', 'Pengembangan'),
('IDX:H', 'BKSL',	'Sentul City Tbk.', '28 Jul 1997', 'Utama'),
('IDX:H', 'BSDE',	'Bumi Serpong Damai Tbk.', '06 Jun 2008', 'Utama'),
('IDX:H', 'CITY',	'Natura City Developments Tbk.', '28 Sep 2018', 'Utama'),
('IDX:H', 'COWL',	'Cowell Development Tbk.', '19 Des 2007', 'PENGEMBANGAN'),
('IDX:H', 'CPRI',	'Capri Nusa Satu Properti Tbk.', '11 Apr 2019', 'PENGEMBANGAN'),
('IDX:H', 'CSIS',	'Cahayasakti Investindo Sukses Tbk.', '10 Mei 2017', 'Pengembangan'),
('IDX:H', 'CTRA',	'Ciputra Development Tbk.', '28 Mar 1994', 'Utama'),
('IDX:H', 'DADA',	'Diamond Citra Propertindo Tbk.', '14 Feb 2020', 'Pengembangan'),
('IDX:H', 'DART',	'Duta Anggada Realty Tbk.', '08 Mei 1990', 'Utama'),
('IDX:H', 'DILD',	'Intiland Development Tbk.', '04 Sep 1991', 'Utama'),
('IDX:H', 'DMAS',	'Puradelta Lestari Tbk.', '29 Mei 2015', 'Utama'),
('IDX:H', 'DUTI',	'Duta Pertiwi Tbk.', '02 Nov 1994', 'Pengembangan'),
('IDX:H', 'ELTY',	'Bakrieland Development Tbk.', '30 Okt 1995', 'UTAMA'),
('IDX:H', 'EMDE',	'Megapolitan Developments Tbk.', '12 Jan 2011', 'Pengembangan'),
('IDX:H', 'FMII',	'Fortune Mate Indonesia Tbk', '30 Jun 2000', 'Pengembangan'),
('IDX:H', 'FORZ',	'Forza Land Indonesia Tbk.', '28 Apr 2017', 'UTAMA'),
('IDX:H', 'GAMA',	'Aksara Global Development Tbk.', '11 Jul 2012', 'UTAMA'),
('IDX:H', 'GMTD',	'Gowa Makassar Tourism Development Tbk.', '11 Des 2000', 'Pengembangan'),
('IDX:H', 'GPRA',	'Perdana Gapuraprima Tbk.', '10 Okt 2007', 'Utama'),
('IDX:H', 'GWSA',	'Greenwood Sejahtera Tbk.', '23 Des 2011', 'UTAMA'),
('IDX:H', 'HOMI',	'Grand House Mulia Tbk.', '10 Sep 2020', 'Pengembangan'),
('IDX:H', 'INDO',	'Royalindo Investa Wijaya Tbk.', '13 Jan 2020', 'Pengembangan'),
('IDX:H', 'INPP',	'Indonesian Paradise Property Tbk.', '12 Jan 2004', 'Pengembangan'),
('IDX:H', 'IPAC',	'Era Graharealty Tbk.', '30 Jun 2021', 'Akselerasi'),
('IDX:H', 'JRPT',	'Jaya Real Property Tbk.', '29 Jun 1994', 'Utama'),
('IDX:H', 'KBAG',	'Karya Bersama Anugerah Tbk.', '08 Apr 2020', 'Pengembangan'),
('IDX:H', 'KIJA',	'Kawasan Industri Jababeka Tbk.', '10 Jan 1995', 'Utama'),
('IDX:H', 'KOTA',	'DMS Propertindo Tbk.', '09 Jul 2019', 'UTAMA'),
('IDX:H', 'LAND',	'Trimitra Propertindo Tbk.', '23 Ags 2018', 'Pengembangan'),
('IDX:H', 'LCGP',	'Eureka Prima Jakarta Tbk.', '13 Jul 2007', 'Pengembangan'),
('IDX:H', 'LPCK',	'Lippo Cikarang Tbk', '24 Jul 1997', 'Utama'),
('IDX:H', 'LPKR',	'Lippo Karawaci Tbk.', '28 Jun 1996', 'Utama'),
('IDX:H', 'LPLI',	'Star Pacific Tbk.', '23 Okt 1989', 'Pengembangan'),
('IDX:H', 'MDLN',	'Modernland Realty Tbk.', '18 Jan 1993', 'Utama'),
('IDX:H', 'MKPI',	'Metropolitan Kentjana Tbk.', '10 Jul 2009', 'PENGEMBANGAN'),
('IDX:H', 'MMLP',	'Mega Manunggal Property Tbk.', '12 Jun 2015', 'Pengembangan'),
('IDX:H', 'MPRO',	'Maha Properti Indonesia Tbk.', '09 Okt 2018', 'Pengembangan'),
('IDX:H', 'MTLA',	'Metropolitan Land Tbk.', '20 Jun 2011', 'UTAMA'),
('IDX:H', 'MTSM',	'Metro Realty Tbk.', '08 Jan 1992', 'Pengembangan'),
('IDX:H', 'MYRX',	'Hanson International Tbk.', '31 Okt 1990', 'Pengembangan'),
('IDX:H', 'NIRO',	'City Retail Developments Tbk.', '13 Sep 2012', 'PENGEMBANGAN'),
('IDX:H', 'NZIA',	'Nusantara Almazia Tbk.', '25 Sep 2019', 'UTAMA'),
('IDX:H', 'OMRE',	'Indonesia Prima Property Tbk', '22 Ags 1994', 'Pengembangan'),
('IDX:H', 'PAMG',	'Bima Sakti Pertiwi Tbk.', '05 Jul 2019', 'Utama'),
('IDX:H', 'PLIN',	'Plaza Indonesia Realty Tbk.', '15 Jun 1992', 'Utama'),
('IDX:H', 'POLI',	'Pollux Hotels Group Tbk.', '10 Jan 2019', 'Pengembangan'),
('IDX:H', 'POLL',	'Pollux Properties Indonesia Tbk.', '11 Jul 2018', 'Utama'),
('IDX:H', 'POSA',	'Bliss Properti Indonesia Tbk.', '10 Mei 2019', 'Pengembangan'),
('IDX:H', 'PPRO',	'PP Properti Tbk.', '19 Mei 2015', 'Utama'),
('IDX:H', 'PUDP',	'Pudjiadi Prestige Tbk.', '18 Nov 1994', 'UTAMA'),
('IDX:H', 'PURI',	'Puri Global Sukses Tbk.', '08 Sep 2020', 'Pengembangan'),
('IDX:H', 'PWON',	'Pakuwon Jati Tbk.', '09 Okt 1989', 'UTAMA'),
('IDX:H', 'RBMS',	'Ristia Bintang Mahkotasejati Tbk.', '19 Des 1997', 'Utama'),
('IDX:H', 'RDTX',	'Roda Vivatex Tbk.', '14 Mei 1990', 'Utama'),
('IDX:H', 'REAL',	'Repower Asia Indonesia Tbk.', '06 Des 2019', 'Pengembangan'),
('IDX:H', 'RIMO',	'Rimo International Lestari Tbk.', '10 Nov 2000', 'Pengembangan'),
('IDX:H', 'ROCK',	'Rockfields Properti Indonesia Tbk.', '10 Sep 2020', 'Pengembangan'),
('IDX:H', 'RODA',	'Pikko Land Development Tbk.', '22 Okt 2001', 'Pengembangan'),
('IDX:H', 'SATU',	'Kota Satu Properti Tbk.', '05 Nov 2018', 'PENGEMBANGAN'),
('IDX:H', 'SMDM',	'Suryamas Dutamakmur Tbk.', '12 Okt 1995', 'Pengembangan'),
('IDX:H', 'SMRA',	'Summarecon Agung Tbk.', '07 Mei 1990', 'Utama'),
('IDX:H', 'TARA',	'Agung Semesta Sejahtera Tbk.', '11 Jul 2014', 'Utama'),
('IDX:H', 'TRIN',	'Perintis Triniti Properti Tbk.', '15 Jan 2020', 'Pengembangan'),
('IDX:H', 'TRUE',	'Triniti Dinamik Tbk.', '10 Jun 2021', 'Pengembangan'),
('IDX:H', 'URBN',	'Urban Jakarta Propertindo Tbk.', '10 Des 2018', 'Pengembangan')
;"""
