-- Створення таблиці пристроїв
CREATE TABLE пристрої (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    модель VARCHAR(255) NOT NULL,
    виробник VARCHAR(255) NOT NULL,
    ОС ENUM('iOS', 'Android') NOT NULL
);

-- Створення таблиці застосунків
CREATE TABLE застосунки (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    назва VARCHAR(255) NOT NULL,
    ОС ENUM('iOS', 'Android') NOT NULL
);

-- Створення таблиці інструкцій
CREATE TABLE інструкції (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    заголовок VARCHAR(255) NOT NULL,
    зміст TEXT NOT NULL,
    категорія VARCHAR(255),
    ОС ENUM('iOS', 'Android') NOT NULL
);

-- Створення таблиці зворотного зв’язку
CREATE TABLE відгуки (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    інструкція_id INTEGER NOT NULL,
    коментарі TEXT,
    рейтинг INTEGER CHECK (рейтинг BETWEEN 1 AND 5),
    дата TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (інструкція_id) REFERENCES інструкції(id) ON DELETE CASCADE
);

-- Створення таблиці ярликів (шорткатів)
CREATE TABLE ярлики (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    інструкція_id INTEGER NOT NULL,
    мітка VARCHAR(255) NOT NULL,
    створено TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (інструкція_id) REFERENCES інструкції(id) ON DELETE CASCADE
);

-- Створення таблиці підтримки (контакти підтримки)
CREATE TABLE контакти_підтримки (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    платформа VARCHAR(255) NOT NULL,
    посилання VARCHAR(255) NOT NULL
);

-- Створення зв’язку між пристроями та інструкціями
CREATE TABLE пристрій_інструкція (
    пристрій_id INTEGER NOT NULL,
    інструкція_id INTEGER NOT NULL,
    PRIMARY KEY (пристрій_id, інструкція_id),
    FOREIGN KEY (пристрій_id) REFERENCES пристрої(id) ON DELETE CASCADE,
    FOREIGN KEY (інструкція_id) REFERENCES інструкції(id) ON DELETE CASCADE
);

-- Створення зв’язку між застосунками та інструкціями
CREATE TABLE застосунок_інструкція (
    застосунок_id INTEGER NOT NULL,
    інструкція_id INTEGER NOT NULL,
    PRIMARY KEY (застосунок_id, інструкція_id),
    FOREIGN KEY (застосунок_id) REFERENCES застосунки(id) ON DELETE CASCADE,
    FOREIGN KEY (інструкція_id) REFERENCES інструкції(id) ON DELETE CASCADE
);