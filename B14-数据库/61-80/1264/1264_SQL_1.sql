Create table If Not Exists Friendship
(
    user1_id int,
    user2_id int
);
Create table If Not Exists Likes
(
    user_id int,
    page_id int
);

# STEP 1
SELECT user1_id AS friend
FROM Friendship
WHERE user2_id = 1;

SELECT user2_id AS friend
FROM Friendship
WHERE user1_id = 1;

# STEP 2
SELECT friend
FROM (SELECT user1_id AS friend
      FROM Friendship
      WHERE user2_id = 1
      UNION
      SELECT user2_id AS friend
      FROM Friendship
      WHERE user1_id = 1) AS Friend;

# STEP 3
SELECT page_id
FROM Likes
WHERE user_id = 1;


# STEP 4
SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE user_id IN (SELECT user1_id AS friend
                  FROM Friendship
                  WHERE user2_id = 1
                  UNION
                  SELECT user2_id AS friend
                  FROM Friendship
                  WHERE user1_id = 1)
  AND page_id NOT IN (SELECT page_id
                      FROM Likes
                      WHERE user_id = 1);
