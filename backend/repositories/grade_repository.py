from backend.db.connection import connect_db
from backend.utils import date_utils

async def get_grades_by_student_id(student_id: int):
    conn = await connect_db()
    rows = await conn.fetch("SELECT progress, grade, date FROM grades WHERE student_id = $1", student_id)
    await conn.close()
    return [dict(row) for row in rows]

async def create_grade(student_id: int, progress: int, grade: float, date_str: str):
    conn = await connect_db()
    print(f"Cadena de fecha recibida: {date_str}")
    try:
        date_obj = date_utils.parse_date_simple(date_str)
        if date_obj:
            await conn.execute(
                "INSERT INTO grades (student_id, progress, grade, date) VALUES ($1, $2, $3, $4)",
                student_id, progress, grade, date_obj
            )
        else:
            print(f"No se pudo parsear la fecha: {date_str}")
    except Exception as e:
        print(f"Error al insertar la calificación: {e}")
    finally:
        await conn.close()

async def filter_grades(student_id: int = None, progress: int = None, start_date: str = None, end_date: str = None):
    conn = await connect_db()
    query = """
        SELECT g.student_id, g.progress, g.grade, g.date, s.nombre AS student_name
        FROM grades g
        JOIN students s ON g.student_id = s.id
        WHERE 1=1
    """
    conditions = []
    params = []

    if student_id is not None:
        conditions.append("g.student_id = $1")
        params.append(student_id)
    if progress is not None:
        conditions.append("g.progress = $" + str(len(params) + 1))
        params.append(progress)

    parsed_start_date = None
    if start_date:
        parsed_start_date = date_utils.parse_date_simple(start_date)
        if parsed_start_date:
            conditions.append("g.date >= $" + str(len(params) + 1))
            params.append(parsed_start_date)
        else:
            print(f"No se pudo parsear la fecha de inicio: {start_date}")

    parsed_end_date = None
    if end_date:
        parsed_end_date = date_utils.parse_date_simple(end_date)
        if parsed_end_date:
            conditions.append("g.date <= $" + str(len(params) + 1))
            params.append(parsed_end_date)
        else:
            print(f"No se pudo parsear la fecha de fin: {end_date}")

    if conditions:
        query += " AND " + " AND ".join(conditions)

    rows = await conn.fetch(query, *params)
    await conn.close()
    return [dict(row) for row in rows]