import os
from datetime import datetime

basedir = '/Users/alessioarcara/Downloads/Python_Script/'
dt = str(datetime.today().strftime('%Y-%m-%d'))
memoryList = []


class FolderCleaner:

    def renameAllFiles(self, z=0, x=0, c=0):
        for filename in os.listdir(basedir):
            memoryList.append(filename.lower())
            if 'basi' in filename.lower():
                if ('basi' in s for s in memoryList):
                    z += 1
                os.replace(basedir + filename, f'{basedir}Basi_dati_{z}_{dt}.mp4')
            elif 'ing' in filename.lower():
                if ('ing' in s for s in memoryList):
                    x += 1
                os.replace(basedir + filename, f'{basedir}Ing_Software_{x}_{dt}.mp4')
            elif 'str' in filename.lower():
                if ('str' in s for s in memoryList):
                    c += 1
                os.replace(basedir + filename, f'{basedir}Strat_Org_Mercati_{c}_{dt}.mp4')
            print(memoryList)

        return True


if __name__ == '__main__':
    folderCleaner = FolderCleaner()
    folderCleaner.renameAllFiles()
