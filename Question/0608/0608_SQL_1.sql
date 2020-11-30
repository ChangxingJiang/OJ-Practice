Create table If Not Exists tree
(
    id int,
    p_id int
);


# STEP 1
SELECT id,
       'Root' AS Type
FROM tree
WHERE p_id IS NULL;

# STEP 2
SELECT id,
       'Inner' AS Type
FROM tree
WHERE p_id IS NOT NULL
  AND id IN (SELECT DISTINCT p_id FROM tree);

# STEP 3
SELECT id,
       'Leaf' AS Type
FROM tree
WHERE p_id IS NOT NULL
  AND id NOT IN (SELECT DISTINCT IFNULL(p_id, -1) FROM tree);

# STEP 4
SELECT id, Type
FROM (SELECT id, 'Root' AS Type
      FROM tree
      WHERE p_id IS NULL) AS N
UNION
(SELECT id, 'Inner' AS Type
 FROM tree
 WHERE p_id IS NOT NULL
   AND id IN (SELECT DISTINCT p_id FROM tree))
UNION
(SELECT id, 'Leaf' AS Type
 FROM tree
 WHERE p_id IS NOT NULL
   AND id NOT IN (SELECT DISTINCT IFNULL(p_id, -1) FROM tree));
