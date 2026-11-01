# A Persistent Homology Pipeline for the Analysis of Neural Spike Train Data

Code and results accompanying the paper by Cagatay Ayhan, Audrey N. Nash,
Roberto Vincis, Martin Bauer, Richard Bertram, and Tom Needham.

**Publication status (October 30, 2026): accepted for publication in SIAM Journal
on Life Sciences (SIALS), to appear** 

[arXiv preprint](https://arxiv.org/abs/2512.08637v1)

## Manuscript versions and notebook map

Section and figure numbers in `notebooks/submitted/` refer to journal version of the paper (to appear).The `arxiv_only` notebooks retain the
December 2025 preprint.

| Notebook | Section / figure | Scope and prerequisites |
| --- | --- | --- |
| [sec04_02_02_fig04B_sampling_stability.ipynb](notebooks/submitted/sec04_02_02_fig04B_sampling_stability.ipynb) | Section 4.2.2; Figure 4B | Primary sampling-convergence notebook. Cached results cover 19 sample sizes. The original generation cell runs only the six largest sizes and appends rows; select sizes deliberately before recomputing. |
| [sec04_03_04-05_fig08_gustatory_cortex_classification.ipynb](notebooks/submitted/sec04_03_04-05_fig08_gustatory_cortex_classification.ipynb) | Sections 4.3.4-4.3.5; Figure 8A-C | Repeated holdout TDA/SVM, single-neuron comparison, and neuron-label shuffling. Cached scores are included; raw GC recordings and Bayesian single-neuron scores are external inputs. |
| [sec04_03_06_fig09_macaque_coordination_test.ipynb](notebooks/submitted/sec04_03_06_fig09_macaque_coordination_test.ipynb) | Section 4.3.6; Figure 9A-C | Genuine versus trial-shuffled macaque rasters. Uses five sessions, nine stimuli per session, and 20 splits. The generation and loading paths now agree. |
| [sec04_03_03_fig07_mixed_coding_regimes.ipynb](notebooks/submitted/sec04_03_03_fig07_mixed_coding_regimes.ipynb) | Section 4.3.3; Figure 7A-C | The manuscript uses 100 neurons. The 1000-neuron cells are supplementary and retained. |
| [arxiv-v1_sec02_03_01_fig02_pointcloud_demo.ipynb](notebooks/arxiv_only/arxiv-v1_sec02_03_01_fig02_pointcloud_demo.ipynb) | arXiv v1 Section 2.3.1; Figure 2 only | The point-cloud illustration was removed from Version_3_submitted. Its Figure 2 is a different pipeline schematic; this notebook does not reproduce submitted Figure 2. |
| [sec04_03_02_fig06_h1_higher_order_structure.ipynb](notebooks/submitted/sec04_03_02_fig06_h1_higher_order_structure.ipynb) | Section 4.3.2; Figure 6A-D | Loop/path templates, noisy trials, and H0/H1/SVM comparison. Run the generation cell to create the template/trial pickle files needed by the full raster/barcode figure. |
| [sec04_02_01_fig04A_victor_purpura_stability.ipynb](notebooks/submitted/sec04_02_01_fig04A_victor_purpura_stability.ipynb) | Section 4.2.1; Figure 4A | Two-class GC parameter sweep with repeated holdout validation. Cached q_values_results.csv contains 38 sessions times 401 q values. |
| [sec04_03_01_fig05_coordinated_synthetic_activity.ipynb](notebooks/submitted/sec04_03_01_fig05_coordinated_synthetic_activity.ipynb) | Section 4.3.1; Figure 5A-B | Synthetic five-neuron example. Retains extra BDM/MDS and historical exploratory cells. Old Figure 4 panel labels have been corrected to the submitted version. |
| [sec02_03_03_fig03_bdm_mds_rasters_legacy_arxiv_fig07.ipynb](notebooks/submitted/sec02_03_03_fig03_bdm_mds_rasters_legacy_arxiv_fig07.ipynb) | Section 2.3.3; Figure 3 (arXiv v1 Figure 7) | The same biological illustration was renumbered. This is legacy code requiring external TDA_Pipeline_with_Victor_Purpura.py and SpikeTrainFunctions.py; these modules are absent from this repository. It is not an arXiv-only figure. |
| [arxiv-v1_sec04_03_fig06_fig08_gc_stability_and_loocv.ipynb](notebooks/arxiv_only/arxiv-v1_sec04_03_fig06_fig08_gc_stability_and_loocv.ipynb) | arXiv v1 Section 4.3; Figures 6 and 8 only | Historical LOOCV plots and external wide-format score tables. These are not the submitted Figure 6 or Figure 8 experiments. |
| [sec04_02_02_fig04B_sampling_stability_duplicate.ipynb](notebooks/archive/sec04_02_02_fig04B_sampling_stability_duplicate.ipynb) | Section 4.2.2; Figure 4B (duplicate) | Preserved duplicate: all original code-cell sources are identical to the primary sampling notebook. Prefer notebooks/submitted/sec04_02_02_fig04B_sampling_stability.ipynb. |


## Repository organization

```text
notebooks/
  submitted/             Version_3_submitted analyses (8 notebooks)
  arxiv_only/            Historical preprint-only figures (2 notebooks)
  archive/               Preserved duplicate sampling notebook
metadata/           Session order and trial-count tables
results/
  stability/             VP q sweep and empirical Wasserstein convergence
  synthetic/             H1 comparison and 100-neuron mixed-coding results
  gustatory_cortex/      Cached GC TDA, SVM, neuron, and shuffling scores
  coordination_test/     Macaque session/stimulus results for Figure 9
  supplementary/         Additional q sweeps, 1000-neuron and varying-k results
Datasets/                Local raw/external inputs (ignored; not distributed)
outputs/                 New figure exports and generated arrays (ignored)
docs/                    Reproduction guide, data inventory, change record
utils.py                 Spike/raster generation, VP, persistence, classifiers
real_data_utils.py       GC loading and raster extraction (loads data on import)
repo_paths.py            Shared input paths and optional environment overrides
environment.yml          Conda environment specification
```

## Getting started

From the repository root:

```bash
conda env create -f environment.yml
conda activate spike-train-tda
jupyter lab
```

Open the notebook for the desired section and run its setup cell first. The
setup finds the repository root, so imports and paths also work when the notebook
kernel starts in its own subdirectory. Use a kernel from the `spike-train-tda` environment.


## Data and implementation

Synthetic data are generated by the notebooks. GC recordings and Bayesian single-neuron scores are external inputs; see the [Vincis lab data/code repository](https://github.com/vincisLab/neuron-response-classification). The macaque experiment uses [CRCNS v1v2-1](https://doi.org/10.6080/K0B27SHN). Local datasets are kept under `Datasets/` and are not added to Git.

The pipeline treats each neuron ensemble as a metric space using Victor-Purpura
distance, computes persistence barcodes, compares them with bottleneck distance,
and classifies stimuli with 1-NN. General VP computations use Elephant; the
discrete-time special case uses `VP_trivial`. Persistent homology uses Ripser;
bottleneck computations use the custom degree-0 `bottleneck_zero`, Persim, or
GUDHI according to the notebook. Classification validation is experiment-specific:
the submitted analyses include repeated 70:30 holdout splits, while the
preprint code includes LOOCV.

For questions related to the manuscript, contact the corresponding author Tom Needham.
