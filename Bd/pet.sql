-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-05-2023 a las 16:22:25
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pet`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertarDueno` (IN `Nombre_Completo` VARCHAR(150), IN `Celular` VARCHAR(20), IN `Celular_Secundario` VARCHAR(20), IN `Correo` VARCHAR(150), IN `Municipio` VARCHAR(50), IN `Mascota` INT(11))   BEGIN
INSERT INTO tbl_dueno(Nombre_Completo_D,Celular_D,Celular_Secundario_D,Correo_D,Municipio_D,Mascota_Id)
VALUES(Nombre_Completo,Celular,Celular_Secundario,Correo,Municipio,Mascota);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
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
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(12, 'pbkdf2_sha256$600000$34T2ttkkiskotFNI4f1y27$GrblB11hyKZr2dwmXuK1T8eMe8+1Mss38ZZk03ABHEQ=', '2023-05-08 03:28:12.385778', 0, 'ARANGUSFT', '', '', 'santiago@gmail.com', 0, 1, '2023-05-08 03:27:59.137458'),
(14, 'pbkdf2_sha256$600000$UoE9Vgxu01nIO2NYwFyqYi$x7jQpe5trzyhcPEvqENWO1jcMJP7JFaZ4oC/AvKFByA=', '2023-05-17 13:51:00.182382', 0, 'Arnol123', '', '', 'arnol@gmail.com', 0, 1, '2023-05-17 11:01:22.115867'),
(15, 'pbkdf2_sha256$600000$Wk7mnB2sOiNs2draTiJMQD$zjeZCPGIrF/U0GeesuwnfDuNtSP72UVllVY2dxsFZnI=', '2023-05-19 11:57:00.453594', 0, 'Arnol_07', '', '', 'arnol5417@gmail.com', 0, 1, '2023-05-17 13:46:45.362379');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-04-24 04:32:50.051253'),
(2, 'auth', '0001_initial', '2023-04-24 04:32:50.346020'),
(3, 'admin', '0001_initial', '2023-04-24 04:32:50.406163'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-04-24 04:32:50.422152'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-24 04:32:50.428104'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-04-24 04:32:50.470263'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-04-24 04:32:50.497727'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-04-24 04:32:50.509729'),
(9, 'auth', '0004_alter_user_username_opts', '2023-04-24 04:32:50.515713'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-04-24 04:32:50.568275'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-04-24 04:32:50.575239'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-04-24 04:32:50.615534'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-04-24 04:32:50.629420'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-04-24 04:32:50.641870'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-04-24 04:32:50.654500'),
(16, 'auth', '0011_update_proxy_permissions', '2023-04-24 04:32:50.661482'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-04-24 04:32:50.672670'),
(18, 'sessions', '0001_initial', '2023-04-24 04:32:50.690620');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('33299nqpa50l9h8ex6l0kgn6ft2wjwi1', '.eJxVjEEOwiAQRe_C2hCGUhhcuvcMZGAmUjU0Ke3KeHdt0oVu_3vvv1Siba1p67KkidVZOXX63TKVh7Qd8J3abdZlbusyZb0r-qBdX2eW5-Vw_w4q9fqto3OAFn0phJ4zMPrRxDzIEAAjjtlKQBQMVjxzMQRgWcAYYG8xiHp_AMXkNyU:1pr8Rw:OMQ1wh_9YniImaeexq-53IDzyIHUuKzC29UjiEPWplk', '2023-05-09 02:30:36.526911'),
('3pfiz2blqkq77qov9a0mabr4ggj8dkde', '.eJxVjEsOAiEQBe_C2hBoEGiX7j0D4dPIqIFkmFkZ725IZqHbV1XvzXzYt-r3QatfMrswqdnpd4whPalNkh-h3TtPvW3rEvlU-EEHv_VMr-vh_h3UMOqswZpiRVYkgyUgB9apIowsqI1UaIoWBCpKQIzJZIW6YMlCA-AZhGOfL-45Nvo:1pzF2w:rVJ-ft066CW5nUF219KwXq-YARQls80KszBsrR1MfPU', '2023-05-31 11:10:18.332767'),
('dc7jzflwr9pmumfd7ac8yuo55qoxto63', '.eJxVjDkOwjAUBe_iGlmxgzdKes5g_U04gGwpTirE3UmkFNDOzHtvlWFdSl67zHlidVFmVKdfiEBPqbvhB9R709TqMk-o90QftutbY3ldj_bvoEAv2zqdwYXReIoMiEPCIGKBOdpk0AJ69FbYESElMnGDwSFY8nEwNiSnPl8lNDiO:1pwDiv:a63vgt5ZFcFZY5rf7BsVAhszyZGcR0vKn3ySVFC9H4A', '2023-05-23 03:09:09.838621'),
('e3zhty5hfu8nr1upbnox44if6ea0hx6z', '.eJxVjEsOAiEQBe_C2hBoEGiX7j0D4dPIqIFkmFkZ725IZqHbV1XvzXzYt-r3QatfMrswqdnpd4whPalNkh-h3TtPvW3rEvlU-EEHv_VMr-vh_h3UMOqswZpiRVYkgyUgB9apIowsqI1UaIoWBCpKQIzJZIW6YMlCA-AZhGOfL-45Nvo:1pzEuS:QxvLuxdwoRuhWrV3dUv_C689dfVjTlxV2zkOaGuuWMk', '2023-05-31 11:01:32.922340'),
('j03kamvodem4k1ydsiw5wavg7m8ixa1j', '.eJxVjMsOwiAQRf-FtSE8JiAu3fsNhGEGqRpISrtq_Hdt0oVu7znnbiKmdalxHTzHicRFaCNOvyOm_OS2E3qkdu8y97bME8pdkQcd8taJX9fD_TuoadRvDQUVBguKHTjWGjSwPxOywwDO2RyS98FkZQpli6A8ETDaAhaDByfeH_uvN9w:1pvrXo:jRqBxEIahI93_Cr75DS6hK_nE7GKst5Zf2rDwsHvj_A', '2023-05-22 03:28:12.389864'),
('k2ql7aq26kmpitvjuaw7eiq1vhi0assz', '.eJxVjDEOwjAMRe-SGUXYSRzCyM4ZKid2aAG1UtNOiLtDpQ6w_vfef5mO16Xv1qZzN4g5Gwjm8DtmLg8dNyJ3Hm-TLdO4zEO2m2J32ux1En1edvfvoOfWf-sopC5kKJKAqmphpewEvMPkKKKiTxgrCmvIBNF7PHlMR4JKtYCa9wcSDDfe:1pzyjE:89nSwRz8Jw0wOYtvujZg-N7oIQL7yjnb2ddhYhr8Wh4', '2023-06-02 11:57:00.454846'),
('sdvgm7g03rudsay78hucn4tnx6pbuvwi', '.eJxVjE0OwiAYBe_C2pACBcGle89Avr9K1dCktCvj3W2TLnQ7M--9VYZ1KXltMueR1UVFdfplCPSUugt-QL1Pmqa6zCPqPdGHbfo2sbyuR_t3UKCVbT2Ic3QO1gigCWzJeMtMYXDihVOE2McNIqGVZJm8c8l3GIPBnrtk1ecLAXM4MA:1psDwo:4PtElfGk13A9C8zv6rOx8V_tw1-cFKou9gs3uMdc5hE', '2023-05-12 02:34:58.183266');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_caracteristicas`
--

CREATE TABLE `tbl_caracteristicas` (
  `Id_Caracteristicas` int(11) NOT NULL,
  `Estilo_Placa_C` varchar(50) NOT NULL,
  `Estilo_Color_C` varchar(50) NOT NULL,
  `Dueno_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_dueno`
--

CREATE TABLE `tbl_dueno` (
  `Id_Dueno` int(11) NOT NULL,
  `Nombre_Completo_D` varchar(150) NOT NULL,
  `Celular_D` varchar(20) NOT NULL,
  `Celular_Secundario_D` varchar(20) NOT NULL,
  `Correo_D` varchar(150) NOT NULL,
  `Municipio_D` varchar(50) NOT NULL,
  `Mascota_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_mascota`
--

CREATE TABLE `tbl_mascota` (
  `Id_Mascota` int(11) NOT NULL,
  `Nombre_M` varchar(50) NOT NULL,
  `Raza_M` varchar(50) NOT NULL,
  `Color_M` varchar(50) NOT NULL,
  `Foto_M` varchar(255) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `tbl_caracteristicas`
--
ALTER TABLE `tbl_caracteristicas`
  ADD PRIMARY KEY (`Id_Caracteristicas`),
  ADD KEY `Dueno_Id` (`Dueno_Id`);

--
-- Indices de la tabla `tbl_dueno`
--
ALTER TABLE `tbl_dueno`
  ADD PRIMARY KEY (`Id_Dueno`),
  ADD KEY `Mascota_Id` (`Mascota_Id`);

--
-- Indices de la tabla `tbl_mascota`
--
ALTER TABLE `tbl_mascota`
  ADD PRIMARY KEY (`Id_Mascota`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `tbl_caracteristicas`
--
ALTER TABLE `tbl_caracteristicas`
  MODIFY `Id_Caracteristicas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tbl_dueno`
--
ALTER TABLE `tbl_dueno`
  MODIFY `Id_Dueno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `tbl_mascota`
--
ALTER TABLE `tbl_mascota`
  MODIFY `Id_Mascota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `tbl_caracteristicas`
--
ALTER TABLE `tbl_caracteristicas`
  ADD CONSTRAINT `tbl_caracteristicas_ibfk_1` FOREIGN KEY (`Dueno_Id`) REFERENCES `tbl_dueno` (`Id_Dueno`);

--
-- Filtros para la tabla `tbl_dueno`
--
ALTER TABLE `tbl_dueno`
  ADD CONSTRAINT `tbl_dueno_ibfk_1` FOREIGN KEY (`Mascota_Id`) REFERENCES `tbl_mascota` (`Id_Mascota`);

--
-- Filtros para la tabla `tbl_mascota`
--
ALTER TABLE `tbl_mascota`
  ADD CONSTRAINT `tbl_mascota_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
