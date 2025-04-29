ALTER TABLE weather
ADD COLUMN air_quality_id INT;

UPDATE weather
SET air_quality_id = (
    SELECT air_quality.id
    FROM air_quality
    WHERE air_quality.id = weather.id
);

ALTER TABLE weather
ADD CONSTRAINT fk_air_quality
FOREIGN KEY (air_quality_id) REFERENCES air_quality(id);




