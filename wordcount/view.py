from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'front.html')


def about(request):
    data=request.GET['text']
    datalen=data.split()
    lendata=len(datalen)
    odictionary={}

    for word in datalen:
        if word in odictionary:
            odictionary[word] +=1
        else:
            odictionary[word]=1

    return render(request,'count.html',{'text1':lendata,'text2':data,'text3':odictionary.items()})

def about1(request):
    return render(request,'front.html')
