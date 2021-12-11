from waitress import serve

from main import app
import env


serve(app, host=env.host, port=env.port)
