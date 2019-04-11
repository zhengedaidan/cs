# import requests
# headers = {
#     "User_Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
#
# }
# ret = requests.get(url="https://www.cnblogs.com/mvc/blog/BlogPostInfo.aspx?blogId=365037&postId=7253321&blogApp=stuqx&blogUserGuid=2bc224ea-16db-4a96-06c4-08d49c352df3&_=1540734729403",headers=headers)
# print(ret.content)






import pika
import time

credentials = pika.PlainCredentials("ls", "123")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    "192.168.0.104",credentials=credentials))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.

# 一对一模式下 声明队列 防止接受端先启动时没有队列
channel.queue_declare(queue='hello',
                      durable=True  # 要跟发送端保持一直
                      )


# # 广播模式
# channel.exchange_declare(exchange="logs",
#                         exchange_type="fanout"
#                         )
#
# result = channel.queue_declare(exclusive=True)  # 单独的
# queue_name = result.method.queue  # 随机生成一个队列名字
# channel.queue_bind(exchange="logs", queue=queue_name)  # 绑定交换器上


# # 组播模式
# channel.exchange_declare(exchange="direct_logs",
#                          exchange_type="direct"
#                          )
# result = channel.queue_declare(exclusive=True)  # 单独的
# queue_name = result.method.queue  # 随机生成一个队列名字

import sys
# severitys = sys.argv[1:]
# if not severitys:
#     sys.stderr.write('use %s [info] [warning] [error]' % sys.argv[0])
#     exit()
# for severity in severitys:
#     channel.queue_bind(exchange="logs",
#                        queue=queue_name,
#                        routing_key=severity # 可以绑定多个级别
#                        )  # 绑定交换器上
# channel.queue_bind(exchange="direct_logs",
#                    queue=queue_name,
#                    routing_key="info"
#                    )  # 绑定交换器上


# 匹配模式
# channel.exchange_declare(exchange="topic_logs",
#                          exchange_type="topic"
#                          )
# result = channel.queue_declare(exclusive=True)  # 单独的
# queue_name = result.method.queue  # 随机生成一个队列名字
# routing_key = sys.argv[1]
# channel.queue_bind(exchange="topic_logs",
#                    queue=queue_name,
#                    routing_key=routing_key
#                    )  # 绑定交换器上


def callback(ch, method, properties, body):

    print("start_consuming")
    # time.sleep(5)  # 模拟接收端单点故障
    print(body)
    # ch.basic_ack(delivery_tag=method.delivery_tag)  # 接收端消息防止单点故障 广播消息注释


channel.basic_consume(callback,
                      queue='hello',
                      # queue=queue_name,
                      # no_ack=True  # 接收端消息防止单点故障 广播消息至为true
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
