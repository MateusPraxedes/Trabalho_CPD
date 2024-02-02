import pandas as pd
import pickle
from pathlib import Path
import csv 
import os

caminho_arquivos = os.path.join(os.environ['USERPROFILE'],'Desktop')

# Testa se já existe um arquivo com os dados em binário, caso não exista lê o arquivo csv original e escreve esses dados 
def le_dados():
    caminho_projeto = Path()    
    path_dados_bin =  Path(f"{caminho_projeto.absolute()}\\bin\\steam_data_bin.bin")
        
    if not path_dados_bin.is_file():
        dados = []
        with open(f"{caminho_arquivos}\\csv\\steam_data.csv",'r',encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            headers = next(reader)
            print(headers)
            '''
                row[0] - url
                row[1] - nome
                row[2] - categoria
                row[3] - url_img
                row[4] - user reviews
                row[5] - all_reviews
                row[6] - data
                row[7] - desenvolvedora
                row[8] - distribuidora
                row[9] - preco
                row[10] - pegi
                row[11] - pegi_url
            '''
            for row in reader:    
                if row[1] != '-':
                    dados.append(row)
        
        # Escreve os dados em um arquivo binário
        with open(path_dados_bin, 'ab') as arquivo_binario:   # Abre o arquivo binário para escrita
            for dado in dados:
                arquivo_binario.write(bytes(str(dado),'utf-8'))
                arquivo_binario.write('b\n')
                
        print("Dados gravados com sucesso no arquivo binário.")

        
    
    # Ler os dados do arquivo binário
    with open(path_dados_bin, 'rb') as arquivo_binario:   # Abre o arquivo binário para leitura
        dados_bin = arquivo_binario.read()
        
        dados = dados_bin.split(b'\n')
        
        print(dados_bin)
        for dados in dados_bin:
            print(dados.decode('utf-8'))
            
        jogos_lidos = len(dados_bin)
    
   
    return jogos_lidos
    
