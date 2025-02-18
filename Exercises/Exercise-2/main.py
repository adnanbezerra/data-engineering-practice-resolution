from parser import encontrar_urls_por_data


def main():
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    items = encontrar_urls_por_data(url, "2024-01-19 10:27")
    print(items)
    pass


if __name__ == "__main__":
    main()
