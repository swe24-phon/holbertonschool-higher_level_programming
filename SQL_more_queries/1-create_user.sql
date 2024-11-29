-- Create a new MySQL user 'user_0d_1' with the specified password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to the new user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
