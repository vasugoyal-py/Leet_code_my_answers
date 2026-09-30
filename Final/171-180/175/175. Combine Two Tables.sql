-- Write your PostgreSQL query statement below
Select 
    p.firstname,
    p.lastname,
    a.city,
    a.state
FROM
    Person as p
    left JOIN
       Address as a
       ON
           p.personID = a.personID
   
    