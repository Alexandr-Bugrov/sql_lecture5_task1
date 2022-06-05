import sqlalchemy as sql

engine = sql.create_engine('postgresql://postgres:19851234@localhost:5432/lecture4')
connection = engine.connect()


def band():
    connection.execute("""INSERT INTO band(band_name)
        VALUES('Ария');
        VALUES('Rammstein');  
        VALUES('AC/DC'); 
        VALUES('Гражданская оборона');
        VALUES('Mozart');
        VALUES('Manowar');
        VALUES('Майкл Джексон');
        VALUES('Любэ');
    """)


def genre():
    connection.execute("""INSERT INTO genre(genre_name)
        VALUES('Pop');
        VALUES('Industrial metal');
        VALUES('Classical');
        VALUES('Heavy metal');
        VALUES('Russian rock');
    """)


def album():
    connection.execute("""INSERT INTO album(album_name, year_of_realise)
        VALUES('Number Ones', 2003);
        VALUES('Super album', 2018);
        VALUES('Плохой альбом', 2022);
        VALUES('Замечательный альбом', 2021);
        VALUES('Rosenrot', 2015);
        VALUES('Здорово и вечно', 1989);
        VALUES('Battle Hymns', 1980);
        VALUES('Fly On The Wall', 1985);
    """)


def track():
    connection.execute("""INSERT INTO track(album_id, track_name, duration)
        VALUES(1 'You Rock My World', 265);
        VALUES(1 'Triller', 311, 3);
        VALUES(2, 'Длинный трек', 500);
        VALUES(2, 'Короткий трек', 100);
        VALUES(3, 'Плохой трек', 150);
        VALUES(3, 'Ужасный трек', 199);
        VALUES(4, 'Сносный трек', 325);
        VALUES(4, 'Нормально', 189);
        VALUES(5, 'Rosenrot', 345);
        VALUES(5, 'Benzin', 445);
        VALUES(6, 'Моя оборона', 240);
        VALUES(6, 'Здорово и вечно', 445);
        VALUES(7, 'Manowar', 450);
        VALUES(7, 'Battle Hymn', 635);
        VALUES(8, 'Danger', 636);
    """)


def collection():
    connection.execute("""INSERT INTO collection(collection_name, year_of_realise)
        VALUES('Зарубежный рок', 2014);
        VALUES('Классическая музыка', 2013);
        VALUES('Pop music', 2020);
        VALUES('Отечественный исполнитель', 2015);
        VALUES('Лучшее за 20 век', 2000);
        VALUES('Худшее за 20 век', 2018);
        VALUES('Сборик 20.22 год', 2022);
        VALUES('Русский рок', 2022);
    """)


def tracks_in_collection():
    connection.execute("""INSERT INTO tracks_in_collection(track_id, collection_id)
        VALUES(15, 1);
        VALUES(14, 1);
        VALUES(13, 1);
        VALUES(3, 2);
        VALUES(4, 2);
        VALUES(7, 3);
        VALUES(6, 3);
        VALUES(5, 6);
        VALUES(5, 7);
        VALUES(9, 4);
        VALUES(10, 4);
        VALUES(5, 5);
        VALUES(6, 6);
        VALUES(7, 7);
        VALUES(6, 7);
        VALUES(12, 8);
        VALUES(13, 8);
    """)


def band_album():
    connection.execute("""INSERT INTO band_album(band_id, album_id)
        VALUES(1, 3);
        VALUES(2, 5);
        VALUES(3, 8);
        VALUES(4, 6);
        VALUES(5, 2);
        VALUES(6, 7);
        VALUES(7, 1);
        VALUES(8, 4);
        VALUES(4, 2)
    """)


def band_genre():
    connection.execute("""INSERT INTO band_genre(band_id, genre_id)
        VALUES(1, 5);
        VALUES(2, 2);
        VALUES(3, 4);
        VALUES(4, 5);
        VALUES(5, 3);
        VALUES(6, 4);
        VALUES(7, 1);
        VALUES(8, 1);
        VALUES(8, 5);
""")


if __name__ == '__main__':
    band()
    album()
    track()
    genre()
    collection()
    tracks_in_collection()
    band_album()
    band_genre()
