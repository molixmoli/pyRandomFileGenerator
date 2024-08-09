import os
import random
import string
import time


def rename_randomly(path, prefix: str = "IMM"):
    # Recopilar todos los nombres de archivos y carpetas
    paths = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            paths.append(os.path.join(root, name))
        for name in dirs:
            paths.append(os.path.join(root, name))

    # Cambiar los nombres
    for old_path in paths:
        head, tail = os.path.split(old_path)
        extension = os.path.splitext(tail)[1]
        new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        new_name = f'ABC {new_name}'
        if not os.path.isdir(old_path):
            new_name += extension
        new_path = os.path.join(head, new_name)
        os.rename(old_path, new_path)
        print(f"Renombrado: {old_path} a {new_path}")


def generate_random_string(length=3):
    # Genera una cadena aleatoria de longitud especificada
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return result_str


# Uso de la función
random_string = generate_random_string()

# path = 'C:/Users/imolina/EDITIONS LEFEBVRE SARRUT/RCLONE - Documentos/Compartido/Carpeta 1'
path = 'carpeta4'


if __name__ == '__main__':
    # Uso de la función
    # rename_randomly('./Carpeta22')
    # while True:
    # for i in range(1, 6):

        # rename_randomly(path=path)
        #
        # time.sleep(300)

    rename_randomly(path=path)
