from django.shortcuts import render, redirect
from .models import Person, Agent, Hotel, Vehicle

# Create your views here.


# global variables

user = ''
agent = ''
usernameNotAvailable = False
invalidLoginDetails = False
agentnameNotAvailable = False
invalidAgentLoginDetails = False
hotelAdded = False
vehicleAdded = False

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def user_login(request):
    global invalidLoginDetails
    if invalidLoginDetails:
        invalidLoginDetails = False
        pop_up = '''
        <script>
            alert("Invalid Login Details!");
        </script>
        '''
    else:
        pop_up = ''

    return render(request, 'user_login.html', {'pop_up':pop_up})

def agent_login(request):
    global invalidAgentLoginDetails
    if invalidAgentLoginDetails:
        invalidAgentLoginDetails = False
        pop_up = '''
        <script>
            alert("Invalid Login Details!");
        </script>
        '''
    else:
        pop_up = ''

    return render(request, 'agent_login.html', {'pop_up':pop_up})

def user_signup(request):
    global usernameNotAvailable
    if usernameNotAvailable:
        usernameNotAvailable = False
        pop_up = '''
        <script>
            alert("username already taken!");
        </script>
        '''
    else:
        pop_up = ''

    return render(request, 'user_signup.html', {'pop_up':pop_up})

def agent_signup(request):
    global agentnameNotAvailable
    if agentnameNotAvailable:
        agentnameNotAvailable = False
        pop_up = '''
        <script>
            alert("username already taken!");
        </script>
        '''
    else:
        pop_up = ''

    return render(request, 'agent_signup.html', {'pop_up':pop_up})

def user_signup_handle(request):
    global usernameNotAvailable
    nm = request.POST['name']
    usname = request.POST['username']
    pswd = request.POST['password']
    try:
        obj = Person.objects.get(username=usname)
        usernameNotAvailable = True
        return redirect(user_signup)
    except:
        obj = Person()
        obj.name = nm
        obj.username = usname
        obj.password = pswd
        obj.save()
        return redirect(user_login)

def agent_signup_handle(request):
    global agentnameNotAvailable
    nm = request.POST['name']
    usname = request.POST['username']
    pswd = request.POST['password']
    try:
        obj = Agent.objects.get(username=usname)
        agentnameNotAvailable = True
        return redirect(agent_signup)
    except:
        obj = Agent()
        obj.name = nm
        obj.username = usname
        obj.password = pswd
        obj.save()
        return redirect(agent_login)

def user_login_handle(request):
    global user, invalidLoginDetails
    usname = request.POST['username']
    pswd = request.POST['password']
    try:
        obj = Person.objects.get(username=usname)
        if obj.password == pswd:
            user = usname
            return redirect(user_home)
        invalidLoginDetails = True
        return redirect(user_login)
    except:
        invalidLoginDetails = True
        return redirect(user_login)

def agent_login_handle(request):
    global agent, invalidAgentLoginDetails
    usname = request.POST['username']
    pswd = request.POST['password']
    try:
        obj = Agent.objects.get(username=usname)
        if obj.password == pswd:
            agent = usname
            return redirect(agent_home)
        invalidAgentLoginDetails = True
        return redirect(agent_login)
    except:
        invalidAgentLoginDetails = True
        return redirect(agent_login)

def user_home(request):
    obj = Person.objects.get(username = user)
    nm = obj.name
    return render(request, 'user_home.html', {'name':nm})

def agent_home(request):
    obj = Agent.objects.get(username = agent)
    nm = obj.name
    return render(request, 'agent_home.html', {'name':nm})

def agent_hotel(request):
    global hotelAdded
    if hotelAdded:
        hotelAdded = False
        pop_up = '''
        <script>
            alert("Hotel Added Succesfully!");
        </script>
        '''
    else:
        pop_up = ''
    return render(request, 'agent_hotel.html', {'pop_up':pop_up})

def user_hotel(request):

    hotelList = Hotel.objects.all()

    code = ''
    top = 10
    temp = '''
    <div class="hotel_box" style="top:{}%">
        <div id="hotel_image">
            {}
        </div>
        <div id="hotel_addr">
            {}
        </div>
        <div id="hotel_name">
            {}
        </div>
        <div id="hotel_desc">
            {}
        </div>
        <div id="hotel_refund" class="{}">
            {}
        </div>
        <div id="hotel_price">
            {}
        </div>
        <div id="hotel_agent">
            {}
        </div>
        <div id="hotel_book_btn">
            {}
        </div>
    </div>
    '''

    for htl in hotelList:
        flag = False
        for i in htl.person.all():
            if i.username == user:
                flag = True
                break
        if flag:
            btn = '''
                <form action="hotel_cancle_handle" style="height:100%">
                    <input type="submit" value="Cancle" class="hotel_cancle_btn">
                    <input type="hidden" value="''' +  htl.name + '''" name="hidden">
                </form>
            '''
        else:
            btn = '''
                <form action="hotel_booking_handle" style="height:100%">
                    <input type="submit" value="Book" class="hotel_booking_btn">
                    <input type="hidden" value="''' +  htl.name + '''" name="hidden">
                </form>
            '''
        code += temp.format(
            top,
            '''
            <img src="'''+ str(htl.image) +'''" class="hotel_img">
            ''',
            "<b>Address:</b> " + htl.address,
            htl.name,
            "<b>Description:</b> " + htl.desc,
            "hotel_refund_green" if htl.isRefundable else "hotel_refund_red",
            "Refundable" if htl.isRefundable else "Non Refunable",
            "<b>Price:</b> ₹" + str(htl.price),
            "<b>Agent:</b> " + htl.agent.name,
            btn
        )
        top += 90

    return render(request, 'user_hotel.html', {'code':code})

def hotel_booking_handle(request):
    nm = request.GET['hidden']
    obj = Hotel.objects.get(name=nm)
    obj.person.add(Person.objects.get(username=user))

    return redirect(user_hotel)

def vehicle_booking_handle(request):
    nm = request.GET['hidden']
    obj = Vehicle.objects.get(number=nm)
    obj.person.add(Person.objects.get(username=user))

    return redirect(user_vehicle)

def hotel_cancle_handle(request):
    nm = request.GET['hidden']
    obj = Hotel.objects.get(name=nm)
    obj.person.remove(Person.objects.get(username=user))

    return redirect(user_hotel)

def vehicle_cancle_handle(request):
    nm = request.GET['hidden']
    obj = Vehicle.objects.get(number=nm)
    obj.person.remove(Person.objects.get(username=user))

    return redirect(user_vehicle)

def agent_hotel_handle(request):
    global hotelAdded
    nm = request.POST['name']
    addr = request.POST['address']
    fl = request.FILES['image']
    refund = request.POST['refund']
    prs = request.POST['price']
    description = request.POST['description']

    obj = Hotel()
    obj.name = nm
    obj.address = addr
    obj.image = fl
    if refund == 'Yes':
        obj.isRefundable = True
    else:
        obj.isRefundable = False
    obj.price = int(prs)
    obj.desc = description
    obj.agent = Agent.objects.get(username = agent)
    obj.save()
    hotelAdded = True
    return redirect(agent_hotel)

def agent_vehicle_handle(request):
    global vehicleAdded
    tp = request.POST['type']
    im = request.FILES['image']
    num = request.POST['number']
    rt = request.POST['rent']
    com = request.POST['company']

    obj = Vehicle()
    obj.vehicleType = tp
    obj.image = im
    obj.number = num
    obj.rent = rt
    obj.company = com
    obj.agent = Agent.objects.get(username=agent)
    obj.save()
    vehicleAdded = True
    return redirect(agent_vehicle)

def agent_vehicle(request):
    global vehicleAdded
    if vehicleAdded:
        vehicleAdded = False
        pop_up = '''
        <script>
            alert("Vehicle Added Succesfully!");
        </script>
        '''
    else:
        pop_up = ''
    return render(request, 'agent_vehicle.html', {'pop_up':pop_up})

def user_vehicle(request):
    vehicleList = Vehicle.objects.all()

    code = ''
    top = 10
    temp = '''
    <div class="hotel_box" style="top:{}%">
        <div id="vehicle_image">
            {}
        </div>
        <div id="vehicle_type">
            {}
        </div>
        <div id="vehicle_number">
            {}
        </div>
        <div id="vehicle_rent">
            {}
        </div>
        <div id="vehicle_company">
            {}
        </div>
        <div id="vehicle_agent">
            {}
        </div>
        <div id="vehicle_book_btn">
            {}
        </div>
    </div>
    '''

    for vcl in vehicleList:
        flag = False
        for i in vcl.person.all():
            if i.username == user:
                flag = True
                break
        if flag:
            btn = '''
                <form action="vehicle_cancle_handle" style="height:100%">
                    <input type="submit" value="Cancle" class="vehicle_cancle_btn">
                    <input type="hidden" value="''' +  vcl.number + '''" name="hidden">
                </form>
            '''
        else:
            btn = '''
                <form action="vehicle_booking_handle" style="height:100%">
                    <input type="submit" value="Book" class="vehicle_booking_btn">
                    <input type="hidden" value="''' +  vcl.number + '''" name="hidden">
                </form>
            '''
        code += temp.format(
            top,
            '''
            <img src="'''+ str(vcl.image) +'''" class="vehicle_img">
            ''',
            "<b>Vehicle Type:</b> " + vcl.vehicleType,
            "<b>Vehicle Number:</b> " + vcl.number,
            "<b>Rent:</b> " + str(vcl.rent),
            "<b>Company:</b> " + vcl.company,
            "<b>Agent:</b> " + vcl.agent.name,
            btn
        )
        top += 90

    return render(request, 'user_vehicle.html', {'code':code})

def aboutus(request):
    return render(request, 'aboutus.html')

def aboutusUser(request):
    return render(request, 'aboutusUser.html')