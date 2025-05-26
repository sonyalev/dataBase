INSERT INTO air_quality (
    weather_id,
    air_quality_carbon_monoxide,
    air_quality_ozone,
    air_quality_nitrogen_dioxide,
    air_quality_sulphur_dioxide,
    air_quality_pm2_5,
    air_quality_pm10,
    air_quality_us_epa_index,
    air_quality_gb_defra_index
)
SELECT
    id,
    air_quality_carbon_monoxide,
    air_quality_ozone,
    air_quality_nitrogen_dioxide,
    air_quality_sulphur_dioxide,
    air_quality_pm2_5,
    air_quality_pm10,
    air_quality_us_epa_index,
    air_quality_gb_defra_index
FROM weather;