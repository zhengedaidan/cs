import logging
logging.basicConfig(level=logging.DEBUG,
                    format='等级:[%(levelname)s]<>'
                           '%(threadName)s线程 >> %(filename)s文件>> %(lineno)d行>> %(message)s信息'
                           ' >>时间:%(asctime)s', datefmt='%Y/%m/%d %H:%M:%S',
                    filename='log.log')
logger = logging.getLogger("nihao")
# logger = logging.getLogger(__name__)
logger.debug("debug123")
logger.warning("warning")