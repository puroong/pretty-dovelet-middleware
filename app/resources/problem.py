from app import api_root
from app.common import util
from flask import request
from flask_restful import Resource, reqparse

@api_root.resource('/v1/problem')
class Problem(Resource):
  """
  @api {get} /v1/problem Get dovelet problem
  @apiVersion 1.0.0
  @apiName GetProblem
  @apiGroup Problem

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
    
  @apiParam {String} title Problem title

  @apiSuccess {String} problem Problem html

  @apiError {String} problem Dovelet 404 html
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
    
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)

    args = parser.parse_args()
    title = args['title']

    dovelet = util.Dovelet()

    code, problem = dovelet.problem_text(title, cookies)

    return {
      'problem': problem
    }, code

  """
  @api {post} /v1/problem Submit dovelet problem
  @apiVersion 1.0.0
  @apiName SubmitProblem
  @apiGroup Problem

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
    
  @apiParam {String} title Problem title
  @apiParam {String} language Programming language of source code
  @apiParam {String} source Source code submitting

  @apiSuccess {String} result Result page html

  @apiError {String} result Result page html
  """
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