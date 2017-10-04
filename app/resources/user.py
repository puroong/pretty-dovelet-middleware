from app import api_root
from app.common import util
from flask import request
from flask_restful import Resource, reqparse

@api_root.resource('/v1/login')
class Login(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str, required=True)
    parser.add_argument('passwd', type=str, required=True)
    
    args = parser.parse_args()
    id = args['id']
    passwd = args['passwd']

    dovelet = util.Dovelet()

    success, cookies = dovelet.login(id, passwd)
    code = 200

    if not success:
      code = 401
    
    return {
      'success': success,
      'cookies': cookies
    }, code

  @api_root.resource('v1/me')
  class Profile(Resource):
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
      
      dovelet = util.Dovelet()

      profile = dovelet.profile(cookies=cookies)

      return {
        'profile': profile
      }