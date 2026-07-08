"""
A function named passed(submissions: list, lowest_passing: int) 
which takes a list of exam submissions and an integer number representing the lowest passing grade as its arguments.
The function should create and return a new list, 
which contains only the passed submissions from the original list.
"""

class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'ExamSubmission (examinee: {self.examinee}, points: {self.points})'

def passed(submissions: list, lowest_passing: int):

    passed_examinees = []

    for submission in submissions:
        if submission.points >= lowest_passing:
            passed_examinees.append(submission)
    return passed_examinees

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)
