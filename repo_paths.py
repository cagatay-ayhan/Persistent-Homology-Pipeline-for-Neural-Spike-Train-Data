"""Shared file locations; optional overrides are read when the module is imported."""
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

def _path(variable, default):
    return Path(os.environ.get(variable, str(default))).expanduser().resolve()

GC_NEURON_DF = _path("SPIKE_TRAIN_NEURON_DF", REPO_ROOT / "Datasets/NeuronDF.pickle")
GC_SINGLE_NEURON_SCORES = _path("SPIKE_TRAIN_SINGLE_NEURON_SCORES", REPO_ROOT / "Datasets/gctemp_sna_withMDpair_info.csv")
CRCNS_ARCHIVE = _path("SPIKE_TRAIN_CRCNS_ARCHIVE", REPO_ROOT / "Datasets/CRCNS/v1-v2_gratings.zip")
LEGACY_DATA_DIR = _path("SPIKE_TRAIN_LEGACY_DATA", REPO_ROOT / "Datasets/legacy_arxiv")
LEGACY_CODE_DIR = _path("SPIKE_TRAIN_LEGACY_CODE", REPO_ROOT) if os.environ.get("SPIKE_TRAIN_LEGACY_CODE") else None
GENERATED_DATA_DIR = REPO_ROOT / "outputs/generated"
