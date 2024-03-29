import pandas as pd
import pickle
from pathlib import Path
import csv 
import os
from prettytable import PrettyTable

caminho_arquivos = os.path.join(os.environ['USERPROFILE'],'Desktop')


# Testa se já existe um arquivo com os dados em binário, caso não exista lê o arquivo csv original e escreve esses dados 
def le_dados():
    caminho_projeto = Path()    
    path_dados_bin = Path(f"{caminho_projeto.absolute()}\\bin\\steam_data_bin.bin")
    
    if not path_dados_bin.is_file():
        #Lê csv completo
        df = pd.read_csv(f"{caminho_arquivos}\\csv\\steam_data.csv")
        
        #Exclui colunas que nao seram tratadas
        df = df.drop(["all_reviews","pegi","pegi_url"],axis=1)
    
        # Exclui as linhas onde a coluna "name" é "-"
        df = df.drop(df[df['name'] == '-'].index)
        rows = df.shape[0]
        
        with open(path_dados_bin,'wb') as arquivo_bin:
            pickle.dump(df,arquivo_bin)
    
    with open(path_dados_bin,'rb') as arquivo_bin:
        arquivo_bin.seek(0)
        df = pickle.load(arquivo_bin)
        return df
    

