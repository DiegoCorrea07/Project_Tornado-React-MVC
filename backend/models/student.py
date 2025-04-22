from pydantic import BaseModel

class Student(BaseModel):
    id: int
    IdBanner: str
    name: str
