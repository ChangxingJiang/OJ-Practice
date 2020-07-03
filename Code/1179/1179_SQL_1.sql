select id,
       max(case when month = 'Jan' then revenue end) Jan_Revenue,
       max(case when month = 'Feb' then revenue end) Feb_Revenue,
       max(case when month = 'Mar' then revenue end) Mar_Revenue,
       max(case when month = 'Apr' then revenue end) Apr_Revenue,
       max(case when month = 'May' then revenue end) May_Revenue,
       max(case when month = 'Jun' then revenue end) Jun_Revenue,
       max(case when month = 'Jul' then revenue end) Jul_Revenue,
       max(case when month = 'Aug' then revenue end) Aug_Revenue,
       max(case when month = 'Sep' then revenue end) Sep_Revenue,
       max(case when month = 'Oct' then revenue end) Oct_Revenue,
       max(case when month = 'Nov' then revenue end) Nov_Revenue,
       max(case when month = 'Dec' then revenue end) Dec_Revenue
from Department
group by id;