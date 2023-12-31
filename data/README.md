# LaGOT groundtruth

This directory contains the LaGOT groundtruth annotations in two formats (for SOT
evaluation and MOT evaluation) as well as the inference results of different trackers (for the
trackers published in WACV'24 paper) on LaGOT in
the corresponding formats.

**The groundtruth annotations are located in the corresponding .zip files.**

We provide inference results for the following trackers: 

- DiMP/PrDiMP/SuperDiMP [SOT]
- KeepTrack [SOT]
- MixFormer [SOT]
- Stark [SOT]
- ToMP [SOT]
- TransT [SOT]
- QDTrack [MOT]
- OVTrack [MOT]
- **TaMOS [GOT]**

## SOT evaluation on LaGOT

For computing SOT metrics, first unpack lagot_got_sot_format.zip into
`$PATH_EVAL`.

Install and setup the pytracking framework (in particular, result location should be set correctly) from [GitHub](https://github.com/visionml/pytracking/tree/master).

To reproduce the numbers and plots in the paper:

``
python scripts/lagot_plots.py
``



## MOT evaluation on LaGOT

For computing MOT metrics install the TrackEval toolbox from [GitHub](https://github.com/JonathonLuiten/TrackEval)

Unpack lagot_motchallenge_format.zip into `$PATH_EVAL`.

To reproduce the numbers in the paper:

     TRACKERS_TO_EVAL=<which trackers you want to evaluate>
     python scripts/run_mot_challenge.py --USE_PARALLEL False --METRICS HOTA CLEAR Identity --BENCHMARK LaGOT --SPLIT_TO_EVAL val --DO_PREPROC False --GT_FOLDER $PATH_EVAL/lagot_motchallenge_format/data/gt/mot_challenge --TRACKERS_FOLDER $PATH_EVAL/lagot_motchallenge_format/data/trackers/mot_challenge/ --OUTPUT_FOLDER $PATH_TO_RESULTS/results/ --TRACKERS_TO_EVAL TRACKERS_TO_EVAL

**NOTE**: scripts folder is the scripts folder of the TrackEval toolbox.
