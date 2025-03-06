-- Description
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
