from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import numpy as np 
from scipy.stats import norm
import sys

# Definir precisão 
print("Quantos algarismos de presisao sao necessarios? de 1 a 30")
precisao = int(input())
getcontext().prec = precisao

#leitura do arquivo
print("Digite o nome do arquivo:")
nome_arquivo = input()

try:
    with open(nome_arquivo, 'r') as file:
        conteudo = file.read()
        values_str = [valor.strip() for valor in conteudo.split(',')]
except FileNotFoundError:
    print(f"o arquivo '{nome_arquivo}' não foi encontrado, lembre-se de adicionar o path completo.")
    sys.exit()


#Calculos

try:
    #conversão para decimal para precisão ajustavel
    values_decimal = [Decimal(v) for v in values_str]
except:
    print("Erro ao converter os valores para Decimal. Verifique se o arquivo contém apenas números separados por vírgula e como separador decimal '.' .")
    sys.exit()


#numero de elementos
N = Decimal(len(values_str))


#media
media_decimal = sum(values_decimal)/N


#desvio padrão amostral
soma_quadrados = sum((x-media_decimal)*(x-media_decimal) for x in values_decimal)
desvio_padrao_amostral = (soma_quadrados/Decimal(N-1)).sqrt()


#desvio padrão da média
desvio_padrao_da_media = desvio_padrao_amostral/N.sqrt()


#desvio padrão sistemico
print("qual a incerteza sistemico do equipamento? use o ponto como separador decimal")
desvio_padrao_sistemico = Decimal(input())

#incerteza final
incerteza_resultante = (desvio_padrao_da_media*desvio_padrao_da_media + desvio_padrao_sistemico*desvio_padrao_sistemico).sqrt()

#printando as respostas
saida = f"Media = {media_decimal:.{precisao}f}\n desvio padrao amostral = {desvio_padrao_amostral:.{precisao}f}\n desvio padrao da media = {desvio_padrao_da_media:.{precisao}f}\n incerteza final = {incerteza_resultante:.{precisao}f}"
print(saida)

#Para o historiograma
values_float = [float(v) for v in values_str]
media_float = float(media_decimal)
desvio_padrao_amostral_float = float(desvio_padrao_amostral)
N = len(values_float)

counts, bin_edges, patches = plt.hist(values_float, bins='auto', edgecolor='black', alpha=0.7, label='Frequência Experimental')

bin_width = bin_edges[1]-bin_edges[0]
scale_factor = N*bin_width

x_min, X_max = plt.xlim()
x = np.linspace(x_min,X_max,100)
p_normalized = norm.pdf(x, media_float, desvio_padrao_amostral_float)
p_scaled_to_frequency= p_normalized*scale_factor

plt.plot(x, p_scaled_to_frequency, 'r--', linewidth = 2, label='Curva de Frequência Teórica')

plt.title('')
plt.xlabel('Valor do período(s)')
plt.ylabel('frequencia')
plt.legend()
plt.grid(axis='y',alpha = 0.75)

plt.savefig('historiograma_frequencia.png')

print("Grafico salvo como historiograma_frequencia.png!")