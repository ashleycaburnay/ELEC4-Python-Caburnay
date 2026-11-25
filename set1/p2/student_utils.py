# Student Utilities Module
# Name: ASHLEY MAE CABURNAY
# Section: IV-BSIT A
# Activity: P2

def calculate_average(grades):
    return sum(grades) / len(grades)


def determine_status(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)