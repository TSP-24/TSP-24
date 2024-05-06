import numpy as np

# Utilify functions

# Chi-square test to measure consistency of grades
def chi_square_compare(grades_and_scores):
    # Last element of scores_and_grades is the newest score
    _, new_score = grades_and_scores[-1]
    scores = [score for grade, score in grades_and_scores]
    average_score = np.mean(scores)
    distance_from_average = new_score - average_score

    new_score_chi = distance_from_average ** 2 / average_score
    chi_square_score = 0

    for _, score in grades_and_scores:
        chi_square_score += (score - average_score) ** 2 / average_score

    if chi_square_score == 0:
        return 0
    # Measure of how inconsistent the new score is, i.e how much it contributes to the deviation 
    # away from the uniform distribution of scores
    inconsistency_contribution = new_score_chi / chi_square_score

    return inconsistency_contribution*distance_from_average

# Convert score to grade
def score_to_grade(score):
    if 80 <= score <= 100:
        return 'HD'
    elif 70 <= score < 80:
        return 'D'
    elif 60 <= score < 70:
        return 'CR'
    elif 50 <= score < 60:
        return 'Pass'
    else:
        return 'Fail'

# Student class
class Student:
    def __init__(self, uni_id):
        self.uni_id = uni_id
        self.assignments = []
        self.quizzes = []
        self.midsem_exam = None
        self.final_exam = None
        self.attendance = None # Later to be implemented
        self.labs = [] # Later to be implemented
        self.engagement_score = 100
        self.failed_assessments = []
        self.late_submissions = [] # To be implemented!!!
        self.weights = {
            'quiz': 0.5,
            'assignment': 1,
            'midsem_exam': 1.5,
            'final_exam': 1.5,
            'attendance': 1,
            'labs': 1
        }
        self.failed_punishments = {
            'quiz': 5,
            'assignment': 10,
            'midsem_exam': 15,
            'final_exam': 20
        }
        self.hd_rewards = {
            'quiz': 0,
            'assignment': 5,
            'midsem_exam': 10,
            'final_exam': 15
        }

    def set_weights(self, weights):
        self.weights = weights

    def add_quiz(self, score):
        grade = score_to_grade(score)
        self.quizzes.append((grade, score))
        # Check if the student failed the quiz or got a HD
        if grade == 'Fail':
            self.engagement_score -= self.failed_punishments['quiz']
            self.failed_assessments.append('Quiz ' + str(len(self.quizzes)))
        elif grade == 'HD':
            self.engagement_score += self.hd_rewards['quiz']

        # Check if the student is consistent with their quiz scores
        if len(self.quizzes) > 1:
            inconsistency = chi_square_compare(self.quizzes)
            self.engagement_score += np.round(inconsistency * self.weights['quiz'])

    def add_assignment(self, score):
        grade = score_to_grade(score)
        self.assignments.append((grade, score))
        # Check if the student failed the assignment or got a HD
        if grade == 'Fail':
            self.engagement_score -= self.failed_punishments['assignment']
            self.failed_assessments.append('Assignment ' + str(len(self.assignments)))
        elif grade == 'HD':
            self.engagement_score += self.hd_rewards['assignment']
        
        # Check if the student is consistent with their assignment scores
        if len(self.assignments) > 1:
            inconsistency = chi_square_compare(self.assignments)
            self.engagement_score += np.round(inconsistency * self.weights['assignment'])

    def add_midsem_exam(self, score):
        grade = score_to_grade(score)
        self.midsem_exam = (grade, score)
        # Check if the student failed the midsem exam or got a HD
        if grade == 'Fail':
            self.engagement_score -= self.failed_punishments['midsem_exam']
            self.failed_assessments.append('Midsem Exam')
        elif grade == 'HD':
            self.engagement_score += self.hd_rewards['midsem_exam']

    def add_final_exam(self, score):
        grade = score_to_grade(score)
        self.final_exam = (grade, score)
        # Check if the student failed the final exam or got a HD
        if grade == 'Fail':
            self.engagement_score -= self.failed_punishments['final_exam']
            self.failed_assessments.append('Final Exam')
        elif grade == 'HD':
            self.engagement_score += self.hd_rewards['final_exam']

    # TODO: Implement attendance and labs
    def add_lab(self, score):
        self.labs.append(score)

    def add_attendance(self, attendance):
        self.attendance = attendance