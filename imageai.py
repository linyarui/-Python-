#__author:林亚锐
#date:2018/4/7
# *_*coding:utf-8 *_*

from aip import AipOcr

def get_words_by_img(img):
    """
    根据图片信息识别其中的文字
    :param img: 图片的二进制信息
    :return: 返回字典信息
    """
    APP_ID = '11058897'
    API_KEY = '2myGtqLVAEtXq9D8EXYqKN4N'
    SECRET_KEY = 'iEqNuVhCNo8EGxb94beO3Xkrxo0Sjnut '
    # client 就是一个客户端，他去帮我们识别文字
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 交给客户端去识别
    options = {'probability' : 'true'}
    res = client.basicGeneral(img, options=options)
    return res