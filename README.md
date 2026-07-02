# Student Grades Analysis using NumPy

## Overview
This Python project demonstrates how to analyze student grades using the NumPy library. It generates a random dataset of marks for students and computes various statistical measures such as maximum, minimum, and average marks.

## Features
- Generates a 5 × 5 matrix of random grades.
- Finds the highest marks for each student.
- Finds the highest marks for each subject.
- Finds the lowest marks for each student.
- Finds the lowest marks for each subject.
- Calculates the average marks for each student.
- Calculates the average marks for each subject.

## Technologies Used
- Python 3
- NumPy

## Project Structure
```
project.py
README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Navigate to the project folder:
```bash
cd <repository-folder>
```

3. Install NumPy:
```bash
pip install numpy
```

## How to Run

Run the Python file using:

```bash
python project.py
```

## Sample Output

```
[[95 81 88 99 90]
 [87 94 82 91 96]
 [89 85 97 84 90]
 [92 88 91 95 83]
 [98 90 86 89 94]]

stud_max [99 96 97 95 98]
sub_max [98 94 97 99 96]

student_min [81 82 84 83 86]
subj_min [87 81 82 84 83]

student_avg [90.6 90.0 89.0 89.8 91.4]
subj_avg [92.2 87.6 88.8 91.6 90.6]
```

> Note: The output will be different each time because the grades are generated randomly.

## Concepts Used
- NumPy Arrays
- Random Number Generation
- Array Indexing
- `np.max()`
- `np.min()`
- `np.mean()`
- Axis Operations
