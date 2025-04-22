from backend.repositories import student_repository, grade_repository
from backend.services.calculator import calcular_promedio, nota_necesaria_etapa3
import json

async def get_students_controller(self):
    students = await student_repository.get_all_students()
    self.write(json.dumps(students))

async def create_student_controller(self, nombre: str, idbanner: str):
    await student_repository.create_student(idbanner, nombre)
    self.write({"status": "Estudiante creado exitosamente"})

async def get_student_performance_controller(self, student_id: int):
    student = await student_repository.get_student_by_id(student_id)
    if not student:
        return self.write(json.dumps({"mensaje": "Estudiante no encontrado."}))

    grades = await grade_repository.get_grades_by_student_id(student_id)
    if not grades:
        return self.write(json.dumps({"mensaje": "No hay notas registradas para este estudiante."}))

    promedio_final, promedios_por_etapa = calcular_promedio(grades)

    performance = {
        "id": student['id'],
        "nombre": student['nombre'],
        "promedio_final": promedio_final,
        "promedios_por_etapa": promedios_por_etapa,
        "estado": "aprobado" if promedio_final >= 6 else "reprobado"
    }

    if 1 in promedios_por_etapa and 2 in promedios_por_etapa and 3 not in promedios_por_etapa:
        nota_requerida = nota_necesaria_etapa3(promedios_por_etapa.get(1, 0), promedios_por_etapa.get(2, 0))
        performance["nota_necesaria_etapa3"] = nota_requerida

    self.write(json.dumps(performance))