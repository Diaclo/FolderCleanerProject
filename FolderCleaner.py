import os
from datetime import datetime
import shutil

extensions = ['flv', 'mkv', 'mp4']
basedir = '/Users/alessioarcara/Downloads/Python_Script/'
enddir = '/Users/alessioarcara/Downloads/End_Dir/'
memoryList = []


class FolderCleaner:

    @staticmethod
    def renameFiles(base_dir, nome, nome_def):
        for filename in os.listdir(base_dir):
            c = 1
            try:
                mtimeUnix = int(os.path.getmtime(f'{base_dir}{filename}'))
                mtimDate = datetime.fromtimestamp(mtimeUnix).strftime('%d-%m-%Y')
            except OSError:
                mtimDate = 0
            if nome in filename.lower() and filename.lower().endswith(tuple(extensions)):
                filename_def = f'{nome_def}_{c}_{mtimDate}.mp4'
                while filename_def in memoryList:
                    filename_def = f'{nome_def}_{c}_{mtimDate}.mp4'
                    c += 1
                os.replace(os.path.join(base_dir, filename), os.path.join(base_dir, filename_def))
                memoryList.append(filename_def)
        return True

    @staticmethod
    def moveFiles(base_dir, end_dir, nome):
        for filename in os.listdir(base_dir):
            if nome in filename.lower():
                shutil.move(os.path.join(base_dir, filename), os.path.join(end_dir, filename))
        return True

    @staticmethod
    def deleteFiles(base_dir):
        for filename in os.listdir(base_dir):
            if not filename.endswith(tuple(extensions)):
                os.remove(os.path.join(base_dir, filename))
        return False

if __name__ == '__main__':
    folderCleaner = FolderCleaner()
    folderCleaner.renameFiles('basi', 'Basi_dati')
    folderCleaner.renameFiles('ing', 'Ing_Software')
    folderCleaner.renameFiles('str', 'Strat_Org_Mercati')
