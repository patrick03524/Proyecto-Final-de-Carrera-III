# -*- coding: utf-8 -*-
"""Replica Modelo Difusion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JB4oPLVADhCk66zeV6RsoUw_p6h_qY25
"""

# Replica del Modelo de Difusión "*Palette: Image-to-Image Diffusion Models*"
## Alumno: Patrick Xavier Marquez Choque
## Curso: Proyecto Final de Carrera III
## Periodo: 2024-I

######
#@title 1. Configuración del Entorno del Modelo de Difusión
######

!nvidia-smi --query-gpu=gpu_name,driver_version,memory.total --format=csv

# Commented out IPython magic to ensure Python compatibility.
######
#@title 2. Clonar Repositorio
######

# %cd /content/
!git clone https://github.com/Janspiry/Palette-Image-to-Image-Diffusion-Models

# Commented out IPython magic to ensure Python compatibility.
######
#@title 3. Preparar el Modelo Pre-entrenado
######

#https://drive.google.com/file/d/1UYSFscugYN8msv7dQjIliWdQbd29h0HR/view?usp=sharing
#https://drive.google.com/file/d/1-X9jx3AzMdJg4lfIrWGoysTYZ1oN0OcK/view?usp=sharing

# %cd /content/Palette-Image-to-Image-Diffusion-Models/
!gdown --id 1-X9jx3AzMdJg4lfIrWGoysTYZ1oN0OcK

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/Palette-Image-to-Image-Diffusion-Models/config/

# Commented out IPython magic to ensure Python compatibility.
# ######
# #@title 4. Ingreso de los Hiper-parámetros del Modelo
# ######
# 
# %%writefile inpainting_celebahq.patch
# --- a/config/inpainting_celebahq.json
# +++ b/config/inpainting_celebahq.json
# @@ -10,7 +10,7 @@
#          "tb_logger": "tb_logger", // path of tensorboard logger
#          "results": "results",
#          "checkpoint": "checkpoint",
# -        "resume_state": "experiments/train_inpainting_celebahq_220426_233652/checkpoint/190"
# +        "resume_state": "200"
#          // "resume_state": null // ex: 100, loading .state  and .pth from given epoch and iteration
#      },
# 
# @@ -48,7 +48,7 @@
#              "which_dataset": {
#                  "name": "InpaintDataset", // import Dataset() class / function(not recommend) from default file
#                  "args":{
# -                    "data_root": "datasets/celebahq/flist/test.flist",
# +                    "data_root": "input",
#                      "mask_config": {
#                          "mask_mode": "center"
#                      }
# @@ -56,8 +56,8 @@
#              },
#              "dataloader":{
#                  "args":{
# -                    "batch_size": 8,
# -                    "num_workers": 4,
# +                    "batch_size": 1,
# +                    "num_workers": 1,
#                      "pin_memory": true
#                  }
#              }
# --

######
#@title 5. Parcheando el Modelo
######

!apt-get install dos2unix
!dos2unix inpainting_celebahq.json
!patch < inpainting_celebahq.patch

# Commented out IPython magic to ensure Python compatibility.
######
#@title 6. Subir imagen para el experimento
######

# %cd /content/Palette-Image-to-Image-Diffusion-Models/
!mkdir -p input
# %cd /content/Palette-Image-to-Image-Diffusion-Models/input/
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  savefile = open(fn, 'wb')
  savefile.write(uploaded[fn])
  print('Successfully uploaded "{}" ({} bytes).'.format(fn, len(uploaded[fn])))
  savefile.close()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

for fn in uploaded.keys():
  img = mpimg.imread(fn)
  plt.imshow(img)
  plt.axis('off')
  plt.show()

# Commented out IPython magic to ensure Python compatibility.
######
#@title 6. Subir imagen para el experimento
######

# %cd /content/Palette-Image-to-Image-Diffusion-Models/
!python run.py -c config/inpainting_celebahq.json -p test