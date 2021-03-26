Create table If Not Exists Movies
(
    movie_id int,
    title varchar(30)
);
Create table If Not Exists Users
(
    user_id int,
    name varchar(30)
);
Create table If Not Exists Movie_Rating
(
    movie_id int,
    user_id int,
    rating int,
    created_at date
);

SELECT U.name
FROM Movie_Rating AS T
         LEFT JOIN
     Users U on T.user_id = U.user_id
GROUP BY T.user_id
ORDER BY COUNT(*) DESC, U.name
LIMIT 1;

SELECT M.title
FROM Movie_Rating AS T
         LEFT JOIN
     Movies AS M ON T.movie_id = M.movie_id
where T.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY T.movie_id
ORDER BY AVG(rating) DESC, M.title
LIMIT 1;

(SELECT U.name AS results
       FROM Movie_Rating AS T
                LEFT JOIN
            Users U on T.user_id = U.user_id
       GROUP BY T.user_id
       ORDER BY COUNT(*) DESC, U.name
       LIMIT 1)
UNION
(SELECT M . title AS results
      FROM Movie_Rating AS T
      LEFT JOIN
      Movies AS M ON T . movie_id = M . movie_id
      where T . created_at BETWEEN '2020-02-01' AND '2020-02-29'
      GROUP BY T . movie_id
      ORDER BY AVG(rating) DESC, M.title
         LIMIT 1);


