from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from ..database import mongo

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/", methods=["POST"])
def criar_usuario():
    data = request.get_json()
    if not data.get("nome") or not data.get("email") or not data.get("idade"):
        return jsonify({"erro": "Dados incompletos"}), 400

    usuario_id = mongo.db.usuarios.insert_one({
        "nome": data["nome"],
        "email": data["email"],
        "idade": data["idade"]
    }).inserted_id

    return jsonify({"id": str(usuario_id), "mensagem": "Usuário criado com sucesso!"}), 201

@usuarios_bp.route("/", methods=["GET"])
def listar_usuarios():
    usuarios = []
    for u in mongo.db.usuarios.find():
        usuarios.append({
            "id": str(u["_id"]),
            "nome": u["nome"],
            "email": u["email"],
            "idade": u["idade"]
        })
    return jsonify(usuarios), 200

@usuarios_bp.route("/<id>", methods=["GET"])
def consultar_usuario(id):
    usuario = mongo.db.usuarios.find_one({"_id": ObjectId(id)})
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    return jsonify({
        "id": str(usuario["_id"]),
        "nome": usuario["nome"],
        "email": usuario["email"],
        "idade": usuario["idade"]
    }), 200