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
        self.attendance = None # TODO Later to be implemented
        self.labs = [] # TODO Later to be implemented

        self.engagement_score = 100
        self.engagement_changes = []
        self.failed_assessments = []
        self.late_submissions = []

        self.deadlines = {
            'quiz': [],
            'assignment': [],
            'midsem_exam': [],
            'final_exam': [],
            'lab': []
        }
        self.weights = {
            'quiz': [0.35] * 12,
            'assignment': [0.7] * 12,
            'midsem_exam': [1],
            'final_exam': [1],
            'attendance': [1],
            'lab': [1] * 12
        }
        self.late_punishments = {
            'quiz': 2,
            'assignment': 5,
            'midsem_exam': 10,
            'final_exam': 15
        }
        self.failed_punishments = {
            'quiz': 2,
            'assignment': 5,
            'midsem_exam': 10,
            'final_exam': 15
        }
        self.hd_rewards = {
            'quiz': 2,
            'assignment': 5,
            'midsem_exam': 10,
            'final_exam': 15
        }
        self.d_rewards = {
            'quiz': 1,
            'assignment': 3,
            'midsem_exam': 5,
            'final_exam': 8
        }

    def set_deadlines(self, deadlines):
        self.deadlines = deadlines

    def set_weights(self, weights):
        self.weights = weights

    def add_quiz(self, score, submission_date):
        grade = score_to_grade(score)
        self.quizzes.append((grade, score))
        q_number = len(self.quizzes)
        q_weight = self.weights['quiz'][q_number - 1]

        # Check if the student submitted the quiz late
        if submission_date > self.deadlines['quiz'][q_number - 1]:
            score_change = np.round(-self.late_punishments['quiz']*q_weight)
            self.engagement_score += score_change
            self.late_submissions.append((f'Quiz {str(q_number)}:', score))
            self.engagement_changes.append((f'Late Quiz {str(q_number)}', score_change))

        # Check if the student failed the quiz or got a HD
        if grade == 'Fail':
            score_change = np.round(-self.failed_punishments['quiz']*q_weight)
            self.engagement_score += score_change
            self.failed_assessments.append((f'Quiz {str(q_number)}:', score))
            self.engagement_changes.append((f'Failed Quiz {str(q_number)}', score_change))
        elif grade == 'HD':
            self.engagement_score += np.round(self.hd_rewards['quiz']*q_weight)
        elif grade == 'D':
            self.engagement_score += np.round(self.d_rewards['quiz']*q_weight)

        # Check if the student is consistent with their quiz scores
        if len(self.quizzes) > 1:
            inconsistency = chi_square_compare(self.quizzes)
            score_change = np.round(inconsistency * q_weight)
            self.engagement_score += score_change
            if score_change < 0:
                self.engagement_changes.append((f'Inconsistent Quiz {str(q_number)}', score_change))

    def add_assignment(self, score, submission_date):
        grade = score_to_grade(score)
        self.assignments.append((grade, score))
        as_number = len(self.assignments)
        as_weight = self.weights['assignment'][as_number - 1]
        # Check if the student submitted the assignment late
        if submission_date > self.deadlines['assignment'][as_number - 1]:
            score_change = np.round(-self.late_punishments['assignment']*as_weight)
            self.engagement_score += score_change
            self.late_submissions.append((f'Assignment {str(as_number)}:', score))
            self.engagement_changes.append((f'Late Assignment {str(as_number)}', score_change))

        # Check if the student failed the assignment or got a HD
        if grade == 'Fail':
            score_change = np.round(-self.failed_punishments['assignment']*as_weight)
            self.engagement_score += score_change
            self.failed_assessments.append((f'Assignment {str(as_number)}:', score))
            self.engagement_changes.append((f'Failed Assignment {str(as_number)}', score_change))
        elif grade == 'HD':
            self.engagement_score += np.round(self.hd_rewards['assignment']*as_weight)
        elif grade == 'D':
            self.engagement_score += np.round(self.d_rewards['assignment']*as_weight)
        
        # Check if the student is consistent with their assignment scores
        if len(self.assignments) > 1:
            inconsistency = chi_square_compare(self.assignments)
            score_change = np.round(inconsistency * as_weight)
            self.engagement_score += score_change
            if score_change < 0:
                self.engagement_changes.append((f'Inconsistent Assignment {str(as_number)}', score_change))

    def add_midsem_exam(self, score):
        grade = score_to_grade(score)
        self.midsem_exam = (grade, score)
        # Check if the student failed the midsem exam or got a HD
        if grade == 'Fail':
            diseng_score = np,round(self.failed_punishments['midsem_exam'] * self.weights['midsem_exam'][0])
            self.engagement_score -= diseng_score
            self.failed_assessments.append((f'Midsem Exam:', score))
            self.engagement_changes.append(('Failed Midsem Exam', -diseng_score))
        elif grade == 'HD':
            self.engagement_score += np.round(self.hd_rewards['midsem_exam'] * self.weights['midsem_exam'][0])
        elif grade == 'D':
            self.engagement_score += np.round(self.d_rewards['midsem_exam'] * self.weights['midsem_exam'][0])

    def add_final_exam(self, score):
        grade = score_to_grade(score)
        self.final_exam = (grade, score)
        # Check if the student failed the final exam or got a HD
        if grade == 'Fail':
            diseng_score = np.round(self.failed_punishments['final_exam'] * self.weights['final_exam'][0])
            self.engagement_score -= diseng_score
            self.failed_assessments.append((f'Final Exam:', score))
            self.engagement_changes.append(('Failed Final Exam', -diseng_score))
        elif grade == 'HD':
            self.engagement_score += np.round(self.hd_rewards['final_exam'] * self.weights['final_exam'][0])
        elif grade == 'D':
            self.engagement_score += np.round(self.d_rewards['final_exam'] * self.weights['final_exam'][0])




    # TODO: Implement attendance and labs
    def add_lab(self, score):
        self.labs.append(score)

    def add_attendance(self, attendance):
        self.attendance = attendance



    def disengagement_reasons(self):
        # Sort the engagement changes by the engagement score change
        self.engagement_changes.sort(key=lambda x: x[1])
        # Print the top 3 assessments that caused the most decrease in engagement score
        return self.engagement_changes[:5]