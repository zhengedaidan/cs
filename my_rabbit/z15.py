import pika


credentials = pika.PlainCredentials("ls", "123")
connection_socket = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.0.104",
                                                                      credentials=credentials))


# 建立rabbit通道
channel = connection_socket.channel()

# # 声明队列(一对一发送)
channel.queue_declare(queue="hello",
                      durable=True  # 服务端的队列持久化
                      )

channel.basic_publish(exchange='',
                      routing_key="hello",  # 把消息转发到哪个队列
                      body="hello_world",
                      properties=pika.BasicProperties(delivery_mode=2)  # 服务端的消息持久化
                      )


# # 广播 声明转发器 不需要声明队列
# channel.exchange_declare(exchange="logs",
#                          exchange_type="fanout"  # 类型是广播
#                          )
#
# channel.basic_publish(exchange='logs',
#                       routing_key="",  # 不写 把消息转发到所有绑定转发器的队列
#                       body="hello_world",
#                       # properties=pika.BasicProperties(delivery_mode=2)  # 服务端的消息持久化
#                       )


# # 组播
# channel.exchange_declare(exchange="direct_logs",
#                          exchange_type="direct"  # 类型是组播
#                          )
#
# severity = "info"  # 组播级别
#
# channel.basic_publish(exchange='direct_logs',
#                       routing_key=severity,  # 组播级别 那些队列绑定这个级别 那些队列能收到
#                       body="hello_world",
#                       # properties=pika.BasicProperties(delivery_mode=2)  # 服务端的消息持久化
#                       )


# 匹配通知
# channel.exchange_declare(exchange="topic_logs",
#                          exchange_type="topic"  # 类型是匹配
#                          )
import sys
# routing_key = sys.argv[1]  # 发送端方表示需要匹配的格式    接收端表示 #匹配所有发送端的格式 .*代表一个点后面跟任意 但不能在有点

# channel.basic_publish(exchange='topic_logs',
#                       routing_key=routing_key,  # 组播级别 那些队列绑定这个级别 那些队列能收到
#                       body="hello_world",
#                       # properties=pika.BasicProperties(delivery_mode=2)  # 服务端的消息持久化
#                       )

print("已发送")

connection_socket.close()

