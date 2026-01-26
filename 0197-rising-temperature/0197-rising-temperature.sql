# Write your MySQL query statement below
select w.id from Weather w
left join Weather w2
on w.recordDate-Interval 1 day=w2.recordDate
where w.temperature >w2.temperature 