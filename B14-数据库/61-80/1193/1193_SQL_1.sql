create table if not exists Transactions
(
    id int,
    country varchar(4),
    state enum ('approved', 'declined'),
    amount int,
    trans_date date
);