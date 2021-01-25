import pickle
import matplotlib.pyplot as plt
import os
from os import listdir
from os.path import isfile, join

#Lista todos os arquivos do diretorio (sem contar as pastas)
mypath = os.getcwd()
mypath = os.path.join(mypath, 'Results')
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in range(len(onlyfiles)):
    print("******************************* " + onlyfiles[f] + "*********************************************")
    fileName = mypath + '/' + onlyfiles[f]

    # open a file, where you stored the pickled data
    file = open(fileName, 'rb')

    # dump information to that file
    data = pickle.load(file)

    # close the file
    file.close()

    #Todos os parametros salvos no arquivo
    #cnt = 0
    #for item in data:
        #print('The data ', cnt, ' is : ', item)
        #cnt += 1

    #Parametros variados em cada experimento
    params_variados = ['n_steps', 'batch_size', 'n_epochs', 'learning_rate', 'total_timesteps']

    #Dados coletados no experimento
    data_colected = ['time', 'win', 'loss', 'mean', 'std', 'rewards']

    #Imprime somente os parametros desejados de acordo com a variação do experimento
    for i in range(len(params_variados)):
        print(params_variados[i], ': ', data[params_variados[i]])

    for i in range(len(data_colected)-1):#para nao imprimir o array de rewards
        print(data_colected[i], ': ', data[data_colected[i]])

    #plota grafico de reward (deve sempre ser o ultimo parametro)
    plt.plot(data[data_colected[len(data_colected)-1]])
    plt.ylabel('Reward')
    plt.xlabel('Game')
    plt.title('Game x Reward')
    plt.savefig(fileName.strip(".pkl")+'.png', format='png')
    plt.show()


