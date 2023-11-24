import os
import coloredlogs, logging
import configparser

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger)

configFilePath = "./config.ini"

config = configparser.RawConfigParser(allow_no_value=True)
config.read(configFilePath)

walk_dir = config.get("main", "pathTarget")
walk_dir = './carpeta2'

print('walk_dir = ' + walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
walk_dir = os.path.abspath(walk_dir)

def searchRLEF(files):
    for file in files:
        if file.lower().endswith('.rlef'):
            return os.path.splitext(file)[0]
        else:
            return None


rootExpediente=None
idExpediente = None
for root, subdirs, files in os.walk(walk_dir):

    #print(root)
    if idExpediente is None:
        idExpediente = searchRLEF(files)
        if idExpediente is not None:
            rootExpediente = root
            print(idExpediente)
            print(rootExpediente)
    if rootExpediente is not None:
        if not rootExpediente in root:
            idExpediente = None
            rootExpediente = None
            print(root)


    # else:
    #     if not rootExpediente in root:
    #         idExpediente = None
    #         rootExpediente = None
    #
    # if idExpediente:
    #     rootExpediente = root
    #     print(rootExpediente)


    # for subdir in subdirs:
    #     print(subdir)


exit()
directorios = []
for root, subdirs, files in os.walk(walk_dir):
    directorio = root.split(walk_dir)[1]
    directorio = root
    if directorio is not "":
        directorios.append(directorio)
    print(root)

print(directorios)

def getSubdirs(walk_dir):
    for root, subdirs, files in os.walk(walk_dir):
        return subdirs, files

def searchRLEF(files):
    for file in files:
        if file.lower().endswith('.rlef'):
            return os.path.splitext(file)[0]
        else:
            return None

for directorio in directorios:
    subdirs, files = getSubdirs(directorio)
    idExpediente = searchRLEF(files)
    if idExpediente is not None:
        print(idExpediente)
        print(directorio)

exit()






def searchDirs(dir):

    subdirs, files = getSubdirs(dir)
    idExpediente = searchRLEF(files)
    if not idExpediente is None:
        return idExpediente
    if len(subdirs) == 0:
        return 0

    while (idExpediente is None):
        searchDirs(os.path.join(dir, subdirs[0]))

#print(searchDirs(walk_dir))

dirs, files = getSubdirs(walk_dir)
idExpediente = searchRLEF(files)
print(searchRLEF(files))

if not idExpediente:

    for dir in dirs:
        print(dir)

        subdirs, subfiles = getSubdirs(os.path.join(walk_dir, dir))
        print(subdirs)
        print(searchRLEF(subfiles))

exit()
for dir in dirs:
    subdirs, files = getSubdirs(os.path.join(walk_dir, dir))
    for subdir in subdirs:
        subdirs, subfiles = getSubdirs(os.path.join(walk_dir, dir, subdir))
        print(subdirs)
        idExpediente = searchRLEF(subfiles)
        print(idExpediente)
    idExpediente = searchRLEF(files)
    print(idExpediente)

exit()

while (idExpediente is None): # or len(subdirs) < 0:
    for subdir in subdirs:
        subdirs, files = getSubdirs(os.path.join(walk_dir, subdir))
        print(subdirs)
        idExpediente = searchRLEF(files)



exit()
for subdir in subdirs:
    for root, subdirs, files in os.walk(os.path.join(walk_dir, subdir)):
        print(subdirs)



    # print('--\nroot = ' + root)

    # idExpediente = ""
    #
    # for file in files:
    #
    #     if file.lower().endswith('.rlef'):
    #         idExpediente = os.path.splitext(file)[0]
    #         print('--\nrlef = ' + idExpediente)
    #     else:
    #         print('--\nfile = ' + file)
    #
    # for subdir in subdirs:
    #     print('--\nsubdir = ' + subdir)




