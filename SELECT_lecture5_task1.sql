SELECT genre_name, COUNT(band_name) FROM genre g
JOIN band_genre bg ON g.id = bg.genre_id 
JOIN band b ON bg.band_id = b.id 
GROUP BY g.genre_name;

SELECT COUNT(track_name) FROM album a
JOIN track t ON a.id = t.album_id
WHERE year_of_realise BETWEEN 2019 AND 2020;

SELECT album_name, AVG(duration) FROM album a
JOIN track t ON a.id = t.album_id
GROUP BY a.album_name;

SELECT band_name FROM band b
JOIN band_album ba ON b.id = ba.band_id
JOIN album a ON ba.album_id = a.id
WHERE year_of_realise NOT IN (2020);

SELECT DISTINCT collection_name FROM collection c
JOIN tracks_in_collection tic ON c.id = tic.collection_id
JOIN track t ON tic.track_id = t.id
JOIN album a ON t.album_id = a.id
JOIN band_album ba ON a.id = ba.album_id
JOIN band b ON ba.band_id = b.id
WHERE band_name LIKE 'Гражданская оборона';

SELECT album_name FROM album a
JOIN band_album ba ON a.id = ba.album_id
JOIN band b ON ba.band_id = b.id
JOIN band_genre bg ON b.id = bg.band_id
GROUP BY album_name
HAVING COUNT(genre_id) > 1;

SELECT track_name FROM track t
LEFT JOIN tracks_in_collection tic ON t.id = tic.track_id
WHERE tic.track_id IS NULL;

SELECT band_name FROM band b
JOIN band_album ba ON b.id = ba.band_id
JOIN album a ON ba.album_id = a.id
JOIN track t ON a.id = t.album_id
WHERE duration = (SELECT MIN(duration) FROM track);

SELECT album_name FROM album a
JOIN track t ON a.id = t.album_id
GROUP BY album_name
HAVING count(track_name) = (SELECT count(track_name) FROM album a
	JOIN track t ON a.id = t.album_id
	GROUP BY album_name 
	ORDER BY count(track_name) ASC
	LIMIT 1)
	