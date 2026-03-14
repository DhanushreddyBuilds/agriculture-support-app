-- Database Export for AgroAI
-- Import this file in phpMyAdmin to set up the database automatically.

-- 1. Create the Database
CREATE DATABASE IF NOT EXISTS agroai_db;
USE agroai_db;

-- 2. Create Users Table (for Login/Register)
CREATE TABLE IF NOT EXISTS admin_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Create Chats Table (for storing history)
-- (Optional: Matches your existing structure)
CREATE TABLE IF NOT EXISTS chats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_message TEXT NOT NULL,
    bot_reply TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Insert Default Admin User (Optional)
-- Username: admin
-- Password: password123 (hashed for security, this is just a placeholder example)
-- INSERT INTO admin_users (username, password) VALUES ('admin', 'scrypt:32768:8:1$...'); 
