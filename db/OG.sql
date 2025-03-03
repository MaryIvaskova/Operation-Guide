-- Створення таблиці пристроїв
CREATE TABLE devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model VARCHAR(255) NOT NULL,
    manufacturer VARCHAR(255) NOT NULL,
    os ENUM('iOS', 'Android') NOT NULL
);

-- Створення таблиці застосунків
CREATE TABLE apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    os ENUM('iOS', 'Android') NOT NULL
);

-- Створення таблиці інструкцій
CREATE TABLE instructions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    category VARCHAR(255),
    os ENUM('iOS', 'Android') NOT NULL
);

-- Створення таблиці зворотного зв'язку
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    instruction_id INTEGER NOT NULL,
    comments TEXT,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instruction_id) REFERENCES instructions(id) ON DELETE CASCADE
);

-- Створення таблиці ярликів (шорткатів)
CREATE TABLE shortcuts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    instruction_id INTEGER NOT NULL,
    label VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instruction_id) REFERENCES instructions(id) ON DELETE CASCADE
);

-- Створення таблиці підтримки (контакти підтримки)
CREATE TABLE support_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform VARCHAR(255) NOT NULL,
    link VARCHAR(255) NOT NULL
);

-- Створення зв'язку між пристроями та інструкціями
CREATE TABLE device_instruction (
    device_id INTEGER NOT NULL,
    instruction_id INTEGER NOT NULL,
    PRIMARY KEY (device_id, instruction_id),
    FOREIGN KEY (device_id) REFERENCES devices(id) ON DELETE CASCADE,
    FOREIGN KEY (instruction_id) REFERENCES instructions(id) ON DELETE CASCADE
);

-- Створення зв'язку між застосунками та інструкціями
CREATE TABLE app_instruction (
    app_id INTEGER NOT NULL,
    instruction_id INTEGER NOT NULL,
    PRIMARY KEY (app_id, instruction_id),
    FOREIGN KEY (app_id) REFERENCES apps(id) ON DELETE CASCADE,
    FOREIGN KEY (instruction_id) REFERENCES instructions(id) ON DELETE CASCADE
);
