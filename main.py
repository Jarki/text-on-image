from os.path import join
import random_file

from flask import Flask
from flask import request
from flask import send_file

import text_placing


image_dir = "images/"
image_path = random_file.get(image_dir)
result_dir = "results/"
result_filename = "result.jpg"
result_path = join(result_dir, result_filename)

font_path = "fonts/static/Inter-Bold.ttf"

app = Flask(__name__)


@app.route('/get_image', methods=["POST", "GET"])
def create_image():
	text = request.args.get('text')

	if text is not None:
		image = text_placing.place(text, image_path, font_path)

		if image is None:
			return 'Something went wrong'

		image.save(result_path)

		return send_file(result_path, mimetype='image/jpeg')

	return ''
