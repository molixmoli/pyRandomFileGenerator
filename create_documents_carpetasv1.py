import os
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

config = configparser.RawConfigParser(allow_no_value=True)
config.read(configFilePath)

while True:

    path_target = config.get("main", "pathTarget")

    size = convert_bytes(get_path_size(path_target))
    logger.info("### Tamaño directorio destino: " + size)

    # Comprobar si el directorio de documentos se supera el tamaño esperado (3Gb)
    if size.split()[1] == config.get("main", "localSizeUnit"):
        if float(size.split()[0]) > config.getint("main", "localSize"):
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
        if config.getboolean("extension", "pdf"):
            carpeta_pdf = os.path.join(path_target, "pdf " + str(uuid.uuid4()))
            os.makedirs(carpeta_pdf)
        if config.getboolean("extension", "docx"):
            carpeta_docx = os.path.join(path_target, "docx " + str(uuid.uuid4()))
            os.makedirs(carpeta_docx)
        if config.getboolean("extension", "txt"):
            carpeta_txt = os.path.join(path_target, "txt " + str(uuid.uuid4()))
            os.makedirs(carpeta_txt)
        if config.getboolean("extension", "bin"):
            carpeta_bin = os.path.join(path_target, "bin " + str(uuid.uuid4()))
            os.makedirs(carpeta_bin)
        if config.getboolean("extension", "doc"):
            carpeta_doc = os.path.join(path_target, "doc " + str(uuid.uuid4()))
            os.makedirs(carpeta_doc)
        if config.getboolean("extension", "dat"):
            carpeta_dat = os.path.join(path_target, "dat " + str(uuid.uuid4()))
            os.makedirs(carpeta_dat)
        if config.getboolean("extension", "jpg"):
            carpeta_jpg = os.path.join(path_target, "jpg " + str(uuid.uuid4()))
            os.makedirs(carpeta_jpg)
        if config.getboolean("extension", "png"):
            carpeta_png = os.path.join(path_target, "png " + str(uuid.uuid4()))
            os.makedirs(carpeta_png)
        if config.getboolean("extension", "mp3"):
            carpeta_mp3 = os.path.join(path_target, "mp3 " + str(uuid.uuid4()))
            os.makedirs(carpeta_mp3)


        for i in range(1, config.getint("files", "num")+1):
            filename = str(uuid.uuid4()) + " " + config.get("files", "name")

            if config.getboolean("extension", "txt"):
                media.generate_big_random_sentences(os.path.join(path_target, filename + ".txt"), num_sentences)
            if config.getboolean("extension", "docx"):
                media.generate_docx(os.path.join(path_target, filename + ".txt"), os.path.join(path_target, filename + ".docx"))
            if config.getboolean("extension", "pdf"):
                media.generate_pdf_from_docx(os.path.join(path_target, filename + ".txt"), os.path.join(path_target, filename + ".pdf"))

            # crear imagenes (jpg)
            if config.getboolean("extension", "jpg"):
                media.generate_img(os.path.join(path_target, filename + ".txt"), os.path.join(path_target, filename + ".jpg"))
                for f in glob.glob(os.path.join(path_target, "*.jpg")):
                    shutil.move(f, carpeta_jpg)

            # crear imagenes (png)
            if config.getboolean("extension", "png"):
                media.generate_img(os.path.join(path_target, filename + ".txt"), os.path.join(path_target, filename + ".png"))
                for f in glob.glob(os.path.join(path_target, "*.png")):
                    shutil.move(f, carpeta_png)

            # crear audios
            if config.getboolean("extension", "mp3"):
                try:
                    media.generate_audio(os.path.join(path_target, filename + ".txt"), os.path.join(path_target, filename + ".mp3"))
                except:
                    logger.error("ERROR: Creando audio")
                for f in glob.glob(os.path.join(path_target, "*.mp3")):
                    shutil.move(f, carpeta_mp3)

            if config.getboolean("extension", "pdf"):
                for f in glob.glob(os.path.join(path_target, "*.pdf")):
                    shutil.move(f, carpeta_pdf)

            if config.getboolean("extension", "txt"):
                for f in glob.glob(os.path.join(path_target, "*.txt")):
                    shutil.move(f, carpeta_txt)

            if config.getboolean("extension", "docx"):
                for f in glob.glob(os.path.join(path_target, "*.docx")):
                    shutil.move(f, carpeta_docx)

            # crear archivos binarios (bin)
            if config.getboolean("extension", "bin"):
                media.generate_big_random_bin_file(os.path.join(path_target, filename + ".bin"), config.getint("extprop", "sizeBIN"))
                for f in glob.glob(os.path.join(path_target, "*.bin")):
                    shutil.move(f, carpeta_bin)

            # crear archivos texto
            if config.getboolean("extension", "doc"):
                media.generate_big_random_letters(os.path.join(path_target, filename + ".doc"), config.getint("extprop", "sizeDOC"))
                for f in glob.glob(os.path.join(path_target, "*.doc")):
                    shutil.move(f, carpeta_doc)

            # crear archivos binarios (dat)
            if config.getboolean("extension", "dat"):
                media.generate_big_sparse_file(os.path.join(path_target, filename + ".dat"), config.getint("extprop", "sizeDAT"))
                for f in glob.glob(os.path.join(path_target, "*.dat")):
                    shutil.move(f, carpeta_dat)

        # crear video
        if config.getboolean("extension", "mp3"):
            media.generate_avi(os.path.join(path_target, filename + ".avi"), os.path.join(carpeta_png))

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