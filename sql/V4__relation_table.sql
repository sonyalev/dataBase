--зовнішній ключ до таблиці weather
ALTER TABLE weather
ADD COLUMN air_quality_id INT;

--зовнішній ключ для зв'язку з таблицею air_quality
ALTER TABLE weather
ADD CONSTRAINT fk_air_quality
FOREIGN KEY (air_quality_id) REFERENCES air_quality(id);