from flask_socketio import SocketIO

socketio = SocketIO()

def send_message_to_js(message):
    socketio.emit('py-js_communication', message)