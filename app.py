import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import cloudinary
import cloudinary.uploader

app = Flask(__name__, template_folder='.', static_folder='.')

# CONFIGURACIÓN LIMPIA (Sin caracteres ocultos)
cloudinary.config( 
    cloud_name = "dlszw4utt", 
    api_key = "651939736339191", 
    api_secret = "sNjw0vO0dykSgexKuXV1TzbkV2k", 
    secure = True
)

urls_guardadas = []

@app.route('/')
def index():
    return render_template('index.html', enlaces=urls_guardadas)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        # Esto subirá la imagen a tu cuenta dlszw4utt
        res = cloudinary.uploader.upload(file, resource_type="auto")
        urls_guardadas.append({'url': res['secure_url'], 'tipo': res['resource_type']})
    return redirect(url_for('index'))

# RUTA ÚNICA PARA ARCHIVOS (CSS, JS, GIF)
# Esto arregla el fondo blanco de golpe
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)
@app.route('/delete/<int:indice>')
def delete_file(indice):

    if 0 <= indice < len(urls_guardadas):
        # 1. Obtenemos el Public ID de Cloudinary (necesario para borrar allá)
        # El ID se saca de la URL: es lo que está entre la última '/' y la extensión
        imagen = urls_guardadas[indice]
        public_id = imagen['url'].split('/')[-1].split('.')[0]
        
        # 2. Borramos en Cloudinary
        cloudinary.uploader.destroy(public_id)
        
        # 3. Borramos de nuestra lista local
        urls_guardadas.pop(indice)
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)