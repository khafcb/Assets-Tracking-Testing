from django.shortcuts   import render
from django.http        import HttpResponse
from .models import *


# Create your views here.


def home(request): 
    subscriber = Subscriber.objects.all()
    
    total_subscribers = subscriber.count()

    borrowing = Borrowing.objects.all()

    return render(request, 'assetstracking/home.html', 
        {'subscriber': subscriber, 'total_subscribers':total_subscribers, 'borrowing':borrowing }
        )
    

def subscriber(request, subscriber_test): 

    subscriber = Subscriber.objects.get(id=subscriber_test)
	
    borrowings = subscriber.borrowing_set.all()
    borrowing_count = borrowings.count()

    employees = subscriber.employee_set.all()
    employee_count = employees.count()

    tags = subscriber.tag_set.all()
    tag_count = tags.count()
    
    rfids = subscriber.rfid_set.all()
    rfid_count = rfids.count()

    context =   {'subscriber': subscriber, 
                'borrowings': borrowings, 'borrowing_count': borrowing_count,
                'employees': employees, 'employee_count': employee_count,
                'tags': tags , 'tag_count': tag_count,
                 'rfids': rfids , 'rfid_count': rfid_count
                }
    return render(request, 'assetstracking/subscriber.html', context)


def employee(request, employee_test): 

    employee = Employee.objects.get(id=employee_test)
	
    borrowings = employee.borrowing_set.all()
    borrowing_count = borrowings.count()

    context = {'employee': employee, 'borrowings': borrowings, 'borrowing_count':borrowing_count}
    return render(request, 'assetstracking/employee.html', context)


def rfid(request): 
    rfid = RFID.objects.all()
    return HttpResponse('RDID reader page')


def tags(request): 
    tags = Tag.objects.all()
    return render(request, 'assetstracking/tags.html', {'tags': tags})


def index(request): 
    return render(request, 'assetstracking/index.html')
