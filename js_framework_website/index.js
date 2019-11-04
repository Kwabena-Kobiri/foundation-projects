const express = require('express');
//const mongoose =require('mongoose');
//const config = require('config');
const app = express();


const bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static('public'));

app.get('/home', function(req, res) {
    res.sendFile(__dirname + '/public/HOME.html');
});

app.get('/about', function(req, res){
    res.sendFile(__dirname + '/public/ABOUT.html');
});

app.get('/services', function(req, res){
    res.sendFile(__dirname + '/public/SERVICES.html');
});

app.get('/login', function(req, res){
    res.sendFile(__dirname + '/public/LOGIN.html');
})

app.post('/login', function(req, res){
    res.send(JSON.stringify(req.body));
});

app.get('/register', function(req, res) {
    res.sendFile(__dirname + '/public/REGISTER.html');
});

app.post('/register', function(req, res) {
    res.send(JSON.stringify(req.body));
});

app.listen(5000, function(){
    console.log('Listening on port 5000');
});
