from os.path import dirname, realpath
import os
import re
import nibabel as nib

def junta_e_mudaClasse(lista,folder_path):
       a=nib.load(lista[0])  #carrega imagem
       lesao = a.get_data()
       lesao[lesao > 0] = 1 #normaliza
       #print(folder_path)  

       for i in lista[1:]: 
              a=nib.load(i)
              lesao1 = a.get_data()
              lesao1[lesao1 > 0] = 1
              lesao=lesao+lesao1 #unifica as imagens
       
       lesao[lesao > 0] = 1
       added_lesions = nib.Nifti1Image(lesao, a.affine, a.header) #efetivamente gera a imagem unificada
       path = folder_path+"/unified_lesion.nii.gz"
       print(path)
       nib.save(added_lesions,path) #salva na pasta especificada




pasta_atual = realpath(__file__)
atlas = dirname(pasta_atual)

contador=0

for site in os.listdir(atlas):
       if 'Site' in site:
              for paciente in os.listdir(atlas+"/"+site):
                     for t in os.listdir(atlas+"/"+site+"/"+paciente):
                            lista=[]
                            folder_path= atlas+"/"+site+"/"+paciente+"/"+t

                            for t1 in os.listdir(atlas+"/"+site+"/"+paciente+"/"+t):
                                   print('got here')
                                   if '_LesionSmooth_' in t1:
                                          path= atlas+"/"+site+"/"+paciente+"/"+t+"/"+t1
                                          lista.append(path)
                                          contador=contador+1
                                          #print(path)
                            
                            junta_e_mudaClasse(lista,folder_path)        

print(contador)


