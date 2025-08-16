FROM python:3.9-slim

# 2. Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# 3. Copie o arquivo de requisitos para dentro do contêiner
COPY requirements.txt .

# 4. Instale as bibliotecas listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copie o seu script Python para dentro do contêiner
COPY lab.py .

# 6. Defina o comando que será executado quando o contêiner iniciar
CMD ["python3", "lab.py"]