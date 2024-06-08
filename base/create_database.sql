CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS veiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    categoria TEXT CHECK (categoria IN ('Pequeno', 'Médio', 'Grande', 'SUV', 'Luxo')) NOT NULL,
    tipo TEXT CHECK (tipo IN ('Carro', 'Moto')) NOT NULL,
    valor_diaria REAL NOT NULL,
    capacidade INTEGER NOT NULL,
    data_ultima_revisao DATE NOT NULL,
    data_proxima_revisao DATE NOT NULL,
    data_ultima_inspecao DATE NOT NULL,
    disponivel BOOLEAN NOT NULL CHECK (disponivel IN (0, 1)),
    transmissao TEXT CHECK (transmissao IN ('Manual', 'Automatico')) NOT NULL,
    categoria_quantidade TEXT CHECK (categoria_quantidade IN ('1-4', '5-6', '7 ou mais')) NOT NULL
);

CREATE TABLE IF NOT EXISTS reservas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    veiculo_id INTEGER NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    forma_pagamento TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
);


INSERT INTO usuarios (nome, email, senha) VALUES 
('John Doe', 'john@example.com', 'password_hash1'),
('Jane Smith', 'jane@example.com', 'password_hash2'),
('Alice Johnson', 'alice@example.com', 'password_hash3'),
('Bob Brown', 'bob@example.com', 'password_hash4'),
('Charlie Davis', 'charlie@example.com', 'password_hash5'),
('Diana Evans', 'diana@example.com', 'password_hash6'),
('Ethan Frank', 'ethan@example.com', 'password_hash7'),
('Fiona Green', 'fiona@example.com', 'password_hash8'),
('George Hill', 'george@example.com', 'password_hash9'),
('Hannah King', 'hannah@example.com', 'password_hash10'),
('Ivan Lee', 'ivan@example.com', 'password_hash11'),
('Julia Martin', 'julia@example.com', 'password_hash12'),
('Kevin Nelson', 'kevin@example.com', 'password_hash13'),
('Laura Owen', 'laura@example.com', 'password_hash14'),
('Michael Parker', 'michael@example.com', 'password_hash15'),
('Nancy Quinn', 'nancy@example.com', 'password_hash16'),
('Oscar Reed', 'oscar@example.com', 'password_hash17'),
('Paula Scott', 'paula@example.com', 'password_hash18'),
('Quentin Turner', 'quentin@example.com', 'password_hash19'),
('Rachel Underwood', 'rachel@example.com', 'password_hash20');


INSERT INTO veiculos (marca, modelo, categoria, tipo, valor_diaria, capacidade, data_ultima_revisao, data_proxima_revisao, data_ultima_inspecao, disponivel, transmissao, categoria_quantidade) VALUES 
-- Carros
('Toyota', 'Corolla', 'Médio', 'Carro', 30.0, 5, '2023-11-15', '2024-11-15', '2023-09-15', 1, 'Automatico', '5-6'),
('Honda', 'Civic', 'Médio', 'Carro', 35.0, 5, '2023-11-05', '2024-11-05', '2023-09-05', 1, 'Manual', '5-6'),
('Ford', 'Focus', 'Pequeno', 'Carro', 28.0, 5, '2023-10-15', '2024-10-15', '2023-08-15', 1, 'Automatico', '5-6'),
('Chevrolet', 'Malibu', 'Médio', 'Carro', 33.0, 5, '2023-09-15', '2024-09-15', '2023-07-15', 1, 'Manual', '5-6'),
('Nissan', 'Altima', 'Médio', 'Carro', 29.0, 5, '2023-08-15', '2024-08-15', '2023-06-15', 1, 'Automatico', '5-6'),
('Hyundai', 'Elantra', 'Médio', 'Carro', 32.0, 5, '2023-07-15', '2024-07-15', '2023-05-15', 1, 'Manual', '5-6'),
('Kia', 'Optima', 'Médio', 'Carro', 31.0, 5, '2023-06-15', '2024-06-15', '2023-04-15', 1, 'Automatico', '5-6'),
('Volkswagen', 'Passat', 'Médio', 'Carro', 34.0, 5, '2023-05-15', '2024-05-15', '2023-03-15', 1, 'Manual', '5-6'),
('Subaru', 'Impreza', 'Pequeno', 'Carro', 27.0, 5, '2023-04-15', '2024-04-15', '2023-02-15', 1, 'Automatico', '5-6'),
('Mazda', 'Mazda3', 'Pequeno', 'Carro', 30.0, 5, '2023-03-15', '2024-03-15', '2023-01-15', 1, 'Manual', '5-6'),
('BMW', '3 Series', 'Luxo', 'Carro', 45.0, 5, '2023-02-15', '2024-02-15', '2022-12-15', 1, 'Automatico', '5-6'),
('Mercedes-Benz', 'C-Class', 'Luxo', 'Carro', 50.0, 5, '2023-01-15', '2024-01-15', '2022-11-15', 1, 'Manual', '5-6'),
('Audi', 'A4', 'Luxo', 'Carro', 48.0, 2, '2022-12-15', '2023-12-15', '2022-10-15', 1, 'Automatico', '1-4'),
('Lexus', 'ES', 'Luxo', 'Carro', 47.0, 2, '2022-11-15', '2023-11-15', '2022-09-15', 1, 'Manual', '1-4'),
('Acura', 'TLX', 'Luxo', 'Carro', 46.0, 2, '2022-10-15', '2023-10-15', '2022-08-15', 1, 'Automatico', '1-4'),
('Infiniti', 'Q50', 'Luxo', 'Carro', 49.0, 3, '2022-09-15', '2023-09-15', '2022-07-15', 1, 'Manual', '1-4'),
('Tesla', 'Model 3', 'Luxo', 'Carro', 55.0, 3, '2022-08-15', '2023-08-15', '2022-06-15', 1, 'Automatico', '1-4'),
('Volvo', 'S60', 'Luxo', 'Carro', 51.0, 3, '2022-07-15', '2023-07-15', '2022-05-15', 1, 'Manual', '1-4'),
('Jaguar', 'XE', 'Luxo', 'Carro', 52.0, 5, '2022-06-15', '2023-06-15', '2022-04-15', 1, 'Automatico', '5-6'),
('Cadillac', 'CT5', 'Luxo', 'Carro', 53.0, 5, '2022-05-15', '2023-05-15', '2022-03-15', 1, 'Manual', '5-6'),

-- Motos
('Yamaha', 'MT-07', 'Médio', 'Moto', 25.0, 2, '2023-06-10', '2024-06-10', '2023-04-10', 1, 'Manual', '1-4'),
('Honda', 'CBR500R', 'Médio', 'Moto', 27.0, 2, '2023-07-11', '2024-07-11', '2023-05-11', 1, 'Manual', '1-4'),
('Kawasaki', 'Ninja 400', 'Pequeno', 'Moto', 20.0, 2, '2023-08-12', '2024-08-12', '2023-06-12', 1, 'Manual', '1-4'),
('Suzuki', 'GSX250R', 'Pequeno', 'Moto', 22.0, 2, '2023-09-13', '2024-09-13', '2023-07-13', 1, 'Manual', '1-4'),
('Ducati', 'Monster 797', 'Médio', 'Moto', 30.0, 2, '2023-10-14', '2024-10-14', '2023-08-14', 1, 'Manual', '1-4'),
('BMW', 'G310R', 'Pequeno', 'Moto', 23.0, 2, '2023-11-15', '2024-11-15', '2023-09-15', 1, 'Manual', '1-4'),
('KTM', 'Duke 390', 'Pequeno', 'Moto', 24.0, 2, '2023-12-16', '2024-12-16', '2023-10-16', 1, 'Manual', '1-4'),
('Harley-Davidson', 'Iron 883', 'Grande', 'Moto', 40.0, 2, '2024-01-17', '2025-01-17', '2023-11-17', 1, 'Manual', '1-4'),
('Triumph', 'Street Triple', 'Médio', 'Moto', 35.0, 2, '2024-02-18', '2025-02-18', '2023-12-18', 1, 'Manual', '1-4'),
('Aprilia', 'RS 660', 'Médio', 'Moto', 32.0, 2, '2024-03-19', '2025-03-19', '2024-01-19', 1, 'Manual', '1-4');


INSERT INTO reservas (usuario_id, veiculo_id, data_inicio, data_fim, forma_pagamento) VALUES 
(1, 1, '2024-06-04', '2024-06-09', 'Cartão de Crédito'),
(2, 2, '2024-06-10', '2024-06-15', 'Cartão de Débito'),
(3, 3, '2024-06-16', '2024-06-21', 'PayPal'),
(4, 4, '2024-06-22', '2024-06-27', 'Cartão de Crédito'),
(5, 5, '2024-06-28', '2024-07-03', 'Cartão de Débito'),
(6, 6, '2024-07-04', '2024-07-09', 'PayPal'),
(7, 7, '2024-07-10', '2024-07-15', 'Cartão de Crédito'),
(8, 8, '2024-07-16', '2024-07-21', 'Cartão de Débito'),
(9, 9, '2024-07-22', '2024-07-27', 'PayPal'),
(10, 10, '2024-07-28', '2024-08-02', 'Cartão de Crédito'),
(11, 11, '2024-08-03', '2024-08-08', 'Cartão de Débito'),
(12, 12, '2024-08-09', '2024-08-14', 'PayPal'),
(13, 13, '2024-08-15', '2024-08-20', 'Cartão de Crédito'),
(14, 14, '2024-08-21', '2024-08-26', 'Cartão de Débito'),
(15, 15, '2024-08-27', '2024-09-01', 'PayPal'),
(16, 16, '2024-09-02', '2024-09-07', 'Cartão de Crédito'),
(17, 17, '2024-09-08', '2024-09-13', 'Cartão de Débito'),
(18, 18, '2024-09-14', '2024-09-19', 'PayPal'),
(19, 19, '2024-09-20', '2024-09-25', 'Cartão de Crédito'),
(20, 20, '2024-09-26', '2024-10-01', 'Cartão de Débito');


INSERT INTO veiculos (marca, modelo, categoria, tipo, valor_diaria, capacidade, data_ultima_revisao, data_proxima_revisao, data_ultima_inspecao, disponivel, transmissao, categoria_quantidade) VALUES 

-- Veículos adicionais com outras categorias_quantidade
('Ford', 'Explorer', 'Grande', 'Carro', 60.0, 7, '2023-01-01', '2024-01-01', '2023-12-01', 1, 'Automatico', '7 ou mais'),
('Chevrolet', 'Suburban', 'Grande', 'Carro', 70.0, 8, '2023-02-01', '2024-02-01', '2023-11-01', 1, 'Automatico', '7 ou mais'),
('Toyota', 'Sienna', 'Grande', 'Carro', 65.0, 8, '2023-03-01', '2024-03-01', '2023-10-01', 1, 'Automatico', '7 ou mais'),
('Honda', 'Odyssey', 'Grande', 'Carro', 63.0, 5, '2023-04-01', '2024-04-01', '2023-09-01', 1, 'Automatico', '5-6'),
('Chrysler', 'Pacifica', 'Grande', 'Carro', 68.0, 8, '2023-05-01', '2024-05-01', '2023-08-01', 1, 'Automatico', '7 ou mais'),
('Mercedes-Benz', 'Sprinter', 'Luxo', 'Carro', 80.0, 12, '2023-06-01', '2024-06-01', '2023-07-01', 1, 'Automatico', '7 ou mais');
