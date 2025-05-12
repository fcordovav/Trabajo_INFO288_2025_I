from flask import Flask, request, jsonify
import os
from datetime import datetime
import time
from dotenv import load_dotenv
import mysql.connector

# Cargar variables del .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

# Obtener variables
puerto = int(os.environ.get("PORT"))
host = os.environ.get("IP")
id_maquina = os.environ.get("ID")
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

users_db_config = {
    "host": db_host,
    "user": db_user,
    "password": db_password,
    "database": "users"
}

try:
    users_connection = mysql.connector.connect(**users_db_config)
    users_cursor = users_connection.cursor(dictionary=True)
    print("Conexión a la base de datos de usuarios exitosa.")
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos de usuarios: {err}")
    users_connection = None

# Prueba de conexión
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
    start_time = time.time()
    titulo = request.args.get("titulo")
    edad = request.args.get("edad")
    resultados = []
    total_score = 0

    try:
        if connection is None:
            return jsonify({"error": "No hay conexión a la base de datos"}), 500

        if titulo and titulo.strip():
            palabras_busqueda = [p.lower() for p in titulo.split()]
            print(f"Palabras de búsqueda: {palabras_busqueda}")

            # Traer todos los documentos del tipo
            sql = f"SELECT titulo, category_id, 0 AS ranking FROM {tipo_documento_esclavo};"
            cursor.execute(sql)
            docs = cursor.fetchall()

            # Calcular ranking para cada documento
            for doc in docs:
                palabras_titulo = [p.lower() for p in doc["titulo"].split()]
                for palabra in palabras_busqueda:
                    if palabra in palabras_titulo:
                        doc["ranking"] += 1

            
            # Filtrar documentos con ranking mayor a 0
            resultados = [doc for doc in docs if doc["ranking"] > 0]
           
            #  Procesar resultados
            for doc in resultados:
                category_id = doc["category_id"]

                # Consulta en la base de datos de usuarios
                query = """
                    SELECT u.nombre
                    FROM users u
                    JOIN user_categories uc ON u.id = uc.user_id
                    WHERE uc.category_id = %s AND %s BETWEEN u.edad_min AND u.edad_max
                    LIMIT 1
                """
                
                users_cursor.execute(query, (category_id, edad))
                match = users_cursor.fetchone()

                if match:
                    doc["ranking"] += 1
                    doc["rango_etario"] = match["nombre"]


            # Score → suma de los rankings
            total_score = sum(doc["ranking"] for doc in resultados)
            resultados.sort(key=lambda x: x["ranking"], reverse=True)

        else:
            # Si no hay título, traer todos los del tipo
            sql = f"SELECT *, 1 AS ranking FROM {tipo_documento_esclavo};"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            total_score = sum(doc["ranking"] for doc in resultados)

    except mysql.connector.Error as err:
        return jsonify({"error": f"Error en consulta a la base de datos: {err}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {e}"}), 500

    timestamp_fin = datetime.now().isoformat()
    end_time = time.time()
    tiempo_total_ms = round((end_time - start_time) * 1000, 2)  # tiempo en milisegundos

    log_line = f"{timestamp_ini},{timestamp_fin},{id_maquina},{tipo_documento_esclavo},{titulo if titulo else {tipo_documento_esclavo}},{tiempo_total_ms},{total_score}\n"
    log_file = os.path.join(os.path.dirname(__file__), "log.txt")
    with open(log_file, "a") as f:
        f.write(log_line)

    return jsonify({"resultados": resultados})

if __name__ == "__main__":
    print(f"Esclavo corriendo en http://{host}:{puerto} tipo={tipo_documento_esclavo}")
    app.run(host=host, port=puerto)