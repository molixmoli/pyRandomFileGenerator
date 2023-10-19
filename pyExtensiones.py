import os
import shutil
import uuid
from itertools import permutations
import errno
import configparser

configFilePath = "./config.ini"

config = configparser.RawConfigParser(allow_no_value=True)
config.read(configFilePath)

def path_create(path):
    try:
        os.mkdir(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

extensionFeed = config.get("randomExtensions", "extensionFeed")

pathExtensions = config.get("randomExtensions", "pathExtensions")
filename = config.get("randomExtensions", "fileExample")

path_create(pathExtensions)

for i in range(1, config.getint("randomExtensions", "extensionLength")+1):
    path_extension = os.path.join(pathExtensions, "extension"+str(i))
    path_create(path_extension)
    for c in permutations(extensionFeed, i):
        extension = "".join(c)
        if i == 1:
            path_target = path_extension
        else:
            path_target = os.path.join(path_extension, extension[0])
        path_create(path_target)
        shutil.copy(filename, os.path.join(path_target, str(uuid.uuid4()) + " " + config.get("files", "name") + "." + extension))
