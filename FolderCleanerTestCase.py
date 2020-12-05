import unittest
from FolderCleaner import FolderCleaner
import os
from datetime import datetime


class FolderCleanerTestCase(unittest.TestCase):
    dir = '/Users/alessioarcara/Downloads/Python_Script/'
    dt = str(datetime.today().strftime('%Y-%m-%d'))

    def setUp(self):
        files = ['basi.mp4', 'basi2.mp4', 'ing.mp4', 'ing2.mp4', 'str.mp4', 'str2.mp4']
        for file in files:
            with open(self.dir + file, 'a'):
                os.utime(self.dir + file, None)

    def tearDown(self):
        for filename in os.listdir(self.dir):
            file_path = os.path.join(self.dir, filename)
            print(filename)
            try:
                os.remove(file_path)
            except Exception as e:
                print('Impossibile da cancellare %s. Reason %s' % (file_path, e))

    def testRenameMultipleFiles(self):
        files = [f'{self.dir}Basi_dati_{1}_{self.dt}.mp4',
                 f'{self.dir}Basi_dati_{2}_{self.dt}.mp4',
                 f'{self.dir}Ing_Software_{1}_{self.dt}.mp4',
                 f'{self.dir}Ing_Software_{2}_{self.dt}.mp4',
                 f'{self.dir}Strat_Org_Mercati_{1}_{self.dt}.mp4',
                 f'{self.dir}Strat_Org_Mercati_{2}_{self.dt}.mp4']
        self.assertEqual(FolderCleaner.renameAllFiles(self), os.path.isfile(
            files[0] and files[1] and files[2] and files[3] and files[4] and files[5]))
