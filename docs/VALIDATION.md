# Validation record - October 30, 2026

Validation used the available local Python 3.11 environment (not a newly created
Conda environment) and a temporary copy of the proposed repository layout.
Notebook outputs in Git were not replaced by the validation runs.

## Passed

- All 116 relocated scientific CSVs are byte-for-byte identical to the original
  working tree. SHA-256 values are recorded in [CSV_SHA256.csv](CSV_SHA256.csv).
- All 11 notebooks pass nbformat validation; all 212 Python code cells compile.
  Setup works from every notebook subdirectory. Original notebook metadata, cell
  outputs, execution counts, and cell order are preserved after the two new
  introductory/setup cells.
- An independent AST comparison of each original/new analysis cell agrees after
  normalizing file locations and the corrected plotting display call. Numerical
  settings, algorithms, and classifiers are unchanged. `utils.py` is identical.
- The q sweep has 38 sessions with 401 q values each (15,238 rows). Session order
  has 38 entries; the trial-count table has 114 mouse/date/taste entries. The
  sampling-convergence table has 19 sample sizes.
- All five macaque all-stimuli tables have nine stimuli and 20 completed splits
  per stimulus. Each corresponding split table has 20 rows; its TDA/RBF means
  agree with the all-stimuli summary. TDA exceeds RBF SVM in 38 of 45 pairs.
- Utility smoke checks pass for Victor-Purpura distances, neuron permutation
  invariance, persistence computation, bottleneck self-distance, and tiny
  TDA/SVM classifications.
- Cached plotting cells execute for submitted Figures 4A, 4B, 6D, 7C, 8A-C,
  and 9B-C, including the five per-session macaque bar plots.
- The full submitted five-neuron notebook executes with its original settings;
  its final run gives TDA accuracy 0.8941666667 and SVM accuracy 0.495.
- The full arXiv-only point-cloud notebook executes.
- H1 raster/barcode plotting cells execute using trusted pre-existing local
  template and example-trial caches copied into the temporary validation tree.
- Rendered GC, H1, and macaque figure exports were visually inspected.
- Local Markdown links resolve.
- After installation, all tracked payload bytes matched the validated proposal,
  notebook setup resolved paths in all 11 actual repository subdirectories, and
  local documentation links resolved. The whitespace check for edited code,
  notebooks, and documentation passed. The original `main` reference was verified
  unchanged before saving the local commit.

The plotting check exposed a pre-existing `plt.show(fig)` error in the macaque
bar-plot cell. It was changed to `plt.show()`, and the cached plotting checks
then passed. This affects display compatibility, not the analysis.

## Not recomputed / known limits

- The full GC q sweep, 19-size sampling experiment, template optimization,
  100/1000-neuron classification sweeps, full raw GC classifications, and all
  raw macaque session/stimulus computations were not rerun.
- The submitted Figure 3 / legacy arXiv Figure 7 notebook needs the two absent
  historical Python modules documented in [REPRODUCIBILITY.md](REPRODUCIBILITY.md).
- The arXiv-only Figures 6/8 notebook needs missing historical wide-format CSVs.
- `multiprocess` was absent from the current local Python environment. It was
  added to the environment specification; the parallel q-sweep was not launched.
- The Conda environment was not rebuilt, and dependency versions are not locked.
- Stored notebook outputs remain historical. No claim of exact full-paper
  numerical reproduction follows from these cleanup checks.
