import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
from PIL import Image

def reducer(img, quality, loc):
    y = img[:,:,0].copy()
    q = quality/100
    pc = PCA(q)
    img_reduced = pc.fit_transform(y)
    img_inv_reduced = pc.inverse_transform(img_reduced)
    plt.imsave(loc,img_inv_reduced)