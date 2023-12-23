# LaGOT

We release the LaGOT evaluation benchmark for both single-object trackers (SOT) and multi-object trackers (MOT) / open-world trackers (OWT).

The LaGOT benchmark is built on top of the LaSOT validation set. We added up to 9
additional tracks per video to the LaSOT validation set annotations.

![LaGOT teaser](.imgs/dataset_teaser.png?raw=true "LaGOT dataset")


## Download

Additional annotations are located in `data/`.
To obtain pixels, please follow the instructions of the [official LaSOT repository](https://vision.cs.stonybrook.edu/~lasot/download.html). 

In addition to the new annotations, we also release the inference results of
multiple state-of-the-art SOT and MOT / OWT trackers.

## Usage

The scripts for results visualizations are located in `scripts/`.
To use those the [pytracking toolbox](https://github.com/visionml/pytracking) and/or the [TrackEval toolbox](https://github.com/JonathonLuiten/TrackEval) is needed.

## Citation

If you use LaGOT, please cite our paper:

```
@InProceedings{Mayer_2024_WACV,
    author    = {Mayer, Christoph and Danelljan, Martin and Yang, Ming-Hsuan and Ferrari, Vittorio and Van Gool, Luc and Kuznetsova, Alina},
    title     = {Beyond SOT: Tracking Multiple Generic Objects at Once},
    booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
    month     = {January},
    year      = {2024},
    pages     = {6826-6836}
}
```

## Contacts

If you have any questions, please contact
[lagot-benchmark@googlegroups.com](mailto:lagot-benchmark@googlegroups.com).
