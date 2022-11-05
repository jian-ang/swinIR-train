import cv2
import os
import math
from tqdm import trange
# im = cv2.imread('dataset/train-HR/0001.jpg')
# dim = im.shape
# ratio = 512 / dim[0]
# print(ratio)
# downsample = cv2.resize(im, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_CUBIC)
# cv2.imwrite('0001.jpg', downsample)
root = '/home/angj/data/dataset'
factor = 2
for i in trange(1, 7143):
    fromPath = os.path.join(root, 'train-original', f'{i:04}.jpg')
    toHRPath = os.path.join(root, 'train-HR', f'{i:04}.jpg')
    toLR2Path = os.path.join(root, 'train-LRx2', f'{i:04}.jpg')
    toLR4Path = os.path.join(root, 'train-LRx4', f'{i:04}.jpg')
    toLR8Path = os.path.join(root, 'train-LRx8', f'{i:04}.jpg')
    img = cv2.imread(fromPath)
    dim = img.shape
    ratio = 128 / dim[0]
    h = int(math.floor(dim[0] * ratio))
    w = int(math.floor(dim[1] * ratio))
    hr = cv2.resize(img, dsize=(h*8, w*8), interpolation=cv2.INTER_AREA)
    lr2 = cv2.resize(img, dsize=(h*4, w*4), interpolation=cv2.INTER_AREA)
    lr4 = cv2.resize(img, dsize=(h*2, w*2), interpolation=cv2.INTER_AREA)
    lr8 = cv2.resize(img, dsize=(h, w), interpolation=cv2.INTER_AREA)
    cv2.imwrite(toHRPath, hr)
    cv2.imwrite(toLR2Path, lr2)
    cv2.imwrite(toLR4Path, lr4)
    cv2.imwrite(toLR8Path, lr8)

for i in trange(1, 1786):
    fromPath = os.path.join(root, 'test-original', f'{i:04}.jpg')
    toHRPath = os.path.join(root, 'test-HR', f'{i:04}.jpg')
    toLR2Path = os.path.join(root, 'test-LRx2', f'{i:04}.jpg')
    toLR4Path = os.path.join(root, 'test-LRx4', f'{i:04}.jpg')
    toLR8Path = os.path.join(root, 'test-LRx8', f'{i:04}.jpg')
    img = cv2.imread(fromPath)
    dim = img.shape
    ratio = 128 / dim[0]
    h = int(math.floor(dim[0] * ratio))
    w = int(math.floor(dim[1] * ratio))
    hr = cv2.resize(img, dsize=(h*8, w*8), interpolation=cv2.INTER_AREA)
    lr2 = cv2.resize(img, dsize=(h*4, w*4), interpolation=cv2.INTER_AREA)
    lr4 = cv2.resize(img, dsize=(h*2, w*2), interpolation=cv2.INTER_AREA)
    lr8 = cv2.resize(img, dsize=(h, w), interpolation=cv2.INTER_AREA)
    cv2.imwrite(toHRPath, hr)
    cv2.imwrite(toLR2Path, lr2)
    cv2.imwrite(toLR4Path, lr4)
    cv2.imwrite(toLR8Path, lr8)