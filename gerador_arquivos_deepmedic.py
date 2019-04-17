from os.path import dirname, realpath
import os
import re
from sklearn.model_selection import train_test_split
import nibabel as nib

#O que esse programa faz:

       #Cria(ou adiciona novos valores neles se já os mesmos já existirem) os  arquivos testChannels_t1c.cfg, testGtLabels.cfg , validationGtLabels.cfg ,validationChannels_t1c ,trainChannels_t1c.cfg
       # trainGtLabels.

       #Pra isso, usa extensão Nibabel para 
       #      a) criar a 'label' a partir das lesoes do individuo(='unificar' as lesoes em uma unica imagem)
       #      b)normalizar a label de modo que ela só tenha 2 classes.[0=não é lesão ou 1=é lesão]

       #Futuro: separar funcionalidades

def junta_e_mudaClasse(lista,folder_path):
       #Objetivo: normalizar e unificar imagens de lesão de um sujeito.
       #Entrada: lista de nomes das imagens de lesão de um determinado sujeito, caminho para pasta do sujeito
       #Saída: Nada.
       
       a=nib.load(lista[0])  #carrega imagem
       lesao = a.get_data()
       lesao[lesao > 0] = 1 #normaliza
       print(folder_path)   #desnecessario, porém é util para ver está funcionando corretamente

       for i in lista[1:]: 
              a=nib.load(i)
              lesao1 = a.get_data()
              lesao1[lesao1 > 0] = 1
              lesao=lesao+lesao1 #unifica as imagens
       
       lesao[lesao > 0] = 1 #normaliza o resultado, útil pois pode haver sopbreposição de lesões, gerando uma nova classe de valor maior que 1 
       added_lesions = nib.Nifti1Image(lesao, a.affine, a.header) #efetivamente gera a imagem unificada
       path = str(folder_path)+"\\lesao.nii.gz"
       nib.save(added_lesions,path) #salva na pasta especificada




pasta_atual = realpath(__file__) #retorna pasta atual. Esse programa foi feito para estar dentro da pasta train(seguindo o modelo do deepmedic).

um_nivel_acima = dirname(pasta_atual)
dois_niveis_acima = dirname(um_nivel_acima)
quatro_niveis= dirname(dirname(dois_niveis_acima)) #pasta example
X=[] #amostras
y=[] #labels 

atlas=quatro_niveis+'\dataForExamples\ATLAS_R1.1'
total_de_pacientes=0


for pasta in os.listdir(atlas):
        for subpasta in os.listdir(atlas+"\\"+pasta):
              
              for sub_subpasta in os.listdir(atlas+"\\"+pasta+"\\"+subpasta): 
                     lista=[]
                     sub_subpasta_path = str(atlas+"\\"+pasta+"\\"+subpasta+"\\"+sub_subpasta)

                     for arquivo in os.listdir(atlas+"\\"+pasta+"\\"+subpasta+"\\"+sub_subpasta): #para cada arquivo em t01 ou t02 do sujeito:
                            
                            if '_t1w_deface_stx.nii.gz' in arquivo:
                                   total_de_pacientes=total_de_pacientes+1
                                   arquivo_path = sub_subpasta_path+"\\"+arquivo
                                   X.append([arquivo_path])

                            elif('_LesionSmooth_' in arquivo):
                                   
                                   lista.append(sub_subpasta_path+"\\"+arquivo)

                     junta_e_mudaClasse(lista,str(sub_subpasta_path))
                     arquivo_path = sub_subpasta_path+"\\"+'lesao.nii.gz' 
                     y.append(arquivo_path)            
                              

                        
print("total de pacientes:"+str(total_de_pacientes)) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)        #separa dados em teste e treino
X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=0.2, random_state=42) #separa dados em treino e validação

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
       f = open("../test/testChannels_t1c.cfg", "a")
       f.write(X_test[i][0]+"\n")
       f.close()
       g = open('../test/testGtLabels.cfg','a')
       g.write(y_test[i]+"\n")
       g.close()


       


# print("Train: "+str(len(X_validation))+"  "+str(len(y_validation)))
# #for i in range(len(X_train)-1):
# print(X_validation[36],y_validation[36])









