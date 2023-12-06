const express = require("express");
const config = require('config');
const app = express();
PORT = 8000;
app.use(express.json());


app.get('/', (req, res) => {
    return res.send('Received a GET HTTP method');
});

app.get('/status', (req, res) => {
    res.json({ key: "value" });
    return res.send();
});

app.post('/', (req, res) => {
    return res.send('Received a POST HTTP method');
});

app.put('/', (req, res) => {
    return res.send('Received a PUT HTTP method');
});

app.delete('/', (req, res) => {
    return res.send('Received a DELETE HTTP method');
});

app.listen(PORT, () => {
    console.log("Server Listening on PORT:", PORT);
});
