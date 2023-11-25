# 请编写网站实现如下功能。
# 需求：
# 实现MIDDLEWARE_CLASSES中的所有类，并约束每个类中必须有process方法。 =====> 想起了异常处理，主动抛异常和ABCMeta 模块
# 用户访问时，使用importlib和反射
# 让 MIDDLEWARE_CLASSES中的每个类对login、logout、index 方法的返回值进行包装，最终让用户看到包装后的结果。
# 如：
# 用户访问: http: // 127.0.0.1.txt: 8000 / login / ，
# 页面显示： 【csrf】【auth】【session】 登录 【session】 【auth】 【csrf】
# 用户访问: http: // 127.0.0.1.txt: 8000 / index / ，
# 页面显示： 【csrf】【auth】【session】 登录 【session】 【auth】 【csrf】

# 即：每个类都是对view中返回返回值的内容进行包装。
#
# MIDDLEWARE_CLASSES = [
#     'utils.session.SessionMiddleware',
#     'utils.auth.AuthMiddleware',
#     'utils.csrf.CrsfMiddleware',
# ]
#
# from wsgiref.simple_server import make_server

# class View(object):
#     def login(self):
#         return '登陆'
#
#     def logout(self):
#         return '等处'
#
#     def index(self):
#         return '首页'
#
#
# def func(environ, start_response):
#     start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
#     obj = View()
#     method_name = environ.get('PATH_INFO').strip('/')
#     if not hasattr(obj, method_name):
#         return ["".encode("utf-8"), ]
#     response = getattr(obj, method_name)()
#     return [response.encode("utf-8")]
#
#
# server = make_server('127.0.0.1.txt', 8000, func)
# server.serve_forever()