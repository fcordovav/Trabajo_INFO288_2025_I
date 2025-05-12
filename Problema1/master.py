# master.py
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

load_dotenv()

# Lista de URLs y tipo de los esclavos
slaves = [
    {"url": os.getenv("URL1"), "tipo": os.getenv("TIPO_DOCUMENTO1")},
    {"url": os.getenv("URL2"), "tipo": os.getenv("TIPO_DOCUMENTO2")},
    {"url": os.getenv("URL3"), "tipo": os.getenv("TIPO_DOCUMENTO3")},
    {"url": os.getenv("URL4"), "tipo": os.getenv("TIPO_DOCUMENTO4")},
]


@app.route('/query', methods=['GET'])
def query():
    try:
        titulo = request.args.get('titulo')  # parámetro título
        tipo_doc = request.args.get('tipo_doc')  # parámetro tipo_doc
        edad = request.args.get('edad')  # parámetro edad

        #Búsqueda por titulo
        if titulo: 
            resultados = []
            for esclavo in slaves:  
                response = requests.get(esclavo["url"], params={'titulo': titulo, 'edad': edad})
                resultados.extend(response.json()['resultados'])
            resultados.sort(key=lambda x: x['ranking'], reverse=True)
            return jsonify(resultados)
        

        # Búsqueda por tipo de documento
        elif tipo_doc:
            resultados = []
            tipos_docs = tipo_doc.split(' ')  
            
            # Filtrar esclavos según los tipos de documentos solicitados
            esclavos_seleccionados = [esclavo for esclavo in slaves if esclavo["tipo"] in tipos_docs]
            
            # Consultar solo a los esclavos que manejan los tipos de documentos solicitados
            for esclavo in esclavos_seleccionados:
                print(f"Consultando esclavo {esclavo['url']} para tipo_doc: {esclavo['tipo']}")
                try:
                    response = requests.get(esclavo["url"], params={'titulo': ''}) 
                    if 'resultados' in response.json():
                        resultados.extend(response.json()['resultados'])
                except Exception as e:
                    print(f"Error al consultar esclavo {esclavo['url']}: {str(e)}")
            
           
                
            return jsonify(resultados)

        # Si no se recibe ni tipo_doc ni titulo, retornar un error
        else:
            return jsonify({"Error": 'No se especificó operación'})


    except Exception as e:
        return jsonify({"Error": str(e)})


if __name__ == '__main__':
    app.run(port=5000)
