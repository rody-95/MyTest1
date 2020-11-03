#蝗虫

from locust import TaskSet,HttpUser,task
class TsetIndex(TaskSet):

    def getIndex(self):
        self.client.get("/login")
        print("here")


class WebSite(HttpUser):
    task_set = TsetIndex
    min_wait = 1000
    max_wait = 2000

