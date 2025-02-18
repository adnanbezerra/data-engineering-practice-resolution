import requests
import pandas as pd
from html.parser import HTMLParser


# Parser para extrair tabelas HTML
class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.current_row = []
        self.table_data = []
        self.headers = []

    def handle_starttag(self, tag, attrs):
        if tag == "a" and self.in_cell:  # Verifica se está dentro de uma célula
            for attr in attrs:
                if attr[0] == "href":  # Extrai o atributo href
                    self.current_link = attr[1]
                break

    def handle_data(self, data):
        if self.in_cell:
            self.current_row.append(data.strip())
            if self.current_link:  # Adiciona o link se existir
                self.current_row.append(self.current_link)
                self.current_link = None  # Reseta o link para a próxima célula

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_table = False
        elif tag == "tr" and self.in_table:
            self.in_row = False
            if self.headers:  # Se já tiver os cabeçalhos, adiciona como linha de dados
                self.table_data.append(self.current_row)
            else:  # Se não, assume que é a linha de cabeçalho
                self.headers = self.current_row
        elif tag in ["td", "th"] and self.in_row:
            self.in_cell = False


def extrair_tabela_da_pagina(url):
    # Faz a requisição HTTP
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao acessar a página: {response.status_code}")
        return None

    # Usa o parser para extrair a tabela
    parser = TableParser()
    parser.feed(response.text)
    return parser.headers, parser.table_data


def encontrar_urls_por_data(url, data_modificacao):
    headers, table_data = extrair_tabela_da_pagina(url)
    if not headers or not table_data:
        print("Nenhuma tabela encontrada.")
        return None

    df = pd.DataFrame(table_data, columns=headers + ["URL"])  # Adiciona coluna "URL"
    df_filtrado = df[df["Last modified"] == data_modificacao]

    # Retorna a primeira URL encontrada
    if not df_filtrado.empty:
        return df_filtrado.iloc[0]["URL"]
    return None
