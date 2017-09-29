from app.dove_request import DoveRequest
from flask_restful import Resource, reqparse
from app import api_root, app

dove_request = DoveRequest()

@api_root.resource('/login')
class DoveletLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('passwd')

        args = parser.parse_args()

        id = args['id']
        passwd = args['passwd']

        cookies = dove_request.login(id, passwd)

        return {'cookies': cookies}

@api_root.resource('/stair/<int:stair_num>')
class DovletStair(Resource):
    def get(self, stair_num):
        stair = dove_request.get_stair(stair_num)

        return {'stair': stair}

@api_root.resource('/problem')
class DovletProblem(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('full_link')

        args = parser.parse_args()

        full_link = args['full_link']

        problem = dove_request.get_problem(full_link)

        return {'problem': problem}

@api_root.resource('/submit')
class DovletSubmit(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('language')
        parser.add_argument('src')

        args = parser.parse_args()

        title = args['title']
        language = args['language']
        src = args['src']

        print(title, language, src)
        submit = dove_request.submit(title, language, src)
        print(submit)

        return {'submit': submit}
