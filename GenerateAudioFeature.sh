#!/bin/bash

#Check for argument
if [ -z "$1" ]
  then
    cat usage
    exit 1;
fi

snd="snd/"
wavTimes=0

while getopts ":t:" opt; do
  case $opt in
    t)
      dirName=$(dirname "$2")
      if [ -z "$dirName/$snd" ]
        then
          echo "no directory "snd" found with sounds."
          exit 1;
      fi
      echo "Getting wav file start time..."
      wavTimes=$((python GetWavTime.py $dirName/$snd) 2>&1)
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

###Generate arff using supercollider and ML library###
#check if sclang and scsynth exists
command -v sclang >/dev/null 2>&1 || { printf \
"sclang not found. May be run \
\nsudo ln -s /Applications/SuperCollider/SuperCollider.app/Contents/Resources/sclang /usr/local/bin/sclang \
\nsudo ln -s /Applications/SuperCollider/SuperCollider.app/Contents/Resources/scsynth /usr/local/bin/scsynth"; \
exit 1;}

echo "Running supercollider..."
if [ -z "$2" ]
  then
    dir=$1
    dirName=$(dirname "$1")
    fileName=$(basename "$1")
  else
    dir=$2
    dirName=$(dirname "$2")
    fileName=$(basename "$2")
fi

extension="${fileName##*.}"
fileName="${fileName%.*}"

wavTimes=$(echo $wavTimes | tr -d '[')
wavTimes=$(echo $wavTimes | tr -d ']')
wavTimes=$(echo $wavTimes | tr -d ',')
sclang ${PWD}/GenerateAudioFeature.sc "$dir" $wavTimes >/dev/null
rm "$dirName"/*.scmirZ

echo "Running weka..."
#Convert arff to csv
java -classpath /Applications/weka-3-6-8/weka.jar weka.core.converters.CSVSaver -i "$dirName"/"$fileName".arff -o "$dirName"/"$fileName".csv
rm "$dirName"/"$fileName".arff

echo "Normalizing data..."
$((python NormalizeCSV.py "$dirName"/"$fileName".csv) 2>&1)

audioFeatures="MFCC0,MFCC1,MFCC2,MFCC3,MFCC4,MFCC5,SpecCentroid,SpecPcile,SpecFlatness,FFTCrest,FFTSpread,FFTSlope,Loudness,SensoryDissonance"
#prepend field name to csv file
cat "$dirName"/"$fileName".csv | pbcopy && echo $audioFeatures > "$dirName"/"$fileName".csv && pbpaste >> "$dirName"/"$fileName".csv

echo "Converting csv to json..."
$((python csv2json.py "$dirName"/ "$dirName"/) 2>&1)
rm "$dirName"/"$fileName".csv

echo "Done :)"
exit 0
