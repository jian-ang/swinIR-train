files=open("files.txt").readlines()
import random
random.shuffle(files)
n=len(files)
nTest=0.2*n
nTest=int(nTest)
testFiles=files[:nTest]
trainFiles=files[nTest:]
open('test.txt', 'w').writelines(testFiles)
open('train.txt', 'w').writelines(trainFiles)

from tqdm.auto import tqdm
from shutil import copyfile
import os
os.makedirs('testWindows', exist_ok=True)
for i, f in enumerate(tqdm(testFiles), start=1):
    copyfile(f.strip(), os.path.join('testWindows', f'{i:04}.jpg'))

