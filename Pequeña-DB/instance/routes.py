from flask import Blueprint, request, jsonify
from models import db, Cliente, Salon, Evento, Servicio, EventoServicio, Pago
from datetime import datetime

routes = Blueprint('routes', __name__)


# CLIENTES

@routes.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.json
    cliente = Cliente(nombre=data['nombre'], telefono=data.get('telefono'), email=data.get('email'))
    db.session.add(cliente)
    db.session.commit()
    return jsonify({"mensaje": "Cliente creado"}), 201

@routes.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([{"id": c.cliente_id, "nombre": c.nombre, "telefono": c.telefono, "email": c.email} for c in clientes])

@routes.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    data = request.json
    cliente.nombre = data.get("nombre", cliente.nombre)
    cliente.telefono = data.get("telefono", cliente.telefono)
    cliente.email = data.get("email", cliente.email)
    db.session.commit()
    return jsonify({"mensaje": "Cliente actualizado"})

@routes.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"mensaje": "Cliente eliminado"})


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
        cliente_id=data['cliente_id']
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
            "cliente": e.cliente.nombre
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