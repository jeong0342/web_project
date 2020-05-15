from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

class xxy1:
    def __init__(self,x1,x2):
        self.x1 = x1
        self.x2 = x2
    def getPredict(self):
        y = self.x1 + self.x2
        print('Predict Result:', y)
        

def home(request):
    first = request.GET['x1']
    second = request.GET['x2']
    # requestDict = request.GET
    # result = int(age02)+5
    # requestDict = {'result_response':result}

    xxy = xxy1(first,second)    

    requestDict = {'result_response': xxy1.getPredict(xxy) }
    return JsonResponse(requestDict)

# return HttpResponse("Hello, Django!")