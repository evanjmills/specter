import click
import cv2
# import face_recognition
# import numpy as np
# import copy
# import time

@click.command()
@click.option('--file', help='Optional video file')
@click.option('--faces', '-f', multiple=True, help='Images of faces to be removed')
@click.option('--outfile', '-o', help='File to save the processed video to')
def main(file, faces, outfile):
	capture = None
	if file == None:
		compile
	else:
		capture = cv2.VideoCapture(file)

	


if __name__ == '__main__':
	main()