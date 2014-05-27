import requests
from werkzeug.contrib.cache import (
    MemcachedCache,
    SimpleCache
)

from flask import (
    Flask,
    render_template,
    jsonify
)

# initialize the app
app = Flask(__name__)

# initialize settings
app.config.from_object('settings')


if app.config['DEBUG']:
    cache = SimpleCache()
else:
    cache = MemcachedCache(['127.0.0.1:11211'])


def get_posts():
    url = '{}/post/'.format(app.config['CODRSPACE_API_URL'])
    payload = {
        'format': 'json',
        'limit': 5,
        'username': app.config['CODRSPACE_API_USERNAME'],
        'api_key': app.config['CODRSPACE_API_KEY']
    }

    response = requests.get(url, params=payload)
    return response.json()


@app.context_processor
def context():
    return {
        'APP_NAME': app.config['APP_NAME'],
        'APP_TAGLINE': app.config['APP_TAGLINE']
    }


@app.route('/')
def index():
    ctx = {}

    # get or set posts from cach
    posts = cache.get('posts')
    if posts is None:
        print 'here'
        posts = get_posts()
        cache.set('posts', posts, timeout=86400)

    # update the context
    ctx['posts'] = posts

    print dir(posts)

    return render_template('index.html', **ctx)


if __name__ == "__main__":
    app.run()
