# Problem 2 : Number of Unique Subjects Taught By Each Teacher ( https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)

import pandas as pd

# solution 1: using a for loop
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    dict = {}
    for i in range(len(teacher)):
        t_id = teacher['teacher_id'][i]
        s_id = teacher['subject_id'][i]
        if t_id not in dict:
            dict[t_id] = set()
        dict[t_id].add(s_id)

    result = []
    for key,value in dict.items():
        result.append([key, len(value)])

    return pd.DataFrame(result, columns=['teacher_id', 'cnt'])

# solution 2: using pandas built-in functions
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.groupby('teacher_id').nunique().reset_index()
    return teacher[['teacher_id', 'subject_id']].rename(columns={'subject_id':'cnt'})

