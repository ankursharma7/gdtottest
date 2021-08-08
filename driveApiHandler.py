from Google import Create_Service


class Drive:
    CLIENT_SECRET_FILE = "config.json"
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    def __init__(self, folder_id) -> None:
        self.folder_id = folder_id

    def get_file_id_by_name(self, file_name):
        #  this will return the file object with id and name
        query = f"parents = '{self.folder_id}'"
        response = self.service.files().list(q=query).execute()
        files = response.get("files")

        for file in files:
            if file["name"] == file_name:
                return file

        raise Exception("file not found.")


if __name__ == "__main__":
    drive = Drive("14oDKaoukF3AiIZ1g9-9fw33E5MgwPI-k")
    file = drive.get_file_id_by_name(
        "Gully Boy 2019 BluRay Hindi 1080p x264 DD 5.1 ESub - mkvCinemas [Telly].mkv"
    )
    print(file)
