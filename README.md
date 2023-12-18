# LaGOT

We release LaGOT evaluation benchmark for both single-object trackers (SOT) and multi-object trackers (MOT) / open-world trackers (OWT).

LaGOT benchmark is built on top of LaSOT validation set. We added up to 9
additional tracks to the LaSOT validation set.

![LaGOT teaser](.imgs/dataset_teaser.png?raw=true "LaGOT dataset")


## Download

Additional annotations are located in `data/`.
To obtain pixels, please follow the instructions of the [LaSOT official
repository](https://vision.cs.stonybrook.edu/~lasot/download.html). 

In addition to the new annotations, we also release the inference results of
multiple state-of-art SOT and MOT / OWT trackers.

## Usage

The scripts for results visualizations are located in `scripts/`.
To use those [pytracking toolbox](https://github.com/visionml/pytracking) and/or [TrackEval toolbox](https://github.com/JonathonLuiten/TrackEval) is needed.

## Citation

If you use LaGOT, please consider citing our paper:

- [Beyond SOT: Tracking Multiple Generic Objects at Once](https://arxiv.org/abs/2212.11920) 
  Christoph Mayer, Martin Danelljan, Ming-Hsuan Yang, Vittorio Ferrari, Luc Van Gool, Alina Kuznetsova

## Contacts

If you have any questions, please contact
[lagot-benchmark@googlegroups.com](mailto:lagot-benchmark@googlegroups.com).
