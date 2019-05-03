from os.path import dirname, realpath
import os
import numpy as np
import re
#from sklearn.model_selection import train_test_split
import nibabel as nib


pasta_atual = realpath(__file__)
atlas = dirname(pasta_atual)

contador=0
for site in os.listdir(atlas):
       if 'Site' in site:
              for paciente in os.listdir(atlas+"/"+site):
                     for t in os.listdir(atlas+"/"+site+"/"+paciente):
                            for t1 in os.listdir(atlas+"/"+site+"/"+paciente+"/"+t):
                                    if 'b' in t1[0]:
                                          path= atlas+"/"+site+"/"+paciente+"/"+t+"/"+t1
                                          print(path)
                                          out_path = atlas+"/"+site+"/"+paciente+"/"+t+"/"+"norm_"+t1
                                          #print(out_path)                                          
                                          img = nib.load(path)
                                          data = img.get_fdata()
                                          mean = np.mean(data[data > 0])
                                          std = np.std(data[data > 0])
                                          data[data > 0] = (data[data > 0] - mean) / std
                                          normalized_img = nib.Nifti1Image(data, img.affine, img.header)
                                          nib.save(normalized_img,out_path)
                                          contador=contador+1

print(contador)
