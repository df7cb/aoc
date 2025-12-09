drop schema if exists day09 cascade;

begin;
create schema day09;
set search_path = day09, public;

create table day09 (x int, y int);
\copy day09 from '09.txt' delimiter ','

create table floor (geom geometry);
insert into floor
select 'POLYGON((' || string_agg(x::text || ' ' || y::text, ',') || '))' from
(select * from day09 union all (select * from day09 limit 1));

create table floor2 (geom geometry);
insert into floor2 select st_buffer(geom, 0.5, 'join=mitre') from floor;

create table tiles (geom geometry);
insert into tiles
select st_buffer(format('POLYGON((%s %s, %s %s, %s %s, %s %s, %s %s))', a.x, a.y, a.x, b.y, b.x, b.y, b.x, a.y, a.x, a.y)::geometry, 0.5, 'join=mitre') geom
from day09 a, day09 b
where (a.x, a.y) < (b.x, b.y);

select max(st_area(tiles.geom)) from tiles, floor2 where st_contains(floor2.geom, tiles.geom);

create table best_tile as
select st_area(tiles.geom), tiles.geom from tiles, floor2 where st_contains(floor2.geom, tiles.geom) order by 1 desc limit 1;

select st_area from best_tile;

commit;
