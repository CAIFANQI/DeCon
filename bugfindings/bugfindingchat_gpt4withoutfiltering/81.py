
def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """

   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E+")
    return letter_grade
assert numerical_letter_grade([3.8, 2.5, 1.2, 0.9, 2.1, 3.6]) == ['A', 'B-', 'D+', 'D', 'C+', 'A-']
assert numerical_letter_grade([0.8, 0.7, 0.6, 0.5, 0.4]) == ['D', 'D-', 'D-', 'D-', 'D-']
assert numerical_letter_grade([0.4, 0.3, 0.2, 0.1, 0.0]) == ['D-', 'D-', 'D-', 'D-', 'E']
assert numerical_letter_grade([0.0, 0.0, 0.0, 0.0, 0.0]) == ['E', 'E', 'E', 'E', 'E'], "Test case 6 failed"
assert numerical_letter_grade([0.0, 0.0, 0.0]) == ['E', 'E', 'E']
assert numerical_letter_grade([3.6, 3.5, 3.4, 3.3, 3.2, 3.1]) == ['A-', 'A-', 'A-', 'B+', 'B+', 'B+'], "Test case 2 failed"
assert numerical_letter_grade([3.2, 3.1, 3.0, 2.9, 2.8, 2.7]) == ['B+', 'B+', 'B', 'B', 'B', 'B-'], "Test case 3 failed"
assert numerical_letter_grade([2.6, 2.5, 2.4, 2.3, 2.2, 2.1]) == ['B-', 'B-', 'B-', 'C+', 'C+', 'C+'], "Test case 4 failed"
assert numerical_letter_grade([0.5, 0.0]) == ['D-', 'E']
assert numerical_letter_grade([4.0, 4.0, 4.0, 4.0, 4.0, 4.0]) == ['A+', 'A+', 'A+', 'A+', 'A+', 'A+']
