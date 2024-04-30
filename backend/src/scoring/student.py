class Student:
    def __init__(self, uni_id):
        self.uni_id = uni_id
        self.assignments = []
        self.quizzes = []
        self.exams = []
        self.attendance = 0
        self.labs = []
        self.engagement_score = 100

    def add_assignment(self, score):
        self.assignments.append(score)

    def add_quiz(self, score):
        self.quizzes.append(score)

    def add_exam(self, score):
        self.exams.append(score)

    def attend_class(self, attendance):
        self.attendance = attendance

    def add_lab(self, score):
        self.labs.append(score)

    # TODO
    def assignment_engagement(self):
        return sum(self.assignments) / len(self.assignments)
    # TODO
    def quiz_engagement(self):
        return sum(self.quizzes) / len(self.quizzes)
    # TODO
    def exam_engagement(self):
        return sum(self.exams) / len(self.exams)
    # TODO
    def attendance_engagement(self):
        return self.attendance
    # TODO
    def lab_engagement(self):
        return sum(self.labs) / len(self.labs)


    def calculate_engagement_score(self):
        return self.engagement_score
    