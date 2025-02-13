import os
import requests

def validar_e_baixar_url(url, output_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Download concluído. Arquivo salvo em: {output_path}")
        return True

    except requests.exceptions.RequestException:
        print("URL inválida ou erro ao fazer o download.")
        return False