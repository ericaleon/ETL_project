select * from bees_data;
select * from pesticides;

select b.state, b.colony_change, sum(p.high_estimate)
from pesticides as p
right join bees_data as b
on p.state = b.state
GROUP BY p.state
ORDER BY b.colony_change ASC
LIMIT 5;

select b.state, b.colony_change, sum(p.high_estimate)
from pesticides as p
right join bees_data as b
on p.state = b.state
GROUP BY p.state
ORDER BY b.colony_change DESC
LIMIT 5;