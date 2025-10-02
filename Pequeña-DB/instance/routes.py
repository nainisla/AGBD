from flask import Blueprint, request, jsonify
from models import db, Contacto, Usuario, Salon, Evento, Servicio, EventoServicio, Pago
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

routes = Blueprint('routes', __name__)

# **********************************************
# DECORADORES DE SEGURIDAD (NUEVO)
# **********************************************

def admin_required(f):
    """Verifica si el usuario es un administrador y está logueado."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # El frontend debe enviar estos headers
        user_id = request.headers.get('User-Id')
        user_role = request.headers.get('User-Role')

        if not user_id or user_role != 'admin':
            return jsonify({"mensaje": "Acceso denegado: Rol de administrador requerido."}), 403

        # Opcional: Verificar que el ID sea real (buena práctica)
        usuario = Usuario.query.get(user_id)
        if not usuario or usuario.rol != 'admin':
            return jsonify({"mensaje": "Acceso denegado: Usuario inválido o rol incorrecto."}), 403

        return f(*args, **kwargs)
    return decorated_function

# **********************************************
# APLICACIÓN DEL DECORADOR
# **********************************************

# USUARIOS - Ahora protegida
@routes.route('/usuarios', methods=['GET'])
@admin_required  # <--- Aplicamos el decorador aquí
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([
        {"id": u.id, "nombre": u.nombre, "email": u.email, "rol": u.rol}
        for u in usuarios
    ])


# **********************************************
# RUTA: LOGIN
# **********************************************
@routes.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if not email or not password or not role:
        return jsonify({"mensaje": "Faltan correo electrónico, contraseña o rol"}), 400

    # 1. Buscar el usuario por email
    usuario = Usuario.query.filter_by(email=email).first()

    # 2. Verificar usuario y contraseña (usando el hash)
    if usuario and check_password_hash(usuario.password, password) and usuario.rol == role:
        # Autenticación exitosa
        return jsonify({
            "mensaje": "Inicio de sesión exitoso",
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "rol": usuario.rol  # Devolvemos el rol, que es clave para el frontend
        }), 200
    else:
        # Autenticación fallida
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

# **********************************************
# RUTAS PARA USUARIOS
# **********************************************
@routes.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    # Hashing de la contraseña antes de guardarla
    hashed_password = generate_password_hash(data['password'])
    usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        password=hashed_password,
        rol=data['rol']
    )
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado"}), 201

@routes.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.json
    usuario.nombre = data.get("nombre", usuario.nombre)
    usuario.email = data.get("email", usuario.email)
    if "password" in data:
        usuario.password = generate_password_hash(data["password"], method='pbkdf2:sha256')
    usuario.rol = data.get("rol", usuario.rol)
    db.session.commit()
    return jsonify({"mensaje": "Usuario actualizado"})

@routes.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario eliminado"})

# **********************************************
# RUTAS PARA SALONES
# **********************************************
@routes.route('/salones', methods=['POST'])
def crear_salon():
    data = request.json
    salon = Salon(nombre=data['nombre'], direccion=data.get('direccion'), capacidad=data.get('capacidad'))
    db.session.add(salon)
    db.session.commit()
    return jsonify({"mensaje": "Salón creado"}), 201

@routes.route('/salones', methods=['GET'])
def listar_salones():
    salones = Salon.query.all()
    return jsonify([{"id": s.salon_id, "nombre": s.nombre, "direccion": s.direccion, "capacidad": s.capacidad} for s in salones])

@routes.route('/salones/<int:id>', methods=['PUT'])
def actualizar_salon(id):
    salon = Salon.query.get_or_404(id)
    data = request.json
    salon.nombre = data.get("nombre", salon.nombre)
    salon.direccion = data.get("direccion", salon.direccion)
    salon.capacidad = data.get("capacidad", salon.capacidad)
    db.session.commit()
    return jsonify({"mensaje": "Salón actualizado"})

@routes.route('/salones/<int:id>', methods=['DELETE'])
def eliminar_salon(id):
    salon = Salon.query.get_or_404(id)
    db.session.delete(salon)
    db.session.commit()
    return jsonify({"mensaje": "Salón eliminado"})

# **********************************************
# RUTAS PARA EVENTOS
# **********************************************
@routes.route('/eventos', methods=['POST'])
@admin_required  # <--- Aplicamos el decorador aquí
def crear_evento():
    data = request.json
    evento = Evento(
        nombre_evento=data['nombre_evento'],
        fecha=datetime.strptime(data['fecha'], "%Y-%m-%d"),
        tema=data.get('tema'),
        informe_detallado=data.get('informe_detallado'),
        salon_id=data['salon_id'],
        cliente_id=data['cliente_id']
    )
    db.session.add(evento)
    db.session.commit()
    return jsonify({"mensaje": "Evento creado exitosamente", "id": evento.evento_id}), 201

@routes.route('/eventos', methods=['GET'])
def listar_eventos():
    eventos = Evento.query.all()
    return jsonify([
        {
            "id": e.evento_id,
            "nombre_evento": e.nombre_evento,
            "fecha": e.fecha.isoformat(),
            "tema": e.tema,
            "informe_detallado": e.informe_detallado,
            "salon": e.salon.nombre,
            "cliente": e.usuario.nombre
        } for e in eventos
    ])

@routes.route('/eventos/<int:id>', methods=['PUT'])
def actualizar_evento(id):
    evento = Evento.query.get_or_404(id)
    data = request.json
    evento.nombre_evento = data.get("nombre_evento", evento.nombre_evento)
    if "fecha" in data:
        evento.fecha = datetime.strptime(data["fecha"], "%Y-%m-%d")
    evento.tema = data.get("tema", evento.tema)
    evento.informe_detallado = data.get("informe_detallado", evento.informe_detallado)
    db.session.commit()
    return jsonify({"mensaje": "Evento actualizado"})

@routes.route('/eventos/<int:id>', methods=['DELETE'])
def eliminar_evento(id):
    evento = Evento.query.get_or_404(id)
    db.session.delete(evento)
    db.session.commit()
    return jsonify({"mensaje": "Evento eliminado"})

# **********************************************
# RUTAS PARA SERVICIOS
# **********************************************
@routes.route('/servicios', methods=['POST'])
def crear_servicio():
    data = request.json
    servicio = Servicio(nombre_servicio=data['nombre_servicio'], descripcion=data.get('descripcion'), costo=data.get('costo'))
    db.session.add(servicio)
    db.session.commit()
    return jsonify({"mensaje": "Servicio creado"}), 201

@routes.route('/servicios', methods=['GET'])
def listar_servicios():
    servicios = Servicio.query.all()
    return jsonify([{"id": s.servicio_id, "nombre_servicio": s.nombre_servicio, "descripcion": s.descripcion, "costo": str(s.costo)} for s in servicios])

@routes.route('/servicios/<int:id>', methods=['PUT'])
def actualizar_servicio(id):
    servicio = Servicio.query.get_or_404(id)
    data = request.json
    servicio.nombre_servicio = data.get("nombre_servicio", servicio.nombre_servicio)
    servicio.descripcion = data.get("descripcion", servicio.descripcion)
    servicio.costo = data.get("costo", servicio.costo)
    db.session.commit()
    return jsonify({"mensaje": "Servicio actualizado"})

@routes.route('/servicios/<int:id>', methods=['DELETE'])
def eliminar_servicio(id):
    servicio = Servicio.query.get_or_404(id)
    db.session.delete(servicio)
    db.session.commit()
    return jsonify({"mensaje": "Servicio eliminado"})

# **********************************************
# RUTAS PARA CONECTAR EVENTOS Y SERVICIOS
# **********************************************
@routes.route('/eventos/<int:evento_id>/servicios', methods=['POST'])
def asignar_servicio(evento_id):
    data = request.json
    evento_servicio = EventoServicio(evento_id=evento_id, servicio_id=data['servicio_id'])
    db.session.add(evento_servicio)
    db.session.commit()
    return jsonify({"mensaje": "Servicio asignado al evento"}), 201

@routes.route('/eventos/<int:evento_id>/servicios', methods=['GET'])
def listar_servicios_evento(evento_id):
    servicios = EventoServicio.query.filter_by(evento_id=evento_id).all()
    return jsonify([
        {"servicio": s.servicio.nombre_servicio, "descripcion": s.servicio.descripcion, "costo": str(s.servicio.costo)}
        for s in servicios
    ])

@routes.route('/eventos_servicios/<int:id>', methods=['DELETE'])
def eliminar_evento_servicio(id):
    es = EventoServicio.query.get_or_404(id)
    db.session.delete(es)
    db.session.commit()
    return jsonify({"mensaje": "Servicio eliminado del evento"})

# **********************************************
# RUTAS PARA PAGOS
# **********************************************
@routes.route('/pagos', methods=['POST'])
def registrar_pago():
    data = request.json
    pago = Pago(
        evento_id=data['evento_id'],
        monto=data['monto'],
        fecha_pago=datetime.strptime(data['fecha_pago'], "%Y-%m-%d"),
        metodo=data.get('metodo')
    )
    db.session.add(pago)
    db.session.commit()
    return jsonify({"mensaje": "Pago registrado"}), 201

@routes.route('/pagos', methods=['GET'])
def listar_pagos():
    pagos = Pago.query.all()
    return jsonify([
        {"id": p.pago_id, "evento": p.evento.nombre_evento, "monto": str(p.monto), "fecha_pago": p.fecha_pago.isoformat(), "metodo": p.metodo}
        for p in pagos
    ])

@routes.route('/pagos/<int:id>', methods=['PUT'])
def actualizar_pago(id):
    pago = Pago.query.get_or_404(id)
    data = request.json
    pago.monto = data.get("monto", pago.monto)
    if "fecha_pago" in data:
        pago.fecha_pago = datetime.strptime(data["fecha_pago"], "%Y-%m-%d")
    pago.metodo = data.get("metodo", pago.metodo)
    db.session.commit()
    return jsonify({"mensaje": "Pago actualizado"})

@routes.route('/pagos/<int:id>', methods=['DELETE'])
def eliminar_pago(id):
    pago = Pago.query.get_or_404(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify({"mensaje": "Pago eliminado"})

# **********************************************
# RUTA PARA CONTACTO
# **********************************************
@routes.route('/contacto', methods=['POST'])
def enviar_contacto():
    data = request.json
    contacto = Contacto(
         nombre_completo=data['nombreCompleto'],
         email=data['email'],
         celular=data.get('celular'),
         tipo_evento=data.get('tipoEvento'),
         cantidad_personas=data.get('cantidadPersonas'),
         fecha_inicio=datetime.strptime(data['fechaInicio'], "%Y-%m-%d"),
         fecha_fin=datetime.strptime(data['fechaFin'], "%Y-%m-%d"),
         mensaje=data.get('mensaje')
    )
    db.session.add(contacto)
    db.session.commit()
    return {"mensaje": "Mensaje recibido, un ejecutivo se contactará a la brevedad."}, 201

# **********************************************
# RUTA DE BIENVENIDA
# **********************************************
@routes.route('/')
def home():
    return {"mensaje": "Bienvenido a la API del sistema de gestión de salones y eventos"}
