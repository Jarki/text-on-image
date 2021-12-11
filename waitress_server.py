from waitress import serve
from main import app

serve(app, host='localhost', port=8080)
