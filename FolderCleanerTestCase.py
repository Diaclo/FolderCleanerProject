import unittest
from FolderCleaner import FolderCleaner
import os
import time
from datetime import datetime


class FolderCleanerTestCase(unittest.TestCase):
    base_dir = '/Users/alessioarcara/Downloads/Python_Script/'
    end_dir = '/Users/alessioarcara/Downloads/End_Dir/'

    def setUp(self):

        with open('/Users/alessioarcara/Downloads/Files.txt', 'r') as f:
            for lines in f:
                fields = lines.split('; ')
                namefile = fields[0]
                date = datetime.strptime(fields[1].rstrip("\n"), "%d/%m/%Y")
                # datetime into untix timestamp
                utime = time.mktime(date.timetuple())

                # os.utime(path, (atime, mtime)): atime, mtime: untix timestamp
                with open(self.base_dir + namefile, 'a'):
                    os.utime(self.base_dir + namefile, (utime, utime))

    def tearDown(self):
        # TODO: teardown -> base_dir e end_dir
        for filename in os.listdir(self.base_dir):
            file_path = os.path.join(self.base_dir, filename)
            print(filename)
            try:
                os.remove(file_path)
            except Exception as e:
                print('Impossibile da cancellare %s. Reason %s' % (file_path, e))

    def testRenameFiles(self):
        files = [f'{self.base_dir}Basi_dati_{1}_20-11-2020.mp4',
                 f'{self.base_dir}Basi_dati_{1}_21-11-2020.mp4']
        self.assertEqual(
            FolderCleaner.renameFiles(self.base_dir, 'basi', 'Basi_dati'),
            os.path.isfile(files[0] and files[1]))

    def testMoveFiles(self):
        files = [f'{self.end_dir}Basi.mp4',
                 f'{self.end_dir}Basi2.mp4',
                 f'{self.end_dir}Basi3.mp4']
        self.assertEqual(
            FolderCleaner.moveFiles(self.base_dir, self.end_dir, 'basi'),
            os.path.isfile(files[0] and files[1]))

    def testDeleteFiles(self):
        files = [f'{self.base_dir}Garbage.mp4',
                 f'{self.base_dir}Garbage2.mp4',
                 f'{self.base_dir}Garbage3.mp4',
                 f'{self.base_dir}Garbage4.mp4']
        self.assertEqual(
            FolderCleaner.deleteFiles(self.base_dir),
            os.path.isfile(files[0] and files[1] and files[2] and files[3]))

    # def testHasAudio(self):
    #     files = [f'{self.base_dir}Garbage.mp4',
    #              f'{self.base_dir}Garbage2.mp4',
    #              f'{self.base_dir}Garbage3.mp4',
    #              f'{self.base_dir}Garbage4.mp4']
    #     self.assertEqual(
    #         FolderCleaner.hasAudioFilter(self.base_dir),
    #         os.path.isfile(files[0] and files[1] and files[2] and files[3]))