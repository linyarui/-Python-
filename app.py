#__author:林亚锐
#date:2018/4/7
# *_*coding:utf-8 *_*

from tornado import web, ioloop, httpserver
from imageai import get_words_by_img

#逻辑处理模块
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('未来的ai工程师们你们好！')
        self.render('index.html')

    def post(self, *args, **kwargs):
        # 接收文件
        file = self.request.files.get('file')[0]
        #识别文字
        res = get_words_by_img(file['body'])
        #展示给前端
        self.render('result.html', content = res['words_result'])

#设置
settings = {
    #模板路径设置
    'template_path' : 'templates',
    #静态文件路径设置
    'static_path' : 'static',
}

#路由 将请求转发给逻辑处理模块
application = web.Application([
            (r"/index.html", MainPageHandler),
        ], **settings)

#socket服务，处理http请求的
if __name__ == '__main__':

    http_server = httpserver.HTTPServer(application)
    http_server.listen(8082)#端口
    ioloop.IOLoop.current().start()