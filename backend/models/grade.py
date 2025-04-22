from pydantic import BaseModel

class Grade(BaseModel):
    student_id: int
    progress: int
    grade: float
    date: str
