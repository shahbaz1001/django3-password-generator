from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
# render is a funtion which allow you to pass tempolates into HttpResponse

#use dictionary and we can search using key(password).........find the value of passwordwhic is admin
#  {'password': 'admin'}
def home(request):
    return render(request, 'generator/home.html')


def about(request):
        return render(request, 'generator/about.html')



def password(request):
    # characters declaration and list of characters using that random password will be Generated.....
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # Uppercase list to create random passsword generated.....
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # Numbers list to create random passsword generated.....
    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))
    # Special list to create random passsword generated.....
    if request.GET.get('Special'):
        characters.extend(list('%$#@^&(+_}{<>})'))




    length = int(request.GET.get('length', 12))


    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
