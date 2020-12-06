import unittest
from FolderCleaner import FolderCleaner
import os
import time
from datetime import datetime


class FolderCleanerTestCase(unittest.TestCase):
    dir = '/Users/alessioarcara/Downloads/Python_Script/'
    dt = str(datetime.today().strftime('%Y-%m-%d'))

    def setUp(self):

        with open('/Users/alessioarcara/Downloads/Files.txt', 'r') as f:
            for l in f:
                fields = l.split('; ')
                namefile = fields[0]
                date = datetime.strptime(fields[1].rstrip("\n"), "%d/%m/%Y")
                # datetime into untix timestamp
                utime = time.mktime(date.timetuple())

                # os.utime(path, (atime, mtime)): atime, mtime: untix timestamp
                with open(self.dir + namefile, 'a'):
                    os.utime(self.dir + namefile, (utime, utime))

    # def tearDown(self):
    #     for filename in os.listdir(self.dir):
    #         file_path = os.path.join(self.dir, filename)
    #         print(filename)
    #         try:
    #             os.remove(file_path)
    #         except Exception as e:
    #             print('Impossibile da cancellare %s. Reason %s' % (file_path, e))

    def testRenameMultipleFiles(self):
        files = [f'{self.dir}Basi_dati_{1}_20-11-2020.mp4',
                 f'{self.dir}Basi_dati_{1}_21-11-2020.mp4',
                 f'{self.dir}Ing_Software_{1}_22-10-2020.mp4',
                 f'{self.dir}Ing_Software_{2}_22-10-2020.mp4',
                 f'{self.dir}Strat_Org_Mercati_{1}_23-12-1998.mp4',
                 f'{self.dir}Strat_Org_Mercati_{1}_24-12-1998.mp4']
        self.assertEqual(FolderCleaner.renameAllFiles(self), os.path.isfile(
            files[0] and files[1] and files[2] and files[3] and files[4] and files[5]))
