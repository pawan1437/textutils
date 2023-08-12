
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    spaceremover=request.POST.get('spaceremover', 'off')
    if removepunc == 'on':
    
        punctuactions = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =''
        for char in djtext:
            if char not in punctuactions:
                analyzed = analyzed + char
        params = {'purpose':'removed puncuation','analyze_text' :analyzed}
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'cahnge to uppercase','analyze_text' :analyzed}
        djtext=analyzed
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'removed new lines','analyze_text' :analyzed}
        djtext=analyzed
    if(spaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':'removed new lines','analyze_text' :analyzed}
    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and spaceremover != 'on'):
        return HttpResponse('please select any operation')

    return render(request, 'analyze.html',params)

        
