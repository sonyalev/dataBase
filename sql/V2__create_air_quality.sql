CREATE TABLE air_quality (
    id SERIAL PRIMARY KEY,
    air_quality_Carbon_Monoxide FLOAT,
    air_quality_Ozone FLOAT,
    air_quality_Nitrogen_dioxide FLOAT,
    air_quality_Sulphur_dioxide FLOAT,
    air_quality_PM2_5 FLOAT,
    air_quality_PM10 FLOAT,
    air_quality_us_epa_index INT,
    air_quality_gb_defra_index INT
);