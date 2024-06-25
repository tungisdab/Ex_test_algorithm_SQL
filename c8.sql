-- Tạo database
CREATE DATABASE vmo;
USE vmo;

-- Phần a
-- Tạo bảng user
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    fullname VARCHAR(255) NOT NULL,
    avatar VARCHAR(255),
    birthday TIMESTAMP,
    created_time TIMESTAMP NOT NULL
);

-- Tạo bảng friend
CREATE TABLE friend
(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    sender_id    INT NOT NULL,
    receiver_id  INT NOT NULL,
    status       VARCHAR(50) CHECK (status IN ('pending', 'accepted', 'rejected')),
    created_time TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES user (id),
    FOREIGN KEY (receiver_id) REFERENCES user (id)
);

-- Tạo bảng message
CREATE TABLE message
(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    sender_id    INT         NOT NULL,
    receiver_id  INT         NOT NULL,
    type         VARCHAR(50) CHECK(type IN('text', 'image', 'video', 'file')) NOT NULL,
    content      VARCHAR(255),
    status       VARCHAR(50) CHECK(status IN('sent', 'pending_read', 'read')),
    created_time DATETIME,
    FOREIGN KEY (sender_id) REFERENCES user (id),
    FOREIGN KEY (receiver_id) REFERENCES user (id)
);

-- Phần b
-- insert dữ liệu vào bảng user
INSERT INTO user (username, password, fullname, avatar, birthday, created_time) VALUES
('khanh', '123456', 'Cong Khanh', 'ava1.jpg', '1990-05-15 00:00:00', CURRENT_TIMESTAMP),
('hue', '654321', 'Ta Hue', 'ava2.png', '1992-08-22 00:00:00', CURRENT_TIMESTAMP),
('mit', '888888', 'Mai Anh', 'ava3.gif', '1985-11-30 00:00:00', CURRENT_TIMESTAMP),
('tung', 'password', 'Nguyen Tung', 'ava4.bmp', '1978-02-18 00:00:00', CURRENT_TIMESTAMP);

-- insert dữ liệu vào bảng friend
INSERT INTO friend (sender_id, receiver_id, status, created_time) VALUE
(1, 3, 'accepted', '2024-06-25 11:11:00'),
(3, 2, 'pending', '2024-06-25 11:23:00'),
(3, 1, 'rejected', '2024-06-25 11:33:00'),
(2, 4, 'accepted', '2024-06-25 12:15:00');

-- insert dữ liệu vào bảng message
INSERT INTO message (sender_id, receiver_id, type, content, status, created_time) VALUE
(2, 4, 'image', '', 'sent', CURRENT_TIMESTAMP),
(4, 2, 'video', '', 'pending_read', CURRENT_TIMESTAMP),
(2, 4, 'image', '', 'read', CURRENT_TIMESTAMP),
(1, 3, 'text', 'hihi', 'sent', CURRENT_TIMESTAMP);

-- Phần c
-- Lấy id, username, fullname, avatar: của các user có id =  2, 3.
SELECT id, username, fullname, avatar FROM user
WHERE id in(2,3);

-- Lấy các bạn bè (gồm thông tin sau: id, username, fullname, avatar) của user có id = 2.
SELECT u.id, u.username, u.fullname, u.avatar
FROM user u JOIN friend f 
ON u.id = f.sender_id OR u.id = f.receiver_id
WHERE (f.sender_id = 2 OR f.receiver_id = 2) AND u.id != 2 AND f.status = 'accepted';

-- Lấy tin nhắn của user có id = 2 với một bàn bè nào đó (ví dụ: id bạn bè = 3). Các trường lấy ra gồm: message_id, sender_id, receiver_id, type, status, content, created_time.
SELECT id AS message_id, sender_id, receiver_id, type, status, content, created_time FROM message
WHERE (sender_id = 3 and receiver_id = 2) OR (sender_id = 2 and receiver_id = 3);



