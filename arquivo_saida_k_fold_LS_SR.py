# EXPERIMENTO ATLAS - Reconstrução de sinal - Métodos dos Mínimos Quadrados Sem restrição (Least Squares - LS) - Estimação da amplitude, fase ou pedestal.
# Autor: Guilherme Barroso Morett.
# Data: 08 de setembro de 2024.

# Objetivo do código: implementação da validação cruzada K-Fold para o método LS sem restrição para a estimação da amplitude, fase ou pedestal.

""" 
Organização do código:

Importação de arquivos.
Método LS sem restrição para a estimação da amplitude, fase ou pedestal: metodo_LS_SR.py

Funções presentes:

1) Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold.
Entrada: número de ocupação, número do janelamento, média do dado estatístico, variância do dado estatístico, desvio padrão do dado estatístico de interesse.
Saída: nada.

2) Instrução da validação cruzada K-Fold.
Entrada: parâmetro, número de ocupação, número e janelamento, matriz de pulsos de sinais janelada, vetor do parâmetro de referência.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação de bibliotecas.
import numpy as np
import os
from tqdm import tqdm
import time
from termcolor import colored

# Importação dos arquivos.
from metodo_LS_SR import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída pela técnica de validação cruzada K-Fold para o Método dos Mínimos Quadrados Sem Restrição (LS):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------------------------- 1) INSTRUÇÃO PARA SALVAR OS DADOS ESTATÍSTICOS DO K-FOLD PELO MÉTODO LS SEM RESTRIÇÃO ---------------------------- ###

# Definição da instrução para salvar as médias dos dados estatísticos da validação cruzada K-Fold em arquivo de saída para o método LS sem restrição.
def arquivo_saida_dados_estatisticos_k_fold_erro_LS_SR(parametro, n_ocupacao, n_janelamento, media_dado_erro, var_dado_erro, DP_dado_erro, dado):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = f"janelamento,media_{dado}_erro,var_{dado}_erro,DP_{dado}_erro\n"

    # Definição da pasta que contém o arquivo de saída.
    pasta_saida = f"K_Fold_{parametro}_{dado}_Dados_Estatisticos_LS_SR_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = f"k_fold_{parametro}_{dado}_dados_estatisticos_LS_SR_OC_{n_ocupacao}.txt"

    # Caminho completo para o arquivo de saída.
    caminho_arquivo_saida = os.path.join(pasta_saida, arquivo_saida)

    # Verifica se o arquivo existe e está vazio
    try:
        with open(caminho_arquivo_saida, 'r') as arquivo_saida_dados_estatisticos:
            primeiro_caractere = arquivo_saida_dados_estatisticos.read(1)
            if not primeiro_caractere:
                # Arquivo está vazio, escreva o título
                with open(caminho_arquivo_saida, 'a') as file:
                    file.write(titulo_arquivo_saida)
    except FileNotFoundError:
        # Se o arquivo não existe, cria e escreve o título
        with open(caminho_arquivo_saida, 'w') as file:
            file.write(titulo_arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        # Abre o arquivo de saída no modo de acrescentar (append).
        with open(caminho_arquivo_saida, "a") as arquivo_saida_dados_estatisticos:
            # Escrita dos dados de interesse.
            arquivo_saida_dados_estatisticos.write(f"{n_janelamento},{media_dado_erro},{var_dado_erro},{DP_dado_erro}\n")
    # Excessão.
    except Exception as e:
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------------------ 2) INSTRUÇÃO PARA A VALIDAÇÃO CRUZADA K-FOLD PELO MÉTODO LS SEM RESTRIÇÃO ----------------------------------- ###

# Definição da instrução da técnica de validação cruzada K-Fold para o método LS sem restrição.
def K_fold_LS_SR(parametro, n_ocupacao, n_janelamento, Matriz_Pulsos_Sinais_Janelado, vetor_parametro_referencia_janelado,):
    
    # Criação da lista vazia blocos_pulsos_sinais.
    blocos_pulsos_sinais = []

    # Criação da lista vazia blocos_parametro_referencia.
    blocos_parametro_referencia = []
    
    # Criação da variável quantidade_blocos que armazena a quantidade de blocos.
    quantidade_blocos = 100

    # Definição da quantidade de elementos de cada bloco.
    quantidade_elementos_bloco = len(Matriz_Pulsos_Sinais_Janelado) // quantidade_blocos
    
    # Para i de início em zero até a quantidade de elementos de amostras com incremento igual a quantidade_elementos_bloco.
    for i in range(0, len(Matriz_Pulsos_Sinais_Janelado), quantidade_elementos_bloco):
    
        # Definição do bloco de pulsos de sinais.
        bloco_pulsos_sinais = Matriz_Pulsos_Sinais_Janelado[i:i+quantidade_elementos_bloco]
        # O bloco dos pulsos de sinais é acrescentado a lista dos blocos dos pulsos de sinais.
        blocos_pulsos_sinais.append(bloco_pulsos_sinais)
    
        # Definição do bloco dos dados do parâmetro de referência.
        bloco_parametro_referencia = vetor_parametro_referencia_janelado[i:i+quantidade_elementos_bloco]
        # O bloco do parâmetro de referência é acrescentado a lista dos blocos dos parâmetros de referência.
        blocos_parametro_referencia.append(bloco_parametro_referencia)
    
    # Definição da lista vazia lista_bloco_media_erro_estimacao.
    lista_blocos_media_erro_estimacao = []
    
    # Definição da lista vazia lista_bloco_var_erro_estimacao.
    lista_blocos_var_erro_estimacao = []
    
    # Definição da lista vazia lista_bloco_DP_erro_estimacao.
    lista_blocos_DP_erro_estimacao = []
     
    # Para indice_bloco de zero até o tamanho da matriz de dados de entrada com incremento igual a quantidade de elementos no bloco.
    for indice_teste in range(0, len(blocos_pulsos_sinais)):
        
        # Definição do bloco_teste_pulsos_sinais como sendo aquele de índice igual ao indice_teste.
        bloco_teste_pulsos_sinais = blocos_pulsos_sinais[indice_teste]
        
        # Definição do bloco_treino_pulsos_sinais como sendo aqueles de índices diferentes do indice_teste.
        bloco_treino_pulsos_sinais = blocos_pulsos_sinais[:indice_teste]+blocos_pulsos_sinais[indice_teste+1:]
        
        # Reescreve os elementos bloco_treino_pulsos_sinais em sequência, uma lista unidimensional.
        bloco_treino_pulsos_sinais = [elemento for sublista in bloco_treino_pulsos_sinais for elemento in sublista]
        
        # Definição do bloco_teste_parametro_referencia como sendo aquele de índice igual ao indice_teste.
        bloco_teste_parametro_referencia = blocos_parametro_referencia[indice_teste]
        
        # Definição do bloco_treino_parametro_referencia como sendo aqueles de índices diferentes do indice_teste.
        bloco_treino_parametro_referencia = blocos_parametro_referencia[:indice_teste]+blocos_parametro_referencia[indice_teste+1:]
        
        # Reescreve os elementos bloco_treino_parametro_referencia em sequência, uma lista unidimensional.
        bloco_treino_parametro_referencia = [elemento for sublista in bloco_treino_parametro_referencia for elemento in sublista]
        
        # A variável bloco_vetor_erro_estimacao_parametro recebe o valor de retorno da função metodo_LS_SR.
        Bloco_vetor_erro_estimacao_parametro = metodo_LS_SR(n_janelamento, bloco_treino_pulsos_sinais, bloco_teste_pulsos_sinais, bloco_treino_parametro_referencia, bloco_teste_parametro_referencia)

        # Cálculo dos dados estatísticos de cada bloco.
        bloco_media_erro_estimacao = np.mean(Bloco_vetor_erro_estimacao_parametro)
        bloco_var_erro_estimacao = np.var(Bloco_vetor_erro_estimacao_parametro)
        bloco_DP_erro_estimacao = np.std(Bloco_vetor_erro_estimacao_parametro)
        
        # Adiciona essas informações em suas respectivas listas.    
        lista_blocos_media_erro_estimacao.append(bloco_media_erro_estimacao)
        lista_blocos_var_erro_estimacao.append(bloco_var_erro_estimacao)
        lista_blocos_DP_erro_estimacao.append(bloco_DP_erro_estimacao)
        
    # Cálculo dos dados estatísticos da média.
    media_media_blocos_erro_estimacao_parametro = np.mean(lista_blocos_media_erro_estimacao)
    var_media_blocos_erro_estimacao_parametro = np.var(lista_blocos_media_erro_estimacao)
    DP_media_blocos_erro_estimacao_parametro = np.std(lista_blocos_media_erro_estimacao)
     
    # Salva a informação dos dados estatísticos da média do erro de estimação do parâmetro em seus respectivos arquivos de saída.   
    arquivo_saida_dados_estatisticos_k_fold_erro_LS_SR(parametro, n_ocupacao, n_janelamento, media_media_blocos_erro_estimacao_parametro, var_media_blocos_erro_estimacao_parametro, DP_media_blocos_erro_estimacao_parametro, dado = "media")
        
    # Cálculo dos dados estatísticos da variância.
    media_var_blocos_erro_estimacao_parametro = np.mean(lista_blocos_var_erro_estimacao)
    var_var_blocos_erro_estimacao_parametro = np.var(lista_blocos_var_erro_estimacao)
    DP_var_blocos_erro_estimacao_parametro = np.std(lista_blocos_var_erro_estimacao)
      
    # Salva a informação dos dados estatísticos da variância do erro de estimação do parâmetro em seus respectivos arquivos de saída.  
    arquivo_saida_dados_estatisticos_k_fold_erro_LS_SR(parametro, n_ocupacao, n_janelamento, media_var_blocos_erro_estimacao_parametro, var_var_blocos_erro_estimacao_parametro, DP_var_blocos_erro_estimacao_parametro, dado = "var")
        
    # Cálculo dos dados estatísticos do desvio padrão.
    media_DP_blocos_erro_estimacao_parametro = np.mean(lista_blocos_DP_erro_estimacao)
    var_DP_blocos_erro_estimacao_parametro = np.var(lista_blocos_DP_erro_estimacao)
    DP_DP_blocos_erro_estimacao_parametro = np.std(lista_blocos_DP_erro_estimacao)
    
    # Salva a informação dos dados estatísticos do desvio padrão do erro de estimação do parâmetro em seus respectivos arquivos de saída.
    arquivo_saida_dados_estatisticos_k_fold_erro_LS_SR(parametro, n_ocupacao, n_janelamento, media_DP_blocos_erro_estimacao_parametro, var_DP_blocos_erro_estimacao_parametro, DP_DP_blocos_erro_estimacao_parametro, dado = "DP")
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ### 

### ----------------------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO ----------------------------------------------------- ###
  
# Definição da instrução principal (main) do código.
def principal_K_fold_LS_SR():
    
    # A variável parametro_amplitude armazena a string "amplitude".
    parametro_amplitude = "amplitude"
    
    # A variável parametro_fase armazena a string "fase".
    parametro_fase = "fase"
    
    # A variável parametro_pedestal armazena a string "pedestal".
    parametro_pedestal = "pedestal"
    
    # A variável ocupacao_inicial armazena o valor inicial da ocupação que é 0.
    ocupacao_inicial = 0
    
    # A variável ocupacao_final armazena o valor final da ocupação que é 100.
    ocupacao_final = 100
    
    # A variável incremento_ocupacao armazena o valor de incremento entre as ocupações.
    incremento_ocupacao = 10
    
    # A variável n_janelamento_inicial armazena o valor inicial do janelamento que é 7.
    n_janelamento_inicial = 7
    
    # A variável n_janelamento_final armazena o valor final do janelamento que é 19.
    n_janelamento_final = 19
    
    # A variável incremento_janelamento armazena o valor do incremento entre os janelamentos.
    incremento_janelamento = 2
    
    # Para o número de ocupações de 0 até 100 com incremento de 10. 
    for n_ocupacao in tqdm(range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao)):
    
        # Para o número de janelamento de 7 até 19 com incremento de 2.
        for n_janelamento in tqdm(range(n_janelamento_inicial, n_janelamento_final+1, incremento_janelamento)):
    
            # Chamada ordenada das funções.
    
            Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao)
            
            Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
            
            vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
            
            vetor_pedestal_referencia = np.random.uniform(1, 100, len(Matriz_Dados_OC))
        
            Matriz_Pulsos_Sinais_Amplitude_Janelado, vetor_amplitude_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
            
            Matriz_Pulsos_Sinais_Fase_Janelado, vetor_fase_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento)
            
            Matriz_Pulsos_Sinais_Pedestal_Janelado, vetor_pedestal_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_pedestal_referencia, n_janelamento)
    
            K_fold_LS_SR(parametro_amplitude, n_ocupacao, n_janelamento, Matriz_Pulsos_Sinais_Amplitude_Janelado, vetor_amplitude_referencia_janelado)
            
            K_fold_LS_SR(parametro_fase, n_ocupacao, n_janelamento, Matriz_Pulsos_Sinais_Fase_Janelado, vetor_fase_referencia_janelado)
            
            K_fold_LS_SR(parametro_pedestal, n_ocupacao, n_janelamento, Matriz_Pulsos_Sinais_Pedestal_Janelado, vetor_pedestal_referencia_janelado)
     
# Chamada da instrução principal do código.
principal_K_fold_LS_SR()       
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

# Impressão de uma linha que representa o fim do programa.

print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")