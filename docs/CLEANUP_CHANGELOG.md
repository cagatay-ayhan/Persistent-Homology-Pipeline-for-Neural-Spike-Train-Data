# Local cleanup, October 30, 2026

Base: `main` at `b35b0db580bc8d79049d2296ed04dc9bb128d575`.
Work branch: `clean-branch`, created locally from that commit after confirming
the working tree was clean and the branch did not already exist.

## Changes

- Renamed all 11 notebooks: eight submitted-version analyses, two arXiv-only
  notebooks, and one preserved sampling duplicate. Each name identifies the
  appropriate section and figure; the submitted Figure 3 notebook also states
  its legacy arXiv Figure 7 origin.
- Added a reference/scope note and a root/path setup cell to each notebook.
  Retained original cell order, saved outputs, execution counts, and metadata.
- Corrected the five-neuron notebook's stale Figure 4 labels to submitted Figure
  5A/B. Identified its BDM heatmap as supplementary rather than submitted Figure
  5B. Replaced its stale appendix reference with a description of the actual
  single-neuron method used by that code.
- Moved all 116 tracked scientific CSVs: two metadata tables, two stability
  tables, two synthetic tables, eight GC tables, five supplementary tables, and
  97 macaque coordination-test tables. No CSV contents were changed. Every move
  appears in [FILE_MOVES.csv](FILE_MOVES.csv).
- Updated active CSV readers/writers and commented CSV export paths to their new
  locations. Unified the macaque writer's old `Results for CRCNS
  Coordination-test/` path with the loader's results directory.
- Routed new figure exports to `outputs/figures/<notebook-stem>/` and generated
  arrays/templates to `outputs/generated/`.
- Corrected the macaque bar-plot cell's `plt.show(fig)` to `plt.show()` after
  validation exposed an incompatible positional argument in the plotting backend.
- Added `repo_paths.py` for portable local input defaults and environment-variable
  overrides. Replaced personal absolute GC data paths in the notebook and
  `real_data_utils.py`. Added the explicit IPython `display` import required by
  that helper module.
- Added SciPy, tqdm, joblib, JupyterLab, ipykernel, and multiprocess to
  `environment.yml` to match imports used by the notebooks.
- Removed seven Finder `.DS_Store` files from Git tracking, while preserving
  their local files; ignored them, `outputs/`, and local `.pickle` files.
- Rewrote the README with publication status, version-specific mappings,
  repository layout, coordination-test explanation, and reproducibility links.
  Removed the stale reference to a nonexistent `Data for Figure Generation.zip`
  and the unsupported claim that all figures reproduce from the checkout alone.

`utils.py` and all scientific numerical settings were preserved. Missing legacy
helpers were documented, not replaced with a different scientific pipeline.
No raw recordings or existing ignored research artifacts were moved or deleted.
Six existing local generated arrays/template caches were also copied into the
ignored `outputs/generated/` directory so their new paths work locally; the
original root-level copies were retained.

## References used for the mapping

- `Version_3_submitted.pdf`: primary reference (37 pages), especially Sections
  2.3.3, 4.2.1-4.2.2, 4.3.1-4.3.6 and Figures 3-9.
- `Cagatay_CV.pdf`: October 2026 publication entry states acceptance in SIAM
  Journal on Life Sciences, to appear. The README dates the status to October
  30, 2026 and does not claim journal publication.
- [arXiv:2512.08637v1](https://arxiv.org/abs/2512.08637v1): used only to
  distinguish removed/renumbered figures and the older LOOCV analyses.

These reference PDFs were read locally and are not redistributed in the branch.
The personal CV's other contents are not included.

## Validation and remaining limits

See [VALIDATION.md](VALIDATION.md) for the completed checks. Scientific algorithms
were not changed to force outputs to agree with a manuscript. Full expensive
parameter sweeps, sampling convergence, and legacy analyses were not claimed as
recomputed. All changes are local; no remote update or branch merge is part of
this cleanup.


Reference file SHA-256 values (file identity only):

- `Version_3_submitted.pdf`: `b079b8e77abf4f66b282ecbd2b77e6d345337348eb13341fe536ac3751c6a54f`
- `Cagatay_CV.pdf`: `068d61b000e939e78d4a478534c9fdbf37513afadd43a71fbb98e45a5f157e1b`
