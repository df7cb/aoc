begin;
    create table day01 (l int, r int);
    \copy day01 from program 'column -t -o "	" 01.txt'
    with l as (select row_number() over (order by l), l from day01),
         r as (select row_number() over (order by r), r from day01)
    select sum(abs(l - r)) from l join r on l.row_number = r.row_number;
