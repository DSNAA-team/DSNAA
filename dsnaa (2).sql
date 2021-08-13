-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 13 août 2021 à 12:13
-- Version du serveur :  5.7.31
-- Version de PHP : 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `dsnaa`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=105 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add contact form', 8, 'add_contactform'),
(30, 'Can change contact form', 8, 'change_contactform'),
(31, 'Can delete contact form', 8, 'delete_contactform'),
(32, 'Can view contact form', 8, 'view_contactform'),
(33, 'Can add documents', 9, 'add_documents'),
(34, 'Can change documents', 9, 'change_documents'),
(35, 'Can delete documents', 9, 'delete_documents'),
(36, 'Can view documents', 9, 'view_documents'),
(37, 'Can add gallery', 10, 'add_gallery'),
(38, 'Can change gallery', 10, 'change_gallery'),
(39, 'Can delete gallery', 10, 'delete_gallery'),
(40, 'Can view gallery', 10, 'view_gallery'),
(41, 'Can add video library', 11, 'add_videolibrary'),
(42, 'Can change video library', 11, 'change_videolibrary'),
(43, 'Can delete video library', 11, 'delete_videolibrary'),
(44, 'Can view video library', 11, 'view_videolibrary'),
(45, 'Can add video', 12, 'add_video'),
(46, 'Can change video', 12, 'change_video'),
(47, 'Can delete video', 12, 'delete_video'),
(48, 'Can view video', 12, 'view_video'),
(49, 'Can add task', 13, 'add_task'),
(50, 'Can change task', 13, 'change_task'),
(51, 'Can delete task', 13, 'delete_task'),
(52, 'Can view task', 13, 'view_task'),
(53, 'Can add library', 14, 'add_library'),
(54, 'Can change library', 14, 'change_library'),
(55, 'Can delete library', 14, 'delete_library'),
(56, 'Can view library', 14, 'view_library'),
(57, 'Can add image', 15, 'add_image'),
(58, 'Can change image', 15, 'change_image'),
(59, 'Can delete image', 15, 'delete_image'),
(60, 'Can view image', 15, 'view_image'),
(61, 'Can add blog', 16, 'add_blog'),
(62, 'Can change blog', 16, 'change_blog'),
(63, 'Can delete blog', 16, 'delete_blog'),
(64, 'Can view blog', 16, 'view_blog'),
(65, 'Can add site', 17, 'add_site'),
(66, 'Can change site', 17, 'change_site'),
(67, 'Can delete site', 17, 'delete_site'),
(68, 'Can view site', 17, 'view_site'),
(69, 'Can add kv store', 18, 'add_kvstore'),
(70, 'Can change kv store', 18, 'change_kvstore'),
(71, 'Can delete kv store', 18, 'delete_kvstore'),
(72, 'Can view kv store', 18, 'view_kvstore'),
(73, 'Can add article', 19, 'add_article'),
(74, 'Can change article', 19, 'change_article'),
(75, 'Can delete article', 19, 'delete_article'),
(76, 'Can view article', 19, 'view_article'),
(77, 'Can add message', 20, 'add_message'),
(78, 'Can change message', 20, 'change_message'),
(79, 'Can delete message', 20, 'delete_message'),
(80, 'Can view message', 20, 'view_message'),
(81, 'Can add newsletter', 21, 'add_newsletter'),
(82, 'Can change newsletter', 21, 'change_newsletter'),
(83, 'Can delete newsletter', 21, 'delete_newsletter'),
(84, 'Can view newsletter', 21, 'view_newsletter'),
(85, 'Can add submission', 22, 'add_submission'),
(86, 'Can change submission', 22, 'change_submission'),
(87, 'Can delete submission', 22, 'delete_submission'),
(88, 'Can view submission', 22, 'view_submission'),
(89, 'Can add subscription', 23, 'add_subscription'),
(90, 'Can change subscription', 23, 'change_subscription'),
(91, 'Can delete subscription', 23, 'delete_subscription'),
(92, 'Can view subscription', 23, 'view_subscription'),
(93, 'Can add event', 24, 'add_event'),
(94, 'Can change event', 24, 'change_event'),
(95, 'Can delete event', 24, 'delete_event'),
(96, 'Can view event', 24, 'view_event'),
(97, 'Can add media category', 25, 'add_mediacategory'),
(98, 'Can change media category', 25, 'change_mediacategory'),
(99, 'Can delete media category', 25, 'delete_mediacategory'),
(100, 'Can view media category', 25, 'view_mediacategory'),
(101, 'Can add album', 26, 'add_album'),
(102, 'Can change album', 26, 'change_album'),
(103, 'Can delete album', 26, 'delete_album'),
(104, 'Can view album', 26, 'view_album');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$XTPJgZnc6LtcitXL0OFmrL$RxkdWi0CvL2ZLKe7c3V5VX0JJg2bI9zKyMlT3T1lF9E=', '2021-08-13 11:59:29.823427', 1, 'marin', '-Amin', '-Ben Cheikh', 'amin.bencheikh@esprit.tn', 0, 1, '2021-07-13 13:21:10.316989');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'dsnaaapp', 'category'),
(8, 'dsnaaapp', 'contactform'),
(9, 'dsnaaapp', 'documents'),
(10, 'dsnaaapp', 'gallery'),
(11, 'dsnaaapp', 'videolibrary'),
(12, 'dsnaaapp', 'video'),
(13, 'dsnaaapp', 'task'),
(14, 'dsnaaapp', 'library'),
(15, 'dsnaaapp', 'image'),
(16, 'dsnaaapp', 'blog'),
(17, 'sites', 'site'),
(18, 'thumbnail', 'kvstore'),
(19, 'newsletter', 'article'),
(20, 'newsletter', 'message'),
(21, 'newsletter', 'newsletter'),
(22, 'newsletter', 'submission'),
(23, 'newsletter', 'subscription'),
(24, 'dsnaaapp', 'event'),
(25, 'dsnaaapp', 'mediacategory'),
(26, 'dsnaaapp', 'album');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-07-13 13:20:20.411214'),
(2, 'auth', '0001_initial', '2021-07-13 13:20:20.601439'),
(3, 'admin', '0001_initial', '2021-07-13 13:20:20.653199'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-07-13 13:20:20.664452'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-07-13 13:20:20.673432'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-07-13 13:20:20.708375'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-07-13 13:20:20.727288'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-07-13 13:20:20.745242'),
(9, 'auth', '0004_alter_user_username_opts', '2021-07-13 13:20:20.757209'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-07-13 13:20:20.776157'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-07-13 13:20:20.778151'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-07-13 13:20:20.788125'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-07-13 13:20:20.807187'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-07-13 13:20:20.825102'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-07-13 13:20:20.844055'),
(16, 'auth', '0011_update_proxy_permissions', '2021-07-13 13:20:20.854024'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-07-13 13:20:20.873716'),
(18, 'dsnaaapp', '0001_initial', '2021-07-13 13:20:21.186906'),
(19, 'sites', '0001_initial', '2021-07-13 13:20:21.198877'),
(20, 'newsletter', '0001_initial', '2021-07-13 13:20:21.625550'),
(21, 'newsletter', '0002_auto_20150416_1555', '2021-07-13 13:20:21.701853'),
(22, 'newsletter', '0003_auto_20160226_1518', '2021-07-13 13:20:21.762240'),
(23, 'newsletter', '0004_auto_20180407_1043', '2021-07-13 13:20:21.786177'),
(24, 'newsletter', '0005_auto_20190918_0122', '2021-07-13 13:20:21.810113'),
(25, 'newsletter', '0006_auto_20210707_1813', '2021-07-13 13:20:22.061545'),
(26, 'sessions', '0001_initial', '2021-07-13 13:20:22.081780'),
(27, 'sites', '0002_alter_domain_unique', '2021-07-13 13:20:22.111733'),
(28, 'thumbnail', '0001_initial', '2021-07-13 13:20:22.124697'),
(29, 'dsnaaapp', '0002_auto_20210718_1409', '2021-07-18 13:09:57.580622'),
(30, 'dsnaaapp', '0003_alter_documents_pays', '2021-07-26 15:51:47.209247'),
(31, 'dsnaaapp', '0004_auto_20210726_1653', '2021-07-26 15:53:40.333555'),
(32, 'dsnaaapp', '0005_alter_documents_titre', '2021-07-27 14:48:53.183770'),
(33, 'dsnaaapp', '0002_auto_20210813_1233', '2021-08-13 11:33:40.452045'),
(34, 'dsnaaapp', '0003_rename_titre_image_title', '2021-08-13 11:54:15.562489'),
(35, 'dsnaaapp', '0004_rename_title_image_titre', '2021-08-13 11:56:00.474399');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('oqah9dje71v36n6lzk2ffoiyidm398x1', '.eJxVjEEOwiAQRe_C2hAYkIJL956BzDCjVA1NSrsy3l2bdKHb_977L5VxXWpeu8x5ZHVSVh1-N8LykLYBvmO7TbpMbZlH0puid9r1ZWJ5nnf376Bir9_aWyuhcABid4yDQwmUzNUXEyOl4NEXFwqgi4MgIXJyJkUgCAAWvFHvD9-dN2E:1m3ILe:yHofMjTS3XUMVqI5vSNSx7pvbuW39Jg8wq1BXVfPUdA', '2021-07-27 13:21:18.959412'),
('dbndypxhs1ba4n2fq7f23nbipcdzjanx', '.eJxVjEEOwiAQRe_C2hAYkIJL956BzDCjVA1NSrsy3l2bdKHb_977L5VxXWpeu8x5ZHVSVh1-N8LykLYBvmO7TbpMbZlH0puid9r1ZWJ5nnf376Bir9_aWyuhcABid4yDQwmUzNUXEyOl4NEXFwqgi4MgIXJyJkUgCAAWvFHvD9-dN2E:1m8NoS:_BQ9cQinqBciIYyhPFEoKvmOc5tPJpy9R7MF8l8HKe8', '2021-08-10 14:12:04.238759'),
('sf2xa45hykvxczysxtt7asb9mxhg3wrn', '.eJxVjEEOwiAQRe_C2hAYkIJL956BzDCjVA1NSrsy3l2bdKHb_977L5VxXWpeu8x5ZHVSVh1-N8LykLYBvmO7TbpMbZlH0puid9r1ZWJ5nnf376Bir9_aWyuhcABid4yDQwmUzNUXEyOl4NEXFwqgi4MgIXJyJkUgCAAWvFHvD9-dN2E:1mEVqT:sI7pi4iQjWnp1wf2eq_vddJmC-Qlif6AbC-Q6IiFb0s', '2021-08-27 11:59:29.825454'),
('7xvjp47iqrz7awgr3skegivj4j7q34yq', '.eJxVjEEOwiAQRe_C2pBCYSgu3XsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwkzgLJU6_W8T04LoDumO9NZlaXZc5yl2RB-3y2oifl8P9OyjYy7ceFIyGkkqJHUcTrXeRJ681I2SnIimbLYyA7EZLhnzK4IyiDJqngY14fwDylThA:1m7gF0:MBD_W2kxHlVuNrupRH3FNbbMpTj0Wz-IujdGUmqYw-E', '2021-08-08 15:40:34.652410'),
('p1sl52om4rh4t7klac5dedyosjbkc8wp', '.eJxVjEEOwiAQRe_C2pBCYSgu3XsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwkzgLJU6_W8T04LoDumO9NZlaXZc5yl2RB-3y2oifl8P9OyjYy7ceFIyGkkqJHUcTrXeRJ681I2SnIimbLYyA7EZLhnzK4IyiDJqngY14fwDylThA:1m2Cg9:U5yoHpwVkvJ9Jutfbm_rVM3_bTaoji1-CjZmzg2W3vs', '2021-07-24 13:05:57.949814'),
('zobzkz8xg6tqs31e6faa8inp6k6hrvsv', '.eJxVjEEOwiAQRe_C2pBCYSgu3XsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwkzgLJU6_W8T04LoDumO9NZlaXZc5yl2RB-3y2oifl8P9OyjYy7ceFIyGkkqJHUcTrXeRJ681I2SnIimbLYyA7EZLhnzK4IyiDJqngY14fwDylThA:1m2ald:qtCCbqMV5RThkQ4rs2uT_H42oylqSVAMBi1lFS_DPjI', '2021-07-25 14:49:13.894052');

-- --------------------------------------------------------

--
-- Structure de la table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_album`
--

DROP TABLE IF EXISTS `dsnaaapp_album`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_album` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` longtext NOT NULL,
  `description` longtext NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `Category_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dsnaaapp_album_Category_id_d63ac72b` (`Category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `dsnaaapp_album`
--

INSERT INTO `dsnaaapp_album` (`id`, `title`, `description`, `date_creation`, `thumbnail`, `Category_id`) VALUES
(2, 'second album', 'second album description', '2021-07-23 20:20:09.051797', 'AI_Getty-1179477351-scaled-e1611778221405_a0yMV3o.jpg', 1),
(3, 'aaaa', 'eee', '2021-07-28 17:01:03.138773', 'ai-article-pic10_mUHSkaI.jpg', 1),
(4, 'thrid album', 'this is description example', '2021-07-31 17:50:15.169937', 'ai-article-pic10_BGN4Xkz.jpg', 1),
(5, 'machine learning album', 'this is machine learning album\'s description', '2021-07-31 20:11:30.959632', 'machineLearning3.png', 3);

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_blog`
--

DROP TABLE IF EXISTS `dsnaaapp_blog`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_blog` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titre` varchar(255) DEFAULT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `content` longtext,
  `date_creation` datetime(6) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `autheur_id` int(11) DEFAULT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dsnaaapp_blog_slug_eb6e1d06` (`slug`),
  KEY `dsnaaapp_blog_autheur_id_8351eff1` (`autheur_id`),
  KEY `dsnaaapp_blog_category_id_6934d0d8` (`category_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_category`
--

DROP TABLE IF EXISTS `dsnaaapp_category`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `theme` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_contactform`
--

DROP TABLE IF EXISTS `dsnaaapp_contactform`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_contactform` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_documents`
--

DROP TABLE IF EXISTS `dsnaaapp_documents`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_documents` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titre` varchar(20) NOT NULL,
  `autheur` varchar(20) NOT NULL,
  `organization` varchar(20) NOT NULL,
  `date_publication` date NOT NULL,
  `fichier` varchar(100) DEFAULT NULL,
  `lien` varchar(30) NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `language` varchar(30) DEFAULT NULL,
  `mot_cle` varchar(30) DEFAULT NULL,
  `pays` varchar(50) DEFAULT NULL,
  `strategie_national` varchar(10) DEFAULT NULL,
  `type_de_doc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dsnaaapp_documents_titre_7a93b122_uniq` (`titre`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `dsnaaapp_documents`
--

INSERT INTO `dsnaaapp_documents` (`id`, `titre`, `autheur`, `organization`, `date_publication`, `fichier`, `lien`, `thumbnail`, `language`, `mot_cle`, `pays`, `strategie_national`, `type_de_doc`) VALUES
(3, 'Deloitte-gx-ai-and-r', 'xxx', 'aeaz', '2021-07-03', 'uploads/a_faire_vCCcSsA.txt', 'lien', 'images/deloitte-gx_lnzlNva.png', '1', '#IA', '236', 'True', '2'),
(4, 'deloitte-nl-innovati', 'xxx', 'dasx', '2021-07-17', 'uploads/deloitte-nl-innovatie-artificial-intelligence-16-practical-cases.pdf', 'xxxxx', 'images/deloitte-nl-innovatie-artificial-intelligence-16-practical-cases.png', '1', '#IA', '79', 'True', '1');

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_documents_library`
--

DROP TABLE IF EXISTS `dsnaaapp_documents_library`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_documents_library` (
  `id` bigint(20) NOT NULL,
  `documents_id` bigint(20) NOT NULL,
  `library_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_event`
--

DROP TABLE IF EXISTS `dsnaaapp_event`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_event` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `date_event` date NOT NULL,
  `organizer` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `place` varchar(50) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `dsnaaapp_event`
--

INSERT INTO `dsnaaapp_event` (`id`, `title`, `description`, `date_event`, `organizer`, `type`, `place`, `image`) VALUES
(2, 'new ppp', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic', '2021-01-15', 'Aziz', 'gaming', 'Tunis', 'images/AI_Getty-1179477351-scaled-e1611778221405.jpg'),
(4, 'second event', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum', '2021-12-02', 'amin ben cheikh', 'ai open event', 'Sousse', 'images/ai-article-pic10.jpg');

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_image`
--

DROP TABLE IF EXISTS `dsnaaapp_image`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_image` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titre` longtext NOT NULL,
  `description` longtext NOT NULL,
  `date_publication` datetime(6) NOT NULL,
  `lieu` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `album_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dsnaaapp_image_album_id_d4e29dd6` (`album_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `dsnaaapp_image`
--

INSERT INTO `dsnaaapp_image` (`id`, `titre`, `description`, `date_publication`, `lieu`, `image`, `album_id`) VALUES
(1, 'hh', 'oo', '2021-07-25 15:51:40.722428', 'tunis', 'AI_Getty-1179477351-scaled-e1611778221405_X0khDVq.jpg', 2),
(3, 'ai image', 'this is ai image', '2021-07-31 21:42:11.596403', 'tunis', 'ai2x.png', 2);

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_library`
--

DROP TABLE IF EXISTS `dsnaaapp_library`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_library` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titre` varchar(255) NOT NULL,
  `date_creation` date NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `dsnaaapp_library`
--

INSERT INTO `dsnaaapp_library` (`id`, `titre`, `date_creation`, `image`) VALUES
(9, 'digital transformation monitor UE', '2021-08-26', 'images/digital_transformation_monitor_UE.jpg'),
(8, 'Deloitte', '2021-07-31', 'images/Deloitte_5zakBro.jpg');

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_library_document`
--

DROP TABLE IF EXISTS `dsnaaapp_library_document`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_library_document` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `library_id` bigint(20) NOT NULL,
  `documents_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dsnaaapp_library_document_library_id_documents_id_b72007cc_uniq` (`library_id`,`documents_id`),
  KEY `dsnaaapp_library_document_library_id_b8234a75` (`library_id`),
  KEY `dsnaaapp_library_document_documents_id_c76b53a4` (`documents_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `dsnaaapp_library_document`
--

INSERT INTO `dsnaaapp_library_document` (`id`, `library_id`, `documents_id`) VALUES
(5, 8, 3);

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_mediacategory`
--

DROP TABLE IF EXISTS `dsnaaapp_mediacategory`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_mediacategory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` longtext NOT NULL,
  `description` longtext NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `dsnaaapp_mediacategory`
--

INSERT INTO `dsnaaapp_mediacategory` (`id`, `title`, `description`, `thumbnail`) VALUES
(1, 'data science', 'this categrory  reflects  data science field in our media', 'ai-article-pic10.jpg'),
(3, 'machine learning', 'machine lerning category', 'unnamed.png');

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_task`
--

DROP TABLE IF EXISTS `dsnaaapp_task`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_task` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext,
  `complete` tinyint(1) NOT NULL,
  `create` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dsnaaapp_task_user_id_e5903e30` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_video`
--

DROP TABLE IF EXISTS `dsnaaapp_video`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_video` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titre` longtext NOT NULL,
  `date_publication` datetime(6) NOT NULL,
  `organisation` longtext NOT NULL,
  `longueur` double NOT NULL,
  `description` longtext NOT NULL,
  `lien` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_videolibrary`
--

DROP TABLE IF EXISTS `dsnaaapp_videolibrary`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_videolibrary` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titre` longtext NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  `theme` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `dsnaaapp_video_videolibrary`
--

DROP TABLE IF EXISTS `dsnaaapp_video_videolibrary`;
CREATE TABLE IF NOT EXISTS `dsnaaapp_video_videolibrary` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `video_id` bigint(20) NOT NULL,
  `videolibrary_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dsnaaapp_video_videoLibr_video_id_videolibrary_id_e93b2789_uniq` (`video_id`,`videolibrary_id`),
  KEY `dsnaaapp_video_videoLibrary_video_id_c5d6c9e9` (`video_id`),
  KEY `dsnaaapp_video_videoLibrary_videolibrary_id_0e10d495` (`videolibrary_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `newsletter_article`
--

DROP TABLE IF EXISTS `newsletter_article`;
CREATE TABLE IF NOT EXISTS `newsletter_article` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sortorder` int(10) UNSIGNED NOT NULL,
  `title` varchar(200) NOT NULL,
  `text` longtext NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `post_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `newsletter_article_post_id_sortorder_cbe3c629_uniq` (`post_id`,`sortorder`),
  KEY `newsletter_article_post_id_c481e545` (`post_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `newsletter_message`
--

DROP TABLE IF EXISTS `newsletter_message`;
CREATE TABLE IF NOT EXISTS `newsletter_message` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `date_create` datetime(6) NOT NULL,
  `date_modify` datetime(6) NOT NULL,
  `newsletter_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `newsletter_message_slug_newsletter_id_a2ab3653_uniq` (`slug`,`newsletter_id`),
  KEY `newsletter_message_slug_6dae36a9` (`slug`),
  KEY `newsletter_message_newsletter_id_b77d9df1` (`newsletter_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `newsletter_newsletter`
--

DROP TABLE IF EXISTS `newsletter_newsletter`;
CREATE TABLE IF NOT EXISTS `newsletter_newsletter` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `sender` varchar(200) NOT NULL,
  `visible` tinyint(1) NOT NULL,
  `send_html` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `newsletter_newsletter_visible_db80e140` (`visible`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `newsletter_newsletter_site`
--

DROP TABLE IF EXISTS `newsletter_newsletter_site`;
CREATE TABLE IF NOT EXISTS `newsletter_newsletter_site` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `newsletter_id` bigint(20) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `newsletter_newsletter_site_newsletter_id_site_id_eaadd4df_uniq` (`newsletter_id`,`site_id`),
  KEY `newsletter_newsletter_site_newsletter_id_d5cf228e` (`newsletter_id`),
  KEY `newsletter_newsletter_site_site_id_2a546dc1` (`site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `newsletter_submission`
--

DROP TABLE IF EXISTS `newsletter_submission`;
CREATE TABLE IF NOT EXISTS `newsletter_submission` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `publish_date` datetime(6) DEFAULT NULL,
  `publish` tinyint(1) NOT NULL,
  `prepared` tinyint(1) NOT NULL,
  `sent` tinyint(1) NOT NULL,
  `sending` tinyint(1) NOT NULL,
  `message_id` bigint(20) NOT NULL,
  `newsletter_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `newsletter_submission_publish_date_6c3d8801` (`publish_date`),
  KEY `newsletter_submission_publish_2ceb081e` (`publish`),
  KEY `newsletter_submission_prepared_12eea099` (`prepared`),
  KEY `newsletter_submission_sent_7c1e3f56` (`sent`),
  KEY `newsletter_submission_sending_40b87529` (`sending`),
  KEY `newsletter_submission_message_id_35227c2e` (`message_id`),
  KEY `newsletter_submission_newsletter_id_8fa5ae76` (`newsletter_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `newsletter_submission_subscriptions`
--

DROP TABLE IF EXISTS `newsletter_submission_subscriptions`;
CREATE TABLE IF NOT EXISTS `newsletter_submission_subscriptions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `submission_id` bigint(20) NOT NULL,
  `subscription_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `newsletter_submission_su_submission_id_subscripti_fa14b47b_uniq` (`submission_id`,`subscription_id`),
  KEY `newsletter_submission_subscriptions_submission_id_0cda0c3f` (`submission_id`),
  KEY `newsletter_submission_subscriptions_subscription_id_be932b58` (`subscription_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `newsletter_subscription`
--

DROP TABLE IF EXISTS `newsletter_subscription`;
CREATE TABLE IF NOT EXISTS `newsletter_subscription` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `ip` char(39) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `activation_code` varchar(40) NOT NULL,
  `subscribed` tinyint(1) NOT NULL,
  `subscribe_date` datetime(6) DEFAULT NULL,
  `unsubscribed` tinyint(1) NOT NULL,
  `unsubscribe_date` datetime(6) DEFAULT NULL,
  `newsletter_id` bigint(20) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `newsletter_subscription_user_id_email_newsletter_0a9641e0_uniq` (`user_id`,`email`,`newsletter_id`),
  KEY `newsletter_subscription_email_3b8020aa` (`email`),
  KEY `newsletter_subscription_subscribed_350402fe` (`subscribed`),
  KEY `newsletter_subscription_unsubscribed_8ae75c15` (`unsubscribed`),
  KEY `newsletter_subscription_newsletter_id_e9d08ab9` (`newsletter_id`),
  KEY `newsletter_subscription_user_id_4185bd67` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `thumbnail_kvstore`
--

DROP TABLE IF EXISTS `thumbnail_kvstore`;
CREATE TABLE IF NOT EXISTS `thumbnail_kvstore` (
  `key` varchar(200) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
