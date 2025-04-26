CREATE TABLE air_quality (
    id SERIAL PRIMARY KEY,
    air_quality_carbon_monoxide FLOAT,
    air_quality_ozone FLOAT,
    air_quality_nitrogen_dioxide FLOAT,
    air_quality_sulphur_dioxide FLOAT,
    air_quality_pm2_5 FLOAT,
    air_quality_pm10 FLOAT,
    air_quality_us_epa_index INT,
    air_quality_gb_defra_index INT
);