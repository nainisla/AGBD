from config import db
from datetime import datetime


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    puntos_fidelidad = db.Column(db.Integer, default=0)
    # Relación con eventos
    eventos = db.relationship('Evento', backref='usuario', lazy=True)

class Salon(db.Model):
    __tablename__ = 'salones'
    salon_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255))
    capacidad = db.Column(db.Integer)

    eventos = db.relationship('Evento', backref='salon', lazy=True)

class Evento(db.Model):
    __tablename__ = 'eventos'
    evento_id = db.Column(db.Integer, primary_key=True)
    nombre_evento = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    tema = db.Column(db.String(255))
    informe_detallado = db.Column(db.Text)

    salon_id = db.Column(db.Integer, db.ForeignKey('salones.salon_id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    pagos = db.relationship('Pago', backref='evento', lazy=True)
    servicios = db.relationship('EventoServicio', backref='evento', lazy=True)

class Servicio(db.Model):
    __tablename__ = 'servicios'
    servicio_id = db.Column(db.Integer, primary_key=True)
    nombre_servicio = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    costo = db.Column(db.Numeric(10, 2))

    eventos = db.relationship('EventoServicio', backref='servicio', lazy=True)

class EventoServicio(db.Model):
    __tablename__ = 'eventos_servicios'
    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.evento_id'), nullable=False)
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicios.servicio_id'), nullable=False)

class Pago(db.Model):
    __tablename__ = 'pagos'
    pago_id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.evento_id'), nullable=False)
    monto = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_pago = db.Column(db.Date, nullable=False)
    metodo = db.Column(db.String(50))

class Contacto(db.Model):
    __tablename__ = 'contactos'
    contacto_id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(50))
    tipo_evento = db.Column(db.String(100))
    cantidad_personas = db.Column(db.Integer)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    mensaje = db.Column(db.Text)
    fecha_envio = db.Column(db.DateTime, default=datetime.utcnow)
