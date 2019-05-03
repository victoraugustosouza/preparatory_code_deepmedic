from os.path import dirname, realpath
import os
import re
#from sklearn.model_selection import train_test_split
import nibabel as nib


pasta_atual = realpath(__file__) #retorna pasta atual. Esse programa foi feito para estar dentro da pasta train(seguindo o modelo do deepmedic).

atlas = dirname(pasta_atual)

contador=0
for site in os.listdir(atlas):
       if 'Site' in site:
              for paciente in os.listdir(atlas+"/"+site):
                     for t in os.listdir(atlas+"/"+site+"/"+paciente):
                            for t1 in os.listdir(atlas+"/"+site+"/"+paciente+"/"+t):
                                    if 'bet_' in t1:
                                          print(atlas+"/"+site+"/"+paciente+"/"+t+"/"+t1)
                                          path= atlas+"/"+site+"/"+paciente+"/"+t+"/"+t1
                                          out_path = atlas+"/"+site+"/"+paciente+"/"+t+"/"+"mask_"+t1
                                          os.system('fslmaths %s -bin %s' % (path, out_path))                                          
                                          contador=contador+1
                                          

print(contador)
