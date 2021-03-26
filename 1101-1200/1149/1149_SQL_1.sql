Create table If Not Exists Views
(
    article_id int,
    author_id int,
    viewer_id int,
    view_date date
);

SELECT DISTINCT viewer_id AS id
FROM Views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1;
