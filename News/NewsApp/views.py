from django.shortcuts import render
import requests
# Create your views here.
def input(request):
    newsapi = 'dbeaad2890e74a0a8370b3ed8f8f09f9'
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}'
    main_page = requests.get(url).json()
    article = main_page['articles']
    head = []
    data=[]
    for ar in article:
        x={}
        x["description"]=ar["description"]
        x["title"]=ar["title"]
        x["url"]=ar["url"]
        x['publishedAt']=ar['publishedAt']
        x['urlToImage']=ar['urlToImage']
        head.append(x)
    for i in range(6):
        data.append(head[i])
    if request.method=="GET":
        return render(request,'base.html',{'data':{'data':data,'head':head}})
    return render(request,'base.html',{'data':{'data':data,'head':head}})