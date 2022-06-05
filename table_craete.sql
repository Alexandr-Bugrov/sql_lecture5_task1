CREATE TABLE IF NOT EXISTS genre (
	id SERIAL PRIMARY KEY,
	genre_name VARCHAR(40) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS band (
	id SERIAL PRIMARY KEY,
	band_name VARCHAR(30) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS album (
	id SERIAL PRIMARY KEY,
	album_name VARCHAR(30) NOT NULL UNIQUE,
	year_of_realise INTEGER NOT NULL
);


CREATE TABLE IF NOT EXISTS track(
	id SERIAL PRIMARY KEY,
	album_id INTEGER REFERENCES album(id),
	name VARCHAR(30) NOT NULL,
	duration INTEGER NOT NULL
);


CREATE TABLE IF NOT EXISTS collection(
	id SERIAL PRIMARY KEY,
	collection_name VARCHAR(30) NOT NULL UNIQUE,
	year_of_realise INTEGER NOT NULL
);


CREATE TABLE IF NOT EXISTS band_genre(
	genre_id INTEGER REFERENCES genre(id),
	band_id INTEGER REFERENCES band(id),
	CONSTRAINT pk_band_genre PRIMARY KEY(genre, band)
);


CREATE TABLE IF NOT EXISTS band_album(
	band_id INTEGER REFERENCES band(id),
	album_id INTEGER REFERENCES album(id),
	CONSTRAINT pk_band_album PRIMARY KEY(band, album)
);


CREATE TABLE IF NOT EXISTS tracks_in_collection(
	track_id INTEGER REFERENCES track(id),
	collection_id INTEGER REFERENCES collection(id),
	CONSTRAINT pk_tracks_in_collection PRIMARY KEY(track, collection)
);


