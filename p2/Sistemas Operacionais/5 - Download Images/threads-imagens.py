import os
import requests
from threading import Thread
import time

def download_imagem(url, nome_arquivo):
    response = requests.get(url)
    with open(nome_arquivo, "wb") as file:
        file.write(response.content)
    print(f"Imagem {nome_arquivo} baixada com sucesso!")


def download_imagens_sequential(urls, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for index, url in enumerate(urls):
        nome_arquivo = os.path.join(folder, f"image_seq{index + 1}.jpg")
        download_imagem(url, nome_arquivo)

    print("Todas as imagens foram baixadas sequencialmente com sucesso!")


def download_imagens_threaded(urls, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    threads = []

    for index, url in enumerate(urls):
        nome_arquivo = os.path.join(folder, f"image_thread{index + 1}.jpg")
        threads.append(Thread(target = download_imagem, args = (url, nome_arquivo,)))

    for thread in threads:
        thread.start()
        thread.join()

    print("Todas as imagens foram baixadas com threads com sucesso!")


if __name__ == "__main__":
    image_urls = [
        "https://embrapii.org.br/wp-content/images/2018/11/ifpb_2000x1200_baixa_resolucao-480x480.jpg",
        "https://a.cdn-hotels.com/gdcs/production164/d1916/76adf5d6-a867-49c6-872d-524b3ca73da5.jpg?impolicy=fcrop&w=1600&h=1066&q=medium",
        "https://img.olhardigital.com.br/wp-content/uploads/2023/01/google_fachada.jpg",
    ]

    hora_inicio = time.time()
    download_imagens_sequential(image_urls, "imagens_sequencial")
    tempo_total_sequencial = time.time() - hora_inicio

    hora_inicio = time.time()
    download_imagens_threaded(image_urls, "imagens_threaded")
    tempo_total_threads = time.time() - hora_inicio

    print(f"Tempo gasto no download sequencial: {tempo_total_sequencial:.2f} segundos")
    print(f"Tempo gasto no download com threads: {tempo_total_threads:.2f} segundos")
