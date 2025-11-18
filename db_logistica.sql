-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 18/11/2025 às 18:12
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `db_logistica`
--
CREATE DATABASE IF NOT EXISTS `db_logistica` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_logistica`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_auditoria`
--

DROP TABLE IF EXISTS `tb_auditoria`;
CREATE TABLE IF NOT EXISTS `tb_auditoria` (
  `id_auditoria` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` int(11) NOT NULL,
  `status_antigo` varchar(100) NOT NULL,
  `status_novo` varchar(100) NOT NULL,
  `local_antigo` varchar(100) NOT NULL,
  `local_novo` varchar(100) NOT NULL,
  `data_hora` varchar(100) NOT NULL,
  PRIMARY KEY (`id_auditoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_envios`
--

DROP TABLE IF EXISTS `tb_envios`;
CREATE TABLE IF NOT EXISTS `tb_envios` (
  `id_envio` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` int(10) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `condicao` enum('Pendente','Em trânsito','Entregue') NOT NULL,
  `localizacao` varchar(100) NOT NULL,
  PRIMARY KEY (`id_envio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_users`
--

DROP TABLE IF EXISTS `tb_users`;
CREATE TABLE IF NOT EXISTS `tb_users` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(100) NOT NULL,
  `senha` int(8) NOT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
