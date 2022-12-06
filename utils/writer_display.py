import matplotlib.pyplot as plt
from utils import utils_image as util
import torchvision.transforms as transforms
import cv2
import numpy as np

# def plot_to_image(figure):
#     """Converts the matplotlib plot specified by 'figure' to a PNG image and
#     returns it. The supplied figure is closed and inaccessible after this call."""
#     # Save the plot to a PNG in memory.
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     # Closing the figure prevents it from being displayed directly inside
#     # the notebook.
#     plt.close(figure)
#     buf.seek(0)
#     # Convert PNG buffer to TF image
#     image = tf.image.decode_png(buf.getvalue(), channels=4)
#     # Add the batch dimension
#     image = tf.expand_dims(image, 0)
#     return image

def image_grid(imgE, imgH, imgL, scale):
    """Return a 1x3 grid of the MNIST images as a matplotlib figure."""
    # Nearest neigbor interpolation on imgL
    transform = transforms.CenterCrop(128)
    transformL = transforms.CenterCrop(128/scale)
    imgE = util.tensor2uint(transform(imgE))
    imgH = util.tensor2uint(transform(imgH))
    imgL = util.tensor2uint(transformL(imgL))
    imgL = cv2.resize(imgL, dsize=(100, 100), fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
    # Create a figure to contain the plot.
    figure = plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imgL, cmap=plt.cm.binary)
    plt.subplot(1, 3, 2)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imgE, cmap=plt.cm.binary)
    plt.subplot(1, 3, 3)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imgH, cmap=plt.cm.binary)

    return figure