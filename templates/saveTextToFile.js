const express = require('express');
const bodyParser = require('body-parser');
const multer = require('multer');
const path = require('path');

const app = express();
const port = 63342;

// Настройка multer для сохранения файлов в директории uploads
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/');
    },
    filename: function (req, file, cb) {
        cb(null, 'savedText.txt');
    }
});

const upload = multer({ storage: storage });

app.use(bodyParser.text());

app.get('/', (req, res) => {
    // Отправка HTML-страницы
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/save', upload.single('textFile'), (req, res) => {
    // Получение текста из POST-запроса
    const textToSave = req.body;

    // Отправка ответа клиенту
    res.send('Текст успешно сохранен в файл savedText.txt');
});

app.listen(port, () => {
    console.log(`Сервер запущен на порту ${port}`);
});