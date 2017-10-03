from app import api_root
from app.common import util
from flask import request
from flask_restful import Resource, reqparse

@api_root.resource('/v1/problem')
class Problem(Resource):
  def get(self):
    # flask.request parses multiple set-cookies into string split by comma
    # ex. phpsessid=213123, sessid=dsfjksdlf...

    # parse cookies
    set_cookies = request.headers.get('set-cookie')
    
    set_cookies = set_cookies.split(',')
    cookies = {}
    for set_cookie in set_cookies:
      key = set_cookie.split('=')[0]
      value = set_cookie.split('=')[1]

      cookies[key] = value
    
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)

    args = parser.parse_args()
    title = args['title']

    dovelet = util.Dovelet()

    code, problem = dovelet.problem_text(title, cookies)

    return {
      'problem': problem
    }, code

  def post(self):
     # flask.request parses multiple set-cookies into string split by comma
    # ex. phpsessid=213123, sessid=dsfjksdlf...

    # parse cookies
    set_cookies = request.headers.get('set-cookie')
    
    set_cookies = set_cookies.split(',')
    cookies = {}
    for set_cookie in set_cookies:
      key = set_cookie.split('=')[0]
      value = set_cookie.split('=')[1]

      cookies[key] = value
    
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    parser.add_argument('language', type=int, required=True)
    parser.add_argument('source', type=str, required=True)

    args = parser.parse_args()
    title = args['title']
    language = args['language']
    source = args['source']

    dovelet = util.Dovelet()

    result = dovelet.problem_submit(title, language, source, cookies)

    return {
      'result': result
    }