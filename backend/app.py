
import tornado.ioloop
import tornado.web
from views.routes import StudentsHandler, GradesHandler, StudentPerformanceHandler

class CORSRequestHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")

    def options(self):
        self.set_status(204)
        self.finish()

def make_app():
    return tornado.web.Application([
        (r"/students", StudentsHandler),
        (r"/students/(\d+)/performance", StudentPerformanceHandler),
        (r"/grades", GradesHandler),
    ], default_handler_class=CORSRequestHandler)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Servidor corriendo en http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()