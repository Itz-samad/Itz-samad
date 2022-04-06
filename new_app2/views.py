from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import  *

def myfunctioncall(request):
    return HttpResponse('Hello world!. \n welcom to Yinkuz page <h1> click<a href="/index/"> here </a> to move forward</h1>')

def myfunctionabout(request):
    return HttpResponse('fuck u dumb ass')

def add(request, a, b):
    return HttpResponse(a * b)

def intro(request, name, age):
    my_dictionary = {
        "name":name, 
        "age":age
    }
    return JsonResponse(my_dictionary)

def index(request):
    return render(request, 'index.html')


def second(request):
    return render(request, 'second.html')

def third(request):
    var = 'hello world'
    msg = 'hello there'
    fruits = ['banana', 'apple', 'guava', 'orange', 'cucumba']
    import random
    m = random.randint(1, 100)
    z = random.randint(1, 100)
    num1, num2 = z, m
    ans = num1 > num2
    print(ans)
    


    my_dict = {
        "var" : var,
        "msg": msg,
        "fut" : fruits,
        "num2" : num2,
        'num1' : num1,
        'ans' : ans,
    }
    return render(request, 'third.html', context=my_dict)


def image_page(request):
    return render(request, 'image_page.html')

def image_page2(request):
    return render(request, 'image_page2.html')

def image_page3(request):
    return render(request, 'image_page3.html')

def image_page4(request):
    return render(request, 'image_page4.html')

def image_page5(request, imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    print(myimagename)
    if myimagename == 'django':
        var = True
    elif myimagename == 'python':
        var = False
    
    else:  
        return HttpResponse('wrong input {}'.format(myimagename))
        print('wrong input sucker {}'.format(myimagename))
    my_dict = {
        'var': var
        }
    
    return render(request, 'image_page5.html', context=my_dict)

def myform(request):
    return render(request, 'myform.html')

def submitmyform(request): 
   
   my_dict ={
       "var1": request.POST['mytext'],
       "var2": request.POST['mytextarea'],
       "method": request.method
   }
   print('\n\tFirst: {}. \n\n\tSecond: {}. \n\n\tMethod: {}\n\t'.format(my_dict["var1"], my_dict["var2"], my_dict['method']))
  
  
   return JsonResponse(my_dict)

def myform2(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email'] 
            my_dicte = {
                "form": FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = 'Tilte should be in capital letter'
                Errors.append(errormsg)
                # print('\n\t\n 1. {}.'.format(title))
                # print('\n\t\n 2. {}.\n'.format(subject))
                # print('\n\t\n 3. {}.\n'.format(email))
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = 'Not a valid Email'
                Errors.append(errormsg)
            if errorflag != True:
                my_dicte['success']=True
                my_dicte['successmsg']='Form Submitted'
                print('\n\t\n 1. {}.'.format(title))
                print('\n\t\n 2. {}.\n'.format(subject))
                print('\n\t\n 3. {}. \n'.format(email))
               

            my_dicte["error"] = errorflag
            my_dicte["errors"] = Errors
            print('\n\t\n {} \n'.format(my_dicte))
            return render(request, 'myform2.html', context=my_dicte)
 
            
        else:
            my_dict = {
                "form": form
            } 
            return render(request, 'myform2.html', context=my_dict)
               
    elif request.method == 'GET':
        form = FeedbackForm()   #FeedbackForm(none)
        my_dicta = {
            "form": form
        }
        
        return render(request, 'myform2.html', context=my_dicta)
       
   

