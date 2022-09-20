from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import fields
from utils import crypto_rate


app = Flask(__name__)


@app.route('/rates')
@use_kwargs(
    {
        'crypto': fields.Str(required=True)
    },
    location='query'
)
def res_crypto(crypto):
    return {'rate': crypto_rate(crypto)}


app.run(debug=True)
