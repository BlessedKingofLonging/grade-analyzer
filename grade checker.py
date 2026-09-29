grades = [78, 92, 65, 88, 95, 71, 84]
def calculate_average(grades): 
    total = sum(grades)
    average = total / len(grades)
    return average
def find_highest_grade(grades):
    highest_grade = max(grades)
    return highest_grade
def find_lowest_grade(grades):
    lowest_grade = min(grades)
    return lowest_grade
def count_passing_grades(grades, passing_score=50):
    passing_count = sum(1 for grade in grades if grade >= passing_score)
    return passing_count
def count_failing_grades(grades, passing_score=50):
    failing_count = sum(1 for grade in grades if grade < passing_score)
    return failing_count
print(calculate_average(grades))
print(find_highest_grade(grades))
print(find_lowest_grade(grades))
print(count_passing_grades(grades))
print(count_failing_grades(grades))