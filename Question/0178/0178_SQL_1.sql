SELECT `Score`,
       DENSE_RANK() over (ORDER BY `Score` DESC) AS `rANK`
FROM `Scores`;
