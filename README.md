# ColorSense IA: Identificación de colores para personas con daltonismo

## Cómo usarlo en PC

### Crear el entorno virtual

Se necesita crear un entorno virtual para que los módulos que instalemos solo afecten este desarrollo

**Opción 1:**

- Instalar virtualenv, crear el entorno y activarlo:

```
# sudo apt install virtualenv
# virtualenv env
# source env/bin/activate
```

**Opción 2:**

- Instalar python3-venv, crear el entorno y activarlo

```
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate
```

### Instalar requerimientos

El archivo requeriments.txt contiene los módulo necesarios para que nuestro programa funcione. Con el siguiente comando hacemos que se instalen todos.

```
pip install -r requirements.txt
```

### Correr la aplicación para desktop:

```
python color_recognition.py
```

La aplicación detectará el primer dispositivo de video (cámara) disponible en tu PC de forma automática. Si deseas establecer otro dispositivo deberás cambiar el valor de la variable index por un número específico.

```
cap = cv2.VideoCapture(index, cv2.CAP_V4L2)
```

## Cómo usarlo como un servicio web.

La aplicación no cuenta con un servicio web propiamente dicho, sin embargo se puede utilizar módulos python como apoyo.

En el directorio raiz del proyecto, ejecutar:

```
python -m http.server 8000
```

**Utilizarlo en un navegador de tu PC**

Abre un explorador y ve a http://localhost:8000

**Utilizarlo en un navegador de tu celular:**

Si quieres abrirlo en tu celular, no se puede solo poner la IP local de tu computadora y el puerto, ya que para usar la cámara se requiere HTTPS. Puedes hacer un túnel de HTTPS siguiendo los siguientes pasos.

- Descarga ngrok en tu computadora, y descomprímelo
- Abre una línea de comandos o terminal
- Navega hasta la carpeta donde descargaste ngrok
- Ejecuta el comando ngrok http 8000
- Es importante tener ambos activos: El servidor de python, y el túnel de ngrok
- En la línea de comandos aparecerá un enlace HTTPS. Puedes entrar ahí con tu celular, no importa si no estás en la red local.
- El túnel expira después de 2 horas creo, en dado caso solo reinicias ngrok
- Abre un explorador en tu celular y ve al enlace HTTPS indicado

## Observaciones y notas:

En el caso de usarlo en tu celular puedes dar clic en el botón de "Cambiar camara" para utilizar la cámara delantera o trasera del celular. Solo apunta al objeto en el punto central, y abajo te aparecerá la predicción. Tampoco es el clasificador del futuro entonces si no clasifica perfecto, oops.

## Creación del modelo: Solo para desarrolladores.

El modelo tiene una precisión del 89%. Si deseas mejorarlo, puedes reentrenarlo, cambiar la configuración de la red, e inclusive el dataset. Para ello debes ir al directorio model; allí encontrarás tres archivos .py

- **build_dataset.py:** Script para limpiar y generar los dataset de entrenamiento y pruebas.
- **training_model:** Script para entrenar el modelo.
- **test_model:** Script para testear la predicción del modelo.

Puedes modificar y ejecutar los script para ajustar el modelo.

**Nota:** Al entrenar nuevamente el modelo, ejecutando el archivo **training_model**, el script generará dos estructuras:

- **colors_model.keras** modelo utilizado para la detección en desktop.
- **tf_model:** Un directorio con la estructura del modelo utilizado para la detección web. Para esté último debes hacer una conversión a **graph model** ejecutando, en el terminal y en el directorio model, el siguiente comando:

```
tensorflowjs_converter --input_format=tf_saved_model --output_format=tfjs_graph_model tf_model tfjs_model

```
