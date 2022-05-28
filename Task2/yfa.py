import requests

class YandexFolderApi:

    def __init__(self, token, folder_name):
        self.token = token
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {'Authorization': self.token}
        self.params = {'path': folder_name}

    def create_folder(self):
        return requests.put(self.url, headers=self.headers, params=self.params).status_code


token = 'AQAAAAABvFAmAADLW6axqFZnAEOCjQyptuIe_Us'

if __name__ == '__main__':
    print(YandexFolderApi(token, 'Folder_1').create_folder())