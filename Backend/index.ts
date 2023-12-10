//dependencias
import express from 'express';
import http from 'http';
import bodyParser from 'body-parser';
import cors from 'cors';

//rutas
import administradoresRouter from './routes/administradores.router';
import usuariosRouter from './routes/usuarios.router';

//db
import { Database } from './utils/database';

const app = express();
const db:Database = new Database();
const server = http.createServer(app);

app.use(cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//pagina estatica
app.use(express.static('../Frontend'));

app.get('', (req, res) => {
  res.sendFile('index.html', {root: '../Frontend/web-administrador'});
});

app.get('/web-motoristas', (req, res) => {
  res.sendFile('motoristas.html', {root: '../Frontend/web-motoristas'});
});

//rutas
app.use('/admins', administradoresRouter);
app.use('/users', usuariosRouter);

//iniciar el servidor
server.listen(3000, () => {
  console.log('listening on *:3000');
});