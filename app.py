from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


# Endpoint del chatbot
@app.route('/chat', methods=['POST'])
def chat():
    # Obtener el mensaje del usuario desde la solicitud
    user_message = request.json['message']

    # Definir el modelo que se utilizará
    model = "llama3.2"

    # Ejecutar el comando de Ollama en el terminal y obtener la respuesta
    try:
        result = subprocess.run(
            ["ollama", "run", model, user_message], 
            capture_output=True,  # Captura la salida estándar y los errores
            text=True  # Devuelve la salida como texto, no como bytes
        )
        
        # Verificar si el comando fue exitoso
        if result.returncode == 0:
            response_text = result.stdout.strip()  # Elimina espacios innecesarios
            return jsonify({'response': response_text})
        else:
            # En caso de que el comando falle, devolver el error
            return jsonify({'error': result.stderr.strip()}), 500
    
    except Exception as e:
        # Si hay un error al ejecutar el comando, se captura aquí
        return jsonify({'error': str(e)}), 500

# Endpoint de estado
@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'OK', 'message': 'El servidor está en funcionamiento correcto'})

if __name__ == '__main__':
    app.run(debug=True)

