import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define,options,parse_command_line,parse_config_file
define("port",default=8000,type=int)
define("list",default=[],type=str,multiple=True)
# parse_command_line()  转换命令行不使用使用文件 在使用 列表多个值用逗号隔开
# parse_config_file()  从配置文件导入
#使用以上两种方法时 会有日志显示
# from . import config

# tornado.options.options.port
# tornado.options.options.list

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello tonardo')


if __name__ == '__main__':
    # options.logging = None  # 配置文件关闭日志
    # --logging=None 命令行启动关闭日志
    parse_command_line()
    # parse_config_file("config")

    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    # app.listen(8000)
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.bind(options.port)
    # httpserver.bind(config.options.port)
    httpserver.start()  # 进程数

    tornado.ioloop.IOLoop.current().start()


