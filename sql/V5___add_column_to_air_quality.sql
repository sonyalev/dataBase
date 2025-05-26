ALTER TABLE air_quality
ADD COLUMN going_outside BOOLEAN;


UPDATE air_quality
SET going_outside = CASE
    WHEN air_quality_carbon_monoxide > 1000
      OR air_quality_ozone > 150
    THEN FALSE
    ELSE TRUE
END;