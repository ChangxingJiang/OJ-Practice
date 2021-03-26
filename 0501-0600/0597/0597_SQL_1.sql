Create table If Not Exists FriendRequest
(
    sender_id int,
    send_to_id int,
    request_date date
);
Create table If Not Exists RequestAccepted
(
    requester_id int,
    accepter_id int,
    accept_date date
);

# STEP 1
SELECT DISTINCT sender_id, send_to_id
FROM FriendRequest;

# STEP 2
SELECT DISTINCT requester_id, accepter_id
FROM RequestAccepted;

# STEP 3
SELECT ROUND(IFNULL((SELECT COUNT(*)
                     FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) as A)
                        /
                    (SELECT COUNT(*)
                     FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) as B),
                    0),
             2) AS accept_rate;