from django.http import HttpResponse
from django.shortcuts import render
from .models import IceCream

# Create your views here.
def index(request):
    context = {
        "variable": "This is my message"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is home page")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is About page")
def service(request):
    return render(request,'services.html')
    # return HttpResponse("This is Service page")
def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("This is Contact page")
def catageory(request):
    return render(request,'catageory.html')
    # return HttpResponse("This is Catageory page") 
def cart(request):
    return render(request,'cart.html')
    # return HttpResponse("This is Catageory page")        
def search_results(request):
    query = request.GET.get('query', '')
    if query:
        # Filter your IceCream model for results that match the query
        results = IceCream.objects.filter(name__icontains=query)  # Case-insensitive search
    else:
        results = IceCream.objects.all()  # Show all if no query is provided
    
    return render(request, 'search_results.html', {'results': results})    














