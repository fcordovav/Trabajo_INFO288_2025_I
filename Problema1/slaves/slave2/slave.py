from flask import Flask, request, jsonify
import os
from datetime import datetime
from dotenv import load_dotenv
import mysql.connector

# Cargar variables del .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

# Obtener variables
puerto = int(os.environ.get("PORT"))
host = os.environ.get("IP")
tipo_documento_esclavo = os.environ.get("TIPO_DOCUMENTO")
db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")

# Configuración DB
db_config = {
    "host": db_host,
    "user": db_user,
    "password": db_password,
    "database": db_name
}

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    print("Conexión a la base de datos exitosa.")
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
    connection = None

@app.route("/query", methods=["GET"])
def query():
    timestamp_ini = datetime.now().isoformat()
    titulo = request.args.get("titulo")
    resultados = []

    try:
        if connection is None:
            return jsonify({"error": "No hay conexión a la base de datos"}), 500

        if titulo and titulo.strip():
            palabras_busqueda = [p.lower() for p in titulo.split()]
            print(f"Palabras de búsqueda: {palabras_busqueda}")

            # Traer todos los documentos del tipo
            sql = f"SELECT *, 0 AS ranking FROM {tipo_documento_esclavo};"
            cursor.execute(sql)
            docs = cursor.fetchall()

            # Calcular ranking para cada documento
            for doc in docs:
                palabras_titulo = [p.lower() for p in doc["titulo"].split()]
                for palabra in palabras_busqueda:
                    if palabra in palabras_titulo:
                        doc["ranking"] += 1
            
            # Filtrar documentos con ranking > 0 y ordenar
            resultados = [doc for doc in docs if doc["ranking"] > 0]
            resultados.sort(key=lambda x: x["ranking"], reverse=True)
        else:
            # Si no hay título, traer todos los del tipo
            sql = f"SELECT *, 1 AS ranking FROM {tipo_documento_esclavo};"
            cursor.execute(sql)
            resultados = cursor.fetchall()

    except mysql.connector.Error as err:
        return jsonify({"error": f"Error en consulta a la base de datos: {err}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {e}"}), 500

    timestamp_fin = datetime.now().isoformat()
    log_line = f"{timestamp_ini},{timestamp_fin},{host},{puerto},{tipo_documento_esclavo},{titulo if titulo else 'TODOS'}\n"
    log_file = os.path.join(os.path.dirname(__file__), "log.txt")
    with open(log_file, "a") as f:
        f.write(log_line)

    return jsonify({"resultados": resultados})

if __name__ == "__main__":
    print(f"Esclavo corriendo en http://{host}:{puerto} tipo={tipo_documento_esclavo}")
    app.run(host=host, port=puerto)