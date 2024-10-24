from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO
from utils import socketio, send_message_to_js
from modules.renderMaps import render_maps


app = Flask(__name__)
# socketio = SocketIO(app)
socketio.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


# def send_message_to_js(message):
#     socketio.emit('py-js_communication', message)





@app.route('/send_coordinates', methods=['POST'])
def send_coordinates():
    print('Coordinates receiving')
    data = request.json
    coordinates_list = data.get('coordinates_list')
    config = data.get('config')
    

    # print(f'Coordinates received: {coordinates_list}')
    # print(f'Config received: {config}')

    # Generate the file (ZIP, PDF, or PNG)
    Maps, file_type = render_maps(coordinates_list, config)
    
    # Determine MIME type and download name based on file type
    if file_type == 'zip':
        mimetype = 'application/zip'
        download_name = 'MyMaps.zip'
    elif file_type == 'pdf':
        mimetype = 'application/pdf'
        download_name = 'MyMaps.pdf'
    elif file_type == 'png':
        mimetype = 'image/png'
        download_name = 'MyMaps.png'
    else:
        print('Unknown file type')

    
    return send_file(Maps, mimetype=mimetype, as_attachment=True, download_name=download_name)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()