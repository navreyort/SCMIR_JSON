#! /usr/bin/python
import sys
import os
import csv
import numpy

usage = """
Normalizes csv file. It strips first row and exports only numbers.
Usage:
    python NormalizeCSV.py csvFile

Example:
    python NormalizeCSV.py this.csv
"""

def normalize(sample):
  return (sample - numpy.amin(sample)) / (numpy.amax(numpy.absolute((sample-numpy.amin(sample)))))


def main(path):
  mat = numpy.loadtxt(open(path,"rb"),delimiter=",",skiprows=1)

  newMat = numpy.zeros(mat.shape)

  for n in range(0,mat.shape[1]):
    norm = normalize(mat[:,n])
    newMat[:,n] = norm

  numpy.savetxt(path, newMat, delimiter=",")
  exit();

#TODO pass path name as argument
if __name__ == '__main__':
  try:
    cavPath = sys.argv[1]
  except:
    print usage
    sys.exit(-1)
  main(cavPath)
