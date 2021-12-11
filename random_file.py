"""Contains a function to get a random file from directory"""
from os import listdir
from os.path import isfile, join, exists
from random import randint


def get(directory):
	files = [f for f in listdir(directory) if isfile(join(directory, f))]
	filename = files[randint(0, len(files) - 1)]

	return join(directory, filename)

