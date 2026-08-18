class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score: float) -> None:
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score)