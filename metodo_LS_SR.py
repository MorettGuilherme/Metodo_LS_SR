# EXPERIMENTO ATLAS - Reconstrução de sinal - Métodos dos Mínimos Quadrados Sem restrição (Least Squares - LS) - Estimação da amplitude, fase ou pedestal.
# Autor: Guilherme Barroso Morett.
# Data: 08 de setembro de 2024.

# Objetivo do código: Aplicação do método LS sem restrição para a estimação da amplitude, fase ou pedestal.

"""
Organização do código:

Leitura dos dados de entrada de acordo com o janelamento desejado.
Os dados de entrada das ocupações no formato de arquivo texto (txt) contém informações sobre os pulsos de sinais (ADC Count), a amplitude de referência (ADC Count), a fase de referência (ns) e o ruído (ADC Count).
O valor de referência considerado para o pedestal foi de 30 ADC Count.

Funções presentes:

3) Função para o método LS sem restrição.
Entrada: parâmetro, número de janelamento, matriz com os pulsos de sinais da etapa de treino janelados, matriz com os pulsos de sinais da etapa de teste janelados, vetor do parâmetro de referência da etapa de treino janelado e vetor do parâmetro de referência da etapa de teste janelado.
Saída: lista com o erro de estimação pelo método LS sem restrição.
"""

# Importação das bibliotecas.
import numpy as np

# Importação dos arquivos.
from leitura_dados_ocupacao_LS_SR import *
from leitura_dados_ruidos_LS_SR import *

### ------------------------------------------ 3) FUNÇÃO PARA O MÉTODO LS SEM RESTRIÇÃO -------------------------------------------------------- ###

# Definição da função para o método LS sem restrição.
def metodo_LS_SR(n_janelamento, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_parametro_referencia_treino_janelado, vetor_parametro_referencia_teste_janelado):
    
    # A matriz S_Treino_Janelado recebe a matriz de pulsos de sinais de treino janelado.
    S_Treino_Janelado = Matriz_Pulsos_Sinais_Treino_Janelado
    
    # Essa parte é importante para o K-Fold, pois converte a matriz S_Treino_Janelado para o tipo numpy array.
    S_Treino_Janelado = np.array(S_Treino_Janelado)
    
    # A matriz S_Teste_janelado recebe a matriz de pulsos de sinais de teste janelado.
    S_Teste_Janelado = Matriz_Pulsos_Sinais_Teste_Janelado
    
    # Essa parte é importante para o K-Fold, pois converte a matriz S_Teste_Janelado para o tipo numpy array.
    S_Teste_Janelado = np.array(S_Teste_Janelado)
    
    # A variável x_treino_janelado recebe o vetor vetor_parametro_referencia_treino_janelado.
    x_treino_janelado = vetor_parametro_referencia_treino_janelado
    
    # Essa parte é importante para o K-Fold, pois converte o vetor x_treino_Janelado para o tipo numpy array.
    x_treino_janelado = np.array(x_treino_janelado) 
    
    # A variável x_teste_janelado recebe o vetor vetor_parametro_referencia_teste_janelado.
    x_teste_janelado = vetor_parametro_referencia_teste_janelado
    
    # Essa parte é importante para o K-Fold, pois converte o vetor x_teste_Janelado para o tipo numpy array.
    x_teste_janelado = np.array(x_teste_janelado) 
    
    # Crie uma coluna unitária com o mesmo número de linhas que a matriz S_Teste_Janelado.
    coluna_unitaria_teste = np.ones((S_Teste_Janelado.shape[0], 1))
    
    # Crie uma coluna unitária com o mesmo número de linhas que a matriz S_Treino_Janelado.
    coluna_unitaria_treino= np.ones((S_Treino_Janelado.shape[0], 1))
    
    # Acrescenta a coluna unitária na matriz original S de treino em sua última coluna.
    # Essa parte é empregada justamente para deslocar o hiperplano da origem. Esse termo é conhecido como viés (bias).
    S_C1_Treino_janelado = np.concatenate((S_Treino_Janelado, coluna_unitaria_treino), axis=1)
    
     # Acrescenta a coluna unitária na matriz original S de teste em sua última coluna.
    # Essa parte é empregada justamente para deslocar o hiperplano da origem. Esse termo é conhecido como viés (bias).
    S_C1_Teste_janelado = np.concatenate((S_Teste_Janelado, coluna_unitaria_teste), axis=1)  
    
    # Transposição da matriz S_C1_Treino_janelado.
    S_C1_Treino_janelado_Transp = S_C1_Treino_janelado.transpose()

    # Cálculo da matriz auxiliar A_Aux que corresponde ao resultado do produto matricial entre a matriz S_C1_Treino_janelado_Transp e S_C1_Treino_janelado.
    A_Aux = np.dot(S_C1_Treino_janelado_Transp, S_C1_Treino_janelado)
    
    # A variável A_Aux_Inv recebe a inversa da matriz A_aux.
    A_Aux_Inv = np.linalg.inv(A_Aux)
    
    # Cálculo da matriz auxiliar B_Aux que correpsonde ao resultado do produto matricial entre a matriz A_Aux_Inv e a matriz S_C1_Treino_janelado_Transp.
    B_Aux = np.dot(A_Aux_Inv, S_C1_Treino_janelado_Transp)
    
    # Cálculo dos pesos pelo método LS sem restrição.
    vetor_pesos_LS_SR = np.dot(B_Aux, x_treino_janelado)
    
    # Cálculo do vetor do parâmetro estimado.
    vetor_parametro_estimado = np.dot(S_C1_Teste_janelado, vetor_pesos_LS_SR)
    
    # Cálculo do vetor de erro de estimação do parâmetro.
    vetor_erro_estimacao_parametro = x_teste_janelado - vetor_parametro_estimado

    # A função retorna o vetor do erro de estimação do parametro.
    return vetor_erro_estimacao_parametro
 
### -------------------------------------------------------------------------------------------------------------------------------------------- ###