#redis数据库
import redis
r = redis.StrictRedis(host='127.0.0.1',port='6379',db='0',password='94995',decode_responses=True)
r.set('token',"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwbGF0Q29kZSI6IjAiLCJhY2NJbmZvSWQiOjEyNTQyNTY0NTMxNjg0ODAyNTYsInBob25lIjoiMTUxMTMxOTUzNDMiLCJleHRJZCI6MCwiZXhwIjoxNjA0OTE1MjYwLCJ1c2VySWQiOjE0NTcxNjg2LCJvcmdJZCI6Im51bGwiLCJlbWFpbCI6Inhpbmxpbi56aGFuZ0BtZWRiYW5rcy5jbiJ9.DT9yQBeMxgRBfJNpi8aW6j8cO5Hyatcfrb1gns59lG4")
print(r['token'])
print(r.get('token'))
print(type(r.get('token')))
