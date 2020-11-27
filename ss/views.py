from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import csv
from ss.models import Emp,Emp1
import requests
from bs4 import BeautifulSoup


# Create your views here.



def wscrap(request):
    res=requests.get("https://www.moviebuff.com/vinaya-vidheya-rama-2019-tamil").content
    jsoup=BeautifulSoup(res)
    div=jsoup.find('div',attrs={'id':'cast'})
    result=div.find_all('div',attrs={'class':'col-xs-6 col-sm-4 credit'})
    list = []
    list2=[]
    for k in result:
        p=k.find('div',attrs={'name'}).text
        r=k.img['src']
        list.append(p)
        list2.append(r)
    mylist = zip(list, list2)
    #return render(request, "wscrap.html", {'res': list,'img':list2})
    return render(request, "wscrap.html", {'res': mylist})
        #break

def wscrapJsonResponse(request):
    res=requests.get("https://www.moviebuff.com/vinaya-vidheya-rama-2019-tamil").content
    jsoup=BeautifulSoup(res)
    div=jsoup.find('div',attrs={'id':'cast'})
    result=div.find_all('div',attrs={'class':'col-xs-6 col-sm-4 credit'})
    list = []
    for k in result:
        dummy_dic=dict()
        dummy_dic['Name']=k.find('div',attrs={'name'}).text
        dummy_dic['image']=k.img['src']
        list.append(dummy_dic)
    return JsonResponse(dummy_dic)


def weather(request):
    res=requests.get("http://www.ratingdada.com/1558/prema-pipasi-movie-review-rating").content
    jsoup=BeautifulSoup(res)
    city1=jsoup.find('div', attrs={'class':'main-content-div'})
    city=city1
    return render(request,'weather.html',{'res': city1})











#webscraping is above







def test(request):
    if request.method=='GET':
        name=request.GET['name']
        dob = request.GET['dob']
        emp1=Emp1(name1=name,dob=dob)
        emp1.save()
        emp = Emp1.objects.all()
        return render(request, "test.html", {'emp': emp})
    else:
        emp = Emp1.objects.all()
        return render(request,"test.html",{'emp':emp})

def download_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Description'] = 'attachment; filename="users.csv"'
    writer=csv.writer(response)
    writer.writerow(['Name','Age'])
    users=Emp.objects.all().values_list('name','age')

    for user in users:
        writer.writerow(user)

        return response





#========================Class Based Views========================================================
from rest_framework.views import APIView, View
from .serializer import MoviesSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse, get_object_or_404

class MovieApi(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('pk'):
            pk = kwargs.get('pk')
            saved_movie = get_object_or_404(Emp.objects.all(), pk=pk)
            serializer = MoviesSerializer(saved_movie)
            return Response({"Movie": serializer.data})

        movies = Emp.objects.all()
        movies = MoviesSerializer(movies, many=True)
        return Response({'Movies': movies.data})
        # return HttpResponse({'Movies': movies.data})

    def post(self, request):

        serializer = MoviesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        movie = get_object_or_404(Emp.objects.all(), pk=pk)
        serializer = MoviesSerializer(instance=movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            movie_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(movie_saved.movie_name)})

    def delete(self, request, pk):
        # Get object with this pk
        movie = get_object_or_404(Emp.objects.all(), pk=pk)
        movie.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)



class Demo():
    name="hello python"
    age=25
    def __init__(self):
        self.village="peddampet"
    @classmethod
    def setage(self,sage):
        self.name=sage
obj=Demo()
obj.setage("peddampet")
name1=obj.name
from ss.views2 import name
import json
def home(request):


    # a Python object (dict):
    x = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    return render(request,'home.html',{'name1':y})

def home1(request):
    return HttpResponse("welcome :"+name)



#social media app

from ss.models import Hotel
from django.shortcuts import redirect
from ss.models import Gallery

def hotel(request):
    if request.method=='POST':
        name=request.POST['name']
        file = request.FILES['file']
        stu=Hotel(name=name,file=file)
        stu.save()
        return render(request, 'image.html')
    else:
        return render(request, 'image.html')

def socialapp(request):
    user=Hotel.objects.all().order_by('name')
    return render(request,'socialapp.html',{'user':user})

def delete(request,id):
    user=Hotel.objects.get(id=id)
    user.delete()
    return redirect('socialapp')


def update(request,id):
    user = Hotel.objects.get(id=id)
    if request.method=='POST':
        user.name=request.POST['name']
        user.file=request.FILES['file']
        user.save()
        return redirect('socialapp')
    else:
        return render(request, 'update.html')



def insertgallery(request,id):
    user = Hotel.objects.get(id=id)
    if request.method=='POST':
        gimage=request.FILES['gimage']
        Gallery(gimage=gimage,progallery=user).save()
        return render(request, 'uploadgallery.html',{'user':user})
    elif request.method=='GET':
        return render(request, 'uploadgallery.html',{'user':user})
    return redirect('socialapp')

def deleteimage(request,id):
     user1=Gallery.objects.get(id=id)
     user1.delete()
     return redirect("socialapp")


def updateimage(request,id):
    user=Gallery.objects.get(id=id)
    if request.method=='POST':
        user.gimage=request.FILES['gimage']
        user.save()
        return redirect("socialapp")
    else:
        return render(request, 'insergallery.html')

def testurls(request,id):
    return render(request,"weather.html",{'num':id})
