CREATE SCHEMA IF NOT EXISTS EngineerInspection;

USE EngineerInspection;

CREATE TABLE engineers (
    engineer_id INT PRIMARY KEY,
    available_day DATE NOT NULL,
    slot_09_00 BOOLEAN,
    slot_09_30 BOOLEAN,
    slot_10_00 BOOLEAN,
    slot_10_30 BOOLEAN,
    slot_11_00 BOOLEAN,
    slot_11_30 BOOLEAN,
    slot_12_00 BOOLEAN,
    slot_12_30 BOOLEAN,
    slot_13_00 BOOLEAN,
    slot_13_30 BOOLEAN,
    slot_14_00 BOOLEAN,
    slot_14_30 BOOLEAN,
    slot_15_00 BOOLEAN,
    slot_15_30 BOOLEAN,
    slot_16_00 BOOLEAN,
    slot_16_30 BOOLEAN,
    updated_timestamp DATETIME
);

CREATE TABLE inspections (
    inspection_id INT AUTO_INCREMENT PRIMARY KEY,
    engineer_id INT NOT NULL,
    inspection_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    FOREIGN KEY (engineer_id) REFERENCES engineers(engineer_id) ON DELETE CASCADE
);
