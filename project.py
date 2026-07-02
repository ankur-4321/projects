import numpy as np

grades = np.random.randint(80, 100, size=(5,5))
print(grades)

subject_max = np.max(grades, axis=0)
student_max = np.max(grades, axis=1)

print("stud_max", student_max)
print("sub_max", subject_max)

subject_min = np.min(grades, axis=0)
student_min = np.min(grades, axis=1)

print("student_min", student_min)
print("subj_min", subject_min)

subject_avg = np.mean(grades, axis=0)
student_avg = np.mean(grades, axis=1)

print("student_avg", student_avg)
print("subj_avg", subject_avg)