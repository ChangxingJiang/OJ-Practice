Create table If Not Exists Players
(
    player_id int,
    group_id int
);
Create table If Not Exists Matches
(
    match_id int,
    first_player int,
    second_player int,
    first_score int,
    second_score int
);
