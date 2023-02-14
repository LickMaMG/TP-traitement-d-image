import numpy as np
import cv2
import matplotlib.pyplot as plt
# from matplotlib import animation
import os

liste_file = [name for name in os.listdir(
    'appr') if name.split('.')[-1] == 'png']
liste_img = [cv2.imread('appr'+'/' + file) for file in liste_file]

ref_img = ['reference'+'/' +
           name for name in os.listdir('reference') if name.split('.')[-1] == 'bmp']
ref_img = [cv2.imread(file) for file in ref_img]


liste_txt = [
    'appr'+'/' + name for name in os.listdir('appr') if name.split('.')[-1] == 'txt']


liste_classes = []
for txt in liste_txt:
    with open(txt, 'r') as f:
        liste_classes.append(f.readline())


figure, axes = plt.subplots(1, 2)
figure.suptitle('Visialisation de continue des images')
figure.set_size_inches(8, 6)
axes = axes.flatten()

h1 = axes[0].imshow(liste_img[0])
axes[0].set_title(f"fichier {liste_file[0]}", fontsize=12)
axes[1].set_title(f"image noir et blanc de reference", fontsize=12)
h2 = axes[1].imshow(liste_img[0])


for i in range(len(liste_img)):
    h1.set_data(liste_img[i])
    axes[0].set_title(
        f"fichier {liste_file[i]}, classe {liste_classes[i]}", fontsize=12)
    h2.set_data(ref_img[int(liste_classes[i])-1])

    plt.pause(0.01)
