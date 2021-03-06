import csv, io
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from core.models import Local

@login_required
def local_upload(request):

    template = "local_upload.html"
    data = Local.objects.all()

    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data    
              }
              
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Local.objects.update_or_create(
            nome=column[4],
            logradouro=column[5],
            bairro=column[6],
            cidade=column[7],
        )
    context = {}
    return render(request, template, context)