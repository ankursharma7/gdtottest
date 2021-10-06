from driveApiHandler import Drive
from webAutomation import Gdtot_Handler


def downloader(single_movie_id):
    gdtot = Gdtot_Handler()
    g_drive = Drive("14oDKaoukF3AiIZ1g9-9fw33E5MgwPI-k"
                    )  # drive folder id where gdtot save files
    folder_location = r"E:\gg"

    # this will check the download button and return the file name
    movie_gdrive_id = gdtot.click_on_download_get_file_gdrive_id(
        single_movie_id)

    # this will search by name in gdrive and get g drive movie id
    g_drive_movie = g_drive.get_movie_info_with_id(movie_gdrive_id)

    movie_id = g_drive_movie["id"]
    movie_name = g_drive_movie["name"]

    # this will start downlaoding file to local storage
    g_drive.download_by_id(movie_id, movie_name, folder_location)

    # after download done this will delete the file from google drive
    g_drive.delete_file_by_id(movie_id)


def get_movie_id_from_txt():
    text_file = open("movie_id.txt", "r")
    movie_ids = text_file.read().split("\n")
    return movie_ids


# this will create an list for the item


def create_list_of_downloaded_files_id(movie_id):
    file = open("downloaded.txt", "a")
    file.writelines("\n" + movie_id)
    file.close()


def delete_from_movie_id(movie_id):
    file = open("movie_id.txt", "r")
    all_lines = file.read().split("\n")

    all_lines.remove(movie_id)

    new_text = "\n".join(all_lines)

    file = open("movie_id.txt", "w")
    file.write(new_text)


def main():

    download_list = get_movie_id_from_txt()
    for movie_id in download_list:
        try:
            downloader(movie_id)
            create_list_of_downloaded_files_id(movie_id)
        except:
            pass
        delete_from_movie_id(movie_id)


if __name__ == "__main__":
    main()
