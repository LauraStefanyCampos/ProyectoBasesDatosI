import {Request, Response} from 'express';
import { usuarioSchema } from '../models/usuarios.model';


function handleError(error: Error) {
    // Tu código para manejar el error
  }
  
//obtener todos los usuarios
export const obtenerUsuarios = (req: Request, res: Response) => {
    usuarioSchema.find().then(result => {
        res.json(result);
    }).catch(error => {
        res.status(500).json(error);
    });
}

//obtener usuario segun correo y contrasena
export const obtenerUsuario = (req: Request, res: Response) => {
    const email = req.body.correo;
    const password = req.body.contrasena;
    console.log(req.body);
    usuarioSchema.findOne({email: email, password: password}).then(result => {
        if(result != null){
            res.json(result);
            console.log(result.correo + " " + result.password);
        }
        else{
            res.json("no encontrado");
        }
    }).catch(error => {
        res.status(500).json(error);
    });
}

//obtener usuario segun id
export const obtenerUsuarioPorId = (req: Request, res: Response) => {
    const id = req.body;
    console.log(id.id);
    usuarioSchema.find({id: id.id}).then(result => {
            res.json(result);
            console.log(result)
    }).catch(error => {
        res.status(500).json(error);
    });
}

//añadir un usuario
export const crearUsuario = (req: Request, res: Response) => {
    console.log(req.body);
    const usuario = new usuarioSchema(req.body);
    usuario.save().then(result => {
        res.json(result);
    }).catch(error => {
        res.status(500).json(error);
    });
}

//editar contraseña de un usuario
export const editarContrasena = (req: Request, res: Response) => {
    const usuario = new usuarioSchema(req.body);

    console.log(usuario);
    usuarioSchema.findOneAndUpdate({id: usuario.id}, {contrasena: usuario.contrasena}).then(result => {
        res.json(result);
    }).catch(error => {
        res.status(500).json(error);
    });
}

//editar un usuario
export const editarUsuario = (req: Request, res: Response) => {
    const usuario = new usuarioSchema(req.body);

    console.log(usuario);
    usuarioSchema.findOneAndUpdate({id: usuario.id}, {nombre: usuario.nombre, correo: usuario.correo, apellido: usuario.apellido, telefono: usuario.telefono, direccion: usuario.direccion}).then(result => {
        res.json(result);
    }).catch(error => {
        res.status(500).json(error);
    });
}



