-- Display the max temperature of each state, ordered by state.
SELECT `state`, MAX(`value`) AS `MAX_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
