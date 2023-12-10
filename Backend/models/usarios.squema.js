"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const mongoose_1 = __importDefault(require("mongoose"));
// Definir un esquema con Mongoose
const usuarioSchema = new mongoose_1.default.Schema({
    email: String,
    password: String,
});
const Usuario = mongoose_1.default.model('Usuario', usuarioSchema);
module.exports = Usuario;
