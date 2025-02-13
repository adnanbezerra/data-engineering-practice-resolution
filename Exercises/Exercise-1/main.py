import os
import downloader
import extractor

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q2.zip",
]


def main():
    os.makedirs("./downloads", exist_ok=True)

    for uri in download_uris:
        filename = uri.split("/")[-1]

        downloader.validar_e_baixar_url(uri, f"./downloads/{filename}")

        extractor.extrair_zip_com_sistema(
            f"./downloads/{filename}",
            "./downloads/",
        )
    pass


if __name__ == "__main__":
    main()
