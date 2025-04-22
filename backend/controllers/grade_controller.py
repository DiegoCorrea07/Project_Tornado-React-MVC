import json
import datetime
from backend.repositories import grade_repository


async def create_grade_controller(self, student_id: int, progress: int, grade: float, date: str):
    await grade_repository.create_grade(student_id, progress, grade, date)
    self.write({"status": "Calificación creada exitosamente"})


async def filter_grades_controller(self, student_id: str = None, progress: str = None, start_date: str = None, end_date: str = None):
    student_id_int = None
    if student_id:
        try:
            student_id_int = int(student_id)
        except ValueError:
            self.set_status(400)
            self.write({"error": "El ID del estudiante debe ser un número entero."})
            return

    progress_int = None
    if progress:
        try:
            progress_int = int(progress)
        except ValueError:
            self.set_status(400)
            self.write({"error": "El progreso debe ser un número entero."})
            return

    grades = await grade_repository.filter_grades(student_id_int, progress_int, start_date, end_date)
    formatted_grades = []
    for grade_entry in grades:
        formatted_grade = grade_entry.copy()
        if 'date' in formatted_grade and isinstance(formatted_grade['date'], datetime.datetime):
            formatted_grade['date'] = formatted_grade['date'].isoformat()
        formatted_grades.append(formatted_grade)
    self.write(json.dumps(formatted_grades))