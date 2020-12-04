from django.shortcuts import render,redirect,HttpResponse
from nfoapp.models import NfoMOdels,VoterDetails

# Create your views here.
def nforegistration(request):
    if request.method=='POST':
        email=request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']
        user=NfoMOdels(email=email,psw=psw,psw_repeat=psw_repeat)
        if psw==psw_repeat:
            user.save()
            return redirect('nfologin')
        #return render(request, 'nfologin.html')
        else:
            return render(request, 'nforegistration.html')
    else:
       return render(request,'nforegistration.html')
def page1(request):
    return render(request, 'nforegistration.html')


def nfologin(request):
    if request.method=='POST':
        email=request.POST['email']
        psw = request.POST['psw']
        try:
            NfoMOdels.objects.get(email=email,psw=psw)
            return render(request, 'nfohome.html')
        except:
            return HttpResponse("invalid credentials")
    else:
        return render(request,'nfologin.html')



def nfoform1(request):
    return render(request,'nfoform1.html')

def nfoform2(request):
    return render(request,'nfoform2.html')

def nfoform3(request):
    return render(request,'nfoform3.html')

def nfovoterdetails(request):
    if request.POST.get('nfoform2'):
        yname=request.POST['yname']
        fname = request.POST['fname']
        area = request.POST['area']
        gender = request.POST['gender']
        location = request.POST['location']
        context={'yname':yname,'fname':fname,'area':area,'gender':gender,'location':location}
        return render(request,'nfoform2.html')

    if request.POST.get('nfoform3'):
        age=request.POST['age']
        rate = request.POST['rate']
        return render(request,'nfoform3.html')

    if request.POST.get('nfoform4'):
        bewith=request.POST['bewith']
        return HttpResponse("registered successfully")

    return render(request, 'nfoform1.html')
