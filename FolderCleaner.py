import os
from datetime import datetime

basedir = '/Users/alessioarcara/Downloads/Python_Script/'
memoryList = []


class FolderCleaner:

    def renameAllFiles(self):
        for filename in os.listdir(basedir):
            c = 1
            try:
                mtimeUnix = int(os.path.getmtime(f'{basedir}{filename}'))
                mtimDate = datetime.fromtimestamp(mtimeUnix).strftime('%d-%m-%Y')
            except OSError:
                mtimDate = 0
            if 'basi' in filename.lower():
                filename_def = f'Basi_dati_{c}_{mtimDate}.mp4'
                while (filename_def in memoryList):
                    filename_def = f'Basi_dati_{c}_{mtimDate}.mp4'
                    c += 1
                os.replace(basedir + filename, f'{basedir}{filename_def}')
            elif 'ing' in filename.lower():
                filename_def = f'Ing_Software_{c}_{mtimDate}.mp4'
                while (filename_def in memoryList):
                    filename_def = f'Ing_Software_{c}_{mtimDate}.mp4'
                    c += 1
                os.replace(basedir + filename, f'{basedir}{filename_def}')
            elif 'str' in filename.lower():
                filename_def = f'Strat_Org_Mercati_{c}_{mtimDate}.mp4'
                while (filename_def in memoryList):
                    filename_def = f'Strat_Org_Mercati_{c}_{mtimDate}.mp4'
                    c += 1
                os.replace(basedir + filename, f'{basedir}{filename_def}')
            memoryList.append(filename_def)

        return True


if __name__ == '__main__':
    folderCleaner = FolderCleaner()
    folderCleaner.renameAllFiles()
