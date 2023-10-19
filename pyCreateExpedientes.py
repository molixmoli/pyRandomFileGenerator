import json
import os
import coloredlogs, logging
import uuid
import random

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger)

# Reading from file
f = open('expedientes.json', "r")
data = json.loads(f.read())

path_target = r'./Clientes'
#path_target = r'C:\Users\imolina\EDITIONS LEFEBVRE SARRUT\RCLONE2 - Documentos2'

file_name_list_dir = path_target + '/' + 'expedientes.txt'

def create_idExpFile(pathExp, idExp):
    try:
        with open(os.path.join(pathExp, idExp + '.rlef'), 'x') as fp:
            pass
    except:
        logger.error("Creando fichero de expediente: " + idExp + '.lef')

def remove_list_in_file(file_name):
    if os.path.exists(file_name):
        logger.info('Listado de expedientes existe se borra para crear nuevo')
        os.remove(file_name)
    pass

def create_list_in_file(file_name):
    # Si existe el fichero con el listado de directorios nos lo cargamos primero
    remove_list_in_file(file_name)
    fp = open(file_name, 'w')

    dir_clients = os.listdir(path_target)

    for client in dir_clients:
        path_client = os.path.join(path_target, client)
        if not os.path.isfile(path_client):
            dir_exp = os.listdir(path_client)
            for exp in dir_exp:
                path_exp = os.path.join(path_target, client, exp)
                if not os.path.isfile(path_exp):
                    fp.write(path_exp + '\n')
    fp.close()

# Eliminamos fichero con el listado de directorios para crearlo de nuevo
remove_list_in_file(file_name_list_dir)

for expediente in data:
    if expediente['customerName'] is not None:

        # Creamos directorios de clientes reales
        try:
            os.makedirs(os.path.join(path_target, expediente['customerName'].strip()))
        except:
            logger.info("Creando directorio de cliente. Directorio posiblemente ya exista: " + str(expediente['customerName']))

        # Creamos directorios de expedientes reales
        try:
            pathExpediente = os.path.join(path_target, expediente['customerName'].strip(), expediente['idOwnFile'].replace('/','_') + ' - ' + expediente['description'].strip().replace('/','_'))
            os.makedirs(pathExpediente)
        except:
            logger.error("Creando directorio de expediente: " + expediente['idExpedient'])

        # Creamos el ficherito con el id de extension real
        create_idExpFile(pathExpediente, expediente['idExpedient'])

# Closing file
f.close()

# Creamos directorios sin fichero de idExpediente y en alguno ponemos id falsos
dir_clients = os.listdir(path_target)
for client in dir_clients:
    idExp = str(uuid.uuid4())
    pathExp = os.path.join(path_target, client, idExp)
    os.makedirs(pathExp)
    if bool(random.getrandbits(1)):
        create_idExpFile(pathExp, idExp)

# Listamos los directorios de expedientes en un archivo
create_list_in_file(file_name_list_dir)