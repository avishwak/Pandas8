# Problem 1: Find Total Time Spent By Each Employee ( https://leetcode.com/problems/find-total-time-spent-by-each-employee/ )

import pandas as pd

# long-version solution using a dictionary 
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    dict = {}

    for i in range(len(employees)):
        e_id = employees['emp_id'][i]
        day = employees['event_day'][i]
        in_time = employees['in_time'][i]
        out_time = employees['out_time'][i]
        if (day, e_id) in dict:
            dict[(day, e_id)] += out_time - in_time
        else:
            dict[(day, e_id)] = out_time - in_time

    result = []
    for key, value in dict.items():
        result.append([key[0], key[1], value])
    
    return pd.DataFrame(result, columns=['day', 'emp_id', 'total_time'])


# using groupby and sum
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees.rename(columns={'event_day':'day'}, inplace=True)
    return employees.groupby(['day', 'emp_id'])['total_time'].sum().reset_index()

""" 
# Note:
- when we do groupby, we get a DataFrameGroupBy object
- if we use two values in the groupby then it will return a DataFrameGroupBy object with a multi-index, so we need reset index

- transform returns a series and it will not work here because it returns one column and multiple entry for each group, 
and then mapping it to the original DataFrame will not work as expected. (transform is like partition by in SQL, it returns the same number of rows as the original DataFrame)
0    173
1    173
2     41
3     30
4     27

- employees.rename(columns={'event_day':'day'}, inplace=True) if we do not mention columns then it will return error 
because it would not know if it is a column or index. we can also use axis=1 to specify that we are renaming columns.
"""

