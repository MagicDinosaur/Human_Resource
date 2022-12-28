# import json
# from datetime import datetime, timedelta
# import jwt
from rest_framework.response import Response
# from .models import Employee
#
# JWT_SECRET = 'secret'
# JWT_ALGORITHM = 'HS256'
# JWT_EXP_DELTA_SECONDS = 20
#
#
# def json_response(body='', **kwargs):
#     kwargs['body'] = json.dumps(body or kwargs['body']).encode('utf-8')
#     kwargs['content_type'] = 'text/json'
#     return Response(**kwargs)
#
#
# async def login(request):
#     post_data = await request.post()
#
#     try:
#         user = Employee.objects.get(email=post_data['employee_email'])
#         user.match_password(post_data['employee_password'])
#     except (Employee.DoesNotExist, Employee.PasswordDoesNotMatch):
#         return json_response({'message': 'Wrong credentials'}, status=400)
#
#     payload = {
#         'user_id': user.employee_id,
#         'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
#     }
#     jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
#     return json_response({'token': jwt_token.decode('utf-8')})
#
# async def get_user(request):
#     return json_response({'user': str(request.user)})
#
# async def auth_middleware(app, handler):
#     async def middleware(request):
#         request.user = None
#         jwt_token = request.headers.get('authorization', None)
#         if jwt_token:
#             try:
#                 payload = jwt.decode(jwt_token, JWT_SECRET,
#                                      algorithms=[JWT_ALGORITHM])
#             except (jwt.DecodeError, jwt.ExpiredSignatureError):
#                 return json_response({'message': 'Token is invalid'},
#                                      status=400)
#
#             request.user = Employee.objects.get(id=payload['employee_id'])
#         return await handler(request)
#     return middleware
#
#
#
# # #urls
# # app = web.Application(middlewares=[auth_middleware])
# # app.router.add_route('GET', '/get-user', get_user)
# # app.router.add_route('POST', '/login', login)
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
LOGIN_EXEMPT_URLS = [
    '/',
    '/api_url/',
    '/employee/api/token/',
    '/employee/view/'
]
from rest_framework.permissions import IsAuthenticated
class LoginMiddleWare:
    permission_classes = [IsAuthenticated]
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

