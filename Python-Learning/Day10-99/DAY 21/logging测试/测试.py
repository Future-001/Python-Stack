import logging
#  例如做一个计算器，监控他的计算，万一计算出错了，方便义后看看是哪里出错了
fh = logging.FileHandler('log1.log',encoding='utf-8')
sh = logging.StreamHandler() # 为了显示在屏幕上

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(pathname)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)s -  %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S %p',
    # filename = 'log1.log'
    # filemode = 'w' 默认追加
    handlers=[fh,sh],
    level = logging.DEBUG
)
logging.debug('zhangsan  this is debug')
logging.info('from the message we can learn about the info')
