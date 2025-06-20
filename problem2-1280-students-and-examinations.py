import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    df_student_exam_combo = students.merge(subjects, how='cross')
    df_exams = examinations.groupby(["student_id","subject_name"]).size().reset_index(name="attended_exams")
    interDf = pd.merge(df_student_exam_combo , df_exams , on = ['student_id' ,'subject_name'] , how = 'left')
    interDf['attended_exams'] = interDf['attended_exams'].fillna(0)
    return interDf.sort_values(by = ['student_id' ,'subject_name'])