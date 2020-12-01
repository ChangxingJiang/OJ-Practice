Create Table If Not Exists Variables
(
    name varchar(3),
    value int
);
Create Table If Not Exists Expressions
(
    left_operand varchar(3),
    operator ENUM ('>', '<', '='),
    right_operand varchar(3)
);

SELECT left_operand,
       operator,
       right_operand,
       CASE
           WHEN operator = '>' THEN
               IF((SELECT value FROM Variables WHERE name = E.left_operand)
                      >
                  (SELECT value FROM Variables WHERE name = E.right_operand), 'true', 'false')
           WHEN operator = '=' THEN
               IF((SELECT value FROM Variables WHERE name = E.left_operand)
                      =
                  (SELECT value FROM Variables WHERE name = E.right_operand), 'true', 'false')
           WHEN operator = '<' THEN
               IF((SELECT value FROM Variables WHERE name = E.left_operand)
                      <
                  (SELECT value FROM Variables WHERE name = E.right_operand), 'true', 'false')
           END AS value
FROM Expressions AS E;