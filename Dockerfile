# Imagem ultra-leve oficial do Python 3.10
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala as dependências (Superlinked e outras que precisar)
# O --no-cache-dir mantém a imagem pequena
RUN pip install --no-cache-dir superlinked

# Copia todos os arquivos da sua pasta atual para dentro do container
COPY . .

# Comando que será executado ao iniciar o container
# Substitua 'seu_script.py' pelo nome real do seu arquivo
CMD ["python", "recsys_embedd.py"]
