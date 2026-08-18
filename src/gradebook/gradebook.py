class Student:
    """A class representing a student with scores."""

    def __init__(self, name: str, student_id: str):
        """
        Initialize a Student object.

        Args:
            name: Student's full name
            student_id: Unique student identifier
        """
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score: float) -> None:
        """
        Add a score to the student's record.

        Args:
            score: The score to add (must be non-negative)

        Raises:
            ValueError: If score is negative
        """
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score)

    def average(self) -> float:
        """
        Calculate the average of all scores.

        Returns:
            The average score, or 0.0 if no scores exist
        """
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)