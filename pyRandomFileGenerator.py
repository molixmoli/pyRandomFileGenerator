import os
import random
import shutil
import time
import uuid

import coloredlogs, logging
import glob
import configparser
import datetime
from modules.media import Media

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger)

global media

configFilePath = "./config.ini"

config = configparser.RawConfigParser(allow_no_value=True)
config.read(configFilePath)

def convert_bytes(bytes_number):
    tags = ["Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"]

    i = 0
    double_bytes = bytes_number

    while (i < len(tags) and bytes_number >= 1024):
        double_bytes = bytes_number / 1024.0
        i = i + 1
        bytes_number = bytes_number / 1024

    return str(round(double_bytes, 2)) + " " + tags[i]

def get_path_size(folderpath):
    # assign size
    size = 0

    # get size
    for path, dirs, files in os.walk(folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    return size

def create_file(extension, folder, filename):
    txt_source = os.path.join(folder, filename + ".txt")
    if bool(random.getrandbits(1)):
        file_out = os.path.join(folder, (filename + "." + extension).upper())
    else:
        file_out = os.path.join(folder, (filename + "." + extension).lower())
    if (extension == 'txt'):
        media.generate_big_random_sentences(file_out, config.getint("extprop", "numSentences"))
    elif (extension == 'docx'):
        media.generate_docx(txt_source, file_out)
    elif (extension == 'pdf'):
        media.generate_pdf_from_docx(txt_source, file_out)
    elif (extension == 'jpg' or extension == 'png'):
        media.generate_img(txt_source, file_out)
    elif (extension == 'mp3'):
        try:
            media.generate_audio(txt_source, file_out)
        except:
            logger.error("ERROR: Creando audio")
    elif (extension == 'bin'):
        media.generate_big_random_bin_file(file_out, config.getint("extprop", "sizeBIN"))
    elif (extension == 'doc'):
        media.generate_big_random_letters(file_out, config.getint("extprop", "sizeDOC"))
    elif (extension == 'dat'):
        media.generate_big_sparse_file(file_out, config.getint("extprop", "sizeDAT"))


while True:

    path_target = config.get("main", "pathTarget")

    size = convert_bytes(get_path_size(path_target))
    logger.info("### Tamaño directorio destino: " + size)

    # Comprobar si el directorio de documentos se supera el tamaño esperado (3Gb)
    if size.split()[1] == config.get("main", "localSizeUnit"):
        if float(size.split()[0]) > config.getfloat("main", "localSize"):
            logger.info("### Se ha superado el tamaño máximo: " + config.get("main", "localSize") + " " + config.get("main", "localSizeUnit"))
            exit()

    # Creamos varios los niveles de carpeta
    for i in range(1, config.getint("main", "pathLevels")):
        path_target = os.path.join(path_target, str(uuid.uuid4()))
    path_target = os.path.join(path_target, str(uuid.uuid4()))
    os.makedirs(path_target)
    logger.info("### Directorio '% s' creado" % path_target)

    #Generar documentos de forma aleatoria
    if config.getboolean("files", "random"):
        num_sentences = config.getint("extprop", "numSentences")
        media = Media()

        #Cremos los directorios por tipo
        folder = {}
        for extension in config.options("extension"):
            if config.getboolean("extension", extension):
                folder[extension] = os.path.join(path_target, extension + " " + str(uuid.uuid4()))
                os.makedirs(folder[extension])

        for i in range(1, config.getint("files", "num")+1):
            filename = str(uuid.uuid4()) + " " + config.get("files", "name")

            for extension in config.options("extension"):
                if config.getboolean("extension", extension):
                    create_file(extension, path_target, filename)

            for extension in config.options("extension"):
                if config.getboolean("extension", extension):
                    for f in glob.glob(os.path.join(path_target, "*." + extension)):
                        shutil.move(f, folder[extension])
        # crear video
        if config.getboolean("extension", "mp3"):
            media.generate_avi(os.path.join(path_target, filename + ".avi"), os.path.join(folder['png']))

    # Copiar documentos concretos en diferentes carpetas
    else:
        path_default = config.get("main", "pathSource")
        files = os.listdir(path_default)
        logger.info("### Documentos leidos" + str(files))

        for filename in files:
            split_tup = os.path.splitext(filename)
            file_name = split_tup[0]
            file_extension = split_tup[1]

            shutil.copy(os.path.join(path_default, filename), os.path.join(path_target, file_name + ' ' +str(uuid.uuid4())+file_extension))

    # Tiempo de espera para la siguiente ejecucion
    time_wait = config.getint("main", "timeWaitToNextRun")
    logger.info("### Proxima ejecucion: " + str(datetime.datetime.now() + datetime.timedelta(seconds=time_wait)))
    time.sleep(time_wait)