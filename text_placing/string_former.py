"""This module takes an input string and forms it into a
string that can be placed on the image"""
from re import sub
from textwrap3 import wrap
from typing import Optional


max_string_length = 128
characters_in_line = 24


def form_from(input_string: str) -> Optional[str]:
	input_string = input_string.strip()
	input_string = sub(' +', ' ', input_string)

	if len(input_string) > max_string_length:
		return None

	inserted_point = "."
	if input_string.endswith('.'):
		inserted_point = ""

	text = "Коллеги, нужно " \
		f"{input_string} " \
		f"Добавил задачку в notion"

	text = '\n'.join(wrap(text, characters_in_line))

	return text
