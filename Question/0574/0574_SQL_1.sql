Create table If Not Exists Candidate
(
    id int,
    Name varchar(255)
);
Create table If Not Exists Vote
(
    id int,
    CandidateId int
);

# Part 1
SELECT CandidateId,
       COUNT(*) AS votes
FROM Vote
GROUP BY CandidateId;

# Part 2
SELECT MAX(votes)
FROM (SELECT COUNT(*) AS votes
      FROM Vote
      GROUP BY CandidateId) AS T1;

# Part 3
SELECT CandidateId
FROM (SELECT CandidateId,
             COUNT(*) AS votes
      FROM Vote
      GROUP BY CandidateId) AS T2
WHERE votes IN (SELECT MAX(votes)
                FROM (SELECT COUNT(*) AS votes
                      FROM Vote
                      GROUP BY CandidateId) AS T1);

# Part 4
SELECT Name
FROM Candidate
WHERE id IN
      (SELECT CandidateId
       FROM (SELECT CandidateId,
                    COUNT(*) AS votes
             FROM Vote
             GROUP BY CandidateId) AS T2
       WHERE votes IN (SELECT MAX(votes)
                       FROM (SELECT COUNT(*) AS votes
                             FROM Vote
                             GROUP BY CandidateId) AS T1));