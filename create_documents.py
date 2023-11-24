import os
import random
import shutil
import time

while True:
    directorio1 = 'C:/user/RCLONE/SFTP-PRO/Card Shark'
    directorio2 = 'C:/user/RCLONE/SFTP-PRO/Test'

    files = os.listdir(directorio1)
    print(files)
    no_of_files = len(files) // 1

    if no_of_files == 0:
        dir_temp = directorio1
        directorio1 = directorio2
        directorio2 = dir_temp
        files = os.listdir(directorio1)
        print(files)
        no_of_files = len(files) // 1

    print(no_of_files)

    for file_name in random.sample(files, no_of_files):
        shutil.move(os.path.join(directorio1, file_name), directorio2)

    time.sleep(80)