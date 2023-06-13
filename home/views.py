from django.shortcuts import render,HttpResponseRedirect
from .forms import detregi
from .models import regi

# Create your views here.
def home(request):
	if request.method=='POST':
		da=detregi(request.POST)
		if da.is_valid():
			da.save()
		da=detregi()
	else:
		da=detregi()
	allstud=regi.objects.all()
	data={"form":da,'stud':allstud}
	return render(request,'home/addshow.html',data)


def dele(request,id):
	if request.method=='POST':
		pi=regi.objects.get(pk=id)
		pi.delete()
		return HttpResponseRedirect('/')


def update(request,id):
	if request.method=='POST':
		pi=regi.objects.get(pk=id)
		da=detregi(request.POST,instance=pi)
		if da.is_valid():
			da.save()
	else:
		pi=regi.objects.get(pk=id)
		da=detregi(instance=pi)
	return render(request,'home/update.html',{'form':da})