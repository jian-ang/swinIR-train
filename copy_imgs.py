import cv2
import os
from tqdm import trange

root = '/home/angj/thesis/swinIR-train/testsets/WIN'
size = 100
# for i in trange(1, size + 1):
#     fromPath = os.path.join(root, 'test-HR', f'{i:04}.jpg')
#     toPath = os.path.join(root, 'test-HR-100', f'{i:04}.jpg')
#     img = cv2.imread(fromPath)
#     cv2.imwrite(toPath, img)

for i in trange(1, size + 1):
    fromPath = os.path.join(root, 'test-LRx8', f'{i:04}.jpg')
    toPath = os.path.join(root, 'test-LRx8-100', f'{i:04}.jpg')
    img = cv2.imread(fromPath)
    cv2.imwrite(toPath, img)

# root = '/home/angj/thesis/swinIR-train/trainsets/WIN'
# for i in trange(1, 24):
#     fromPath = os.path.join(root, 'train-HR', f'{i:04}.jpg')
#     toPath = os.path.join(root, 'train-test-HR', f'{i:04}.jpg')
#     img = cv2.imread(fromPath)
#     cv2.imwrite(toPath, img)

# root = '/home/angj/thesis/swinIR-train/trainsets/WIN'
# for i in trange(1, 24):
#     fromPath = os.path.join(root, 'train-LR', f'{i:04}.jpg')
#     toPath = os.path.join(root, 'train-test-LR', f'{i:04}.jpg')
#     img = cv2.imread(fromPath)
#     cv2.imwrite(toPath, img)