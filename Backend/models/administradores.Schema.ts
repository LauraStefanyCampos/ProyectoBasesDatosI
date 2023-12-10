import mongoose from 'mongoose';
import { administradores } from './administradores.model';

const administradorSchema = new mongoose.Schema<administradores>({
    id: String,
    name: String,
    lastname: String,
    email: String,
    password: String,
});

export const administradoresSchema = mongoose.model<administradores>('administradores', administradorSchema);