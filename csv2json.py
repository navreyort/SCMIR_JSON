#! /usr/bin/python

import os
import sys
import csv
import json

usage = """
Usage:
    python csvFilePath jsonFilePath

Example:
    python ~/Desktop/ ~/Desktop/

"""

fileExt = [".csv"]

#Recursively get file name
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
			else:
				fileList.extend(getFileNames(fullPathFile))

	return fileList

def csv2json(fileName):
	reader = csv.reader(open(fileName,'r'))
	fieldNames = reader.next()
	fieldNameLength = len(fieldNames)

	data = []
	i = 0
	for row in reader:
		data.append({})
		for j in range(0,len(row)):
			data[i][fieldNames[j]] = row[j]
		i = i + 1

	return json.dumps(data,separators=(',',':'))

def main(csvPath,jsonPath):
	fileList = getFileNames(csvPath)
	for file in fileList:
		json = csv2json(file)
		(filePath, fileName) = os.path.split(file)
		(title, extension) = os.path.splitext(fileName)
		fw = open(jsonPath + title + '.json','w')
		fw.write(json)
		fw.close()

	sys.exit()

if __name__ == '__main__':
        try:
                csvPath = sys.argv[1]
                jsonPath = sys.argv[2]
        except:
                print usage
                sys.exit(-1)
        main(csvPath,jsonPath)
