import pandas as pd
import pickle
from pathlib import Path

# Testa se já existe um arquivo com os dados em binário, caso não exista lê o arquivo csv original e escreve esses dados 
def le_dados():
    
    caminho_projeto = Path() 
    print(caminho_projeto)
    
    path_dados_bin =  Path('C:\\Users\\verti\\Desktop\\GitHub\\Trabalho_CPD\\bin\\steam_data_bin.bin')
   
    if path_dados_bin.is_dir():
        # Ler os dados do arquivo binário
        with open('C:\\Users\\verti\\Desktop\\GitHub\\Trabalho_CPD\\bin\\steam_data_bin.bin', 'rb') as arquivo_binario:   # Abre o arquivo binário para leitura
            dados = []
            while True:
                try:
                    dicionario = pickle.load(arquivo_binario)
                    dados.append(dicionario)
                except EOFError:
                    break
    else:
        df = pd.read_csv('C:\\Users\\verti\\Desktop\\GitHub\\Trabalho_CPD\\csv\\steam_data.csv')  # Le o aquivo original CSV

        with open('C:\\Users\\verti\\Desktop\\GitHub\\Trabalho_CPD\\bin\\steam_data_bin.bin', 'wb') as arquivo_binario:  # Cria um arquivo para salvar os dados em binário
            for linha in df.iterrows():
                dicionario = linha[1].to_dict()
                
                # Gravar o dicionário no arquivo binário
                pickle.dump(dicionario, arquivo_binario)
            
        print("Dados gravados com sucesso no arquivo binário.")
