
from pathlib import Path
import json
import mne
#to fix
#qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read the raw and cov file
data_file_raw = config.pop('fif')
#data_file_cov = config.pop('cov')



# crop() the Raw data to save memory:
raw = mne.io.read_raw_fif(data_file_raw, verbose=False).crop(tmax=60)

noise_cov = mne.compute_raw_covariance(raw, tmin=0, tmax=None)

#cov = mne.read_cov(data_file_cov)
report = mne.Report(title='Covariance example')
#report.add_covariance(cov=data_file_cov, info=data_file_raw, title='Covariance')
report.add_covariance(noise_cov, info=data_file_raw, title='Covariance')


report.save('out_dir_report/report_cov.html', overwrite=True)





