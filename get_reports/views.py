from answers.models import Answers
from check_list.models import Checklist
from django.shortcuts import render
import csv
from django.http import HttpResponse

# Create your views here.

def get_all_report(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

def findItemInArray(item,list):
    found = False
    for i in list:
        if str(i) == str(item): found = True
    return found

def get_report_for_vehicle(request,vehicle):

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    # AddHeader Check
    add_header = False
    add_date = False
    processed = []
    res =  Answers.objects.filter(vehicle=1)
    # Get answers for specific date
    for i in res:
        print(i.updated_at,processed,findItemInArray(i.updated_at,processed))
        if findItemInArray(i.updated_at,processed) == False:
            header = []
            data = []
            for j in Answers.objects.filter(updated_at=i.updated_at):
                if add_date == False:
                    header.append('Date')
                    data.append(i.updated_at)
                    add_date = True
                else:
                    header.append(j.question) 
                    data.append(j.answer)
            if add_header == False:
                writer.writerow(header)
                add_header = True
            else:
                writer.writerow(data) 
                processed.append(str(i.updated_at))
            header = []
            data = [] 
            add_date = False


    return response

def get_report_for_vehicle_by_date(request,vehicle,date):

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)

    # header for csv file 
    header = ['Date']
    data = [date]
    # Get answers for specific date
    for i in Answers.objects.filter(updated_at=date):
        header.append(i.question)
        data.append(i.answer)


    writer.writerow(header)
    writer.writerow(data)

    return response