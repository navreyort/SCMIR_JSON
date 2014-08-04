# SCMIR-JSON

A really complicated way to analyze audio file and generate an analysis file in json format using bash/python/supercollider/weka/.

#### Built and Tested with:
* [CodeRunner](http://krillapps.com/coderunner/)
* [Supercollider](http://supercollider.sourceforge.net/)


## Dependencies
* [Supercollider](http://supercollider.sourceforge.net/)
* [SCMIR](http://www.sussex.ac.uk/Users/nc81/code.html)
* [Weka](http://www.cs.waikato.ac.nz/ml/weka/)
* [Python](https://www.python.org/)
* [numpy](http://www.numpy.org/)

## Usuage
#### on mac:

	sh GenerateAudioFeature.sh path/to/sound/file/snd.wav
	sh GenerateAudioFeature.sh -t path/to/sound/file/snd.wav

## Example Application
* [Constellation](http://toronto.media.mit.edu/scores/constellation/edit/?reload)
	* This audio web application uses JSON file generated with this script to draw graphical dots on the interface and to also synthesize sound when the user interacts with the interface.
	
## TODO
* Find an easier solution to specify blind segmentation duration
* Find an easier solution to specify audio extraction parameter

## License 

MIT License applies to this code repository

    Copyright (C) 2014 Akito van Troyer
        
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
