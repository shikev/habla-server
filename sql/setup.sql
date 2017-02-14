-- phpMyAdmin SQL Dump
-- version 4.6.5.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 31, 2017 at 10:30 AM
-- Server version: 5.6.34
-- PHP Version: 7.1.0

CREATE DATABASE habla;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "-05:00";

USE habla;


-- --------------------------------------------------------

--
-- Table structure for table `Comments`
--

CREATE TABLE `Comments` (
  `id` int(11) NOT NULL,
  `content` text NOT NULL,
  `url` varchar(500) NOT NULL,
  `originalPostTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `lastUpdated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `GroupComments`
--

CREATE TABLE `GroupComments` (
  `commentId` int(11) NOT NULL,
  `groupId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Groups`
--

CREATE TABLE `Groups` (
  `id` int(11) NOT NULL,
  `creator` varchar(64) NOT NULL,
  `password` varchar(128) NOT NULL,
  `name` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Members`
--

CREATE TABLE `Members` (
  `username` varchar(64) NOT NULL,
  `groupId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Comments`
--
ALTER TABLE `Comments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `GroupComments`
--
ALTER TABLE `GroupComments`
  ADD PRIMARY KEY (`commentId`,`groupId`),
  ADD KEY `groupDeletion` (`groupId`);

--
-- Indexes for table `Groups`
--
ALTER TABLE `Groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `Members`
--
ALTER TABLE `Members`
  ADD PRIMARY KEY (`username`,`groupId`),
  ADD KEY `GroupMember` (`groupId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Comments`
--
ALTER TABLE `Comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Groups`
--
ALTER TABLE `Groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `GroupComments`
--
ALTER TABLE `GroupComments`
  ADD CONSTRAINT `commentDeletion` FOREIGN KEY (`commentId`) REFERENCES `Comments` (`id`),
  ADD CONSTRAINT `groupDeletion` FOREIGN KEY (`groupId`) REFERENCES `Groups` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `Members`
--
ALTER TABLE `Members`
  ADD CONSTRAINT `GroupMember` FOREIGN KEY (`groupId`) REFERENCES `Groups` (`id`) ON DELETE CASCADE;
