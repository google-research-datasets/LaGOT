# Make sure the pytracking/pytracking/evaluation/lagotdataset.py uses the annotations 'LaGOT_one_object_per_sequence_annotations_final.json'
# and that the result_path in the pytracking/pytracking/evaluation/local.py file points to the raw result folder.

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [8, 5]

from pytracking.analysis.plot_results import plot_results
from pytracking.evaluation import get_dataset, trackerlist


def plot(mode:str='success'):
    trackers = []
    trackers.extend(trackerlist('lagot_tracking_results/stark_st', 'baseline', 0, 'Stark-50'))
    trackers.extend(trackerlist('lagot_tracking_results/dimp', 'dimp18', 0, 'DiMP-18'))
    trackers.extend(trackerlist('lagot_tracking_results/dimp', 'dimp50', 0, 'DiMP-50'))
    trackers.extend(trackerlist('lagot_tracking_results/dimp', 'prdimp18', 0, 'PrDiMP-18'))
    trackers.extend(trackerlist('lagot_tracking_results/dimp', 'prdimp50', 0, 'PrDiMP-50'))
    trackers.extend(trackerlist('lagot_tracking_results/qdtrack', 'qdtrack_init', None, 'QDTrack'))
    trackers.extend(trackerlist('lagot_tracking_results/qdtrack', 'qdtrack_all', None, 'QDTrack-Oracle'))
    trackers.extend(trackerlist('lagot_tracking_results/tamos', 'tamos_resnet50', 0, r'\bfTaMOs-50'))
    trackers.extend(trackerlist('lagot_tracking_results/tamos', 'tamos_swin_base', 0, r'\bfTaMOs-SwinBase'))
    trackers.extend(trackerlist('lagot_tracking_results/dimp', 'super_dimp', 0, 'SuperDiMP'))
    trackers.extend(trackerlist('lagot_tracking_results/keep_track', 'keep_track_iccv', 0, 'KeepTrack'))
    trackers.extend(trackerlist('lagot_tracking_results/tomp', 'tomp50_cvpr', 0, 'ToMP-50'))
    trackers.extend(trackerlist('lagot_tracking_results/tomp', 'tomp101_cvpr', 0, 'ToMP-101'))
    trackers.extend(trackerlist('lagot_tracking_results/transt', 'transt50', 0, 'TransT'))
    trackers.extend(trackerlist('lagot_tracking_results/stark_st', 'baseline_R101', 0, 'Stark-101'))
    trackers.extend(trackerlist('lagot_tracking_results/mixformer_online', 'baseline', 0, 'MixFormer-22k'))
    trackers.extend(trackerlist('lagot_tracking_results/mixformer_online', 'baseline_large', 0, 'MixFormerLarge-22k'))
    trackers.extend(trackerlist('lagot_tracking_results/ovtrack', 'vanilla_clip_promt_0_init', None, 'OVtrack'))
    trackers.extend(trackerlist('lagot_tracking_results/ovtrack', 'vanilla_clip_promt_0_all', None, 'OVtrack-Oracle'))

    dataset = get_dataset('lagot_sot_mode')

    if mode == 'success':
        plt.rcParams['figure.figsize'] = [8, 7]
        plot_opts = {'ylim': (0, 90), 'font_size_axis': 16, 'line_width': 2, 'font_size_legend': 10,
                     'handlelength': 2.5, 'legend_ncol': 1, 'legend_loc': 'lower left'}
        plot_results(trackers, dataset, 'LaGOT', merge_results=True, plot_types=('success'), plot_opts=plot_opts,
                     skip_missing_seq=False, exclude_invalid_frames=True, force_evaluation=True, plot_bin_gap=0.05)
    elif mode == 'prec_rec':
        plt.rcParams['figure.figsize'] = [8, 7]
        plot_opts = {'ylim': (0, 1), 'font_size_axis': 16, 'line_width': 2, 'font_size_legend': 10,
                     'handlelength': 2.5, 'legend_ncol': 2, 'legend_loc': 'lower right'}
        plot_results(trackers, dataset, 'LaGOT', merge_results=False, plot_types=('f1_prec_rec',), f1_prec_rec=True,
                     skip_missing_seq=False, exclude_invalid_frames=True, force_evaluation=True, plot_bin_gap=0.05,
                     anno_period=3, plot_opts=plot_opts)
    else:
        raise NotImplementedError(f'Mode {mode} is invalid use \'success\' or \'prec_rec\' instead.')


if __name__ == '__main__':
    plot(mode='prec_rec')
    plot(mode='success')