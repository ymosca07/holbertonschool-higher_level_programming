-- Description
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.title = 'Comedy'
ORDER BY tv_shows.title ASC;
