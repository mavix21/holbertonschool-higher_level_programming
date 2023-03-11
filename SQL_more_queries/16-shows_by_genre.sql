-- Lists all shows in the database `hbtn_0d_tvshows`
SELECT
    tv_shows.title,
    tv_genres.name
-- Another way:
-- FROM tv_genres
-- INNER JOIN tv_show_genres
-- ON tv_genres.id = tv_show_genres.genre_id
-- RIGHT OUTER JOIN tv_shows
-- ON tv_show_genres.show_id = tv_shows.id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name
