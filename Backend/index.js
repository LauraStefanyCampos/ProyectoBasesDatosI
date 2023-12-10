"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
//dependencias
const express_1 = __importDefault(require("express"));
const http_1 = __importDefault(require("http"));
const body_parser_1 = __importDefault(require("body-parser"));
const cors_1 = __importDefault(require("cors"));
//rutas
const administradores_router_1 = __importDefault(require("./routes/administradores.router"));
const usuarios_router_1 = __importDefault(require("./routes/usuarios.router"));
//db
const database_1 = require("./utils/database");
const app = (0, express_1.default)();
const db = new database_1.Database();
const server = http_1.default.createServer(app);
app.use((0, cors_1.default)());
app.use(body_parser_1.default.json());
app.use(body_parser_1.default.urlencoded({ extended: true }));
//pagina estatica
app.use(express_1.default.static('../Frontend'));
app.get('', (req, res) => {
    res.sendFile('index.html', { root: '../Frontend/web-administrador' });
});
app.get('/web-motoristas', (req, res) => {
    res.sendFile('motoristas.html', { root: '../Frontend/web-motoristas' });
});
//rutas
app.use('/admins', administradores_router_1.default);
app.use('/users', usuarios_router_1.default);
//iniciar el servidor
server.listen(3000, () => {
    console.log('listening on *:3000');
});
