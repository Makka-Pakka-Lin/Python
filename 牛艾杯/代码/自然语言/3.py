from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sn

im = misc.imread("c:\1.jpg",flatten=True)

flt = np.array([[-1,0,1],
                [-2,0,2],
                [-1,0,1]])
grad = signal.convolve2d(im,
                         flt,
                         boundary="symm",
                         mode="same").astype("int32")

plt.figure("Conv2D")
plt.subplot(121)
plt.imshow(im,cmap="gray")
plt.xticks([])
plt.yticks([])


plt.subplot(122)
plt.imshow(grad,cmap="gray")
plt.xticks([])
plt.yticks([])

plt.show()