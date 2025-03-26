import requests

def baixar_arquivo(url, destino):
    """Baixa um arquivo de uma URL e salva localmente."""
    try:
        resposta = requests.get(url, stream=True)
        resposta.raise_for_status()  # Verifica se houve erro na requisição
        with open(destino, 'wb') as arquivo:
            for chunk in resposta.iter_content(chunk_size=8192):
                arquivo.write(chunk)
        print(f"Arquivo baixado e salvo em '{destino}'.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")

def acessar_api(url, params=None):
    """Faz uma requisição GET a uma API e retorna o resultado."""
    try:
        resposta = requests.get(url, params=params)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

def enviar_dados_para_servidor(url, dados):
    """Envia dados para um servidor usando requisições POST."""
    try:
        resposta = requests.post(url, json=dados)
        resposta.raise_for_status()
        print(f"Dados enviados com sucesso! Resposta: {resposta.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar dados: {e}")
