"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.usuariosSchema = void 0;
const mongoose_1 = __importDefault(require("mongoose"));
const usuarioSchema = new mongoose_1.default.Schema({
    id: Number,
    name: String,
    lastname: String,
    email: String,
    password: String,
    phoneNumber: String,
    address: String,
});
exports.usuariosSchema = mongoose_1.default.model('usuarios', usuarioSchema);
