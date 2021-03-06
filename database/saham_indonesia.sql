-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 23 Mar 2022 pada 11.45
-- Versi server: 10.4.20-MariaDB
-- Versi PHP: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `saham_indonesia`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `daftar_saham_indonesia`
--

CREATE TABLE `daftar_saham_indonesia` (
  `id` int(11) NOT NULL,
  `kode_sektor` varchar(10) DEFAULT NULL,
  `sektor_usaha` varchar(100) DEFAULT NULL,
  `kodeSaham` varchar(4) DEFAULT NULL,
  `namaEmiten` varchar(100) DEFAULT NULL,
  `tglListing` varchar(100) DEFAULT NULL,
  `papanBursa` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `daftar_saham_indonesia`
--

INSERT INTO `daftar_saham_indonesia` (`id`, `kode_sektor`, `sektor_usaha`, `kodeSaham`, `namaEmiten`, `tglListing`, `papanBursa`) VALUES
(1, 'IDX:A', 'Energi', 'ADMR', 'Adaro Minerals Indonesia Tbk.', '2022-01-03', 'Pengembangan'),
(2, 'IDX:A', 'Energi', 'ADRO', 'Adaro Energy Tbk.', '2008-07-16', 'Utama'),
(3, 'IDX:A', 'Energi', 'AIMS', 'Akbar Indo Makmur Stimec Tbk.', '2001-07-20', 'Pengembangan'),
(4, 'IDX:A', 'Energi', 'AKRA', 'AKR Corporindo Tbk.', '1994-10-03', 'Utama'),
(5, 'IDX:A', 'Energi', 'APEX', 'Apexindo Pratama Duta Tbk.', '2013-06-05', 'Pengembangan'),
(6, 'IDX:A', 'Energi', 'ARII', 'Atlas Resources Tbk.', '2011-11-08', 'Pengembangan'),
(7, 'IDX:A', 'Energi', 'ARTI', 'Ratu Prabu Energi Tbk.', '2003-04-30', 'Utama'),
(8, 'IDX:A', 'Energi', 'BBRM', 'Pelayaran Nasional Bina Buana Raya Tbk', '2013-01-09', 'Utama'),
(9, 'IDX:A', 'Energi', 'BESS', 'Batulicin Nusantara Maritim Tbk.', '2020-03-09', 'Pengembangan'),
(10, 'IDX:A', 'Energi', 'BIPI', 'Astrindo Nusantara infrastruktur Tbk', '2010-02-11', 'Pengembangan'),
(11, 'IDX:A', 'Energi', 'BOSS', 'Borneo Olah Sarana Sukses Tbk.', '2018-02-15', 'Pengembangan'),
(12, 'IDX:A', 'Energi', 'BSML', 'Bintang Samudera Mandiri Lines Tbk.', '2021-12-16', 'Pengembangan'),
(13, 'IDX:A', 'Energi', 'BSSR', 'Baramulti Suksessarana Tbk.', '2012-11-08', 'Pengembangan'),
(14, 'IDX:A', 'Energi', 'BULL', 'Buana Lintas Lautan Tbk.', '2011-05-23', 'Utama'),
(15, 'IDX:A', 'Energi', 'BUMI', 'Bumi Resources Tbk.', '1990-07-30', 'Pengembangan'),
(16, 'IDX:A', 'Energi', 'BYAN', 'Bayan Resources Tbk.', '2008-08-12', 'Utama'),
(17, 'IDX:A', 'Energi', 'CANI', 'Capitol Nusantara Indonesia Tbk.', '2014-01-16', 'Pengembangan'),
(18, 'IDX:A', 'Energi', 'CNKO', 'Exploitasi Energi Indonesia Tbk.', '2001-11-20', 'Utama'),
(19, 'IDX:A', 'Energi', 'DEWA', 'Darma Henwa Tbk.', '2007-09-26', 'Utama'),
(20, 'IDX:A', 'Energi', 'DOID', 'Delta Dunia Makmur Tbk.', '2001-06-15', 'Utama'),
(21, 'IDX:A', 'Energi', 'DSSA', 'Dian Swastatika Sentosa Tbk.', '2009-12-10', 'Utama'),
(22, 'IDX:A', 'Energi', 'DWGL', 'Dwi Guna Laksana Tbk.', '2017-12-13', 'Pengembangan'),
(23, 'IDX:A', 'Energi', 'ELSA', 'Elnusa Tbk.', '2008-02-06', 'Utama'),
(24, 'IDX:A', 'Energi', 'ENRG', 'Energi Mega Persada Tbk.', '2004-06-07', 'Pengembangan'),
(25, 'IDX:A', 'Energi', 'ETWA', 'Eterindo Wahanatama Tbk', '1997-05-16', 'Utama'),
(26, 'IDX:A', 'Energi', 'FIRE', 'Alfa Energi Investama Tbk.', '2017-06-09', 'Pengembangan'),
(27, 'IDX:A', 'Energi', 'GEMS', 'Golden Energy Mines Tbk.', '2011-11-17', 'Utama'),
(28, 'IDX:A', 'Energi', 'GTBO', 'Garda Tujuh Buana Tbk', '2009-07-09', 'Pengembangan'),
(29, 'IDX:A', 'Energi', 'GTSI', 'GTS Internasional Tbk.', '2021-09-08', 'Utama'),
(30, 'IDX:A', 'Energi', 'HITS', 'Humpuss Intermoda Transportasi Tbk.', '1997-12-15', 'Utama'),
(31, 'IDX:A', 'Energi', 'HRUM', 'Harum Energy Tbk.', '2010-10-06', 'Utama'),
(32, 'IDX:A', 'Energi', 'INDY', 'Indika Energy Tbk.', '2008-06-11', 'Utama'),
(33, 'IDX:A', 'Energi', 'INPS', 'Indah Prakasa Sentosa Tbk.', '2018-04-06', 'Pengembangan'),
(34, 'IDX:A', 'Energi', 'ITMA', 'Sumber Energi Andalan Tbk.', '1990-12-10', 'Pengembangan'),
(35, 'IDX:A', 'Energi', 'ITMG', 'Indo Tambangraya Megah Tbk.', '2007-12-18', 'Utama'),
(36, 'IDX:A', 'Energi', 'JSKY', 'Sky Energy Indonesia Tbk.', '2018-03-28', 'Utama'),
(37, 'IDX:A', 'Energi', 'KKGI', 'Resource Alam Indonesia Tbk.', '1991-07-01', 'Utama'),
(38, 'IDX:A', 'Energi', 'KOPI', 'Mitra Energi Persada Tbk.', '2015-05-04', 'PENGEMBANGAN'),
(39, 'IDX:A', 'Energi', 'LEAD', 'Logindo Samudramakmur Tbk.', '2013-12-11', 'UTAMA'),
(40, 'IDX:A', 'Energi', 'MBAP', 'Mitrabara Adiperdana Tbk.', '2014-07-10', 'Pengembangan'),
(41, 'IDX:A', 'Energi', 'MBSS', 'Mitrabahtera Segara Sejati Tbk', '2011-04-06', 'Utama'),
(42, 'IDX:A', 'Energi', 'MCOL', 'Prima Andalan Mandiri Tbk.', '2021-09-07', 'Utama'),
(43, 'IDX:A', 'Energi', 'MEDC', 'Medco Energi Internasional Tbk.', '1994-10-12', 'Utama'),
(44, 'IDX:A', 'Energi', 'MITI', 'Mitra Investindo Tbk.', '1997-07-16', 'Pengembangan'),
(45, 'IDX:A', 'Energi', 'MTFN', 'Capitalinc Investment Tbk.', '1990-04-16', 'Pengembangan'),
(46, 'IDX:A', 'Energi', 'MYOH', 'Samindo Resources Tbk.', '2000-07-27', 'Utama'),
(47, 'IDX:A', 'Energi', 'PGAS', 'Perusahaan Gas Negara Tbk.', '2003-12-15', 'Utama'),
(48, 'IDX:A', 'Energi', 'PKPK', 'Perdana Karya Perkasa Tbk.', '2007-07-11', 'Pengembangan'),
(49, 'IDX:A', 'Energi', 'PSSI', 'Pelita Samudera Shipping Tbk.', '2017-12-05', 'Utama'),
(50, 'IDX:A', 'Energi', 'PTBA', 'Bukit Asam Tbk.', '2002-12-23', 'Utama'),
(51, 'IDX:A', 'Energi', 'PTIS', 'Indo Straits Tbk.', '2011-07-12', 'Utama'),
(52, 'IDX:A', 'Energi', 'PTRO', 'Petrosea Tbk.', '1990-05-21', 'Utama'),
(53, 'IDX:A', 'Energi', 'RAJA', 'Rukun Raharja Tbk.', '2006-04-19', 'Utama'),
(54, 'IDX:A', 'Energi', 'RIGS', 'Rig Tenders Indonesia Tbk.', '1990-03-05', 'Pengembangan'),
(55, 'IDX:A', 'Energi', 'RMKE', 'RMK Energy Tbk.', '2021-12-07', 'Utama'),
(56, 'IDX:A', 'Energi', 'RUIS', 'Radiant Utama Interinsco Tbk.', '2006-07-12', 'Pengembangan'),
(57, 'IDX:A', 'Energi', 'SEMA', 'Semacom Integrated Tbk.', '2022-01-10', 'Pengembangan'),
(58, 'IDX:A', 'Energi', 'SGER', 'Sumber Global Energy Tbk.', '2020-08-10', 'Pengembangan'),
(59, 'IDX:A', 'Energi', 'SHIP', 'Sillo Maritime Perdana Tbk.', '2016-06-16', 'Pengembangan'),
(60, 'IDX:A', 'Energi', 'SMMT', 'Golden Eagle Energy Tbk.', '1997-12-01', 'PENGEMBANGAN'),
(61, 'IDX:A', 'Energi', 'SMRU', 'SMR Utama Tbk.', '2011-10-10', 'Pengembangan'),
(62, 'IDX:A', 'Energi', 'SOCI', 'Soechi Lines Tbk.', '2014-12-03', 'Utama'),
(63, 'IDX:A', 'Energi', 'SUGI', 'Sugih Energy Tbk.', '2002-06-19', 'PENGEMBANGAN'),
(64, 'IDX:A', 'Energi', 'SURE', 'Super Energy Tbk.', '2018-10-05', 'PENGEMBANGAN'),
(65, 'IDX:A', 'Energi', 'TAMU', 'Pelayaran Tamarin Samudra Tbk.', '2017-05-10', 'Pengembangan'),
(66, 'IDX:A', 'Energi', 'TCPI', 'Transcoal Pacific Tbk.', '2018-07-06', 'Pengembangan'),
(67, 'IDX:A', 'Energi', 'TEBE', 'Dana Brata Luhur Tbk.', '2019-11-18', 'PENGEMBANGAN'),
(68, 'IDX:A', 'Energi', 'TOBA', 'TBS Energi Utama Tbk.', '2012-07-06', 'Utama'),
(69, 'IDX:A', 'Energi', 'TPMA', 'Trans Power Marine Tbk.', '2013-02-20', 'Pengembangan'),
(70, 'IDX:A', 'Energi', 'TRAM', 'Trada Alam Minera Tbk.', '2008-09-10', 'Utama'),
(71, 'IDX:A', 'Energi', 'UNIQ', 'Ulima Nitra Tbk.', '2021-03-08', 'Utama'),
(72, 'IDX:A', 'Energi', 'WINS', 'Wintermar Offshore Marine Tbk.', '2010-11-29', 'Utama'),
(73, 'IDX:A', 'Energi', 'WOWS', 'Ginting Jaya Energi Tbk.', '2019-11-08', 'Pengembangan'),
(74, 'IDX:H', 'Properti & Real Estate', 'ADCP', 'Adhi Commuter Properti Tbk.', '2021-05-21', 'Utama'),
(75, 'IDX:H', 'Properti & Real Estate', 'AMAN', 'Makmur Berkah Amanda Tbk.', '2020-03-13', 'Utama'),
(76, 'IDX:H', 'Properti & Real Estate', 'APLN', 'Agung Podomoro Land Tbk.', '2010-11-11', 'Utama'),
(77, 'IDX:H', 'Properti & Real Estate', 'ARMY', 'Armidian Karyatama Tbk.', '2017-06-21', 'Pengembangan'),
(78, 'IDX:H', 'Properti & Real Estate', 'ASPI', 'Andalan Sakti Primaindo Tbk.', '2020-02-17', 'Pengembangan'),
(79, 'IDX:H', 'Properti & Real Estate', 'ASRI', 'Alam Sutera Realty Tbk.', '2007-12-18', 'Utama'),
(80, 'IDX:H', 'Properti & Real Estate', 'ATAP', 'Trimitra Prawara Goldland Tbk.', '2020-12-11', 'Pengembangan'),
(81, 'IDX:H', 'Properti & Real Estate', 'BAPA', 'Bekasi Asri Pemula Tbk.', '2008-01-14', 'Utama'),
(82, 'IDX:H', 'Properti & Real Estate', 'BAPI', 'Bhakti Agung Propertindo Tbk.', '2019-09-16', 'Pengembangan'),
(83, 'IDX:H', 'Properti & Real Estate', 'BBSS', 'Bumi Benowo Sukses Sejahtera Tbk.', '2020-04-15', 'Pengembangan'),
(84, 'IDX:H', 'Properti & Real Estate', 'BCIP', 'Bumi Citra Permai Tbk.', '2009-12-11', 'Pengembangan'),
(85, 'IDX:H', 'Properti & Real Estate', 'BEST', 'Bekasi Fajar Industrial Estate Tbk.', '2012-04-10', 'Utama'),
(86, 'IDX:H', 'Properti & Real Estate', 'BIKA', 'Binakarya Jaya Abadi Tbk.', '2015-07-14', 'Pengembangan'),
(87, 'IDX:H', 'Properti & Real Estate', 'BIPP', 'Bhuwanatala Indah Permai Tbk.', '1995-10-23', 'Pengembangan'),
(88, 'IDX:H', 'Properti & Real Estate', 'BKDP', 'Bukit Darmo Property Tbk.', '2007-06-15', 'Pengembangan'),
(89, 'IDX:H', 'Properti & Real Estate', 'BKSL', 'Sentul City Tbk.', '1997-07-28', 'Utama'),
(90, 'IDX:H', 'Properti & Real Estate', 'BSDE', 'Bumi Serpong Damai Tbk.', '2008-06-06', 'Utama'),
(91, 'IDX:H', 'Properti & Real Estate', 'CITY', 'Natura City Developments Tbk.', '2018-09-28', 'Utama'),
(92, 'IDX:H', 'Properti & Real Estate', 'COWL', 'Cowell Development Tbk.', '2007-12-19', 'PENGEMBANGAN'),
(93, 'IDX:H', 'Properti & Real Estate', 'CPRI', 'Capri Nusa Satu Properti Tbk.', '2019-04-11', 'PENGEMBANGAN'),
(94, 'IDX:H', 'Properti & Real Estate', 'CSIS', 'Cahayasakti Investindo Sukses Tbk.', '2017-05-10', 'Pengembangan'),
(95, 'IDX:H', 'Properti & Real Estate', 'CTRA', 'Ciputra Development Tbk.', '1994-03-28', 'Utama'),
(96, 'IDX:H', 'Properti & Real Estate', 'DADA', 'Diamond Citra Propertindo Tbk.', '2020-02-14', 'Pengembangan'),
(97, 'IDX:H', 'Properti & Real Estate', 'DART', 'Duta Anggada Realty Tbk.', '1990-05-08', 'Utama'),
(98, 'IDX:H', 'Properti & Real Estate', 'DILD', 'Intiland Development Tbk.', '1991-09-04', 'Utama'),
(99, 'IDX:H', 'Properti & Real Estate', 'DMAS', 'Puradelta Lestari Tbk.', '2015-05-29', 'Utama'),
(100, 'IDX:H', 'Properti & Real Estate', 'DUTI', 'Duta Pertiwi Tbk.', '1994-11-02', 'Pengembangan'),
(101, 'IDX:H', 'Properti & Real Estate', 'ELTY', 'Bakrieland Development Tbk.', '1995-10-30', 'UTAMA'),
(102, 'IDX:H', 'Properti & Real Estate', 'EMDE', 'Megapolitan Developments Tbk.', '2011-01-12', 'Pengembangan'),
(103, 'IDX:H', 'Properti & Real Estate', 'FMII', 'Fortune Mate Indonesia Tbk', '2000-06-30', 'Pengembangan'),
(104, 'IDX:H', 'Properti & Real Estate', 'FORZ', 'Forza Land Indonesia Tbk.', '2017-04-28', 'UTAMA'),
(105, 'IDX:H', 'Properti & Real Estate', 'GAMA', 'Aksara Global Development Tbk.', '2012-07-11', 'UTAMA'),
(106, 'IDX:H', 'Properti & Real Estate', 'GMTD', 'Gowa Makassar Tourism Development Tbk.', '2000-12-11', 'Pengembangan'),
(107, 'IDX:H', 'Properti & Real Estate', 'GPRA', 'Perdana Gapuraprima Tbk.', '2007-10-10', 'Utama'),
(108, 'IDX:H', 'Properti & Real Estate', 'GWSA', 'Greenwood Sejahtera Tbk.', '2011-12-23', 'UTAMA'),
(109, 'IDX:H', 'Properti & Real Estate', 'HOMI', 'Grand House Mulia Tbk.', '2020-09-10', 'Pengembangan'),
(110, 'IDX:H', 'Properti & Real Estate', 'INDO', 'Royalindo Investa Wijaya Tbk.', '2020-01-13', 'Pengembangan'),
(111, 'IDX:H', 'Properti & Real Estate', 'INPP', 'Indonesian Paradise Property Tbk.', '2004-01-12', 'Pengembangan'),
(112, 'IDX:H', 'Properti & Real Estate', 'IPAC', 'Era Graharealty Tbk.', '2021-06-30', 'Akselerasi'),
(113, 'IDX:H', 'Properti & Real Estate', 'JRPT', 'Jaya Real Property Tbk.', '1994-06-29', 'Utama'),
(114, 'IDX:H', 'Properti & Real Estate', 'KBAG', 'Karya Bersama Anugerah Tbk.', '2020-04-08', 'Pengembangan'),
(115, 'IDX:H', 'Properti & Real Estate', 'KIJA', 'Kawasan Industri Jababeka Tbk.', '1995-01-10', 'Utama'),
(116, 'IDX:H', 'Properti & Real Estate', 'KOTA', 'DMS Propertindo Tbk.', '2019-07-09', 'UTAMA'),
(117, 'IDX:H', 'Properti & Real Estate', 'LAND', 'Trimitra Propertindo Tbk.', '2018-08-23', 'Pengembangan'),
(118, 'IDX:H', 'Properti & Real Estate', 'LCGP', 'Eureka Prima Jakarta Tbk.', '2007-07-13', 'Pengembangan'),
(119, 'IDX:H', 'Properti & Real Estate', 'LPCK', 'Lippo Cikarang Tbk', '1997-07-24', 'Utama'),
(120, 'IDX:H', 'Properti & Real Estate', 'LPKR', 'Lippo Karawaci Tbk.', '1996-06-28', 'Utama'),
(121, 'IDX:H', 'Properti & Real Estate', 'LPLI', 'Star Pacific Tbk.', '1989-10-23', 'Pengembangan'),
(122, 'IDX:H', 'Properti & Real Estate', 'MDLN', 'Modernland Realty Tbk.', '1993-01-18', 'Utama'),
(123, 'IDX:H', 'Properti & Real Estate', 'MKPI', 'Metropolitan Kentjana Tbk.', '2009-01-10', 'PENGEMBANGAN'),
(124, 'IDX:H', 'Properti & Real Estate', 'MMLP', 'Mega Manunggal Property Tbk.', '2015-06-12', 'Pengembangan'),
(125, 'IDX:H', 'Properti & Real Estate', 'MPRO', 'Maha Properti Indonesia Tbk.', '2018-10-09', 'Pengembangan'),
(126, 'IDX:H', 'Properti & Real Estate', 'MTLA', 'Metropolitan Land Tbk.', '2011-06-20', 'UTAMA'),
(127, 'IDX:H', 'Properti & Real Estate', 'MTSM', 'Metro Realty Tbk.', '1992-01-08', 'Pengembangan'),
(128, 'IDX:H', 'Properti & Real Estate', 'MYRX', 'Hanson International Tbk.', '1990-10-31', 'Pengembangan'),
(129, 'IDX:H', 'Properti & Real Estate', 'NIRO', 'City Retail Developments Tbk.', '2012-09-13', 'PENGEMBANGAN'),
(130, 'IDX:H', 'Properti & Real Estate', 'NZIA', 'Nusantara Almazia Tbk.', '2019-09-25', 'UTAMA'),
(131, 'IDX:H', 'Properti & Real Estate', 'OMRE', 'Indonesia Prima Property Tbk', '1994-08-22', 'Pengembangan'),
(132, 'IDX:H', 'Properti & Real Estate', 'PAMG', 'Bima Sakti Pertiwi Tbk.', '2019-07-05', 'Utama'),
(133, 'IDX:H', 'Properti & Real Estate', 'PLIN', 'Plaza Indonesia Realty Tbk.', '1992-06-15', 'Utama'),
(134, 'IDX:H', 'Properti & Real Estate', 'POLI', 'Pollux Hotels Group Tbk.', '2019-01-10', 'Pengembangan'),
(135, 'IDX:H', 'Properti & Real Estate', 'POLL', 'Pollux Properties Indonesia Tbk.', '2018-07-11', 'Utama'),
(136, 'IDX:H', 'Properti & Real Estate', 'POSA', 'Bliss Properti Indonesia Tbk.', '2019-05-10', 'Pengembangan'),
(137, 'IDX:H', 'Properti & Real Estate', 'PPRO', 'PP Properti Tbk.', '2015-05-19', 'Utama'),
(138, 'IDX:H', 'Properti & Real Estate', 'PUDP', 'Pudjiadi Prestige Tbk.', '1994-11-18', 'UTAMA'),
(139, 'IDX:H', 'Properti & Real Estate', 'PURI', 'Puri Global Sukses Tbk.', '2020-09-08', 'Pengembangan'),
(140, 'IDX:H', 'Properti & Real Estate', 'PWON', 'Pakuwon Jati Tbk.', '1989-10-09', 'UTAMA'),
(141, 'IDX:H', 'Properti & Real Estate', 'RBMS', 'Ristia Bintang Mahkotasejati Tbk.', '1997-12-19', 'Utama'),
(142, 'IDX:H', 'Properti & Real Estate', 'RDTX', 'Roda Vivatex Tbk.', '1990-05-14', 'Utama'),
(143, 'IDX:H', 'Properti & Real Estate', 'REAL', 'Repower Asia Indonesia Tbk.', '2019-12-06', 'Pengembangan'),
(144, 'IDX:H', 'Properti & Real Estate', 'RIMO', 'Rimo International Lestari Tbk.', '2000-11-10', 'Pengembangan'),
(145, 'IDX:H', 'Properti & Real Estate', 'ROCK', 'Rockfields Properti Indonesia Tbk.', '2020-09-10', 'Pengembangan'),
(146, 'IDX:H', 'Properti & Real Estate', 'RODA', 'Pikko Land Development Tbk.', '2001-10-22', 'Pengembangan'),
(147, 'IDX:H', 'Properti & Real Estate', 'SATU', 'Kota Satu Properti Tbk.', '2018-11-05', 'PENGEMBANGAN'),
(148, 'IDX:H', 'Properti & Real Estate', 'SMDM', 'Suryamas Dutamakmur Tbk.', '1995-10-12', 'Pengembangan'),
(149, 'IDX:H', 'Properti & Real Estate', 'SMRA', 'Summarecon Agung Tbk.', '1990-05-07', 'Utama'),
(150, 'IDX:H', 'Properti & Real Estate', 'TARA', 'Agung Semesta Sejahtera Tbk.', '2014-07-11', 'Utama'),
(151, 'IDX:H', 'Properti & Real Estate', 'TRIN', 'Perintis Triniti Properti Tbk.', '2020-01-15', 'Pengembangan'),
(152, 'IDX:H', 'Properti & Real Estate', 'TRUE', 'Triniti Dinamik Tbk.', '2021-06-10', 'Pengembangan'),
(153, 'IDX:H', 'Properti & Real Estate', 'URBN', 'Urban Jakarta Propertindo Tbk.', '2018-12-10', 'Pengembangan'),
(154, 'IDX:I', 'Teknologi', 'ATIC', 'Anabatic Technologies Tbk.', '2015-07-08', 'Utama'),
(155, 'IDX:I', 'Teknologi', 'BUKA', 'Bukalapak.com Tbk.', '2021-08-06', 'Pengembangan'),
(156, 'IDX:I', 'Teknologi', 'CASH', 'Cashlez Worldwide Indonesia Tbk.', '2020-05-04', 'Akselerasi'),
(157, 'IDX:I', 'Teknologi', 'DCII', 'DCI Indonesia Tbk.', '2021-01-06', 'Pengembangan'),
(158, 'IDX:I', 'Teknologi', 'DIVA', 'Distribusi Voucher Nusantara Tbk.', '2018-11-27', 'Pengembangan'),
(159, 'IDX:I', 'Teknologi', 'DMMX', 'Digital Mediatama Maxima Tbk.', '2019-10-21', 'Pengembangan'),
(160, 'IDX:I', 'Teknologi', 'EDGE', 'Indointernet Tbk.', '2021-02-08', 'Pengembangan'),
(161, 'IDX:I', 'Teknologi', 'EMTK', 'Elang Mahkota Teknologi Tbk.', '2010-01-12', 'Utama'),
(162, 'IDX:I', 'Teknologi', 'ENVY', 'Envy Technologies Indonesia Tbk.', '2019-07-08', 'Pengembangan'),
(163, 'IDX:I', 'Teknologi', 'GLVA', 'Galva Technologies Tbk.', '2019-12-23', 'Pengembangan'),
(164, 'IDX:I', 'Teknologi', 'HDIT', 'Hensel Davest Indonesia Tbk.', '2019-07-12', 'Utama'),
(165, 'IDX:I', 'Teknologi', 'KIOS', 'Kioson Komersial Indonesia Tbk.', '2017-10-05', 'Pengembangan'),
(166, 'IDX:I', 'Teknologi', 'KREN', 'Kresna Graha Investama Tbk.', '2002-06-28', 'Utama'),
(167, 'IDX:I', 'Teknologi', 'LMAS', 'Limas Indonesia Makmur Tbk.', '2001-12-28', 'Pengembangan'),
(168, 'IDX:I', 'Teknologi', 'LUCK', 'Sentral Mitra Informatika Tbk.', '2018-11-28', 'Pengembangan'),
(169, 'IDX:I', 'Teknologi', 'MCAS', 'M Cash Integrasi Tbk.', '2017-11-01', 'Pengembangan'),
(170, 'IDX:I', 'Teknologi', 'MLPT', 'Multipolar Technology Tbk.', '2013-07-08', 'Utama'),
(171, 'IDX:I', 'Teknologi', 'MTDL', 'Metrodata Electronics Tbk.', '1990-04-09', 'Utama'),
(172, 'IDX:I', 'Teknologi', 'NFCX', 'NFC Indonesia Tbk.', '2018-07-12', 'Pengembangan'),
(173, 'IDX:I', 'Teknologi', 'PGJO', 'Tourindo Guide Indonesia Tbk.', '2020-01-08', 'Akselerasi'),
(174, 'IDX:I', 'Teknologi', 'PTSN', 'Sat Nusapersada Tbk', '2007-11-08', 'Utama'),
(175, 'IDX:I', 'Teknologi', 'RUNS', 'Global Sukses Solusi Tbk.', '2021-09-08', 'Akselerasi'),
(176, 'IDX:I', 'Teknologi', 'SKYB', 'Northcliff Citranusa Indonesia Tbk.', '2010-07-07', 'PENGEMBANGAN'),
(177, 'IDX:I', 'Teknologi', 'TECH', 'Indosterling Technomedia Tbk.', '2020-06-04', 'Pengembangan'),
(178, 'IDX:I', 'Teknologi', 'TFAS', 'Telefast Indonesia Tbk.', '2019-09-17', 'Pengembangan'),
(179, 'IDX:I', 'Teknologi', 'UVCR', 'Trimegah Karya Pratama Tbk.', '2021-07-27', 'Akselerasi'),
(180, 'IDX:I', 'Teknologi', 'WGSH', 'Wira Global Solusi Tbk.', '2021-12-06', 'Akselerasi'),
(181, 'IDX:I', 'Teknologi', 'ZYRX', 'Zyrexindo Mandiri Buana Tbk.', '2021-03-30', 'Pengembangan'),
(182, 'IDX:K', 'Transportasi & Logistik', 'AKSI', 'Mineral Sumberdaya Mandiri Tbk.', '2001-07-13', 'Pengembangan'),
(183, 'IDX:K', 'Transportasi & Logistik', 'ASSA', 'Adi Sarana Armada Tbk.', '2012-11-12', 'Utama'),
(184, 'IDX:K', 'Transportasi & Logistik', 'BIRD', 'Blue Bird Tbk.', '2014-11-05', 'UTAMA'),
(185, 'IDX:K', 'Transportasi & Logistik', 'BLTA', 'Berlian Laju Tanker Tbk.', '1990-03-26', 'Utama'),
(186, 'IDX:K', 'Transportasi & Logistik', 'BPTR', 'Batavia Prosperindo Trans Tbk.', '2018-07-09', 'Utama'),
(187, 'IDX:K', 'Transportasi & Logistik', 'CMPP', 'AirAsia Indonesia Tbk.', '1994-12-08', 'Pengembangan'),
(188, 'IDX:K', 'Transportasi & Logistik', 'DEAL', 'Dewata Freightinternational Tbk.', '2018-11-11', 'Pengembangan'),
(189, 'IDX:K', 'Transportasi & Logistik', 'GIAA', 'Garuda Indonesia (Persero) Tbk.', '2011-02-11', 'Utama'),
(190, 'IDX:K', 'Transportasi & Logistik', 'HAIS', 'Hasnur Internasional Shipping Tbk.', '2021-09-01', 'Utama'),
(191, 'IDX:K', 'Transportasi & Logistik', 'HELI', 'Jaya Trishindo Tbk.', '2018-03-27', 'Pengembangan'),
(192, 'IDX:K', 'Transportasi & Logistik', 'IATA', 'Indonesia Transport & Infrastructure Tbk.', '2006-09-13', 'Pengembangan'),
(193, 'IDX:K', 'Transportasi & Logistik', 'JAYA', 'Armada Berjaya Trans Tbk.', '2019-02-21', 'Pengembangan'),
(194, 'IDX:K', 'Transportasi & Logistik', 'KJEN', 'Krida Jaringan Nusantara Tbk.', '2019-07-01', 'Pengembangan'),
(195, 'IDX:K', 'Transportasi & Logistik', 'LRNA', 'Eka Sari Lorena Transport Tbk.', '2014-04-15', 'Pengembangan'),
(196, 'IDX:K', 'Transportasi & Logistik', 'MIRA', 'Mitra International Resources Tbk.', '1997-01-30', 'Pengembangan'),
(197, 'IDX:K', 'Transportasi & Logistik', 'NELY', 'Pelayaran Nelly Dwi Putri Tbk.', '2012-10-11', 'Pengembangan'),
(198, 'IDX:K', 'Transportasi & Logistik', 'PPGL', 'Prima Globalindo Logistik Tbk.', '2020-07-20', 'Akselerasi'),
(199, 'IDX:K', 'Transportasi & Logistik', 'PURA', 'Putra Rajawali Kencana Tbk.', '2020-01-22', 'Pengembangan'),
(200, 'IDX:K', 'Transportasi & Logistik', 'SAFE', 'Steady Safe Tbk.', '1994-08-15', 'PENGEMBANGAN'),
(201, 'IDX:K', 'Transportasi & Logistik', 'SAPX', 'Satria Antaran Prima Tbk.', '2018-10-03', 'Pengembangan'),
(202, 'IDX:K', 'Transportasi & Logistik', 'SDMU', 'Sidomulyo Selaras Tbk.', '2011-07-12', 'Pengembangan'),
(203, 'IDX:K', 'Transportasi & Logistik', 'SMDR', 'Samudera Indonesia Tbk.', '1999-07-05', 'Utama'),
(204, 'IDX:K', 'Transportasi & Logistik', 'TAXI', 'Express Transindo Utama Tbk.', '2012-11-02', 'Utama'),
(205, 'IDX:K', 'Transportasi & Logistik', 'TMAS', 'Temas Tbk.', '2003-07-09', 'Utama'),
(206, 'IDX:K', 'Transportasi & Logistik', 'TNCA', 'Trimuda Nuansa Citra Tbk.', '2018-06-28', 'Pengembangan'),
(207, 'IDX:K', 'Transportasi & Logistik', 'TRJA', 'Transkon Jaya Tbk.', '2020-08-27', 'Pengembangan'),
(208, 'IDX:K', 'Transportasi & Logistik', 'TRUK', 'Guna Timur Raya Tbk.', '2018-05-23', 'PENGEMBANGAN'),
(209, 'IDX:K', 'Transportasi & Logistik', 'WEHA', 'WEHA Transportasi Indonesia Tbk.', '2007-05-31', 'Utama'),
(212, 'IDX:F', 'Kesehatan', 'BMHS', 'Bundamedik Tbk.', '2021-07-06', 'Utama'),
(213, 'IDX:F', 'Kesehatan', 'CARE', 'Metro Healthcare Indonesia Tbk.', '2020-03-13', 'Pengembangan'),
(214, 'IDX:F', 'Kesehatan', 'DGNS', 'Diagnos Laboratorium Utama Tbk.', '2021-01-15', 'Pengembangan'),
(215, 'IDX:F', 'Kesehatan', 'DVLA', 'Darya-Varia Laboratoria Tbk.', '1994-11-11', 'Utama'),
(216, 'IDX:F', 'Kesehatan', 'HEAL', 'Medikaloka Hermina Tbk.', '2018-05-16', 'Utama'),
(217, 'IDX:F', 'Kesehatan', 'INAF', 'Indofarma Tbk.', '2001-04-17', 'Utama'),
(218, 'IDX:F', 'Kesehatan', 'IRRA', 'Itama Ranoraya Tbk.', '2019-10-15', 'Pengembangan'),
(219, 'IDX:F', 'Kesehatan', 'KAEF', 'Kimia Farma Tbk.', '2001-07-04', 'Utama'),
(220, 'IDX:F', 'Kesehatan', 'KLBF', 'Kalbe Farma Tbk.', '1991-07-30', 'Utama'),
(221, 'IDX:F', 'Kesehatan', 'MERK', 'Merck Tbk.', '1981-07-23', 'PENGEMBANGAN'),
(222, 'IDX:F', 'Kesehatan', 'MIKA', 'Mitra Keluarga Karyasehat Tbk.', '2015-03-24', 'Utama'),
(223, 'IDX:F', 'Kesehatan', 'PEHA', 'Phapros Tbk.', '2018-12-26', 'Utama'),
(224, 'IDX:F', 'Kesehatan', 'PRDA', 'Prodia Widyahusada Tbk.', '2016-12-07', 'Utama'),
(225, 'IDX:F', 'Kesehatan', 'PRIM', 'Royal Prima Tbk.', '2018-05-15', 'Pengembangan'),
(226, 'IDX:F', 'Kesehatan', 'PYFA', 'Pyridam Farma Tbk.', '2001-10-16', 'Pengembangan'),
(227, 'IDX:F', 'Kesehatan', 'RSGK', 'Kedoya Adyaraya Tbk.', '2021-09-08', 'Utama'),
(228, 'IDX:F', 'Kesehatan', 'SAME', 'Sarana Meditama Metropolitan Tbk.', '2013-01-11', 'Pengembangan'),
(229, 'IDX:F', 'Kesehatan', 'SCPI', 'Organon Pharma Indonesia Tbk.', '1990-06-08', 'PENGEMBANGAN'),
(230, 'IDX:F', 'Kesehatan', 'SIDO', 'Industri Jamu dan Farmasi Sidomuncul Tbk', '2013-12-18', 'Utama'),
(231, 'IDX:F', 'Kesehatan', 'SILO', 'Siloam International Hospitals Tbk.', '2013-09-12', 'Utama'),
(232, 'IDX:F', 'Kesehatan', 'SOHO', 'Soho Global Health Tbk.', '2020-09-08', 'Utama'),
(233, 'IDX:F', 'Kesehatan', 'SRAJ', 'Sejahteraraya Anugrahjaya Tbk.', '2011-04-11', 'Utama'),
(234, 'IDX:F', 'Kesehatan', 'TSPC', 'Tempo Scan Pacific Tbk.', '1994-06-17', 'Utama'),
(237, 'IDX:J', 'Infrastruktur', 'ACST', 'Acset Indonusa Tbk.', '2013-06-24', 'Utama'),
(238, 'IDX:J', 'Infrastruktur', 'ADHI', 'Adhi Karya (Persero) Tbk.', '2004-03-18', 'Utama'),
(239, 'IDX:J', 'Infrastruktur', 'BALI', 'Bali Towerindo Sentra Tbk.', '2014-03-13', 'Utama'),
(240, 'IDX:J', 'Infrastruktur', 'BTEL', 'Bakrie Telecom Tbk.', '2006-02-03', 'Utama'),
(241, 'IDX:J', 'Infrastruktur', 'BUKK', 'Bukaka Teknik Utama Tbk.', '2015-06-29', 'Pengembangan'),
(242, 'IDX:J', 'Infrastruktur', 'CASS', 'Cardig Aero Services Tbk.', '2011-12-05', 'Pengembangan'),
(243, 'IDX:J', 'Infrastruktur', 'CENT', 'Centratama Telekomunikasi Indonesia Tbk', '2001-11-01', 'Pengembangan'),
(244, 'IDX:J', 'Infrastruktur', 'CMNP', 'Citra Marga Nusaphala Persada Tbk.', '1995-01-10', 'Utama'),
(245, 'IDX:J', 'Infrastruktur', 'DGIK', 'Nusa Konstruksi Enjiniring Tbk.', '2007-12-19', 'Utama'),
(246, 'IDX:J', 'Infrastruktur', 'EXCL', 'XL Axiata Tbk.', '2005-09-29', 'Utama'),
(247, 'IDX:J', 'Infrastruktur', 'FIMP', 'Fimperkasa Utama Tbk.', '2021-04-09', 'Akselerasi'),
(248, 'IDX:J', 'Infrastruktur', 'FREN', 'Smartfren Telecom Tbk.', '2006-11-29', 'Utama'),
(249, 'IDX:J', 'Infrastruktur', 'GHON', 'Gihon Telekomunikasi Indonesia Tbk.', '2018-04-09', 'Utama'),
(250, 'IDX:J', 'Infrastruktur', 'GMFI', 'Garuda Maintenance Facility Aero Asia Tbk', '2017-10-10', 'Utama'),
(251, 'IDX:J', 'Infrastruktur', 'GOLD', 'Visi Telekomunikasi Infrastruktur Tbk.', '2010-07-07', 'PENGEMBANGAN'),
(252, 'IDX:J', 'Infrastruktur', 'HADE', 'Himalaya Energi Perkasa Tbk.', '2004-04-12', 'PENGEMBANGAN'),
(253, 'IDX:J', 'Infrastruktur', 'IBST', 'Inti Bangun Sejahtera Tbk.', '2012-08-31', 'Utama'),
(254, 'IDX:J', 'Infrastruktur', 'IDPR', 'Indonesia Pondasi Raya Tbk.', '2015-12-10', 'Utama'),
(255, 'IDX:J', 'Infrastruktur', 'IPCC', 'Indonesia Kendaraan Terminal Tbk.', '2018-07-09', 'Utama'),
(256, 'IDX:J', 'Infrastruktur', 'IPCM', 'Jasa Armada Indonesia Tbk.', '2017-12-22', 'Utama'),
(257, 'IDX:J', 'Infrastruktur', 'ISAT', 'Indosat Tbk.', '1994-10-19', 'Utama'),
(258, 'IDX:J', 'Infrastruktur', 'JAST', 'Jasnita Telekomindo Tbk.', '2019-05-16', 'Pengembangan'),
(259, 'IDX:J', 'Infrastruktur', 'JKON', 'Jaya Konstruksi Manggala Pratama Tbk.', '2007-12-04', 'Utama'),
(260, 'IDX:J', 'Infrastruktur', 'JSMR', 'Jasa Marga (Persero) Tbk.', '2007-11-12', 'Utama'),
(261, 'IDX:J', 'Infrastruktur', 'KARW', 'ICTSI Jasa Prima Tbk.', '1994-12-20', 'Pengembangan'),
(262, 'IDX:J', 'Infrastruktur', 'KBLV', 'First Media Tbk.', '2000-02-25', 'Pengembangan'),
(263, 'IDX:J', 'Infrastruktur', 'KEEN', 'Kencana Energi Lestari Tbk.', '2019-09-02', 'Utama'),
(264, 'IDX:J', 'Infrastruktur', 'LAPD', 'Leyand International Tbk.', '2001-07-17', 'Pengembangan'),
(265, 'IDX:J', 'Infrastruktur', 'LCKM', 'LCK Global Kedaton Tbk.', '2018-01-16', 'Pengembangan'),
(266, 'IDX:J', 'Infrastruktur', 'LINK', 'Link Net Tbk.', '2014-06-02', 'Utama'),
(267, 'IDX:J', 'Infrastruktur', 'META', 'Nusantara Infrastructure Tbk.', '2001-07-18', 'Utama'),
(268, 'IDX:J', 'Infrastruktur', 'MPOW', 'Megapower Makmur Tbk.', '2017-07-05', 'Pengembangan'),
(269, 'IDX:J', 'Infrastruktur', 'MTEL', 'Dayamitra Telekomunikasi Tbk.', '2021-11-22', 'Utama'),
(270, 'IDX:J', 'Infrastruktur', 'MTPS', 'Meta Epsi Tbk.', '2019-04-10', 'PENGEMBANGAN'),
(271, 'IDX:J', 'Infrastruktur', 'MTRA', 'Mitra Pemuda Tbk.', '2016-02-10', 'Pengembangan'),
(272, 'IDX:J', 'Infrastruktur', 'NRCA', 'Nusa Raya Cipta Tbk.', '2013-06-27', 'UTAMA'),
(273, 'IDX:J', 'Infrastruktur', 'OASA', 'Protech Mitra Perkasa Tbk.', '2016-07-18', 'Pengembangan'),
(274, 'IDX:J', 'Infrastruktur', 'PBSA', 'Paramita Bangun Sarana Tbk.', '2016-09-28', 'Utama'),
(275, 'IDX:J', 'Infrastruktur', 'PORT', 'Nusantara Pelabuhan Handal Tbk.', '2017-03-16', 'Pengembangan'),
(276, 'IDX:J', 'Infrastruktur', 'POWR', 'Cikarang Listrindo Tbk.', '2016-06-14', 'Pengembangan'),
(277, 'IDX:J', 'Infrastruktur', 'PPRE', 'PP Presisi Tbk.', '2017-11-24', 'Utama'),
(278, 'IDX:J', 'Infrastruktur', 'PTDU', 'Djasa Ubersakti Tbk.', '2020-12-08', 'Pengembangan'),
(279, 'IDX:J', 'Infrastruktur', 'PTPP', 'PP (Persero) Tbk.', '2010-02-09', 'Utama'),
(280, 'IDX:J', 'Infrastruktur', 'PTPW', 'Pratama Widya Tbk.', '2020-02-07', 'Pengembangan'),
(281, 'IDX:J', 'Infrastruktur', 'RONY', 'Aesler Grup Internasional Tbk.', '2020-04-09', 'Pengembangan'),
(282, 'IDX:J', 'Infrastruktur', 'SMKM', 'Sumber Mas Konstruksi Tbk.', '2022-03-09', 'Akselerasi'),
(283, 'IDX:J', 'Infrastruktur', 'SSIA', 'Surya Semesta Internusa Tbk.', '1997-03-27', 'Utama'),
(284, 'IDX:J', 'Infrastruktur', 'SUPR', 'Solusi Tunas Pratama Tbk.', '2011-10-11', 'Pengembangan'),
(285, 'IDX:J', 'Infrastruktur', 'TAMA', 'Lancartama Sejati Tbk.', '2020-02-10', 'Pengembangan'),
(286, 'IDX:J', 'Infrastruktur', 'TBIG', 'Tower Bersama Infrastructure Tbk.', '2010-10-26', 'Utama'),
(287, 'IDX:J', 'Infrastruktur', 'TGRA', 'Terregra Asia Energy Tbk.', '2017-05-16', 'UTAMA'),
(288, 'IDX:J', 'Infrastruktur', 'TLKM', 'Telkom Indonesia (Persero) Tbk.', '1995-11-14', 'Utama'),
(289, 'IDX:J', 'Infrastruktur', 'TOPS', 'Totalindo Eka Persada Tbk.', '2017-06-16', 'Utama'),
(290, 'IDX:J', 'Infrastruktur', 'TOTL', 'Total Bangun Persada Tbk.', '2006-07-25', 'Utama'),
(291, 'IDX:J', 'Infrastruktur', 'TOWR', 'Sarana Menara Nusantara Tbk.', '2010-03-08', 'Utama'),
(292, 'IDX:J', 'Infrastruktur', 'WEGE', 'Wijaya Karya Bangunan Gedung Tbk.', '2017-11-30', 'Utama'),
(293, 'IDX:J', 'Infrastruktur', 'WIKA', 'Wijaya Karya (Persero) Tbk.', '2007-10-29', 'Utama'),
(294, 'IDX:J', 'Infrastruktur', 'WSKT', 'Waskita Karya (Persero) Tbk.', '2012-12-19', 'Utama');

-- --------------------------------------------------------

--
-- Struktur dari tabel `daftar_sektor`
--

CREATE TABLE `daftar_sektor` (
  `kode_sektor` varchar(10) NOT NULL,
  `nama_sektor` varchar(100) NOT NULL,
  `bursa` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `daftar_sektor`
--

INSERT INTO `daftar_sektor` (`kode_sektor`, `nama_sektor`, `bursa`) VALUES
('IDX:A', 'Energi', 'IDX'),
('IDX:B', 'Barang Baku', 'IDX'),
('IDX:C', 'Perindustrian', 'IDX'),
('IDX:D', 'Barang Konsumen Primer', 'IDX'),
('IDX:E', 'Barang Konsumen Non-Primer', 'IDX'),
('IDX:F', 'Kesehatan', 'IDX'),
('IDX:G', 'Keuangan', 'IDX'),
('IDX:H', 'Properti & Real Estate', 'IDX'),
('IDX:I', 'Teknologi', 'IDX'),
('IDX:J', 'Infrastruktur', 'IDX'),
('IDX:K', 'Transportasi & Logistik', 'IDX'),
('IDX:Z', 'Produk Investasi Tercatat', 'IDX');

-- --------------------------------------------------------

--
-- Struktur dari tabel `sektorenergi`
--

CREATE TABLE `sektorenergi` (
  `id` int(11) NOT NULL,
  `kode_sektor` varchar(10) DEFAULT NULL,
  `sektor_usaha` varchar(100) DEFAULT NULL,
  `kodeSaham` varchar(4) NOT NULL,
  `namaEmiten` varchar(100) DEFAULT NULL,
  `tglListing` varchar(100) DEFAULT NULL,
  `jumlahSaham` bigint(20) DEFAULT NULL,
  `papanBursa` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `sektorenergi`
--

INSERT INTO `sektorenergi` (`id`, `kode_sektor`, `sektor_usaha`, `kodeSaham`, `namaEmiten`, `tglListing`, `jumlahSaham`, `papanBursa`) VALUES
(1, 'IDX:A', 'Energi', 'ADMR', 'Adaro Minerals Indonesia Tbk.', '2022 Jan 03', 40882331500, 'Pengembangan'),
(2, 'IDX:A', 'Energi', 'ADRO', 'Adaro Energy Tbk.', '2008 Jul 16', 31985962000, 'Utama'),
(3, 'IDX:A', 'Energi', 'AIMS', 'Akbar Indo Makmur Stimec Tbk.', '2001 Jul 20', 220000000, 'Pengembangan'),
(4, 'IDX:A', 'Energi', 'AKRA', 'AKR Corporindo Tbk.', '1994 Oct 03', 20073474600, 'Utama'),
(5, 'IDX:A', 'Energi', 'APEX', 'Apexindo Pratama Duta Tbk.', '2013 Jun 05', 2659850000, 'Pengembangan'),
(6, 'IDX:A', 'Energi', 'ARII', 'Atlas Resources Tbk.', '2011 Nov 08', 3131000000, 'Pengembangan'),
(7, 'IDX:A', 'Energi', 'ARTI', 'Ratu Prabu Energi Tbk.', '2003 Apr 30', 7840000000, 'Utama'),
(8, 'IDX:A', 'Energi', 'BBRM', 'Pelayaran Nasional Bina Buana Raya Tbk.', '2013 Jan 09', 7618007952, 'Utama'),
(9, 'IDX:A', 'Energi', 'BESS', 'Batulicin Nusantara Maritim Tbk.', '2020 Mar 09', 3412604935, 'Pengembangan'),
(10, 'IDX:A', 'Energi', 'BIPI', 'Astrindo Nusantara infrastruktur Tbk.', '2010 Feb 11', 44693066193, 'Pengembangan'),
(11, 'IDX:A', 'Energi', 'BOSS', 'Borneo Olah Sarana Sukses Tbk.', '2018 Feb 15', 1400000000, 'Pengembangan'),
(12, 'IDX:A', 'Energi', 'BSML', 'Bintang Samudera Mandiri Lines Tbk.', '2021 Dec 16', 1850225000, 'Pengembangan'),
(13, 'IDX:A', 'Energi', 'BSSR', 'Baramulti Suksessarana Tbk.', '2012 Nov 08', 2616500000, 'Pengembangan'),
(14, 'IDX:A', 'Energi', 'BULL', 'Buana Lintas Lautan Tbk.', '2011 May 23', 13432476445, 'Utama'),
(15, 'IDX:A', 'Energi', 'BUMI', 'Bumi Resources Tbk.', '1990 Jul 30', 108772794052, 'Pengembangan'),
(16, 'IDX:A', 'Energi', 'BYAN', 'Bayan Resources Tbk.', '2008 Ags 12', 3333333500, 'Utama'),
(17, 'IDX:A', 'Energi', 'CANI', 'Capitol Nusantara Indonesia Tbk.', '2014 Jan 16', 833440000, 'Pengembangan'),
(18, 'IDX:A', 'Energi', 'CNKO', 'Exploitasi Energi Indonesia Tbk.', '2001 Nov 20', 8956361206, 'Utama'),
(19, 'IDX:A', 'Energi', 'DEWA', 'Darma Henwa Tbk.', '2007 Sep 26', 21853733792, 'Utama'),
(20, 'IDX:A', 'Energi', 'DOID', 'Delta Dunia Makmur Tbk.', '2001 Jun 15', 8621173232, 'Utama'),
(21, 'IDX:A', 'Energi', 'DSSA', 'Dian Swastatika Sentosa Tbk.', '2009 Dec 10', 770552320, 'Utama'),
(22, 'IDX:A', 'Energi', 'DWGL', 'Dwi Guna Laksana Tbk.', '2017 Dec 13', 9244720256, 'Pengembangan'),
(23, 'IDX:A', 'Energi', 'ELSA', 'Elnusa Tbk.', '2008 Feb 06', 7298500000, 'Utama'),
(24, 'IDX:A', 'Energi', 'ENRG', 'Energi Mega Persada Tbk.', '2004 Jun 07', 24821230250, 'Pengembangan'),
(25, 'IDX:A', 'Energi', 'ETWA', 'Eterindo Wahanatama Tbk', '1997 May 16', 4668671400, 'Utama'),
(26, 'IDX:A', 'Energi', 'FIRE', 'Alfa Energi Investama Tbk.', '2017 Jun 09', 1475363179, 'Pengembangan'),
(27, 'IDX:A', 'Energi', 'GEMS', 'Golden Energy Mines Tbk.', '2011 Nov 17', 5882353000, 'Utama'),
(28, 'IDX:A', 'Energi', 'GTBO', 'Garda Tujuh Buana Tbk', '2009 Jul 09', 2500000000, 'Pengembangan'),
(29, 'IDX:A', 'Energi', 'GTSI', 'GTS Internasional Tbk.', '2021 Sep 08', 15819142767, 'Utama'),
(30, 'IDX:A', 'Energi', 'HITS', 'Humpuss Intermoda Transportasi Tbk.', '1997 Dec 15', 7101084801, 'Utama'),
(31, 'IDX:A', 'Energi', 'HRUM', 'Harum Energy Tbk.', '2010 Oct 06', 2703620000, 'Utama'),
(32, 'IDX:A', 'Energi', 'INDY', 'Indika Energy Tbk.', '2008 Jun 11', 5210192000, 'Utama'),
(33, 'IDX:A', 'Energi', 'INPS', 'Indah Prakasa Sentosa Tbk.', '2018 Apr 06', 650000000, 'Pengembangan'),
(34, 'IDX:A', 'Energi', 'ITMA', 'Sumber Energi Andalan Tbk.', '1990 Dec 10', 870701000, 'Pengembangan'),
(35, 'IDX:A', 'Energi', 'ITMG', 'Indo Tambangraya Megah Tbk.', '2007 Dec 18', 1129925000, 'Utama'),
(36, 'IDX:A', 'Energi', 'JSKY', 'Sky Energy Indonesia Tbk.', '2018 Mar 28', 2032540000, 'Utama'),
(37, 'IDX:A', 'Energi', 'KKGI', 'Resource Alam Indonesia Tbk.', '1991 Jul 01', 5000000000, 'Utama'),
(38, 'IDX:A', 'Energi', 'KOPI', 'Mitra Energi Persada Tbk.', '2015 May 04', 697266668, 'PENGEMBANGAN'),
(39, 'IDX:A', 'Energi', 'LEAD', 'Logindo Samudramakmur Tbk.', '2013 Dec 11', 4049616328, 'UTAMA'),
(40, 'IDX:A', 'Energi', 'MBAP', 'Mitrabara Adiperdana Tbk.', '2014 Jul 10', 1227271952, 'Pengembangan'),
(41, 'IDX:A', 'Energi', 'MBSS', 'Mitrabahtera Segara Sejati Tbk.', '2011 Apr 06', 1750026639, 'Utama'),
(42, 'IDX:A', 'Energi', 'MCOL', 'Prima Andalan Mandiri Tbk.', '2021 Sep 07', 3555560000, 'Utama'),
(43, 'IDX:A', 'Energi', 'MEDC', 'Medco Energi Internasional Tbk.', '1994 Oct 12', 25136231252, 'Utama'),
(44, 'IDX:A', 'Energi', 'MITI', 'Mitra Investindo Tbk.', '1997 Jul 16', 2442988366, 'Pengembangan'),
(45, 'IDX:A', 'Energi', 'MTFN', 'Capitalinc Investment Tbk.', '1990 Apr 16', 31842082852, 'Pengembangan'),
(46, 'IDX:A', 'Energi', 'MYOH', 'Samindo Resources Tbk.', '2000 Jul 27', 2206312500, 'Utama'),
(47, 'IDX:A', 'Energi', 'PGAS', 'Perusahaan Gas Negara Tbk.', '2003 Dec 15', 24241508196, 'Utama'),
(48, 'IDX:A', 'Energi', 'PKPK', 'Perdana Karya Perkasa Tbk.', '2007 Jul 11', 600000000, 'Pengembangan'),
(49, 'IDX:A', 'Energi', 'PSSI', 'Pelita Samudera Shipping Tbk.', '2017 Dec 05', 5417063153, 'Utama'),
(50, 'IDX:A', 'Energi', 'PTBA', 'Bukit Asam Tbk.', '2002 Dec 23', 11520659250, 'Utama'),
(51, 'IDX:A', 'Energi', 'PTIS', 'Indo Straits Tbk.', '2011 Jul 12', 550165300, 'Utama'),
(52, 'IDX:A', 'Energi', 'PTRO', 'Petrosea Tbk.', '1990 May 21', 1008605000, 'Utama'),
(53, 'IDX:A', 'Energi', 'RAJA', 'Rukun Raharja Tbk.', '2006 Apr 19', 4227082500, 'Utama'),
(54, 'IDX:A', 'Energi', 'RIGS', 'Rig Tenders Indonesia Tbk.', '1990 Mar 05', 609130000, 'Pengembangan'),
(55, 'IDX:A', 'Energi', 'RMKE', 'RMK Energy Tbk.', '2021 Dec 07', 4375000000, 'Utama'),
(56, 'IDX:A', 'Energi', 'RUIS', 'Radiant Utama Interinsco Tbk.', '2006 Jul 12', 770000000, 'Pengembangan'),
(57, 'IDX:A', 'Energi', 'SEMA', 'Semacom Integrated Tbk.', '2022 Jan 10', 1347000000, 'Pengembangan'),
(58, 'IDX:A', 'Energi', 'SGER', 'Sumber Global Energy Tbk.', '2020 Ags 10', 1959425719, 'Pengembangan'),
(59, 'IDX:A', 'Energi', 'SHIP', 'Sillo Maritime Perdana Tbk.', '2016 Jun 16', 2719790000, 'Pengembangan'),
(60, 'IDX:A', 'Energi', 'SMMT', 'Golden Eagle Energy Tbk.', '1997 Dec 01', 3150000000, 'PENGEMBANGAN'),
(61, 'IDX:A', 'Energi', 'SMRU', 'SMR Utama Tbk.', '2011 Oct 10', 12499385782, 'Pengembangan'),
(62, 'IDX:A', 'Energi', 'SOCI', 'Soechi Lines Tbk.', '2014 Dec 03', 7059000000, 'Utama'),
(63, 'IDX:A', 'Energi', 'SUGI', 'Sugih Energy Tbk.', '2002 Jun 19', 24811541414, 'PENGEMBANGAN'),
(64, 'IDX:A', 'Energi', 'SURE', 'Super Energy Tbk.', '2018 Oct 05', 1497576771, 'PENGEMBANGAN'),
(65, 'IDX:A', 'Energi', 'TAMU', 'Pelayaran Tamarin Samudra Tbk.', '2017 May 10', 37500000000, 'Pengembangan'),
(66, 'IDX:A', 'Energi', 'TCPI', 'Transcoal Pacific Tbk.', '2018 Jul 06', 5000000000, 'Pengembangan'),
(67, 'IDX:A', 'Energi', 'TEBE', 'Dana Brata Luhur Tbk.', '2019 Nov 18', 1285000000, 'PENGEMBANGAN'),
(68, 'IDX:A', 'Energi', 'TOBA', 'TBS Energi Utama Tbk.', '2012 Jul 06', 8049964000, 'Utama'),
(69, 'IDX:A', 'Energi', 'TPMA', 'Trans Power Marine Tbk.', '2013 Feb 20', 2633300000, 'Pengembangan'),
(70, 'IDX:A', 'Energi', 'TRAM', 'Trada Alam Minera Tbk.', '2008 Sep 10', 49643627934, 'Utama'),
(71, 'IDX:A', 'Energi', 'UNIQ', 'Ulima Nitra Tbk.', '2021 Mar 08', 3138983000, 'Utama'),
(72, 'IDX:A', 'Energi', 'WINS', 'Wintermar Offshore Marine Tbk.', '2010 Nov 29', 4346087057, 'Utama'),
(73, 'IDX:A', 'Energi', 'WOWS', 'Ginting Jaya Energi Tbk.', '2019 Nov 08', 2475720000, 'Pengembangan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `sektorinfrastruktur`
--

CREATE TABLE `sektorinfrastruktur` (
  `id` int(11) NOT NULL,
  `kode_sektor` varchar(10) DEFAULT NULL,
  `sektor_usaha` varchar(100) DEFAULT NULL,
  `kodeSaham` varchar(4) NOT NULL,
  `namaEmiten` varchar(100) DEFAULT NULL,
  `tglListing` varchar(100) DEFAULT NULL,
  `jumlahSaham` bigint(20) DEFAULT NULL,
  `papanBursa` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `sektorinfrastruktur`
--

INSERT INTO `sektorinfrastruktur` (`id`, `kode_sektor`, `sektor_usaha`, `kodeSaham`, `namaEmiten`, `tglListing`, `jumlahSaham`, `papanBursa`) VALUES
(1, 'IDX:J', 'Infrastruktur', 'ACST', 'Acset Indonusa Tbk.', '2013-06-24', 12675160000, 'Utama'),
(2, 'IDX:J', 'Infrastruktur', 'ADHI', 'Adhi Karya (Persero) Tbk.', '2004-03-18', 3560849376, 'Utama'),
(3, 'IDX:J', 'Infrastruktur', 'BALI', 'Bali Towerindo Sentra Tbk.', '2014-03-13', 3934592500, 'Utama'),
(4, 'IDX:J', 'Infrastruktur', 'BTEL', 'Bakrie Telecom Tbk.', '2006-02-03', 36822665755, 'Utama'),
(5, 'IDX:J', 'Infrastruktur', 'BUKK', 'Bukaka Teknik Utama Tbk.', '2015-06-29', 2640452000, 'Pengembangan'),
(6, 'IDX:J', 'Infrastruktur', 'CASS', 'Cardig Aero Services Tbk.', '2011-12-05', 2086950000, 'Pengembangan'),
(7, 'IDX:J', 'Infrastruktur', 'CENT', 'Centratama Telekomunikasi Indonesia Tbk', '2001-11-01', 31183464900, 'Pengembangan'),
(8, 'IDX:J', 'Infrastruktur', 'CMNP', 'Citra Marga Nusaphala Persada Tbk.', '1995-01-10', 5433721755, 'Utama'),
(9, 'IDX:J', 'Infrastruktur', 'DGIK', 'Nusa Konstruksi Enjiniring Tbk.', '2007-12-19', 5541165000, 'Utama'),
(10, 'IDX:J', 'Infrastruktur', 'EXCL', 'XL Axiata Tbk.', '2005-09-29', 10724674776, 'Utama'),
(11, 'IDX:J', 'Infrastruktur', 'FIMP', 'Fimperkasa Utama Tbk.', '2021-04-09', 400000955, 'Akselerasi'),
(12, 'IDX:J', 'Infrastruktur', 'FREN', 'Smartfren Telecom Tbk.', '2006-11-29', 308106726183, 'Utama'),
(13, 'IDX:J', 'Infrastruktur', 'GHON', 'Gihon Telekomunikasi Indonesia Tbk.', '2018-04-09', 550000000, 'Utama'),
(14, 'IDX:J', 'Infrastruktur', 'GMFI', 'Garuda Maintenance Facility Aero Asia Tbk', '2017-10-10', 28233511500, 'Utama'),
(15, 'IDX:J', 'Infrastruktur', 'GOLD', 'Visi Telekomunikasi Infrastruktur Tbk.', '2010-07-07', 1277276000, 'PENGEMBANGAN'),
(16, 'IDX:J', 'Infrastruktur', 'HADE', 'Himalaya Energi Perkasa Tbk.', '2004-04-12', 2120000000, 'PENGEMBANGAN'),
(17, 'IDX:J', 'Infrastruktur', 'IBST', 'Inti Bangun Sejahtera Tbk.', '2012-08-31', 1350904927, 'Utama'),
(18, 'IDX:J', 'Infrastruktur', 'IDPR', 'Indonesia Pondasi Raya Tbk.', '2015-12-10', 2003000000, 'Utama'),
(19, 'IDX:J', 'Infrastruktur', 'IPCC', 'Indonesia Kendaraan Terminal Tbk.', '2018-07-09', 1818384820, 'Utama'),
(20, 'IDX:J', 'Infrastruktur', 'IPCM', 'Jasa Armada Indonesia Tbk.', '2017-12-22', 5284811100, 'Utama'),
(21, 'IDX:J', 'Infrastruktur', 'ISAT', 'Indosat Tbk.', '1994-10-19', 8062702740, 'Utama'),
(22, 'IDX:J', 'Infrastruktur', 'JAST', 'Jasnita Telekomindo Tbk.', '2019-05-16', 813626700, 'Pengembangan'),
(23, 'IDX:J', 'Infrastruktur', 'JKON', 'Jaya Konstruksi Manggala Pratama Tbk.', '2007-12-04', 16308519860, 'Utama'),
(24, 'IDX:J', 'Infrastruktur', 'JSMR', 'Jasa Marga (Persero) Tbk.', '2007-11-12', 7257871200, 'Utama'),
(25, 'IDX:J', 'Infrastruktur', 'KARW', 'ICTSI Jasa Prima Tbk.', '1994-12-20', 587152700, 'Pengembangan'),
(26, 'IDX:J', 'Infrastruktur', 'KBLV', 'First Media Tbk.', '2000-02-25', 1742167907, 'Pengembangan'),
(27, 'IDX:J', 'Infrastruktur', 'KEEN', 'Kencana Energi Lestari Tbk.', '2019-09-02', 3666312500, 'Utama'),
(28, 'IDX:J', 'Infrastruktur', 'LAPD', 'Leyand International Tbk.', '2001-07-17', 3966350139, 'Pengembangan'),
(29, 'IDX:J', 'Infrastruktur', 'LCKM', 'LCK Global Kedaton Tbk.', '2018-01-16', 1000000000, 'Pengembangan'),
(30, 'IDX:J', 'Infrastruktur', 'LINK', 'Link Net Tbk.', '2014-06-02', 2863195484, 'Utama'),
(31, 'IDX:J', 'Infrastruktur', 'META', 'Nusantara Infrastructure Tbk.', '2001-07-18', 17710708194, 'Utama'),
(32, 'IDX:J', 'Infrastruktur', 'MPOW', 'Megapower Makmur Tbk.', '2017-07-05', 816997053, 'Pengembangan'),
(33, 'IDX:J', 'Infrastruktur', 'MTEL', 'Dayamitra Telekomunikasi Tbk.', '2021-11-22', 83515452844, 'Utama'),
(34, 'IDX:J', 'Infrastruktur', 'MTPS', 'Meta Epsi Tbk.', '2019-04-10', 2084850829, 'PENGEMBANGAN'),
(35, 'IDX:J', 'Infrastruktur', 'MTRA', 'Mitra Pemuda Tbk.', '2016-02-10', 770000000, 'Pengembangan'),
(36, 'IDX:J', 'Infrastruktur', 'NRCA', 'Nusa Raya Cipta Tbk.', '2013-06-27', 2496258344, 'UTAMA'),
(37, 'IDX:J', 'Infrastruktur', 'OASA', 'Protech Mitra Perkasa Tbk.', '2016-07-18', 358600000, 'Pengembangan'),
(38, 'IDX:J', 'Infrastruktur', 'PBSA', 'Paramita Bangun Sarana Tbk.', '2016-09-28', 1500000000, 'Utama'),
(39, 'IDX:J', 'Infrastruktur', 'PORT', 'Nusantara Pelabuhan Handal Tbk.', '2017-03-16', 2813941985, 'Pengembangan'),
(40, 'IDX:J', 'Infrastruktur', 'POWR', 'Cikarang Listrindo Tbk.', '2016-06-14', 16087156000, 'Pengembangan'),
(41, 'IDX:J', 'Infrastruktur', 'PPRE', 'PP Presisi Tbk.', '2017-11-24', 10224271000, 'Utama'),
(42, 'IDX:J', 'Infrastruktur', 'PTDU', 'Djasa Ubersakti Tbk.', '2020-12-08', 1500000000, 'Pengembangan'),
(43, 'IDX:J', 'Infrastruktur', 'PTPP', 'PP (Persero) Tbk.', '2010-02-09', 6199897354, 'Utama'),
(44, 'IDX:J', 'Infrastruktur', 'PTPW', 'Pratama Widya Tbk.', '2020-02-07', 878187500, 'Pengembangan'),
(45, 'IDX:J', 'Infrastruktur', 'RONY', 'Aesler Grup Internasional Tbk.', '2020-04-09', 1250000000, 'Pengembangan'),
(46, 'IDX:J', 'Infrastruktur', 'SMKM', 'Sumber Mas Konstruksi Tbk.', '2022-03-09', 1253000000, 'Akselerasi'),
(47, 'IDX:J', 'Infrastruktur', 'SSIA', 'Surya Semesta Internusa Tbk.', '1997-03-27', 4705249440, 'Utama'),
(48, 'IDX:J', 'Infrastruktur', 'SUPR', 'Solusi Tunas Pratama Tbk.', '2011-10-11', 1137579698, 'Pengembangan'),
(49, 'IDX:J', 'Infrastruktur', 'TAMA', 'Lancartama Sejati Tbk.', '2020-02-10', 1000000005, 'Pengembangan'),
(50, 'IDX:J', 'Infrastruktur', 'TBIG', 'Tower Bersama Infrastructure Tbk.', '2010-10-26', 22656999445, 'Utama'),
(51, 'IDX:J', 'Infrastruktur', 'TGRA', 'Terregra Asia Energy Tbk.', '2017-05-16', 2750000000, 'UTAMA'),
(52, 'IDX:J', 'Infrastruktur', 'TLKM', 'Telkom Indonesia (Persero) Tbk.', '1995-11-14', 99062216600, 'Utama'),
(53, 'IDX:J', 'Infrastruktur', 'TOPS', 'Totalindo Eka Persada Tbk.', '2017-06-16', 33330000000, 'Utama'),
(54, 'IDX:J', 'Infrastruktur', 'TOTL', 'Total Bangun Persada Tbk.', '2006-07-25', 3410000000, 'Utama'),
(55, 'IDX:J', 'Infrastruktur', 'TOWR', 'Sarana Menara Nusantara Tbk.', '2010-03-08', 51014625000, 'Utama'),
(56, 'IDX:J', 'Infrastruktur', 'WEGE', 'Wijaya Karya Bangunan Gedung Tbk.', '2017-11-30', 9572000000, 'Utama'),
(57, 'IDX:J', 'Infrastruktur', 'WIKA', 'Wijaya Karya (Persero) Tbk.', '2007-10-29', 8969951372, 'Utama'),
(58, 'IDX:J', 'Infrastruktur', 'WSKT', 'Waskita Karya (Persero) Tbk.', '2012-12-19', 28806807016, 'Utama');

-- --------------------------------------------------------

--
-- Struktur dari tabel `sektorkesehatan`
--

CREATE TABLE `sektorkesehatan` (
  `id` int(11) NOT NULL,
  `kode_sektor` varchar(10) DEFAULT NULL,
  `sektor_usaha` varchar(100) DEFAULT NULL,
  `kodeSaham` varchar(4) NOT NULL,
  `namaEmiten` varchar(100) DEFAULT NULL,
  `tglListing` varchar(100) DEFAULT NULL,
  `jumlahSaham` bigint(20) DEFAULT NULL,
  `papanBursa` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `sektorkesehatan`
--

INSERT INTO `sektorkesehatan` (`id`, `kode_sektor`, `sektor_usaha`, `kodeSaham`, `namaEmiten`, `tglListing`, `jumlahSaham`, `papanBursa`) VALUES
(1, 'IDX:F', 'Kesehatan', 'BMHS', 'Bundamedik Tbk.', '2021-07-06', 8603416176, 'Utama'),
(2, 'IDX:F', 'Kesehatan', 'CARE', 'Metro Healthcare Indonesia Tbk.', '2020-03-13', 33250000000, 'Pengembangan'),
(3, 'IDX:F', 'Kesehatan', 'DGNS', 'Diagnos Laboratorium Utama Tbk.', '2021-01-15', 1250000000, 'Pengembangan'),
(4, 'IDX:F', 'Kesehatan', 'DVLA', 'Darya-Varia Laboratoria Tbk.', '1994-11-11', 1120000000, 'Utama'),
(5, 'IDX:F', 'Kesehatan', 'HEAL', 'Medikaloka Hermina Tbk.', '2018-05-16', 14890000000, 'Utama'),
(6, 'IDX:F', 'Kesehatan', 'INAF', 'Indofarma Tbk.', '2001-04-17', 3099267500, 'Utama'),
(7, 'IDX:F', 'Kesehatan', 'IRRA', 'Itama Ranoraya Tbk.', '2019-10-15', 1600000000, 'Pengembangan'),
(8, 'IDX:F', 'Kesehatan', 'KAEF', 'Kimia Farma Tbk.', '2001-07-04', 5554000000, 'Utama'),
(9, 'IDX:F', 'Kesehatan', 'KLBF', 'Kalbe Farma Tbk.', '1991-07-30', 46875122110, 'Utama'),
(10, 'IDX:F', 'Kesehatan', 'MERK', 'Merck Tbk.', '1981-07-23', 448000000, 'PENGEMBANGAN'),
(11, 'IDX:F', 'Kesehatan', 'MIKA', 'Mitra Keluarga Karyasehat Tbk.', '2015-03-24', 14246349500, 'Utama'),
(12, 'IDX:F', 'Kesehatan', 'PEHA', 'Phapros Tbk.', '2018-12-26', 840000000, 'Utama'),
(13, 'IDX:F', 'Kesehatan', 'PRDA', 'Prodia Widyahusada Tbk.', '2016-12-07', 937500000, 'Utama'),
(14, 'IDX:F', 'Kesehatan', 'PRIM', 'Royal Prima Tbk.', '2018-05-15', 3393434905, 'Pengembangan'),
(15, 'IDX:F', 'Kesehatan', 'PYFA', 'Pyridam Farma Tbk.', '2001-10-16', 535080000, 'Pengembangan'),
(16, 'IDX:F', 'Kesehatan', 'RSGK', 'Kedoya Adyaraya Tbk.', '2021-09-08', 929675000, 'Utama'),
(17, 'IDX:F', 'Kesehatan', 'SAME', 'Sarana Meditama Metropolitan Tbk.', '2013-01-11', 17113987263, 'Pengembangan'),
(18, 'IDX:F', 'Kesehatan', 'SCPI', 'Organon Pharma Indonesia Tbk.', '1990-06-08', 3600000, 'PENGEMBANGAN'),
(19, 'IDX:F', 'Kesehatan', 'SIDO', 'Industri Jamu dan Farmasi Sidomuncul Tbk', '2013-12-18', 30000000000, 'Utama'),
(20, 'IDX:F', 'Kesehatan', 'SILO', 'Siloam International Hospitals Tbk.', '2013-09-12', 1625765625, 'Utama'),
(21, 'IDX:F', 'Kesehatan', 'SOHO', 'Soho Global Health Tbk.', '2020-09-08', 1269168239, 'Utama'),
(22, 'IDX:F', 'Kesehatan', 'SRAJ', 'Sejahteraraya Anugrahjaya Tbk.', '2011-04-11', 12000705445, 'Utama'),
(23, 'IDX:F', 'Kesehatan', 'TSPC', 'Tempo Scan Pacific Tbk.', '1994-06-17', 4509864300, 'Utama');

-- --------------------------------------------------------

--
-- Struktur dari tabel `sektorproperti`
--

CREATE TABLE `sektorproperti` (
  `id` int(11) NOT NULL,
  `kode_sektor` varchar(10) DEFAULT NULL,
  `sektor_usaha` varchar(100) DEFAULT NULL,
  `kodeSaham` varchar(4) NOT NULL,
  `namaEmiten` varchar(100) DEFAULT NULL,
  `tglListing` varchar(20) DEFAULT NULL,
  `jumlahSaham` bigint(20) DEFAULT NULL,
  `papanBursa` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `sektorproperti`
--

INSERT INTO `sektorproperti` (`id`, `kode_sektor`, `sektor_usaha`, `kodeSaham`, `namaEmiten`, `tglListing`, `jumlahSaham`, `papanBursa`) VALUES
(1, 'IDX:H', 'Properti & Real Estate', 'ADCP', 'Adhi Commuter Properti Tbk.', '2021 May 21', 22222222200, 'Utama'),
(2, 'IDX:H', 'Properti & Real Estate', 'AMAN', 'Makmur Berkah Amanda Tbk.', '2020 Mar 13', 3873500000, 'Utama'),
(3, 'IDX:H', 'Properti & Real Estate', 'APLN', 'Agung Podomoro Land Tbk.', '2010 Nov 11', 22699326779, 'Utama'),
(4, 'IDX:H', 'Properti & Real Estate', 'ARMY', 'Armidian Karyatama Tbk.', '2017 Jun 21', 9006250000, 'Pengembangan'),
(5, 'IDX:H', 'Properti & Real Estate', 'ASPI', 'Andalan Sakti Primaindo Tbk.', '2020 Feb 17', 681794825, 'Pengembangan'),
(6, 'IDX:H', 'Properti & Real Estate', 'ASRI', 'Alam Sutera Realty Tbk.', '2007 Dec 18', 19649411888, 'Utama'),
(7, 'IDX:H', 'Properti & Real Estate', 'ATAP', 'Trimitra Prawara Goldland Tbk.', '2020 Dec 11', 1250000000, 'Pengembangan'),
(8, 'IDX:H', 'Properti & Real Estate', 'BAPA', 'Bekasi Asri Pemula Tbk.', '2008 Jan 14', 661784520, 'Utama'),
(9, 'IDX:H', 'Properti & Real Estate', 'BAPI', 'Bhakti Agung Propertindo Tbk.', '2019 Sep 16', 5591752986, 'Pengembangan'),
(10, 'IDX:H', 'Properti & Real Estate', 'BBSS', 'Bumi Benowo Sukses Sejahtera Tbk.', '2020 Apr 15', 4800016020, 'Pengembangan'),
(11, 'IDX:H', 'Properti & Real Estate', 'BCIP', 'Bumi Citra Permai Tbk.', '2009 Dec 11', 1429915525, 'Pengembangan'),
(12, 'IDX:H', 'Properti & Real Estate', 'BEST', 'Bekasi Fajar Industrial Estate Tbk.', '2012 Apr 10', 9647311150, 'Utama'),
(13, 'IDX:H', 'Properti & Real Estate', 'BIKA', 'Binakarya Jaya Abadi Tbk.', '2015 Jul 14', 592280000, 'Pengembangan'),
(14, 'IDX:H', 'Properti & Real Estate', 'BIPP', 'Bhuwanatala Indah Permai Tbk.', '1995 Oct 23', 5028669366, 'Pengembangan'),
(15, 'IDX:H', 'Properti & Real Estate', 'BKDP', 'Bukit Darmo Property Tbk.', '2007 Jun 15', 7513992252, 'Pengembangan'),
(16, 'IDX:H', 'Properti & Real Estate', 'BKSL', 'Sentul City Tbk.', '1997 Jul 28', 67083561082, 'Utama'),
(17, 'IDX:H', 'Properti & Real Estate', 'BSDE', 'Bumi Serpong Damai Tbk.', '2008 Jun 06', 21171365812, 'Utama'),
(18, 'IDX:H', 'Properti & Real Estate', 'CITY', 'Natura City Developments Tbk.', '2018 Sep 28', 5405188966, 'Utama'),
(19, 'IDX:H', 'Properti & Real Estate', 'COWL', 'Cowell Development Tbk.', '2007 Dec 19', 4871214021, 'PENGEMBANGAN'),
(20, 'IDX:H', 'Properti & Real Estate', 'CPRI', 'Capri Nusa Satu Properti Tbk.', '2019 Apr 11', 2433375106, 'PENGEMBANGAN'),
(21, 'IDX:H', 'Properti & Real Estate', 'CSIS', 'Cahayasakti Investindo Sukses Tbk.', '2017 May 10', 1307000000, 'Pengembangan'),
(22, 'IDX:H', 'Properti & Real Estate', 'CTRA', 'Ciputra Development Tbk.', '1994 Mar 28', 18560303397, 'Utama'),
(23, 'IDX:H', 'Properti & Real Estate', 'DADA', 'Diamond Citra Propertindo Tbk.', '2020 Feb 14', 7178140108, 'Pengembangan'),
(24, 'IDX:H', 'Properti & Real Estate', 'DART', 'Duta Anggada Realty Tbk.', '1990 May 08', 3141390962, 'Utama'),
(25, 'IDX:H', 'Properti & Real Estate', 'DILD', 'Intiland Development Tbk.', '1991 Sep 04', 10365854185, 'Utama'),
(26, 'IDX:H', 'Properti & Real Estate', 'DMAS', 'Puradelta Lestari Tbk.', '2015 May 29', 48198111100, 'Utama'),
(27, 'IDX:H', 'Properti & Real Estate', 'DUTI', 'Duta Pertiwi Tbk.', '1994 Nov 02', 1850000000, 'Pengembangan'),
(28, 'IDX:H', 'Properti & Real Estate', 'ELTY', 'Bakrieland Development Tbk.', '1995 Oct 30', 43521913019, 'UTAMA'),
(29, 'IDX:H', 'Properti & Real Estate', 'EMDE', 'Megapolitan Developments Tbk.', '2011 Jan 12', 3350000000, 'Pengembangan'),
(30, 'IDX:H', 'Properti & Real Estate', 'FMII', 'Fortune Mate Indonesia Tbk.', '2000 Jun 30', 2721000000, 'Pengembangan'),
(31, 'IDX:H', 'Properti & Real Estate', 'FORZ', 'Forza Land Indonesia Tbk.', '2017 Apr 28', 1984009887, 'UTAMA'),
(32, 'IDX:H', 'Properti & Real Estate', 'GAMA', 'Aksara Global Development Tbk.', '2012 Jul 11', 10011027656, 'UTAMA'),
(33, 'IDX:H', 'Properti & Real Estate', 'GMTD', 'Gowa Makassar Tourism Development Tbk.', '2000 Dec 11', 101538000, 'Pengembangan'),
(34, 'IDX:H', 'Properti & Real Estate', 'GPRA', 'Perdana Gapuraprima Tbk.', '2007 Oct 10', 4276655336, 'Utama'),
(35, 'IDX:H', 'Properti & Real Estate', 'GWSA', 'Greenwood Sejahtera Tbk.', '2011 Dec 23', 7800760000, 'UTAMA'),
(36, 'IDX:H', 'Properti & Real Estate', 'HOMI', 'Grand House Mulia Tbk.', '2020 Sep 10', 787500000, 'Pengembangan'),
(37, 'IDX:H', 'Properti & Real Estate', 'INDO', 'Royalindo Investa Wijaya Tbk.', '2020 Jan 13', 4316469405, 'Pengembangan'),
(38, 'IDX:H', 'Properti & Real Estate', 'INPP', 'Indonesian Paradise Property Tbk.', '2004 Jan 12', 11181971732, 'Pengembangan'),
(39, 'IDX:H', 'Properti & Real Estate', 'IPAC', 'Era Graharealty Tbk.', '2021 Jun 30', 949868500, 'Akselerasi'),
(40, 'IDX:H', 'Properti & Real Estate', 'JRPT', 'Jaya Real Property Tbk.', '1994 Jun 29', 13750000000, 'Utama'),
(41, 'IDX:H', 'Properti & Real Estate', 'KBAG', 'Karya Bersama Anugerah Tbk.', '2020 Apr 08', 7150001509, 'Pengembangan'),
(42, 'IDX:H', 'Properti & Real Estate', 'KIJA', 'Kawasan Industri Jababeka Tbk.', '1995 Jan 10', 20824888369, 'Utama'),
(43, 'IDX:H', 'Properti & Real Estate', 'KOTA', 'DMS Propertindo Tbk.', '2019 Jul 09', 10546185701, 'UTAMA'),
(44, 'IDX:H', 'Properti & Real Estate', 'LAND', 'Trimitra Propertindo Tbk.', '2018 Aug 23', 2792620000, 'Pengembangan'),
(45, 'IDX:H', 'Properti & Real Estate', 'LCGP', 'Eureka Prima Jakarta Tbk.', '2007 Jul 13', 5630000914, 'Pengembangan'),
(46, 'IDX:H', 'Properti & Real Estate', 'LPCK', 'Lippo Cikarang Tbk.', '1997 Jul 24', 2679600000, 'Utama'),
(47, 'IDX:H', 'Properti & Real Estate', 'LPKR', 'Lippo Karawaci Tbk.', '1996 Jun 28', 70898018369, 'Utama'),
(48, 'IDX:H', 'Properti & Real Estate', 'LPLI', 'Star Pacific Tbk.', '1989 Oct 23', 1170432803, 'Pengembangan'),
(49, 'IDX:H', 'Properti & Real Estate', 'MDLN', 'Modernland Realty Tbk.', '1993 Jan 18', 12533067322, 'Utama'),
(50, 'IDX:H', 'Properti & Real Estate', 'MKPI', 'Metropolitan Kentjana Tbk.', '2009 Jul 10', 948194000, 'PENGEMBANGAN'),
(51, 'IDX:H', 'Properti & Real Estate', 'MMLP', 'Mega Manunggal Property Tbk.', '2015 Jun 12', 6889134608, 'Pengembangan'),
(52, 'IDX:H', 'Properti & Real Estate', 'MPRO', 'Maha Properti Indonesia Tbk.', '2018 Oct 09', 9942500000, 'Pengembangan'),
(53, 'IDX:H', 'Properti & Real Estate', 'MTLA', 'Metropolitan Land Tbk.', '2011 Jun 20', 7655126330, 'UTAMA'),
(54, 'IDX:H', 'Properti & Real Estate', 'MTSM', 'Metro Realty Tbk.', '1992 Jan 08', 232848000, 'Pengembangan'),
(55, 'IDX:H', 'Properti & Real Estate', 'MYRX', 'Hanson International Tbk.', '1990 Oct 31', 86703220792, 'Pengembangan'),
(56, 'IDX:H', 'Properti & Real Estate', 'NIRO', 'City Retail Developments Tbk.', '2012 Sep 13', 22198871804, 'PENGEMBANGAN'),
(57, 'IDX:H', 'Properti & Real Estate', 'NZIA', 'Nusantara Almazia Tbk.', '2019 Sep 25', 2197540705, 'UTAMA'),
(58, 'IDX:H', 'Properti & Real Estate', 'OMRE', 'Indonesia Prima Property Tbk.', '1994 Aug 22', 1745000000, 'Pengembangan'),
(59, 'IDX:H', 'Properti & Real Estate', 'PAMG', 'Bima Sakti Pertiwi Tbk.', '2019 Jul 05', 3125000000, 'Utama'),
(60, 'IDX:H', 'Properti & Real Estate', 'PLIN', 'Plaza Indonesia Realty Tbk.', '1992 Jun 15', 3550000000, 'Utama'),
(61, 'IDX:H', 'Properti & Real Estate', 'POLI', 'Pollux Hotels Group Tbk.', '2019 Jan 10', 2010526400, 'Pengembangan'),
(62, 'IDX:H', 'Properti & Real Estate', 'POLL', 'Pollux Properties Indonesia Tbk.', '2018 Jul 11', 8318823600, 'Utama'),
(63, 'IDX:H', 'Properti & Real Estate', 'POSA', 'Bliss Properti Indonesia Tbk.', '2019 May 10', 8388870206, 'Pengembangan'),
(64, 'IDX:H', 'Properti & Real Estate', 'PPRO', 'PP Properti Tbk.', '2015 May 19', 61675671883, 'Utama'),
(65, 'IDX:H', 'Properti & Real Estate', 'PUDP', 'Pudjiadi Prestige Tbk.', '1994 Nov 18', 329560000, 'UTAMA'),
(66, 'IDX:H', 'Properti & Real Estate', 'PURI', 'Puri Global Sukses Tbk.', '2020 Sep 08', 1000000000, 'Pengembangan'),
(67, 'IDX:H', 'Properti & Real Estate', 'PWON', 'Pakuwon Jati Tbk.', '1989 Oct 09', 48159602400, 'UTAMA'),
(68, 'IDX:H', 'Properti & Real Estate', 'RBMS', 'Ristia Bintang Mahkotasejati Tbk.', '1997 Dec 19', 2656212826, 'Utama'),
(69, 'IDX:H', 'Properti & Real Estate', 'RDTX', 'Roda Vivatex Tbk.', '1990 May 14', 268800000, 'Utama'),
(70, 'IDX:H', 'Properti & Real Estate', 'REAL', 'Repower Asia Indonesia Tbk.', '2019 Dec 06', 6633610151, 'Pengembangan'),
(71, 'IDX:H', 'Properti & Real Estate', 'RIMO', 'Rimo International Lestari Tbk.', '2000 Nov 10', 45080600000, 'Pengembangan'),
(72, 'IDX:H', 'Properti & Real Estate', 'ROCK', 'Rockfields Properti Indonesia Tbk.', '2020 Sep 10', 1435185100, 'Pengembangan'),
(73, 'IDX:H', 'Properti & Real Estate', 'RODA', 'Pikko Land Development Tbk.', '2001 Oct 22', 13592128209, 'Pengembangan'),
(74, 'IDX:H', 'Properti & Real Estate', 'SATU', 'Kota Satu Properti Tbk.', '2018 Nov 05', 1375000000, 'PENGEMBANGAN'),
(75, 'IDX:H', 'Properti & Real Estate', 'SMDM', 'Suryamas Dutamakmur Tbk.', '1995 Oct 12', 4772138237, 'Pengembangan'),
(76, 'IDX:H', 'Properti & Real Estate', 'SMRA', 'Summarecon Agung Tbk.', '1990 May 07', 16508568358, 'Utama'),
(77, 'IDX:H', 'Properti & Real Estate', 'TARA', 'Agung Semesta Sejahtera Tbk.', '2014 Jul 11', 10069645750, 'Utama'),
(78, 'IDX:H', 'Properti & Real Estate', 'TRIN', 'Perintis Triniti Properti Tbk.', '2020 Jan 15', 4390558222, 'Pengembangan'),
(79, 'IDX:H', 'Properti & Real Estate', 'TRUE', 'Triniti Dinamik Tbk.', '2021 Jun 10', 7570888050, 'Pengembangan'),
(80, 'IDX:H', 'Properti & Real Estate', 'URBN', 'Urban Jakarta Propertindo Tbk.', '2018 Dec 10', 3232122640, 'Pengembangan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `sektorteknologi`
--

CREATE TABLE `sektorteknologi` (
  `id` int(11) NOT NULL,
  `kode_sektor` varchar(10) DEFAULT NULL,
  `sektor_usaha` varchar(100) DEFAULT NULL,
  `kodeSaham` varchar(4) NOT NULL,
  `namaEmiten` varchar(100) DEFAULT NULL,
  `tglListing` varchar(100) DEFAULT NULL,
  `jumlahSaham` bigint(20) DEFAULT NULL,
  `papanBursa` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `sektorteknologi`
--

INSERT INTO `sektorteknologi` (`id`, `kode_sektor`, `sektor_usaha`, `kodeSaham`, `namaEmiten`, `tglListing`, `jumlahSaham`, `papanBursa`) VALUES
(1, 'IDX:I', 'Teknologi', 'ATIC', 'Anabatic Technologies Tbk.', '2015 Jul 08', 2315361355, 'Utama'),
(2, 'IDX:I', 'Teknologi', 'BUKA', 'Bukalapak.com Tbk.', '2021 Aug 06', 103062019354, 'Pengembangan'),
(3, 'IDX:I', 'Teknologi', 'CASH', 'Cashlez Worldwide Indonesia Tbk.', '2020 May 04', 1431125517, 'Akselerasi'),
(4, 'IDX:I', 'Teknologi', 'DCII', 'DCI Indonesia Tbk.', '2021 Jan 06', 2383745900, 'Pengembangan'),
(5, 'IDX:I', 'Teknologi', 'DIVA', 'Distribusi Voucher Nusantara Tbk.', '2018 Nov 27', 1428571400, 'Pengembangan'),
(6, 'IDX:I', 'Teknologi', 'DMMX', 'Digital Mediatama Maxima Tbk.', '2019 Oct 21', 7692307700, 'Pengembangan'),
(7, 'IDX:I', 'Teknologi', 'EDGE', 'Indointernet Tbk.', '2021 Feb 08', 404050000, 'Pengembangan'),
(8, 'IDX:I', 'Teknologi', 'EMTK', 'Elang Mahkota Teknologi Tbk.', '2010 Jan 12', 61241751483, 'Utama'),
(9, 'IDX:I', 'Teknologi', 'ENVY', 'Envy Technologies Indonesia Tbk.', '2019 Jul 08', 1800000000, 'Pengembangan'),
(10, 'IDX:I', 'Teknologi', 'GLVA', 'Galva Technologies Tbk.', '2019 Dec 23', 1500000000, 'Pengembangan'),
(11, 'IDX:I', 'Teknologi', 'HDIT', 'Hensel Davest Indonesia Tbk.', '2019 Jul 12', 1524680000, 'Utama'),
(12, 'IDX:I', 'Teknologi', 'KIOS', 'Kioson Komersial Indonesia Tbk.', '2017 Oct 05', 717239900, 'Pengembangan'),
(13, 'IDX:I', 'Teknologi', 'KREN', 'Kresna Graha Investama Tbk.', '2002 Jun 28', 18208470100, 'Utama'),
(14, 'IDX:I', 'Teknologi', 'LMAS', 'Limas Indonesia Makmur Tbk.', '2001 Dec 28', 787851525, 'Pengembangan'),
(15, 'IDX:I', 'Teknologi', 'LUCK', 'Sentral Mitra Informatika Tbk.', '2018 Nov 28', 715749640, 'Pengembangan'),
(16, 'IDX:I', 'Teknologi', 'MCAS', 'M Cash Integrasi Tbk.', '2017 Nov 01', 867933300, 'Pengembangan'),
(17, 'IDX:I', 'Teknologi', 'MLPT', 'Multipolar Technology Tbk.', '2013 Jul 08', 1875000000, 'Utama'),
(18, 'IDX:I', 'Teknologi', 'MTDL', 'Metrodata Electronics Tbk.', '1990 Apr 09', 12276884585, 'Utama'),
(19, 'IDX:I', 'Teknologi', 'NFCX', 'NFC Indonesia Tbk.', '2018 Jul 12', 666667500, 'Pengembangan'),
(20, 'IDX:I', 'Teknologi', 'PGJO', 'Tourindo Guide Indonesia Tbk.', '2020 Jan 08', 723859095, 'Akselerasi'),
(21, 'IDX:I', 'Teknologi', 'PTSN', 'Sat Nusapersada Tbk', '2007 Nov 08', 5314344000, 'Utama'),
(22, 'IDX:I', 'Teknologi', 'RUNS', 'Global Sukses Solusi Tbk.', '2021 Sep 08', 983557875, 'Akselerasi'),
(23, 'IDX:I', 'Teknologi', 'SKYB', 'Northcliff Citranusa Indonesia Tbk.', '2010 Jul 07', 585000000, 'PENGEMBANGAN'),
(24, 'IDX:I', 'Teknologi', 'TECH', 'Indosterling Technomedia Tbk.', '2020 Jun 04', 1256300000, 'Pengembangan'),
(25, 'IDX:I', 'Teknologi', 'TFAS', 'Telefast Indonesia Tbk.', '2019 Sep 17', 1666666500, 'Pengembangan'),
(26, 'IDX:I', 'Teknologi', 'UVCR', 'Trimegah Karya Pratama Tbk.', '2021 Jul 27', 2000072603, 'Akselerasi'),
(27, 'IDX:I', 'Teknologi', 'WGSH', 'Wira Global Solusi Tbk.', '2021 Dec 06', 1042500000, 'Akselerasi'),
(28, 'IDX:I', 'Teknologi', 'ZYRX', 'Zyrexindo Mandiri Buana Tbk.', '2021 Mar 30', 1333333300, 'Pengembangan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `sektortransportasi`
--

CREATE TABLE `sektortransportasi` (
  `id` int(11) NOT NULL,
  `kode_sektor` varchar(10) DEFAULT NULL,
  `sektor_usaha` varchar(100) DEFAULT NULL,
  `kodeSaham` varchar(4) NOT NULL,
  `namaEmiten` varchar(100) DEFAULT NULL,
  `tglListing` varchar(100) DEFAULT NULL,
  `jumlahSaham` bigint(20) DEFAULT NULL,
  `papanBursa` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `sektortransportasi`
--

INSERT INTO `sektortransportasi` (`id`, `kode_sektor`, `sektor_usaha`, `kodeSaham`, `namaEmiten`, `tglListing`, `jumlahSaham`, `papanBursa`) VALUES
(1, 'IDX:K', 'Transportasi & Logistik', 'AKSI', 'Mineral Sumberdaya Mandiri Tbk.', '2001 Jul 13', 720000000, 'Pengembangan'),
(2, 'IDX:K', 'Transportasi & Logistik', 'ASSA', 'Adi Sarana Armada Tbk.', '2012 Nov 12', 3565496148, 'Utama'),
(3, 'IDX:K', 'Transportasi & Logistik', 'BIRD', 'Blue Bird Tbk.', '2014 Nov 05', 2502100000, 'UTAMA'),
(4, 'IDX:K', 'Transportasi & Logistik', 'BLTA', 'Berlian Laju Tanker Tbk.', '1990 Mar 26', 25940187103, 'Utama'),
(5, 'IDX:K', 'Transportasi & Logistik', 'BPTR', 'Batavia Prosperindo Trans Tbk.', '2018 Jul 09', 1550000000, 'Utama'),
(6, 'IDX:K', 'Transportasi & Logistik', 'CMPP', 'AirAsia Indonesia Tbk.', '1994 Dec 08', 10685124441, 'Pengembangan'),
(7, 'IDX:K', 'Transportasi & Logistik', 'DEAL', 'Dewata Freightinternational Tbk.', '2018 Nov 11', 1146170959, 'Pengembangan'),
(8, 'IDX:K', 'Transportasi & Logistik', 'GIAA', 'Garuda Indonesia (Persero) Tbk.', '2011 Feb 11', 25886576254, 'Utama'),
(9, 'IDX:K', 'Transportasi & Logistik', 'HAIS', 'Hasnur Internasional Shipping Tbk.', '2021 Sep 01', 2626250000, 'Utama'),
(10, 'IDX:K', 'Transportasi & Logistik', 'HELI', 'Jaya Trishindo Tbk.', '2018 Mar 27', 832862387, 'Pengembangan'),
(11, 'IDX:K', 'Transportasi & Logistik', 'IATA', 'Indonesia Transport & Infrastructure Tbk.', '2006 Sep 13', 11415812114, 'Pengembangan'),
(12, 'IDX:K', 'Transportasi & Logistik', 'JAYA', 'Armada Berjaya Trans Tbk.', '2019 Feb 21', 750000210, 'Pengembangan'),
(13, 'IDX:K', 'Transportasi & Logistik', 'KJEN', 'Krida Jaringan Nusantara Tbk.', '2019 Jul 01', 500000000, 'Pengembangan'),
(14, 'IDX:K', 'Transportasi & Logistik', 'LRNA', 'Eka Sari Lorena Transport Tbk.', '2014 Apr 15', 350000022, 'Pengembangan'),
(15, 'IDX:K', 'Transportasi & Logistik', 'MIRA', 'Mitra International Resources Tbk.', '1997 Jan 30', 3961452039, 'Pengembangan'),
(16, 'IDX:K', 'Transportasi & Logistik', 'NELY', 'Pelayaran Nelly Dwi Putri Tbk.', '2012 Oct 11', 2350000000, 'Pengembangan'),
(17, 'IDX:K', 'Transportasi & Logistik', 'PPGL', 'Prima Globalindo Logistik Tbk.', '2020 Jul 20', 750021341, 'Akselerasi'),
(18, 'IDX:K', 'Transportasi & Logistik', 'PURA', 'Putra Rajawali Kencana Tbk.', '2020 Jan 22', 5941264082, 'Pengembangan'),
(19, 'IDX:K', 'Transportasi & Logistik', 'SAFE', 'Steady Safe Tbk.', '1994 Aug 15', 615145012, 'PENGEMBANGAN'),
(20, 'IDX:K', 'Transportasi & Logistik', 'SAPX', 'Satria Antaran Prima Tbk.', '2018 Oct 03', 833333300, 'Pengembangan'),
(21, 'IDX:K', 'Transportasi & Logistik', 'SDMU', 'Sidomulyo Selaras Tbk.', '2011 Jul 12', 1135225000, 'Pengembangan'),
(22, 'IDX:K', 'Transportasi & Logistik', 'SMDR', 'Samudera Indonesia Tbk.', '1999 Jul 05', 3275120000, 'Utama'),
(23, 'IDX:K', 'Transportasi & Logistik', 'TAXI', 'Express Transindo Utama Tbk.', '2012 Nov 02', 10223647156, 'Utama'),
(24, 'IDX:K', 'Transportasi & Logistik', 'TMAS', 'Temas Tbk.', '2003 Jul 09', 5705150000, 'Utama'),
(25, 'IDX:K', 'Transportasi & Logistik', 'TNCA', 'Trimuda Nuansa Citra Tbk.', '2018 Jun 28', 421640000, 'Pengembangan'),
(26, 'IDX:K', 'Transportasi & Logistik', 'TRJA', 'Transkon Jaya Tbk.', '2020 Aug 27', 1510200000, 'Pengembangan'),
(27, 'IDX:K', 'Transportasi & Logistik', 'TRUK', 'Guna Timur Raya Tbk.', '2018 May 23', 435000000, 'PENGEMBANGAN'),
(28, 'IDX:K', 'Transportasi & Logistik', 'WEHA', 'WEHA Transportasi Indonesia Tbk.', '2007 May 31', 886411265, 'Utama');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `daftar_saham_indonesia`
--
ALTER TABLE `daftar_saham_indonesia`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uk_kode_saham` (`kodeSaham`),
  ADD KEY `fk_kode_sektor_emiten` (`kode_sektor`);

--
-- Indeks untuk tabel `daftar_sektor`
--
ALTER TABLE `daftar_sektor`
  ADD PRIMARY KEY (`kode_sektor`);

--
-- Indeks untuk tabel `sektorenergi`
--
ALTER TABLE `sektorenergi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_kode_sektor` (`kode_sektor`);

--
-- Indeks untuk tabel `sektorinfrastruktur`
--
ALTER TABLE `sektorinfrastruktur`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_kode_sektor_infrastruktur` (`kode_sektor`);

--
-- Indeks untuk tabel `sektorkesehatan`
--
ALTER TABLE `sektorkesehatan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_kode_sektor_kesehatan` (`kode_sektor`);

--
-- Indeks untuk tabel `sektorproperti`
--
ALTER TABLE `sektorproperti`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_kode_sektor_properti` (`kode_sektor`);

--
-- Indeks untuk tabel `sektorteknologi`
--
ALTER TABLE `sektorteknologi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_kode_sektor_teknologi` (`kode_sektor`);

--
-- Indeks untuk tabel `sektortransportasi`
--
ALTER TABLE `sektortransportasi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_kode_sektor_transportasi` (`kode_sektor`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `daftar_saham_indonesia`
--
ALTER TABLE `daftar_saham_indonesia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=295;

--
-- AUTO_INCREMENT untuk tabel `sektorenergi`
--
ALTER TABLE `sektorenergi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT untuk tabel `sektorinfrastruktur`
--
ALTER TABLE `sektorinfrastruktur`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT untuk tabel `sektorkesehatan`
--
ALTER TABLE `sektorkesehatan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT untuk tabel `sektorproperti`
--
ALTER TABLE `sektorproperti`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT untuk tabel `sektorteknologi`
--
ALTER TABLE `sektorteknologi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT untuk tabel `sektortransportasi`
--
ALTER TABLE `sektortransportasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `daftar_saham_indonesia`
--
ALTER TABLE `daftar_saham_indonesia`
  ADD CONSTRAINT `fk_kode_sektor_emiten` FOREIGN KEY (`kode_sektor`) REFERENCES `daftar_sektor` (`kode_sektor`);

--
-- Ketidakleluasaan untuk tabel `sektorenergi`
--
ALTER TABLE `sektorenergi`
  ADD CONSTRAINT `fk_kode_sektor` FOREIGN KEY (`kode_sektor`) REFERENCES `daftar_sektor` (`kode_sektor`);

--
-- Ketidakleluasaan untuk tabel `sektorinfrastruktur`
--
ALTER TABLE `sektorinfrastruktur`
  ADD CONSTRAINT `fk_kode_sektor_infrastruktur` FOREIGN KEY (`kode_sektor`) REFERENCES `daftar_sektor` (`kode_sektor`);

--
-- Ketidakleluasaan untuk tabel `sektorkesehatan`
--
ALTER TABLE `sektorkesehatan`
  ADD CONSTRAINT `fk_kode_sektor_kesehatan` FOREIGN KEY (`kode_sektor`) REFERENCES `daftar_sektor` (`kode_sektor`);

--
-- Ketidakleluasaan untuk tabel `sektorproperti`
--
ALTER TABLE `sektorproperti`
  ADD CONSTRAINT `fk_kode_sektor_properti` FOREIGN KEY (`kode_sektor`) REFERENCES `daftar_sektor` (`kode_sektor`);

--
-- Ketidakleluasaan untuk tabel `sektorteknologi`
--
ALTER TABLE `sektorteknologi`
  ADD CONSTRAINT `fk_kode_sektor_teknologi` FOREIGN KEY (`kode_sektor`) REFERENCES `daftar_sektor` (`kode_sektor`);

--
-- Ketidakleluasaan untuk tabel `sektortransportasi`
--
ALTER TABLE `sektortransportasi`
  ADD CONSTRAINT `fk_kode_sektor_transportasi` FOREIGN KEY (`kode_sektor`) REFERENCES `daftar_sektor` (`kode_sektor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
