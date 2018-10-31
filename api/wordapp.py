import time
import sys
sys.path.append("..")

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_caching import Cache

from word_count import WordCount


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
api = Api(app=app)

@cache.memoize(timeout=300)
def response(url, word):
    return {'Data': WordCount(url, word).count_words(),
                'Time': time.ctime()}

class WordApp(Resource):
    def get(self):
        word = request.args.get('word')
        url = request.args.get('url').split(",")
        return response(url, word)


api.add_resource(WordApp, '/')

if __name__ == '__main__':
    app.run(debug=False)
        
