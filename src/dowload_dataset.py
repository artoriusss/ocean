import gdown
import zipfile
import os

from utils.paths import DATA_DIR

URL = 'https://drive.google.com/uc?id=1UfYJzidIIMBt7aag-XuabmAEHddvO7Ut'

output_zip_path = 'parquet.zip'
print(f'Fetching dataset from {URL}...')
gdown.download(URL, output_zip_path, quiet=False)

os.makedirs(DATA_DIR, exist_ok=True)

with zipfile.ZipFile(output_zip_path, 'r') as zip_ref:
    zip_ref.extractall(DATA_DIR)

os.remove(output_zip_path)

print(f'Dataset downloaded and extracted to {DATA_DIR}')