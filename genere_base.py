import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import random as rd
from skimage import transform
from matplotlib.transforms import Affine2D


def genere_base(N=100):
    reference = 'reference'
    base = 'appr'
    type_image_ref = 'bmp'
    type_image_base = 'png'

    sigma = 0.05
    DeltaX, DeltaY = 22, 22

    NX, NY = 10, 10

    liste = os.listdir(reference)
    Nfile = len(liste)

    for n in range(N):
        classe = rd.randint(0, Nfile-1)
        nom = liste[classe]
        img = cv2.imread(reference+'/'+nom)
        L, C = img.shape[:2]
        rota = np.pi*rd.random()
        ech = 0.4+0.6*rd.random()
        R = np.vstack(([np.cos(rota), -np.sin(rota)],
                      [np.sin(rota), np.cos(rota)]))
        M = ech*R
        U0 = np.array([C/2, L/2])
        X0 = np.array([C/2, L/2])
        TR = X0-np.dot(M, U0)
        A = np.vstack((M, TR))

        # T = Affine2D()
        # T.translate(U0)
        # T.rotate(rota)
        # print(A.shape)
        plt.imshow(img)
        plt.show()


genere_base(N=1)
