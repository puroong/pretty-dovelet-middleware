from app import api_root
from app.common import util
from flask import request
from flask_restful import Resource, reqparse

@api_root.resource('/v1/stair/<int:stair_num>')
class Stair(Resource):
  """
  @api {get} /v1/stair/:stair_num Get stair problems
  @apiVersion 1.0.0
  @apiName GetStair
  @apiGroup Stair

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
      
  @apiParam {Number} stair_num Number of requesting stair

  @apiSuccess {Object[]} problems List of problems in a stair
  """
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