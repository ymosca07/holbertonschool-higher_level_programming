-- Description
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_genres ON tv_genres.id = tv_shows.show_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
