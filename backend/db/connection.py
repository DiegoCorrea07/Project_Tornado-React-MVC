import asyncpg

DATABASE_URL = "url_conexión_a_base_de_datos"

async def connect_db():
    return await asyncpg.connect(DATABASE_URL)
