from app import api_root
from app.common import util
from flask import request
from flask_restful import Resource, reqparse

@api_root.resource('/v1/stair/<int:stair_num>')
class Stiar(Resource):
  def get(self, stair_num):
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
    
    dovelet = util.Dovelet()

    problems = dovelet.stair(stair_num, cookies)

    return {
      'problems': problems
    }