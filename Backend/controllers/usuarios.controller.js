"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.editarUsuario = exports.editarContrasena = exports.crearUsuario = exports.obtenerUsuarioPorId = exports.obtenerUsuario = exports.obtenerUsuarios = void 0;
const usuarios_model_1 = require("../models/usuarios.model");
function handleError(error) {
    // Tu código para manejar el error
}
//obtener todos los usuarios
const obtenerUsuarios = (req, res) => {
    usuarios_model_1.usuarioSchema.find().then(result => {
        res.json(result);
    }).catch(error => {
        res.status(500).json(error);
    });
};
exports.obtenerUsuarios = obtenerUsuarios;
//obtener usuario segun correo y contrasena
const obtenerUsuario = (req, res) => {
    const email = req.body.correo;
    const password = req.body.contrasena;
    console.log(req.body);
    usuarios_model_1.usuarioSchema.findOne({ email: email, password: password }).then(result => {
        if (result != null) {
            res.json(result);
            console.log(result.correo + " " + result.password);
        }
        else {
            res.json("no encontrado");
        }
    }).catch(error => {
        res.status(500).json(error);
    });
};
exports.obtenerUsuario = obtenerUsuario;
//obtener usuario segun id
const obtenerUsuarioPorId = (req, res) => {
    const id = req.body;
    console.log(id.id);
    usuarios_model_1.usuarioSchema.find({ id: id.id }).then(result => {
        res.json(result);
        console.log(result);
    }).catch(error => {
        res.status(500).json(error);
    });
};
exports.obtenerUsuarioPorId = obtenerUsuarioPorId;
//añadir un usuario
const crearUsuario = (req, res) => {
    console.log(req.body);
    const usuario = new usuarios_model_1.usuarioSchema(req.body);
    usuario.save().then(result => {
        res.json(result);
    }).catch(error => {
        res.status(500).json(error);
    });
};
exports.crearUsuario = crearUsuario;
//editar contraseña de un usuario
const editarContrasena = (req, res) => {
    const usuario = new usuarios_model_1.usuarioSchema(req.body);
    console.log(usuario);
    usuarios_model_1.usuarioSchema.findOneAndUpdate({ id: usuario.id }, { contrasena: usuario.contrasena }).then(result => {
        res.json(result);
    }).catch(error => {
        res.status(500).json(error);
    });
};
exports.editarContrasena = editarContrasena;
//editar un usuario
const editarUsuario = (req, res) => {
    const usuario = new usuarios_model_1.usuarioSchema(req.body);
    console.log(usuario);
    usuarios_model_1.usuarioSchema.findOneAndUpdate({ id: usuario.id }, { nombre: usuario.nombre, correo: usuario.correo, apellido: usuario.apellido, telefono: usuario.telefono, direccion: usuario.direccion }).then(result => {
        res.json(result);
    }).catch(error => {
        res.status(500).json(error);
    });
};
exports.editarUsuario = editarUsuario;
