from Google import Create_Service
import os
import io
from googleapiclient.http import MediaIoBaseDownload


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

    def download_by_id(self, file_id, file_name, download_location):

        request = self.service.files().get_media(fileId=file_id)
        fh = io.FileIO(
            os.path.join(download_location, file_name),
            "wb",
        )

        downloader = MediaIoBaseDownload(fd=fh, request=request, chunksize=100000000)
        done = False

        while not done:
            status, done = downloader.next_chunk()
            print("downloading progress", status.progress() * 100)

    def delete_file_by_id(self, file_id):
        # this method will delete file from google drive using its file id
        self.service.files().delete(fileId=file_id).execute()


if __name__ == "__main__":
    drive = Drive("14oDKaoukF3AiIZ1g9-9fw33E5MgwPI-k")
    file = drive.get_file_id_by_name("Dosti Ke Side Effects [816p].mkv")
    drive.download_by_id(file["id"], file["name"], r"D:\test")
    drive.delete_file_by_id(file["id"])
