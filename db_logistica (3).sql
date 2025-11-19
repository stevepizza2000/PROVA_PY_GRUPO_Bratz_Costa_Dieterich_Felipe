-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 19/11/2025 às 17:41
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

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
CREATE TABLE `tb_auditoria` (
  `id_auditoria` int(11) NOT NULL,
  `codigo` int(11) NOT NULL,
  `status_antigo` varchar(100) NOT NULL,
  `status_novo` varchar(100) NOT NULL,
  `local_antigo` varchar(100) NOT NULL,
  `local_novo` varchar(100) NOT NULL,
  `data_hora` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_auditoria`
--

INSERT INTO `tb_auditoria` (`id_auditoria`, `codigo`, `status_antigo`, `status_novo`, `local_antigo`, `local_novo`, `data_hora`) VALUES
(1, 62678705, 'pendente', 'em trânsito', 'Centro de distribuição', 'caxias', '');

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_envios`
--

DROP TABLE IF EXISTS `tb_envios`;
CREATE TABLE `tb_envios` (
  `id_envio` int(11) NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  `condicao` enum('pendente','em trânsito','entregue') DEFAULT 'pendente',
  `localizacao` varchar(255) DEFAULT NULL,
  `remetente` varchar(255) DEFAULT NULL,
  `destinatario` varchar(255) DEFAULT NULL,
  `end_remetente` varchar(255) DEFAULT NULL,
  `end_destinatario` varchar(255) DEFAULT NULL,
  `data_postagem` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_users`
--

DROP TABLE IF EXISTS `tb_users`;
CREATE TABLE `tb_users` (
  `id_user` int(11) NOT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `tipo` enum('usuario','operador','admin') NOT NULL DEFAULT 'usuario'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_users`
--

INSERT INTO `tb_users` (`id_user`, `login`, `senha`, `tipo`) VALUES
(1, 'admin', '$2b$12$SMLkjQzxfL/lYk3ugbAsDeDS88xttcVQ4YRV4ePuqqidJuPEXTgjW', 'admin'),
(3, 'arthur', '$2b$12$IxHbIBcWeDABXb9sidBxl.qDoB8FQxro.jxBCeaQl9GkqlvzIm7IC', 'operador');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `tb_auditoria`
--
ALTER TABLE `tb_auditoria`
  ADD PRIMARY KEY (`id_auditoria`);

--
-- Índices de tabela `tb_envios`
--
ALTER TABLE `tb_envios`
  ADD PRIMARY KEY (`id_envio`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Índices de tabela `tb_users`
--
ALTER TABLE `tb_users`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `login` (`login`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `tb_auditoria`
--
ALTER TABLE `tb_auditoria`
  MODIFY `id_auditoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tb_envios`
--
ALTER TABLE `tb_envios`
  MODIFY `id_envio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tb_users`
--
ALTER TABLE `tb_users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
