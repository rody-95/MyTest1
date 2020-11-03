#连接redis数据库
import redis
r = redis.StrictRedis(host='127.0.0.1',port='6379',db='0',password='94995',decode_responses=True)
r.set('test',"I love study")
print(r['test'])
print(r.get('test'))
print(type(r.get('test')))


