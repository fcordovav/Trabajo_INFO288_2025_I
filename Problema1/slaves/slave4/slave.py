from flask import Flask, request, jsonify
import os
from datetime import datetime
from dotenv import load_dotenv
import mysql.connector

# Cargar las variables de entorno desde el archivo .env en la misma carpeta que este script
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

# Obtener variables de entorno
puerto = int(os.environ.get("PORT"))
host = os.environ.get("IP")
tipo_documento_esclavo = os.environ.get("TIPO_DOCUMENTO")
db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")

# Configuración de la conexión
db_config = {
    "host": db_host,  # dirección IP del servidor de la base de datos
    "user": db_user,  # usuario de la base de datos
    "password": db_password,  # Cambiar según la contraseña configurada
    "database": db_name # nombre de la base de datos
}

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    print("Conexión a la base de datos MariaDB exitosa.")
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
    connection = None

DOCUMENTOS_TODOS = [
    {"titulo": "Ecuaciones diferenciales básicas", "tipo": "libro"},
    {"titulo": "Introducción a las ecuaciones diferenciales", "tipo": "tesis"},
    {"titulo": "Física cuántica explicada", "tipo": "video"},
    {"titulo": "Artículo sobre inteligencia artificial", "tipo": "articulo"},
    {"titulo": "Guía de programación en Python", "tipo": "libro"},
    {"titulo": "Tesis sobre aprendizaje automático", "tipo": "tesis"},
    {"titulo": "Documental sobre el espacio", "tipo": "video"},
    {"titulo": "Investigación en biotecnología", "tipo": "articulo"},
]

# Filtrar documentos por tipo
DOCUMENTOS = [doc for doc in DOCUMENTOS_TODOS if doc["tipo"] == tipo_documento_esclavo]


@app.route("/query", methods=["GET"])
def query():
    timestamp_ini = datetime.now().isoformat()
    titulo = request.args.get("titulo")
    resultados = []
    
    if not titulo or titulo.strip() == "":
        resultados = [dict(doc, ranking=1) for doc in DOCUMENTOS]
    else:
        palabras_busqueda = titulo.lower().split()
        for doc in DOCUMENTOS:
            score = sum(1 for palabra in palabras_busqueda if palabra in doc["titulo"].lower())
            if score > 0:
                doc_resultado = dict(doc)
                doc_resultado["ranking"] = score
                resultados.append(doc_resultado)

    timestamp_fin = datetime.now().isoformat()

    # Construir línea de log
    log_line = f"{timestamp_ini},{timestamp_fin},{host},{puerto},{tipo_documento_esclavo},{titulo if titulo else 'TODOS LOS TIPOS'}\n"

    # Guardar log en archivo
    log_file = os.path.join(os.path.dirname(__file__), "log.txt")
    with open(log_file, "a") as f:
        f.write(log_line)

    return jsonify({"resultados": resultados})


if __name__ == "__main__":
    print(f"Esclavo corriendo en http://{host}:{puerto} tipo={tipo_documento_esclavo}")
    app.run(host=host, port=puerto)
