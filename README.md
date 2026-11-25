<h1 align="center">app- covariance</h1>

<p align="center">
  Computes a noise covariance matrix from the first 60 seconds of a raw MEG FIF recording with MNE-Python compute_raw_covariance and saves it with an HTML report.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.625"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.625-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes a noise covariance matrix from the first 60 seconds of a raw MEG FIF recording with MNE-Python compute_raw_covariance and saves it with an HTML report.**

Reads the raw FIF file, crops it to 60 s, computes the covariance with mne.compute_raw_covariance and writes cov.fif and an MNE report. Use it for a noise covariance for source estimation, ideally on empty-room or baseline data. The registered branch master does not exist on GitHub; this description is based on the main branch.

| | |
|---|---|
| **Inputs** | `neuro/meg/fif` |
| **Outputs** | `neuro/meeg/mne/covariance` · `report/html` |
| **Container** | `brainlife/mne:1.0.2` |
| **Resources** | 8 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.625](https://doi.org/10.25663/brainlife.app.625) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `fif` | `neuro/meg/fif` | yes | Raw MEG recording (FIF). |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/covariance` | Noise covariance matrix (cov.fif). |
| `out_dir_report` | `report/html` | HTML report showing the covariance. |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.625](https://doi.org/10.25663/brainlife.app.625), choose `neuro/meg/fif` from your project and press **Execute**. The results are saved to your project as `neuro/meeg/mne/covariance`, `report/html`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:1.0.2`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "fif": "/path/to/fif/fif"
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- app- covariance. brainlife.io App. [doi:10.25663/brainlife.app.625](https://doi.org/10.25663/brainlife.app.625)
- Gramfort et al. MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience* 7 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

Maintained by [@zahransa](https://github.com/zahransa).
