# Write your MySQL query statement below
select e.name as Employee from Employee e
left join Employee g
on e.managerId=g.id
 where e.salary>g.salary