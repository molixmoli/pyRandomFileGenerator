import os
import shutil
import uuid
import coloredlogs, logging

from modules.media import Media
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger)

if __name__ == '__main__':
    media = Media()

    #crear directorio de trabajo
    directory_default = 'carpeta2'
    uuid_name = str(uuid.uuid4())
    directory_generate = os.path.join(directory_default, uuid_name)
    os.makedirs(directory_generate)
    print("Directory '% s' created" % directory_generate)

    #crear archivos binarios
    media.generate_big_random_bin_file(os.path.join(directory_generate, "IMM_big_bin "+uuid_name+".dat"), 1024*1024)

    #crear archivos texto
    media.generate_big_random_letters(os.path.join(directory_generate, "IMM_big_letters "+uuid_name+".txt"), 1024 * 1024)

    #crear archivos binarios
    media.generate_big_sparse_file(os.path.join(directory_generate, "IMM_big_sparse "+uuid_name+".dat"), 1000)

    # crear archivos texto con frases
    filename = "IMM_big_sentences " + uuid_name
    media.generate_big_random_sentences(os.path.join(directory_generate, filename + ".txt"), 100)

    # crear archivos pdf a partir del txt
    #generate_pdf(os.path.join(directory_generate, filename + ".txt"), os.path.join(directory_generate, filename + ".pdf"))

    # crear archivos imagenes
    media.generate_img(os.path.join(directory_generate, filename + ".txt"),
                 os.path.join(directory_generate, filename + ".png"))
    media.generate_img(os.path.join(directory_generate, filename + ".txt"),
                 os.path.join(directory_generate, filename + ".jpeg"))

    #read_file = pd.read_csv(os.path.join(directory_generate, filename + ".txt"), encoding='ISO-8859-1')
    #read_file.to_csv(os.path.join(directory_generate, filename + ".csv"), index=None)

    # crear archivos docx a partir del txt
    media.generate_docx(os.path.join(directory_generate, filename + ".txt"),
                  os.path.join(directory_generate, filename + ".docx"))

    # crear archivos pdf a partir del docx
    media.generate_pdf_from_docx(os.path.join(directory_generate, filename + ".docx"),
                  os.path.join(directory_generate, filename + ".pdf"))

    # crear archivos avi a partir de png
    media.generate_avi(os.path.join(directory_generate, filename + ".avi"), directory_generate)

    # crear archivos audio a partir de txt
    media.generate_audio(os.path.join(directory_generate, filename + ".txt"),
                  os.path.join(directory_generate, filename))

    # comprimir el directorio en zip
    shutil.make_archive(os.path.join(directory_default, filename), 'zip', directory_generate)
    shutil.move(os.path.join(directory_default, filename + ".zip"), os.path.join(directory_generate, filename + ".zip"))

