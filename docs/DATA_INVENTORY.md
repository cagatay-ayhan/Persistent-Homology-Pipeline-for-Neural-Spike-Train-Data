# CSV inventory

All 116 pre-existing tracked scientific CSVs were relocated without changing
their bytes. The exact mapping is in [FILE_MOVES.csv](FILE_MOVES.csv). This count
excludes documentation manifests introduced during cleanup.

| Location | Files | Interpretation |
| --- | --- | --- |
| `data/metadata/` | `pairs.csv`, `MDT_to_number_of_trials.csv` | Fixed order of 38 mouse/date sessions; 114 mouse/date/taste trial counts. |
| `results/stability/` | `q_values_results.csv` | Long-format GC parameter sweep: 15,238 rows, 38 sessions, 401 q values per session from 0 to 2. Figure 4A. |
| `results/stability/` | `stability_results.csv` | 19 sample sizes; repetition count `M`, empirical Wasserstein mean `W_mean`, standard deviation `W_std`. Figure 4B. |
| `results/synthetic/` | `results_summary_degree_1_homology.csv` | Three method/accuracy rows: SVM, TDA H0, TDA H1. Figure 6D. |
| `results/synthetic/` | `hybrid_experiment_results_100_neurons.csv` | TDA/SVM accuracy by mixed-coding population proportions, using the 100 neurons of Section 4.3.3 / Figure 7. |
| `results/gustatory_cortex/` | `tda_svm_scores_2class.csv`, `tda_svm_scores_3class.csv` | 38 session rows with per-method means and 20 split scores; main Figure 8 plotting tables. |
| `results/gustatory_cortex/` | `tda_scores_rhv_2class.csv`, `tda_scores_rhv_3class.csv` | Compact per-session TDA scores used by earlier plotting cells. |
| `results/gustatory_cortex/` | `SVM_smoothed_rhv_2class.csv`, `SVM_smoothed_rhv_3class.csv` | Compact SVM summaries used by earlier plotting cells. |
| `results/gustatory_cortex/` | `individual_neuron_scores.csv` | Per-session neuron scores and their average. Blank padded columns reflect differing neuron counts. |
| `results/gustatory_cortex/` | `permutation_invariance_scores.csv` | Normal/shuffled TDA and SVM means/standard deviations. Figure 8C. |
| `results/coordination_test/` | 97 CSVs under five `results_<session>/` folders | 45 stimulus summaries, 45 split tables, five all-stimuli summaries, and two historical single-stimulus files. Figure 9. |
| `results/supplementary/` | `hybrid_experiment_results.csv` | 1000-neuron mixed-coding results; notebook explicitly identifies these as outside the manuscript's 100-neuron experiment. |
| `results/supplementary/` | `h1_dataset_q_values_results.csv`, `synthetic_exp1_q_values_results.csv`, `synthetic_hybrid_coding_q_values_results.csv` | Extra synthetic q sweeps. No generator/consumer was identified among the current tracked notebooks; retained without assigning a submitted figure. |
| `results/supplementary/` | `tda_scores_rhv_3class_with_varying_k.csv` | 380 rows of additional GC scores varying `k`. No generator/consumer was identified among current tracked notebooks; no paper panel assignment is asserted. |

## Coordination-test schema

The former `Results_Coordination_test` directory stored outputs of genuine versus
trial-shuffled classification in macaque V1/V2. It did not store coordinates.

- `<session>_stimulus_<0-8>_split_results.csv`: 20 split-level rows, with TDA
  accuracy, linear/RBF SVM train/test accuracy, and genuine/shuffled sample counts.
- `<session>_stimulus_<0-8>_summary.csv`: one summary row with mean and sample
  standard deviation across splits, completed split count, and chance accuracy.
- `<session>_all_stimuli_summary.csv`: nine stimulus rows for the session. The
  submitted Figure 9 aggregation reads these files.
- `results_106r002p70/classification_split_results.csv` and
  `classification_summary.csv`: retained historical single-stimulus files. Their
  exact relationship to the final computation is not inferred from their names;
  the Figure 9 aggregation does not select them.

Sessions, in the notebook's display order, are `105l001p16`, `106r001p26`,
`106r002p70`, `107l002p67`, and `107l003p143`.

## Local files outside Git

`Datasets/` contains the local GC pickle data, Bayesian single-neuron score table,
and the CRCNS archive/extracted files. They were kept in place and were not added
to the branch. Existing ignored root-level arrays, pickle templates, PDFs,
bytecode, and older PDFs under `Results_Coordination_test/` were also retained in
place. Six pre-existing generated arrays/template caches were copied into
`outputs/generated/` while preserving their original root-level copies. New
exports are directed to `outputs/`, so the tracked repository has a
clear structure without deleting local research artifacts.

Finder `.DS_Store` files were removed from Git tracking and are now ignored;
their local files were preserved. No uploaded manuscript or personal CV was added
to the repository.
