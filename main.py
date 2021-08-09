from driveApiHandler import Drive
from webAutomation import Gdtot_Handler


def downloader(movie_file_name):
    g_drive = Drive(
        "14oDKaoukF3AiIZ1g9-9fw33E5MgwPI-k"
    )  # drive folder id where gdtot save files
    folder_location = r"E:\gg"

    # this will search by name in gdrive and get g drive movie id
    g_drive_movie = g_drive.get_file_id_by_name(movie_file_name)

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


def main():
    # gdtot = Gdtot_Handler()
    download_list = iter(get_movie_id_from_txt())
    print("gg")
    Done = True
    while Done:
        movies_threads = []
        for _ in range(2):
            try:
                single_movie_id = next(download_list)
                movies_threads.append(single_movie_id)
                # this will check the download button and return the file name
                # movie_file_name = gdtot.click_on_download_get_file_name(single_movie_id)
            except StopIteration:
                Done = False
                break
        print(movies_threads)


if __name__ == "__main__":
    main()
