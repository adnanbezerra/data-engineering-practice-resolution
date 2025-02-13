import subprocess
import os


def extrair_zip_com_sistema(caminho_zip, pasta_destino):
    if not os.path.exists(caminho_zip):
        print(f"Arquivo {caminho_zip} não encontrado.")
        return

    os.makedirs(pasta_destino, exist_ok=True)

    if os.name == "nt":
        comando = f"powershell Expand-Archive -Path {caminho_zip} -DestinationPath {pasta_destino}"
    else:
        comando = f"unzip {caminho_zip} -d {pasta_destino}"

    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

    if resultado.returncode != 0:
        print(f"Erro ao extrair o arquivo: {resultado.stderr}")
    else:
        print(f"Arquivos extraídos com sucesso para: {pasta_destino}")
        os.remove(caminho_zip)
