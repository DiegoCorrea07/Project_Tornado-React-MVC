
from backend.db.connection import connect_db

async def get_all_students():
    conn = await connect_db()
    rows = await conn.fetch("SELECT id, idbanner, nombre FROM students")
    await conn.close()
    return [dict(row) for row in rows]

async def create_student(idbanner: str, nombre: str):
    conn = await connect_db()
    await conn.execute("INSERT INTO students (idbanner, nombre) VALUES ($1, $2)", idbanner, nombre)
    await conn.close()

async def get_student_by_id(student_id: int):
    conn = await connect_db()
    row = await conn.fetchrow("SELECT id, idbanner, nombre FROM students WHERE id = $1", student_id)
    await conn.close()
    return dict(row) if row else None