drop table if exists part;

create table part (n serial primary key,
	px int, py int, pz int,
	vx int, vy int, vz int,
	ax int, ay int, az int
);

alter sequence part_n_seq restart with 0 minvalue 0;

\copy part (px,py,pz,vx,vy,vz,ax,ay,az) from 20.data (delimiter ',')

with recursive traj as (
	select 0::int as tick, * from part
	union
	select tick+1, n, px+vx+ax, py+vy+ay, pz+vz+az, vx+ax, vy+ay, vz+az, ax, ay, az
		from traj where tick < 100),
coll as (select tick, array_agg(n) as collided, px, py, pz from traj
	group by tick, px, py, pz having count(*) > 1),
exploded as (select unnest(collided) as p from coll)
select count(*) from part where n not in (select p from exploded);
