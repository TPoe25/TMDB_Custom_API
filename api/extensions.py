from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

# Initialize the SQLAlchemy extension with a default SQLite database URI
db = SQLAlchemy()

# Initialize the socketIO extension with CORS settings
socketio = SocketIO(cors_allowed_origins"*")
