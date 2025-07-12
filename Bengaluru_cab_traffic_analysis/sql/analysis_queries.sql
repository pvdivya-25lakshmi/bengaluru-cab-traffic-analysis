USE cab_analysis;

--- Busiest Pickup areas
SELECT pickup_area, COUNT(*) AS trips
FROM bengaluru_trips
GROUP BY pickup_area
ORDER BY trips DESC;

--- Average trip duration by weekday
SELECT weekday, ROUND(AVG(trip_duration_mins), 2) AS avg_duration
FROM bengaluru_trips
GROUP BY weekday
ORDER BY FIELD(weekday, 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday');


--- Ride type distribution
SELECT ride_type, COUNT(*) AS total_rides
FROM bengaluru_trips
GROUP BY ride_type;


--- Peak hour volume rides
SELECT hour, COUNT(*) AS ride_count
FROM bengaluru_trips
WHERE is_peak = 1
GROUP BY hour
ORDER BY hour;