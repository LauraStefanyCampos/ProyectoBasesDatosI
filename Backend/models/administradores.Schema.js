"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.administradoresSchema = void 0;
const mongoose_1 = __importDefault(require("mongoose"));
const administradorSchema = new mongoose_1.default.Schema({
    id: String,
    name: String,
    lastname: String,
    email: String,
    password: String,
});
exports.administradoresSchema = mongoose_1.default.model('administradores', administradorSchema);
