const http = require('http');
const pythonShell = require('python-shell').PythonShell;

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  pythonShell.run('call_model.py', null, function (err, results) {
    if (err) throw err;
    console.log(results);
  });

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  res.end('Hello World\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});