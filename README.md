#Analise de dados para laborátorio com docker
Esse projeto contém um script em python para lidar com dados experimentais.
Ao ser fornecido um arquivo .txt com dados medidos ele calcula:
-Média
-Desvio padrão amostral
-Desvio padrão da média
-Incerteza final
-cria um histograma com curva gaussiana não normalizada sobreposta

O projeto é totalmente conteirizado com docker.
##Pré-requisitos
-   [Docker](https://www.docker.com/get-started)

## Como Rodar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Andre240256/Laboratorio-Fis-16-docker.git](https://github.com/Andre240256/Laboratorio-Fis-16-docker.git)
    cd Laboratorio-Fis-16-docker
    ```

2.  **Tenha seu arquivo de dados:** Certifique-se de que seu arquivo de dados (ex: `dados.txt`) está nesta mesma pasta.

3.  **Construa a imagem Docker:**
    ```bash
    docker build -t lab-analise .
    ```

4.  **Execute o contêiner:** O programa iniciará de forma interativa.
    ```bash
    docker run -it --rm -v "$(pwd)":/app lab-analise
    ```
O script irá então pedir a precisão desejada, o nome do arquivo de dados e a incerteza sistemática. 
O gráfico resultante (`historiograma_frequencia.png`) será salvo nesta mesma pasta.
