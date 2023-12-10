import mongoose from 'mongoose';
import { usuarios } from './usuarios.model';

const usuarioSchema = new mongoose.Schema<usuarios>({
    id: Number,
    name: String,
    lastname: String,
    email: String,
    password: String,
    phoneNumber: String,
    address: String,

    
});

export const usuariosSchema = mongoose.model<usuarios>('usuarios', usuarioSchema);