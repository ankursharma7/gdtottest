from driveApiHandler import Drive
from webAutomation import Gdtot_Handler


def downloader(gdtot_movie_id):
    gdtot = Gdtot_Handler()
    g_drive = Drive(
        "14oDKaoukF3AiIZ1g9-9fw33E5MgwPI-k"
    )  # drive folder id where gdtot save files
    folder_location = r"D:\test"

    # this will check the download button and return the file name
    movie_file_name = gdtot.click_on_download_get_file_name(gdtot_movie_id)

    # this will search by name in gdrive and get g drive movie id
    g_drive_movie = g_drive.get_file_id_by_name(movie_file_name)

    movie_id = g_drive_movie["id"]
    movie_name = g_drive_movie["name"]

    # this will start downlaoding file to local storage
    g_drive.download_by_id(movie_id, movie_name, folder_location)

    # after download done this will delete the file from google drive
    g_drive.delete_file_by_id(movie_id)


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
