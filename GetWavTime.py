#! /usr/bin/python
import sys
import os
import wave
from contextlib import closing

usage = """
Usage:
    python GetWavTime.py sndPath

Example:
    python GetWavTime.py ~/Desktop/

"""

#only get file names with these extensions:
fileExt = [".wav"]

def getFileNames(path):
	dirList = os.listdir(path)
	fileList = []
	for file in dirList:
		(filePath, fileName) = os.path.split(file)
		(title, extension) = os.path.splitext(fileName)
		if extension in fileExt:
			fullPathFile = os.path.join(path,file)
			if os.path.isfile(fullPathFile):
				fileList.append(fullPathFile)
		elif not "." in fileName:
			fileList.extend(getFileNames(os.path.join(path,fileName)))

	return fileList

def main(path):

	fileNames = getFileNames(path)

	start = []
	durs = []
	iter = 0
	for fileName in fileNames:
		with closing(wave.open(fileName,'r')) as file:
			frames = file.getnframes()
			rate = float(file.getframerate())
			durs.append(frames/rate)
			if iter != 0:
				start.append(start[iter-1] + (frames/rate))
			else:
				start.append((frames/rate))
		iter = iter + 1

	start.insert(0,0)
	exit(start)

#TODO pass path name as argument
if __name__ == '__main__':
	try:
		sndPath = sys.argv[1]
	except:
		print usage
		sys.exit(-1)
	main(sndPath)
