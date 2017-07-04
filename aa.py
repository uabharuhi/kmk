import data
import numpy as np
from PIL import Image
im = Image.open('./0')
print(im.size)
a = np.asarray(im, dtype=np.uint8)
print(a[:,:,0])
print(a.shape)

Image.fromarray(a, mode=None).show()
