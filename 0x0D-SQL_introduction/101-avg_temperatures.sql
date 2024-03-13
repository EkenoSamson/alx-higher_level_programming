-- display average of temperature by city

SELECT city, AVG(`value`) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY svg_temp DESC;
