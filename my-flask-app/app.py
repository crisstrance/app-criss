from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Ruta para la API
@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'API is working!'})

# Ruta para servir el frontend
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)