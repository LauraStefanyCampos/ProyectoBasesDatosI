const express = require('express');
const usuarioController = require('../controllers/usuarioController');

const router = express.Router();

router.get('/usuarios', usuarioController.obtenerTodosLosUsuarios);
// Definir otras rutas y conectar a los controladores correspondientes...

module.exports = router;
