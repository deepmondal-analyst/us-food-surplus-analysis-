-- USE food_surplus_project;
SELECT * from sector_metrics;
-- SELECT sector, value FROM sector_metrics WHERE metric = "surplus_food_generated"
-- ORDER BY value DESC;
SELECT * FROM annual_trend;
SELECT s.year, a.value_million_US_short_tons, s.value, s.sector, s.metric, s.unit, 
ROUND (s.value/a.value_million_US_short_tons * 100,2) AS percent_of_total 
FROM annual_trend AS a
INNER JOIN sector_metrics AS s
ON a.year = s.year
WHERE s.metric = 'surplus_food_generated'
ORDER BY s.value DESC
;