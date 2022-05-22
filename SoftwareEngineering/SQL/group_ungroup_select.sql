-- create a table
CREATE TABLE test_groups (
  name VARCHAR(40) NOT NULL,
  test_value INTEGER NOT NULL,
  unique(name));
  
CREATE TABLE test_cases (
    id INTEGER NOT NULL,
    group_name VARCHAR(40) NOT NULL,
    status VARCHAR(5) NOT NULL,
    unique(id));
    
-- insert some values
INSERT INTO test_groups 
VALUES ('performance', 15),
('corner case', 10),
('numerical stability', 20),
('memory usage', 10);

INSERT INTO test_cases 
VALUES (13, 'memory usage', 'OK'),
 (14, 'numerical stability', 'OK'),
 (15, 'memory usage', 'ERROR'),
 (16, 'numerical stability', 'OK'),
 (17, 'numerical stability', 'OK'),
 (18, 'performance', 'ERROR'),
 (19, 'performance', 'ERROR'),
 (20, 'memory usage', 'OK'),
 (21, 'numerical stability', 'OK');

-- fetch some values
SELECT name as group_name,
COUNT(id) as all_test_cases,
SUM(case when status = 'OK' then 1 else 0 end),
sum(case when status = 'OK' then test_value else 0 end) as total_value
FROM test_groups LEFT JOIN test_cases
ON test_groups.name = test_cases.group_name
group by name
order by total_value desc


