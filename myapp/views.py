from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect,render
from django.contrib import messages
import math
# Create your views here.

#Login View - Login page
@csrf_protect
def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        print(username)
        if User.objects.filter(username=username).exists():
            user=auth.authenticate(username=username,password=password)
            print(user)
            if user is not None:
                auth.login(request,user)
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('entry')
            else:
                messages.info(request,'incorrect password')
                return redirect('login')
        else:
            messages.error(request,"user doesn't exists")
            return redirect('login')

    else:

        return render(request,template_name = "login.html")

#Logout View - User Logout
def logout(request):

    auth.logout(request)
    request.session.flush()
    print("logged out")
    messages.success(request,"Successfully logged out")
    for sesskey in request.session.keys():
        del request.session[sesskey]

    return redirect('login')


@csrf_protect
# @login_required(login_url='login')
def dashboard(request):
    return render(request, 'hello_world.html', {})

@csrf_protect
# @login_required(login_url='login')
def entry(request):
    response = render(request, 'entry.html')
    response.set_cookie("name","Manoj")
    response.set_cookie("city",)
    # response.set_cookie("","Pravin")
    # response.set_cookie("","")
    # response.set_cookie(value=1)
    response['Set-Cookie'] = ('=; =air;rock=;power=water; Path=/;')
    return response


def load_charts(request):

    # response.set_cookie('logged_in_status', 'never_use_this_ever') 
    print("Manoj")
    print(request.POST)

    High = float(request.POST['High'])
    Open = float(request.POST['Open']) 
    low = float(request.POST['Low'])


    
    if (High-Open)/50 > (Open-low)/50:
        print(f"{low} is the entry price")
        EntryPrice = float(low)

        result = (math.ceil((Open+1)/50))*50
        StrikePrice = result+50
      
    else:
        print(f"{High} is the entry price")
        EntryPrice = float(High)

        result = (math.floor((Open-1)/50))*50
        StrikePrice = result-50

    # EntryPrice = float(request.POST['entry'])
    # StrikePrice = float(request.POST['strike'])

    print(EntryPrice)
    print(StrikePrice)

    # EntryPrice = 15135
    # StrikePrice	= 14950

    outputValue = (EntryPrice-StrikePrice)/4
    count = 0

    lst = []

    for i in range(0,16):

        # print(outputValue)
        NewValue = round(outputValue*(i+1),2)

        OneFourth = round(outputValue*(count+0.25),2)
        Half = round(outputValue*(count+0.50),2)
        ThreeFourth = round(outputValue*(count+0.75),2)

        count = count+1



        if i ==0:
            lst.append(("(1\\4)",abs(OneFourth)))
            lst.append(("(1\\2)",abs(Half)))
            lst.append(("(3\\4)",abs(ThreeFourth)))
            lst.append((i+1,abs(NewValue)))
        else:
            lst.append((str(i)+"(1\\4)",abs(OneFourth)))
            lst.append((str(i)+"(1\\2)",abs(Half)))
            lst.append((str(i)+"(3\\4)",abs(ThreeFourth)))
            lst.append((i+1,abs(NewValue)))


    # lst.append(("S.no","Value",'1\\4','1\\2','3\\4'))

    def Reverse(lst):
        return [ele for ele in reversed(lst)]

    # Driver Code
    lst = Reverse(lst)

    # print(lst)
    def chunkIt(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return out
    lst = chunkIt(lst, 4)


    # Driver Code
    lst = Reverse(lst)
    response = render(request, 'hello_world.html', {'lst': lst,'EntryPrice':EntryPrice,'StrikePrice':StrikePrice } )

    return response

