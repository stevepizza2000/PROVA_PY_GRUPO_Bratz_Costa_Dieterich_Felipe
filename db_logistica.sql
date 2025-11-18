-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 18/11/2025 às 19:49
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

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_envios`
--

DROP TABLE IF EXISTS `tb_envios`;
CREATE TABLE `tb_envios` (
  `id_envio` int(11) NOT NULL,
  `codigo` int(10) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `condicao` enum('pendente','em trânsito','entregue') NOT NULL,
  `localizacao` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_users`
--

DROP TABLE IF EXISTS `tb_users`;
CREATE TABLE `tb_users` (
  `id_user` int(11) NOT NULL,
  `login` varchar(100) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `tipo` enum('usuario','operador','admin') DEFAULT 'usuario'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_users`
--

INSERT INTO `tb_users` (`id_user`, `login`, `senha`, `tipo`) VALUES
(1, 'arthur', '$2b$12$o3w6G9v4YxFLsz0yjnXfbelmT6oLc7g5LLrvKzzVolh2mJrJUkpJm', 'usuario'),
(2, 'felps', '$2b$12$vCd3GyB08tOO4l0/57ImvuyJvFmzobCfMATKIwGJRCqi6Fnnn5TNW', 'usuario'),
(3, 'costinha', '$2b$12$0cjEjFBi4i.YYASI5km44emWuCVtKzQsejqqpRk9.J4o1O8pe7u12', 'usuario');

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
  ADD PRIMARY KEY (`id_envio`);

--
-- Índices de tabela `tb_users`
--
ALTER TABLE `tb_users`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `tb_auditoria`
--
ALTER TABLE `tb_auditoria`
  MODIFY `id_auditoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tb_envios`
--
ALTER TABLE `tb_envios`
  MODIFY `id_envio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tb_users`
--
ALTER TABLE `tb_users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
