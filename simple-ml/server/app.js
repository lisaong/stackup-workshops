const http = require('http');
const pyshell = require('python-shell')
const hostname = '127.0.0.1';
const port = 3000;

// python process that loads the model and accepts stdin
const model = new pyshell.PythonShell('call_model.py', { mode: 'text'});
model.send('hello');

// get stdout from the python process
model.on('message', function(message){
    console.log(message);
})

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  model.send('hello');
  res.end('Hello World\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});