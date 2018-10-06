from django.shortcuts import render
from django.http import Http404

from .models import UserInfo, contactInfo
from .forms import getInfo, getLoginInfo, getContactInfo,editContactInfo


# Create your views here.

class info:
    name=""
    phone=""
    email=""
    image=""

    def __init__(self, name, phone,email,image):
        self.name = name
        self.phone = phone
        self.email = email
        self.image = image

currentUpdated = ("","","","")


def listOfContact():
    q = []
    i = 0
    for e in contactInfo.objects.all():
        i += 1
        p = e.name
        #p = ''.join(a)

        b = e.phone
       # b = ''.join(a)

        c = e.email
        #c = ''.join(a)

        d = e.image

        new = info(p, b, c, d)
        q.append(new)

    return q


def signup(request) :

    username="not loggeed in"
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = getInfo(request.POST)

        if MyLoginForm.is_valid():
            name = MyLoginForm.cleaned_data['name']
            email = MyLoginForm.cleaned_data['email']
            password = MyLoginForm.cleaned_data['password']
            repass = MyLoginForm.cleaned_data['repass']

            exist_count = UserInfo.objects.filter(email=email).count()
            if exist_count >= 1:
                return render(request, 'signup_fail.html', {})

            if password != repass:
                return render(request, 'wrongpass.html', {})


            newUser = UserInfo(
               name=name, email=email, password=password
               )
            newUser.save()

            objects = UserInfo.objects.all()


    else:
        MyLoginForm = getInfo()

    return render(request, 'login.html',{})


def gotologin(request):
    return render(request, 'login.html', {})



def login(request) :
    q=[]

    if request.method == "POST":
        MyForm = getLoginInfo(request.POST)
        if MyForm.is_valid():

            email = MyForm.cleaned_data['email']
            password = MyForm.cleaned_data['password']

            try:
                n = UserInfo.objects.get(email=email)
            except UserInfo.DoesNotExist:
                return render(request, 'login_fail.html', {})
            k = n.password
            if k != password:
                return render(request, 'login_fail.html', {})
            # un = username
            request.session['username'] = n.name
            request.session.modified = True

            q = listOfContact()

    else:
        MyForm = getInfo()

    return render(request, 'contact_list.html',{"q":q})



def logout(request) :
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'login.html',{})


def home(request) :
    return render(request, 'signup.html',{})



def start(request) :
    username = "not logged in"
    try:
        username = request.session['username']
    except:
        return render(request, 'signup.html', {})
    return render(request, 'contact_list.html',{"username": username})


def contactpage(request) :
    username = "not logged in"
    q=[]
    q = listOfContact()

    try:
        username = request.session['username']
    except:
        return render(request, 'login.html', {});
    return render(request, 'contact_list.html',{"username": username,"q":q})


def addcontact(request) :
    username = "not logged in"
    try:
        username = request.session['username']
    except:
        return render(request, 'signup.html', {})
    return render(request, 'new_contact.html',{"username": username})


def addnewcontact(request) :
    p=""
    q=[]

    username="not loggeed in"
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = getContactInfo(request.POST, request.FILES)

        if MyLoginForm.is_valid():
            name = MyLoginForm.cleaned_data['name']
            email = MyLoginForm.cleaned_data['email']
            phone = MyLoginForm.cleaned_data['phone']
            image = MyLoginForm.cleaned_data['image']

            exist_count = contactInfo.objects.filter(phone=phone).count()
            if exist_count >= 1:
                q = listOfContact()
                return render(request, 'contact_list_.html', {"q":q})


            newContact = contactInfo(
               name=name, email=email, phone=phone,image=image
               )
            newContact.save()

            objects = contactInfo.objects.all()
            q = listOfContact()


    else:
        MyLoginForm = getInfo()

    return render(request, 'contact_list.html',{"q":q})

def updatecontact(request) :
    global currentUpdated
    q=[]
    if request.method == "POST":
        for e in contactInfo.objects.all():
            if e.phone in request.POST:
                p = e.name
                # p = ''.join(a)

                b = e.phone
                #b = ''.join(a)

                c = e.email
                #c = ''.join(a)

                d = e.image

                currentUpdated = info(p, b, c, d)
                return render(request, 'update_contact.html', {"prof": currentUpdated})

            for e in contactInfo.objects.all():
                if e.email in request.POST:
                    n = contactInfo.objects.get(email=e.email)
                    n.delete()

                    q = listOfContact()


    return render(request, 'contact_list_deleted.html',{"q":q})



def contactupdated(request) :
    global currentUpdated
    q=[]
    name=None
    email = None
    phone = None
    image=None

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = editContactInfo(request.POST, request.FILES)

        if MyLoginForm.is_valid():

            name = MyLoginForm.cleaned_data['name']
            phone = MyLoginForm.cleaned_data['phone']
            email = MyLoginForm.cleaned_data['email']
            image = MyLoginForm.cleaned_data['image']


            n = contactInfo.objects.get(phone=currentUpdated.phone)

            if not (name is None):
                n.name = name


            if not (email is None):
                n.email = email


            if not (phone is None):
                n.phone = phone


            if not (image is None):
                n.image = image

            n.save()

            #currentUpdated = ("", "", "", "")

        q = listOfContact()


    else:
        MyLoginForm = getInfo()

    return render(request, 'contact_list.html',{"q":q, "cu":currentUpdated,"name":n.email})



