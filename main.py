
from pathlib import Path
import json
import mne

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read the raw and cov file
data_file_raw = config.pop('raw')
data_file_cov = config.pop('cov')

# crop() the Raw data to save memory:
raw = mne.io.read_raw_fif(data_file_raw, verbose=False).crop(tmax=60)

cov = mne.read_cov(data_file_cov)
report = mne.Report(title='Covariance example')
report.add_covariance(cov=data_file_cov, info=data_file_raw, title='Covariance')


report.save('out_dir_report/report_cov.html', overwrite=True)





