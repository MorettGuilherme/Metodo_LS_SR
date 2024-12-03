O Método dos Mínimos Quadrados (Least Squares - LS) tem como objetivo minimizar os resíduos quadráticos da diferença entre os dados experimentais e os previstos pelo modelo. Dessa maneira, a sua eficicência está atrelada a qualidade dos dados simulados. Em sua versão sem restrições, não há relações impostas para o cálculo dos pesos.
Os resultados foram satisfatórios tanto para a estimação da amplitude como para fase. E especialmente para a fase, o janelamento não tem uma influência tão significativa para a diminuição do desvio padrão.

A seguir são listadas as pastas e também os arquivos contidos nesse repositório, assim como suas respectivas funções:

1. Dados_Estatisticos_LS_SR_amplitude_OC
  * Essa pasta contém arquivos para cada um dos janelamentos com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da amplitude.

2. Dados_Estatisticos_LS_SR_fase_OC
  * Essa pasta contém arquivos para cada um dos janelamentos com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da fase.

3. Dados_Estatisticos_LS_SR_pedestal_OC
  * Essa pasta contém arquivos para cada um dos janelamento com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação do pedestal.

5. Dados_Ocupacoes_Free_Running
  * Essa pasta contém arquivos com os dados para cada uma das ocupações referentes ao pulso de sinal, amplitude de referência, fase de referência e ruído eletrônico computados a cada 25 ns.
  
6. K_Fold_amplitude_DP_Dados_Estatisticos_LS_SR_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

7. K_Fold_amplitude_DP_Desempenho_LS_SR_OC
  * Essa pasta contém um arquivo com os dados da análise estatística do desvio padrão do erro de estimação da amplitude para o janelamento ideal 11 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

8. K_Fold_amplitude_EME_Desempenho_LS_SR_OC
  * Essa pasta contém um arquivo com os dados da análise do erro médio de estimação (EME) da amplitude para o janelamento ideal 11 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

9. K_Fold_amplitude_MAE_Desempenho_LS_SR_OC
  * Essa pasta contém um arquivo com os dados da análise do erro médio absoluto (MAE) da amplitude para o janelamento ideal 11 calculados pela técnica de validação cruzada K-Fold.

10. K_Fold_amplitude_media_Dados_Estatisticos_LS_SR_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

11. K_Fold_amplitude_MSE_Desempenho_LS_SR_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio quadrático (MSE) da amplitude para o janelamento ideal 11 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

12. K_Fold_amplitude_SNR_Desempenho_LS_SR_OC
   * Essa pasta contém um arquivo com os dados da análise da relação sinal ruído (SNR) da amplitude para o janelamento ideal 11 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

13. K_Fold_amplitude_var_Dados_Estatisticos_LS_SR_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das variâncias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

14. K_Fold_fase_DP_Dados_Estatisticos_LS_SR_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da fase calculados pela técnica de validação cruzada K-Fold.

15. K_Fold_fase_DP_Desempenho_LS_SR_OC
  * Essa pasta contém um arquivo dos dados estatísticos para cada ocupação do desvio padrão para o erro de estimação da fase, por meio da amplitude estimada.

16. K_Fold_fase_EME_Desempenho_LS_SR_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio de estimação (EME) da fase para o janelamento ideal 7 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

17. K_Fold_fase_MAE_Desempenho_LS_SR_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio absoluto (MAE) da fase para o janelamento ideal 7 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

18. K_Fold_fase_media_Dados_Estatisticos_LS_SR_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da fase calculados pela técnica de validação cruzada K-Fold.

19. K_Fold_fase_MSE_Desempenho_LS_SR_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio quadrático (MSE) da fase pela amplitude estimada para o janelamento ideal 7 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

20. K_Fold_fase_SNR_Desempenho_LS_SR_OC
   * Essa pasta contém um arquivo com os dados da análise da relação sinal ruído (SNR) da fase pela amplitude estimada para o janelamento ideal 7 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

21. K_Fold_fase_var_Dados_Estatisticos_LS_SR_OC
   * Essa pasta contém arquivos para cada uma das ocupações dos dados estatísticos da variância do erro de estimação da fase pela amplitude estimada.

36. K_Fold_pedestal_DP_Dados_Estatisticos_LS_SR_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

37. K_Fold_pedestal_DP_Desempenho_LS_SR_OC
   * Essa pasta contém arquivos com os dados da análise do desvio padrão do erro estimação para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

38. K_Fold_pedestal_EME_Desempenho_LS_SR_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio de estimação (EME) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

39. K_Fold_pedestal_MAE_Desempenho_LS_SR_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio absoluto (MAE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

40.  K_Fold_pedestal_media_Dados_Estatisticos_LS_SR_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

41. K_Fold_pedestal_MSE_Desempenho_LS_SR_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio quadrático (MSE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

42. K_Fold_pedestal_SNR_Desempenho_LS_SR_OC
   * Essa pasta contém arquivos com os dados da análise da relação sinal ruído (SNR) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

43. K_Fold_pedestal_var_Dados_Estatisticos_LS_SR_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

44. Resultados_LS_SR_Amplitude
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da amplitude pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.

45. Resultados_LS_SR_Fase
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da fase pela amplitude estimada pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.
   
47. Resultados_LS_SR_Pedestal
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação do pedestal pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.

49. arquivo_saida_dados_estatisticos_LS_SR.py
   * Função para o cálculo dos dados estatísticos do erro de estimação pelo método LS sem restrições.
   * Instrução para salvar os dados estatísticos do erro de estimação da amplitude, fase ou pedestal para determinada ocupação em um arquivo de saída.
   * Instrução principal do código.

50. arquivo_saida_desempenho_LS_SR.py
   * Instrução para salvar em arquivos os dados estatísticos do desempenho do método LS sem restrições.
   * Função para o cálculo do desempenho do método LS sem restrições pelo Erro Médio de Estimação (EME).
   * Função para o cálculo do desempenho do método LS sem restrições pelo Erro Médio Quadrático (Mean Squared Error - MSE).
   * Função para o cálculo do desempenho do método LS sem restrições pelo Erro Médio Absoluto (Mean Absolute Error - MAE).
   * Função para o cálculo do desempenho do método LS sem restrições pela Relação Sinal-Ruído (Signal-to-Noise Ratio - SNR).
   * Função para o cálculo do desempenho do método LS sem restrições pelo desvio padrão (DP).
   * Instrução da validação cruzada K-Fold adaptada para o cálculo do desempenho do método LS sem restrições.
   * Instrução principal do código.

51. arquivo_saida_k_fold_LS_SR.py
   * Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold.
   * Instrução da validação cruzada K-Fold.
   * Instrução principal do código.

52. grafico_analise_amplitude_minima_fase_LS_SR.py
   * Função para a leitura dos dados estatísticos da análise erro de estimação da fase para uma dada ocupação pelo método LS sem restrições.
   * Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento pelo processo de estimação da fase.
   * Instrução principal do código.
   
53. grafico_dado_estatistico_janelamento_LS_SR.py
   * Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.
   * Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.
   * Instrução principal do código.

54. grafico_desempenho_LS_SR.py
   * Função para a leitura dos dados do desempenho do método LS sem restrições de todas as ocupações para o janelamento ideal.
   * Instrução para o plote do gráfico do desempenho do método LS sem restrições ao longo das ocupações para o janelamento ideal.
   * Instrução principal do código.

55. grafico_k_fold_LS_SR.py
   * Função para a leitura dos dados estatísticos da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo A da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo B da validação cruzada K-Fold.
   * Instrução principal (main) do código.
   
56. histograma_erro_parametro_LS_SR.py
   * Função para o cálculo da estatística do erro de estimação da amplitude, fase ou pedestal.
   * Instrução para o plote do histograma do tipo A do erro de estimação da amplitude, fase ou pedestal.
   * Instrução para o plote do histograma do tipo B do erro de estimação da amplitude, fase ou pedestal.
   * Instrução principal (main) do código.
   
57. leitura_dados_ocupacao_LS_SR.py
   * Função para a leitura dos dados de ocupação.
   * Função para a retirada do pedestal dos pulsos de sinais.
   * Função para a construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.
   * Função para separação em dados de treino e teste.

58. leitura_dados_ruidos_LS_SR.py
   * Função para a leitura dos dados de ruídos de acordo com a ocupação.
   * Função para a organização dos dados de ruídos de acordo com o janelamento.
   * Função para separação em dados de treino e teste.
   * Função para a construção da matriz de covariância.
   * Função para a construção da matriz de covariância como identidade.

59. metodo_LS_SR.py
   * Função para a definição do vetor pulso de referência.
   * Função para a definição do vetor da derivada temporal do pulso de referência.
   * Função para o método LS sem rstrições.
   
IMPORTANTE: os dados das ocupações foram simulados computacionalmente. As características das distribuições são:

* Distribuição amplitude: exponencial com média 100 ADC Count.
* Distribuição Fase: uniforme com números inteiros no intervalo de -5 a 5 ns.
* Pedestal: 30 ADC Count.
* Nível de deformação: 0,01 ADC Count.
* Número de eventos: 2000000.
* Fold: 100.
* Os dados de ruídos para a matriz de covariância foram os mesmos que para os pulsos de sinais.

Obs.: antes da aplicação do método, o valor constante do pedestal foi retirado dos dados referentes aos pulsos de sinais.
O vetor da fase de referência foi multiplicado por 0,5; pois esse valor representa a resolução da fase.
