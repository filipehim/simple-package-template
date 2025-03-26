import os
import shutil

def criar_diretorio(nome):
    """Cria um diretório local."""
    if not os.path.exists(nome):
        os.makedirs(nome)
        print(f"Diretório '{nome}' criado com sucesso!")
    else:
        print(f"O diretório '{nome}' já existe.")

def mover_arquivo(origem, destino):
    """Move um arquivo de origem para destino."""
    if os.path.exists(origem):
        shutil.move(origem, destino)
        print(f"Arquivo movido de '{origem}' para '{destino}'.")
    else:
        print(f"O arquivo '{origem}' não foi encontrado.")

def limpar_cache(diretorio):
    """Remove todos os arquivos de um diretório (cache)."""
    if os.path.exists(diretorio):
        for arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
                print(f"Arquivo '{caminho_arquivo}' removido.")
    else:
        print(f"O diretório '{diretorio}' não existe.")
