# -*- coding: utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt
import descfour as df

# lecture du fichier image et visualisation
img = cv2.imread('appr\mesure008.png', 0)

plt.figure(), plt.imshow(img, cmap='gray', vmin=0, vmax=255)

# binarisation avec seuillage
_, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.figure(), plt.imshow(img_bin, cmap='gray')

# extraction du contour
contoursliste, _ = \
    cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# visualisation du contour (on suppose qu'il n'y en a qu'un)
img_cont = np.zeros(img.shape, dtype=np.uint8)
cv2.drawContours(img_cont, [contoursliste[0]], 0, 255, 1)
plt.figure(), plt.imshow(img_cont, cmap='gray')

# construction de la suite de nombres complexes décrivant le contour
contour = np.squeeze(contoursliste[0], axis=1)
z = contour[:, 0]+1j*contour[:, 1]

# test de la fonction dfdir et visualisation des coefficients
cmax = 10
coeff = df.dfdir(z, cmax)
plt.figure(), plt.plot(np.arange(-cmax, cmax+1, dtype=int), np.abs(coeff))

# test de la fonction dfinv
N = 500
z_f = df.dfinv(coeff, N)

# visualisation du contour initial et du contour reconstruit
plt.figure(), plt.plot(np.real(z), np.imag(z)), plt.axis(
    'equal'), plt.gca().invert_yaxis()
plt.figure(), plt.plot(np.real(z_f), np.imag(z_f)), plt.axis(
    'equal'), plt.gca().invert_yaxis()

plt.show()
