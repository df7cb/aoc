begin;
    create table day01 (l int, r int);
    \copy day01 from program 'column -t -o "	" 01.txt'
    select sum(l.l) from day01 l join day01 r on l.l = r.r;
