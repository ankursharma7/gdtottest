from driveApiHandler import Drive
from webAutomation import Gdtot_Handler


def downloader(gdtot_movie_id):
    gdtot = Gdtot_Handler()
    # this will check the download button and return the file name
    movie_file_name = gdtot.click_on_download_get_file_name(gdtot_movie_id)


def main():
    download_list = [
        9600686633,
        # 5843169478,
        # 8652176971,
        # 4886328860,
        # 15649968576,
        # 3252564971,
        # 10037126231,
        # 4791101649,
        # 5440624471,
        # 3952435677,
        # 3930462785,
        # 4596393142,
    ]
    for movie_id in download_list:
        downloader(movie_id)


if __name__ == "__main__":
    main()
