import time


class SampleMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        self.count = self.count+1
        response = self.get_response(request)
        end_time = time.time()
        print("Total requests till now: ", self.count)
        print("Total Time in this request:", end_time-start_time)
        return response

    

