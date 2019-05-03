
from os.path import dirname, realpath
import os
import re
from sklearn.model_selection import train_test_split
import nibabel as nib




X=[] #amostras
y=[] #labels 
contador=0
pasta_atual = realpath(__file__)
atlas = dirname(pasta_atual)


for site in os.listdir(atlas):
       if 'Site' in site:
              for paciente in os.listdir(atlas+"/"+site):
                     for t in os.listdir(atlas+"/"+site+"/"+paciente):
                            lista=[]
                            folder_path= atlas+"/"+site+"/"+paciente+"/"+t

                            for t1 in os.listdir(atlas+"/"+site+"/"+paciente+"/"+t):
                                path= atlas+"/"+site+"/"+paciente+"/"+t+"/"+t1   
                                if 'b' in t1[0]:
                                    contador=contador+1                                    
                                    X.append([path])

                                elif('unified_lesion' in t1):                                    
                                    y.append(path)        

print("contador:"+str(contador))          
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=0.2, random_state=42)


#escreve nos arquivos
for i in range(len(X_train)):
        f = open("trainChannels_t1c.cfg", "a")
        f.write(X_train[i][0] +"\n")
        f.close()
        g = open("trainGtLabels.cfg", "a")
        g.write(y_train[i] +"\n")
        g.close()

for i in range(len(X_validation)):
       f = open("./validation/validationChannels_t1c.cfg", "a")
       f.write(X_validation[i][0]+"\n")
       f.close()
       g = open('./validation/validationGtLabels.cfg','a')
       g.write(y_validation[i]+"\n")
       g.close()

for i in range(len(X_test)):
       f = open("./test/testChannels_t1c.cfg", "a")
       f.write(X_test[i][0]+"\n")
       f.close()
       g = open('./test/testGtLabels.cfg','a')
       g.write(y_test[i]+"\n")
       g.close()
