create table c (c1 int, c2 int);

create unique index ci on c (c1, c2);
alter table c add constraint cpk primary key using index ci; 

CREATE TABLE d (d1 INT, d2 INT);
ALTER TABLE d ADD CONSTRAINT dpk PRIMARY KEY (d1,d2);

SELECT *
FROM pg_indexes
WHERE tablename = 'c';

SELECT *
FROM pg_indexes
WHERE tablename = 'd';

SELECT *
FROM pg_indexes
WHERE tablename = 'categoria';