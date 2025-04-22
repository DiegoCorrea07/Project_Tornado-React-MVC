import json

import tornado.web
from backend.controllers import student_controller, grade_controller

class CORSRequestHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()

class StudentsHandler(CORSRequestHandler):
    async def get(self):
        await student_controller.get_students_controller(self)

    async def post(self):
        data = json.loads(self.request.body)
        await student_controller.create_student_controller(self, data["nombre"], data["idbanner"])

class StudentPerformanceHandler(CORSRequestHandler):
    async def get(self, student_id):
        await student_controller.get_student_performance_controller(self, int(student_id))

class GradesHandler(CORSRequestHandler):
    async def post(self):
        data = json.loads(self.request.body)
        await grade_controller.create_grade_controller(self, data["student_id"], data["progress"], data["grade"], data["date"])

    async def get(self):
        student_id = self.get_argument("student_id", None)
        progress = self.get_argument("progress", None)
        start_date = self.get_argument("start_date", None)
        end_date = self.get_argument("end_date", None)
        await grade_controller.filter_grades_controller(self, student_id, progress, start_date, end_date)