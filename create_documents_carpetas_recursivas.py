import os
import random
import shutil
import time
import uuid
from random import randrange

while True:

    directory_default = 'carpeta1'
    directory_generate = 'C:/user/RCLONE/SFTP-PRO/Test'

#        if randrange(10) == 0:
#        shutil.rmtree(directory_generate, ignore_errors=True)
#        os.mkdir(directory_generate)
#        print("Directory '% s' eliminado" % directory_generate)

#    for i in range(0, random.randint(1,8)):
#        directory_generate = os.path.join(directory_generate, str(uuid.uuid4()))

    for i in range(1, 8):
        directory_generate = os.path.join(directory_generate, str(uuid.uuid4()))
    directory_generate = os.path.join(directory_generate, str(uuid.uuid4()))

    os.makedirs(directory_generate)
    print("Directory '% s' created" % directory_generate)

    files = os.listdir(directory_default)
    print(files)

    for filename in files:
        split_tup = os.path.splitext(filename)
        file_name = split_tup[0]
        file_extension = split_tup[1]

        shutil.copy(os.path.join(directory_default, filename), os.path.join(directory_generate, file_name + ' ' +str(uuid.uuid4())+file_extension))
    time.sleep(120)
