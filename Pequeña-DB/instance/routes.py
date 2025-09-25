from flask import Blueprint, request, jsonify
from models import db, Usuario, Salon, Evento, Servicio, EventoServicio, Pago
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

routes = Blueprint('routes', __name__)


# USUARIOS

@routes.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    # Hashing de la contraseña antes de guardarla
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        password=hashed_password,
        rol=data['rol']
    )
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado"}), 201

@routes.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([
        {"id": u.id, "nombre": u.nombre, "email": u.email, "rol": u.rol}
        for u in usuarios
    ])

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

# LOGIN

@routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = Usuario.query.filter_by(email=data.get("email")).first()

    # Se agrego la validacion del rol, para que solo pueda ingresar si el email, la contraseña y el rol coinciden
    if user and check_password_hash(user.password, data.get("password")) and user.rol == data.get("role"):
        return jsonify({
            "token": "fake-jwt-token",
            "role": user.rol
        })
    else:
        return jsonify({"message": "Credenciales inválidas"}), 401


#SALONES

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


# EVENTOS

@routes.route('/eventos', methods=['POST'])
def crear_evento():
    data = request.json
    evento = Evento(
        nombre_evento=data['nombre_evento'],
        fecha=datetime.strptime(data['fecha'], "%Y-%m-%d"),
        tema=data.get('tema'),
        informe_detallado=data.get('informe_detallado'),
        salon_id=data['salon_id'],
        usuario_id=data['cliente_id']
    )
    db.session.add(evento)
    db.session.commit()
    return jsonify({"mensaje": "Evento creado"}), 201

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


# SERVICIOS

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


#CONECTA (eventos_servicios)

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


# PAGOS

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

@routes.route('/usuarios/<int:id>/sumar_puntos', methods=['POST'])
def sumar_puntos(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.json
    puntos = data.get("puntos", 0)
    
    if puntos <= 0:
        return jsonify({"mensaje": "Los puntos deben ser mayores a 0"}), 400
    
    usuario.puntos_fidelidad += puntos
    db.session.commit()
    
    return jsonify({
        "mensaje": f"{puntos} puntos sumados a {usuario.nombre}",
        "puntos_totales": usuario.puntos_fidelidad
    })
