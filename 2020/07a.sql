create table bag (outside text, inside text);
\copy bag from 7.csv
with recursive b as (select outside from bag where inside = 'shiny gold' union select bag.outside from bag join b on bag.inside = b.outside) select * from b;
