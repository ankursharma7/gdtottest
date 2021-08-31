from selenium import webdriver


class Gdtot_Handler:
    #  this will initialize new selenium session for work
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:9222")
        self.web = webdriver.Chrome(
            executable_path="chromedriver.exe", options=options)
        self.web.implicitly_wait(100)
        self.web.set_page_load_timeout(100)

    def click_on_download_get_file_gdrive_id(self, id):
        # this open the link and click on the download link and get the file name then return
        self.web.get("https://new.gdtot.me/")
        id_as_string = str(id)
        self.web.get(f"https://new.gdtot.me/dld?id={id_as_string}")

        file_gdrive_id = self.web.find_element_by_xpath(
            '//*[@id="content"]/div/div/div/div/div[2]/a[1]').get_attribute('href')
        return file_gdrive_id.split("=")[1]


if __name__ == "__main__":
    web = Gdtot_Handler()
    file_name1 = web.click_on_download_get_file_gdrive_id(9600686633)
    # file_name2 = web.click_on_download_get_file_gdrive_id(5843169478)
    print(file_name1)
