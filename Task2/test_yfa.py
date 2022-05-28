import yfa
import unittest


class TestYandexFolderApi(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_existed(self):
        self.assertEqual(yfa.YandexFolderApi(yfa.token, 'Тест1').create_folder(), 409)

    def test_new_create_in_folder(self):
        self.assertEqual(yfa.YandexFolderApi(yfa.token, 'Тест1/новая папкаAPI').create_folder(), 409)

    def test_false_token(self):
        self.assertEqual(yfa.YandexFolderApi('false_token', 'Тест1').create_folder(), 401)

    def test_false_path(self):
        self.assertEqual(yfa.YandexFolderApi(yfa.token, 'Folder_1').create_folder(), 409)


if __name__ == '__main__':
    unittest.main()