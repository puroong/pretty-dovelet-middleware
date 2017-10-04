from app import api_root
from app.common import util
from flask import request
from flask_restful import Resource, reqparse

@api_root.resource('/v1/login')
class Login(Resource):
  """
  @api {post} /v1/login Login
  @apiVersion 1.0.0
  @apiName Login
  @apiGroup User

  @apiParam {String} id Dovelet user id
  @apiParam {String} passwd Dovelet user password

  @apiSuccess {Boolean} success True
  @apiSuccess {Object} cookies Dovelet cookies

  @apiSuccess {Booleam} success False
  @apiError {Object} cookies Empty object
  """
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

@api_root.resource('/v1/logout')
class Logout(Resource):
  """
  @api {get} /v1/logout Logout
  @apiVersion 1.0.0
  @apiName Logout
  @apiGroup User

  @apiHeader {String} PHPSESSID Dovelet phpsessid
  @apiHeader {String} member_id Dovelet member_id
  @apiHeader {String} member_passwd Dovelet member_passwd
  @apiHeader {String} member_sid Dovelet member_sid

  @apiHeaderExample {String} Header-Example:
    Must send with set-cookie header

    Set-Cookie: PHPSESSID=sdafj13123
    Set-Cookie: member_id=dsf324elfsdkj324
    Set-Cookie: member_passwd=2123jfdskljfsdl
    Set-Cookie: member_sid=dfds32432jlrfdslk
    
  @apiSuccess {Boolean} success True
  
  @apiError {Boolean} success 
  """
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

    dovelet.logout(cookies=cookies)

    return {
      'success': True
    }
  
  @api_root.resource('/v1/me')
  class Profile(Resource):
    """
    @api {get} /v1/me User profile
    @apiVersion 1.0.0
    @apiName GetProfile
    @apiGroup User

    @apiHeader {String} PHPSESSID Dovelet phpsessid
    @apiHeader {String} member_id Dovelet member_id
    @apiHeader {String} member_passwd Dovelet member_passwd
    @apiHeader {String} member_sid Dovelet member_sid

    @apiHeaderExample {String} Header-Example:
      Must send with set-cookie header

      Set-Cookie: PHPSESSID=sdafj13123
      Set-Cookie: member_id=dsf324elfsdkj324
      Set-Cookie: member_passwd=2123jfdskljfsdl
      Set-Cookie: member_sid=dfds32432jlrfdslk
      
    @apiSuccess {String} profile User Profile html
    
    @apiError {String} profile 
    """
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