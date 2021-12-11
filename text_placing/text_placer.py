"""This module contains a function that can place text on an image"""
from PIL import Image, ImageFont, ImageDraw

from text_placing import string_former


def place(string: str, image_path, font_path) -> Image:
	point_size = 38
	shadow_color = "#000"
	main_color = "#fff"
	x = 10
	y = 10
	font = ImageFont.truetype(font_path, point_size)

	text = string_former.form_from(string)
	if text is None:
		return

	image = Image.open(image_path)

	draw = ImageDraw.Draw(image)

	draw.text((x - 1, y), text, font=font, fill=shadow_color)
	draw.text((x + 1, y), text, font=font, fill=shadow_color)
	draw.text((x, y - 1), text, font=font, fill=shadow_color)
	draw.text((x, y + 1), text, font=font, fill=shadow_color)

	draw.text((x, y), text, font=font)

	return image

