# pyRandomFileGenerator
Proyecto para la generación de archivos aleatorios


### Instalación
```
pip install -r requirements.txt
```
### Configuración
Parámetros del fichero de configuración (*config.ini*):

* Parámetros generales:
```

[main]
# Modo de funcionamiento:
# - False (Copia archivos de la carpeta origen a la carpeta destino)
# - True (Crea archivos en la carpeta destino)
random = true

# Directorio origen 
pathSource = carpeta1
# Directorio destino
pathTarget = carpeta2
# Numero de niveles de carpetas que se generan
pathLevels = 0

# Control de tamaño del directorio destino
# Valores permitidos: "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"
localSizeUnit = Gigabyte
localSize = 1.2

# Tiempo de espera hasta la próxima ejecución en segundos
timeWaitToNextRun = 120
```

* Parámetros de los archivos generados:

```
[files]
# Numero de archivos que se generan por directorio 
num = 10

# Prefijo identificativo de los archivos
name = IMM

#Numero de caracteres especiales en el nombre del archivo
non_ascii = 10
```


* Archivos que se desean generar:
```
[extension]
txt = true
pdf = true
doc = false
docx = false
bin = false
dat = false
jpg = false
png = false
mp3 = false
avi = false
```

* Tamaño de los archivos que se generan:
```
[extprop]
# Numero de frases en los archivos: txt, word, pdf
numSentences = 10

# Tamaño de los archivos de tipo BIN
#5 * 1024 * 1024 = 5242880
sizeBIN = 5242880

# Tamaño de los archivos de tipo DOC
#3 * 1024 * 1024
sizeDOC = 3145728

# Tamaño de los archivos de tipo DAT
#100* 1024
sizeDAT = 102400
```

### Uso
```
python pyRandomFileGenerator.py
```