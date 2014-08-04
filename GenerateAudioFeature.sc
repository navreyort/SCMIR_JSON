//Requires SCMIR
var argv = thisProcess.argv;

var analyze = { | path, wavTimes |
	var buffer,analysis,segments;
	var blind_segment_count=500;

	"SC: Loading Buffer".postln;
	buffer = Buffer.readChannel(s,path,channels:[0]);

	"SC: Beginning analysis".postln;
	analysis = SCMIRAudioFile(path, [[MFCC,6],[SpecCentroid],[SpecPcile],[SpecFlatness],[FFTCrest],[FFTSpread],[FFTSlope],[Loudness],[SensoryDissonance]]);
	analysis.extractFeatures();
	analysis.extractBeats();
	analysis.save;

	if (wavTimes.size <= 1) {
		segments = (0,(analysis.duration/(blind_segment_count-1))..analysis.duration);
	} {
		segments = wavTimes;
	};

	analysis.gatherFeaturesBySegments(segments, true,1);

	"Processing Finished...analysis ready for use.".postln;
	analysis.exportARFF(PathName(path).pathOnly++PathName(path).fileNameWithoutExtension++".arff");
};

var wavTimes = Array.fill(argv.size-1,{|i|
	argv[i+1].asFloat
});

analyze.(argv[0],wavTimes);

//Important!!
0.exit;
