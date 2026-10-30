# Reproducing the analyses

## Environment and paths

Create the Conda environment from the root `environment.yml`, activate
`spike-train-tda`, and launch `jupyter lab`. The specification includes SciPy,
tqdm, joblib, JupyterLab, ipykernel, and multiprocess, which the notebooks use.
It is a dependency specification, not a version-locked record of the original
environment. Package changes may affect exact numerical or plotting behavior.

Every notebook begins with a reference note and a setup cell. Run setup first;
it resolves the repository root from the current directory or a parent, changes
the working directory to that root, and adds it to the import path. Launch
Jupyter from the repository or a notebook subdirectory. The shared defaults are:

| Input | Default location | Optional environment override |
| --- | --- | --- |
| GC neuron dataframe | `Datasets/NeuronDF.pickle` | `SPIKE_TRAIN_NEURON_DF` |
| Bayesian single-neuron scores | `Datasets/gctemp_sna_withMDpair_info.csv` | `SPIKE_TRAIN_SINGLE_NEURON_SCORES` |
| CRCNS archive | `Datasets/CRCNS/v1-v2_gratings.zip` | `SPIKE_TRAIN_CRCNS_ARCHIVE` |
| Historical wide-format score CSVs | `Datasets/legacy_arxiv/` | `SPIKE_TRAIN_LEGACY_DATA` |
| Historical Python helper modules | Not bundled | `SPIKE_TRAIN_LEGACY_CODE` |

Set overrides before starting the kernel; restart the kernel after changing them.
Use absolute override paths for clarity. `repo_paths.py` is the single place
defining these defaults. Raw inputs are ignored by Git and are not downloaded
automatically. Use trusted recordings and pickle files from their original sources.

Generated figure files go to `outputs/figures/<notebook-stem>/`. Generated H1
templates, example trials, and arrays go to `outputs/generated/`. Result CSVs
remain under `results/`, and session metadata under `data/metadata/`. Full
computation cells can overwrite or append to the supplied CSVs. To compare a new
run with the historical results, preserve a copy of the CSVs first.

## Cached plots, without full recomputation

The snippets below identify existing cells by their first statement or heading;
they are not instructions to execute every earlier computation cell. Always run
the setup cell first. `display` in the notebook environment is provided by IPython.

| Submitted figure | Cells to run after setup | Inputs / limitations |
| --- | --- | --- |
| 4A | `results_real_data = pd.read_csv(...)`, then the following heatmap cell | Saved `results/stability/q_values_results.csv`; skip `from real_data_utils import *` and the parallel sweep when only plotting. |
| 4B | `combined_results = pd.read_csv(...)`, then the final error-bar plot | Saved `results/stability/stability_results.csv`; no new samples needed. |
| 5A-B | Run the synthetic notebook in order | Generates its own data. Additional historical BDM/MDS cells are retained. The final SVM comparison plot supplies Figure 5B; the supplementary BDM is not a submitted panel. |
| 6D | `from utils import *` / the following imports cell, then either CSV bar-chart cell | Saved `results/synthetic/results_summary_degree_1_homology.csv`; no template optimization needed for this panel. |
| 6A-C | Imports, then the template/trial plot cells | Requires four generated pickle files. Create them with the generation cell, or use previously generated trusted copies in `outputs/generated/`. |
| 7C | `from utils import *`, load `hybrid_experiment_results_100_neurons.csv`, then the Figure 7C plot cell | Use the 100-neuron CSV in `results/synthetic/`. The 1000-neuron CSV in `results/supplementary/` is extra. |
| 7A-B | Imports, mixed-regime dataset generator definition, then the Figure 7A/7B plot cell | These example plots regenerate small synthetic datasets; they do not require raw recordings. |
| 8A-C | `from utils import *`; under "summary of all data frames", load permutation scores, both `MD_scores_table_*class` tables, and `neuron_scores_df`; run the refined three-panel plot | Uses the four saved GC tables. Skip the raw-data loader and classifier runs for this route. |
| 9B-C | Package imports, "load the saved results", "Mean over 9 stimuli for each session", session accuracy plot, then paired TDA/RBF plot | Loads the five `*_all_stimuli_summary.csv` tables from `results/coordination_test/`. Figure 9A needs the raw CRCNS archive. |

The archived sampling notebook is an exact duplicate of the original code sources
in the primary sampling notebook; it is retained for provenance. Choose the primary
notebook for future work. Stored execution outputs in all notebooks are historical
and were preserved rather than replaced by the cleanup validation runs.

## Full recomputation and external inputs

**GC (Sections 4.1.2, 4.2.1, 4.3.4-4.3.5).** Obtain the recordings/preprocessing
inputs from the [Vincis lab project](https://github.com/vincisLab/neuron-response-classification).
The loader expects a pandas dataframe with the original `MouseID`, `Date`,
`Taste`, `Trial`, and `Neuron` columns and the spike-bin columns beginning at
column index 7. Dates should retain their original string format. `pairs.csv`
fixes the order of the 38 mouse/date recording sessions. The GC single-neuron
comparison also uses the externally computed Bayesian rate-phase `SNAscore`
values; the repository does not implement their full upstream estimation.
`real_data_utils.py` loads the dataframe and builds trial rasters when imported.
The q sweep uses `multiprocess` and eight workers; its original settings are
preserved. Check memory and CPU availability before starting a full sweep.

**Sampling convergence (Section 4.2.2).** The saved CSV contains 19 sample sizes
from 10 through 5000, rather than every multiple of 10. The original active `Ns`
list contains only `[2500, 3000, 3500, 4000, 4500, 5000]`; an earlier grid is
commented above it. Select the intended grid explicitly when regenerating. The
routine appends rows without deduplicating `N`; clear or redirect the output CSV
for an independent run. It computes an N-by-N cost matrix and an assignment
problem repeatedly, so the largest sizes are costly. Its calls use
`random_state=None`, so a rerun will not exactly reproduce the cached values.

**H1 example (Section 4.3.2).** The generation cell optimizes a path template,
generates noisy trials, writes four `stim*_*.pkl` files and `h1_dataset.npz`, and
computes H0/H1/SVM scores. These intermediate files are intentionally not tracked.
Do not expect the raster/barcode panels to run from the summary CSV alone.
Panel references here follow the Figure 6 caption: A templates, B noisy trials,
C barcodes, D classification. A sentence in Section 4.3.2 calls the
classification panel C; the caption and figure label it D.

**Macaque (Section 4.3.6).** Obtain
[CRCNS v1v2-1](https://doi.org/10.6080/K0B27SHN), retaining the ZIP member paths
`v1-v2_gratings/mat_neural_data/<session>.mat`. The notebook selects one session
near the top; rerun its computation block for each of the five sessions to
regenerate all 45 session/stimulus combinations. Each uses 100 genuine rasters,
20 independent 70:30 splits, and training/test shuffles made separately. The
writer and loader now use `results/coordination_test/`. The generic historical
`classification_*.csv` pair is not used for the paper aggregation. Figure 9 panel
assignments here follow the caption: A rasters, B session accuracy, C paired
accuracy; the prose in Section 4.3.6 refers to the two accuracy panels as A/B.

## Legacy limitations

The submitted Figure 3 / arXiv Figure 7 notebook imports
`TDA_Pipeline_with_Victor_Purpura.py` and `SpikeTrainFunctions.py`. Neither module
is included in this repository. Set `SPIKE_TRAIN_LEGACY_CODE` to the directory
containing the original compatible files before running that notebook. These
imports were not replaced by the newer pipeline because their signatures and
historical outputs differ.

The arXiv-only Figures 6/8 notebook needs these six external CSVs in
`SPIKE_TRAIN_LEGACY_DATA`:

- `data_frame_for_each_mouse_date_over_finer_q_values_between_0_and_1.csv`
- `data_frame_for_each_mouse_date_over_finer_q_values_between_0_and_1_after_34th.csv`
- `data_frame_for_each_mouse_date_over_finer_q_values_between_1_and_2.csv`
- `q2005_3temp_GC_temp_networks_summary.csv`
- `q2005_3temp_GC_temp_networks_detailedLOOscores.csv`
- `gctemp_sna_withMDpair_info.csv`

The first five were not found in this repository. The single-neuron CSV is
available locally under `Datasets/`; it is not tracked. The legacy Figure 3
notebook also reads that single-neuron table from the legacy data directory in
its later exploratory cells. Provide the original historical tables rather than
substituting newer RHV results for the preprint's LOOCV analysis.

The arXiv-only point-cloud notebook illustrates preprint Figure 2 and has no
corresponding submitted figure. Its original plotting behavior, including use
of infinite persistence bars, was preserved.
