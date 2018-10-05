const http = require('http');
const { parse } = require('querystring');
const hostname = '127.0.0.1';
const port = 3000;

const {PythonShell} = require('python-shell')
function spamOrHam(sms, callback) {
    options = {
        args: ['--input', `"${sms}"`]
    }

    PythonShell.run('call_model.py', options, function (err, results) {
        if (err) throw err;
        callback(results)
    });
}

// https://itnext.io/how-to-handle-the-post-request-body-in-node-js-without-using-a-framework-cd2038b93190
const server = http.createServer((req, res) => {
    if (req.method === 'POST') {
        collectRequestData(req, result => {
            spamOrHam(result.sms, (prediction) => {
                res.end(`${result.sms} is "${prediction}"`);
            });
        });
    } 
    else {
        res.end(`
            <!doctype html>
            <html>
            <body style="font-family:verdana">
                <form action="/" method="post">
                    <p>Enter an SMS message</p>
                    <input type="text" name="sms" size="50"/><br />
                    <button>Spam or Ham?</button>
                </form>
            </body>
            </html>
        `);
    }
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});

function collectRequestData(request, callback) {
    const FORM_URLENCODED = 'application/x-www-form-urlencoded';
    if (request.headers['content-type'] === FORM_URLENCODED) {
        let body = '';
        request.on('data', chunk => {
            body += chunk.toString();
        });
        request.on('end', () => {
            callback(parse(body));
        });
    }
    else {
        callback(null);
    }
}
