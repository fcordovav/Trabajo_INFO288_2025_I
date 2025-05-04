from flask import Flask, request, jsonify
import os
import mysql.connector


app = Flask(__name__)
puerto = int(os.environ.get("PORT"))
host = os.environ.get("IP")
tipo_documento_esclavo = os.environ.get("TIPO_DOCUMENTO")


# Configuración de la conexión
db_config = {
    "host": "localhost",
    "user": "user",  # usuario de la base de datos
    "password": "1234",  # Cambiar según la contraseña configurada
    "database": "problema1_SD"  # nombre de la base de datos
}


try:
    # Establecer conexión
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    print("Conexión a la base de datos MariaDB exitosa.")
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
    connection = None



# Ejemplo de documentos en la base de datos para probar
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

# Solo documentos que corresponden al tipo de este esclavo
DOCUMENTOS = [doc for doc in DOCUMENTOS_TODOS if doc["tipo"] == tipo_documento_esclavo]


@app.route("/query", methods=["GET"])
def query():
    titulo = request.args.get("titulo")
    
    # Si no se recibe título o está vacío, devolver todos los documentos
    if not titulo or titulo.strip() == "":
        # Agregar ranking 1 a todos los documentos cuando no hay búsqueda por título
        resultados = [dict(doc, ranking=1) for doc in DOCUMENTOS]
        return jsonify({"resultados": resultados})
    
    # Búsqueda por título (implementación existente)
    palabras_busqueda = titulo.lower().split()
    resultados = []
    for doc in DOCUMENTOS:
        score = sum(1 for palabra in palabras_busqueda if palabra in doc["titulo"].lower())
        if score > 0:
            doc_resultado = dict(doc)
            doc_resultado["ranking"] = score
            resultados.append(doc_resultado)
    return jsonify({"resultados": resultados})
    

if __name__ == "__main__":
    print(f"Esclavo corriendo en puerto http://{host}:{puerto} tipo={tipo_documento_esclavo}")
    app.run(host=host, port=puerto)
