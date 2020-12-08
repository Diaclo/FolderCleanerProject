import os
from datetime import datetime
import shutil
import subprocess

extensions = ['flv', 'mkv', 'mp4']
basedir = '/Users/alessioarcara/Downloads/Python_Script/'
enddir = '/Users/alessioarcara/Downloads/End_Dir/'
memoryList = []
filesAllowed = ['basi', 'ing', 'str']


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
            if not filename.endswith(tuple(extensions)) or not any(s in filename.lower() for s in filesAllowed):
                try:
                    os.remove(os.path.join(base_dir, filename))
                except Exception as e:
                    print('Impossibile da cancellare %s. Reason %s' % (filename, e))
        return False

    @staticmethod
    def hasAudioFilter(base_dir):
        for filename in os.listdir(base_dir):
            ffprobe_term = "ffprobe -v error -of flat=s_ -select_streams 1 -show_entries stream=duration -of " \
                           "default=noprint_wrappers=1:nokey=1 " + os.path.join(base_dir, filename)
            result = subprocess.run(ffprobe_term,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    shell=True)
            if not result.stdout:
                try:
                    os.remove(os.path.join(base_dir, filename))
                except Exception as e:
                    print('Impossibile da cancellare %s. Reason %s' % (filename, e))
        return False


folderCleaner = FolderCleaner()
folderCleaner.deleteFiles(basedir)
folderCleaner.hasAudioFilter(basedir)
folderCleaner.renameFiles(basedir, 'basi', 'Basi_dati')
folderCleaner.renameFiles(basedir, 'ing', 'Ing_Software')
folderCleaner.renameFiles(basedir, 'str', 'Strat_Org_Mercati')
enddir = '/Users/alessioarcara/Downloads/End_Dir/Basi'
folderCleaner.moveFiles(basedir, enddir, 'basi')
enddir = '/Users/alessioarcara/Downloads/End_Dir/Ing'
folderCleaner.moveFiles(basedir, enddir, 'ing')
enddir = '/Users/alessioarcara/Downloads/End_Dir/Strat'
folderCleaner.moveFiles(basedir, enddir, 'str')