files=open("train.txt").readlines()
trainFiles=files
from tqdm.auto import tqdm
from shutil import copyfile
import os
os.makedirs('windows-train-dataset', exist_ok=True)
for i, f in enumerate(tqdm(trainFiles), start=1):
    copyfile(f.strip(), os.path.join('/home/angj/data/windows-train-dataset', f'{i:04}.jpg'))