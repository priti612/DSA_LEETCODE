# Write your MySQL query statement below
select p.firstName,
p.lastName,a.city,a.state from Person p
 Left join Address a
on p.PersonId=a.PersonId

