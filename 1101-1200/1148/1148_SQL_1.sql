Create table If Not Exists Views
(
    article_id int,
    author_id int,
    viewer_id int,
    view_date date
);

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;