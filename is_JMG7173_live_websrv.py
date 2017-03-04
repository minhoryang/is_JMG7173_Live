import os

from flask import Flask
from flask_redis import FlaskRedis

from is_JMG7173_live import (
    is_JMG7173_live,
)


app = Flask(__name__)
app.config['REDIS_URL'] = os.getenv('REDIS_URL', 'redis://localhost')
redis = FlaskRedis(app)

EXPIRED_AT = 60  # seconds


@app.route('/')
def index(key='jmg7173'):
    cached = redis.get(key)
    if cached:
        return cached

    value = 'Yes' if is_JMG7173_live() else 'No'
    redis.set(key, value, ex=EXPIRED_AT)

    return value


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
