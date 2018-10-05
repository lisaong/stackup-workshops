const http = require('http');
const {PythonShell} = require('python-shell')
const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    spamOrHam('hello')
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

function spamOrHam(sms) {
    options = {
        args: ['--input', `"${sms}"`]
    }

    PythonShell.run('call_model.py', options, function (err, results) {
        if (err) throw err;
        console.log(results);
    });
}

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});