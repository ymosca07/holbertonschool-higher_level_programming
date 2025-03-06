-- Description
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS 'Dexter'
ORDER BY tv_genres.name ASC;
