from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def upload_file(request):
    global data
    fs = FileSystemStorage()
    if request.method == 'POST':
        uploaded_data = request.FILES['document']
        try:
            fs.delete('file.xlsx')
        except:
            pass
        fs.save('file.xlsx', uploaded_data)
    return render(request, 'upload/index.html')
    
#os.path.join(BASE_DIR, '\media\file.xls'))
def challenge1(request):
    data = pd.read_excel(r'C:\Users\theja\Desktop\django\Elucidata\elucidata\media\file.xlsx')
    lst_pc = []
    lst_lpc = []
    lst_pasmalogen = []
    count = 0
    for i in data.iloc[:, 2]:
        count += 1
        try:
            if i[-3:] == ' PC':
                lst_pc.append(count - 1)
            elif i[-4:] == ' LPC':
                lst_lpc.append(count - 1)
            elif i[-11:] == ' pasmalogen':
                lst_pasmalogen.append(count - 1)
        except:
            continue
    pc_data = pd.DataFrame([data.iloc[x] for x in lst_pc])
    lpc_data = pd.DataFrame([data.iloc[x] for x in lst_lpc])
    pasmalogen_data = pd.DataFrame([data.iloc[x] for x in lst_pasmalogen])
    pasmalogen_data.to_csv(r'C:\Users\theja\Desktop\django\Elucidata\pasmalogen_data.xlsx')
    lpc_data.to_csv(r'C:\Users\theja\Desktop\django\Elucidata\lpc_data.xlsx')
    pc_data.to_csv(r'C:\Users\theja\Desktop\django\Elucidata\pc_data.xlsx')
    return render(request, 'upload/index.html')

def challenge2(request):
    fs = FileSystemStorage()
    lst = []
    data = pd.read_excel(r'C:\Users\theja\Desktop\django\Elucidata\elucidata\media\file.xlsx','Raw Data')
    for i in data['Retention time (min)']:
        lst.append(round(i))
    data['update_time'] = [x for x in lst]
    try:
        fs.delete('updated_file.xlsx')
    except:
        pass
    data.to_excel(r'C:\Users\theja\Desktop\django\Elucidata\elucidata\media\updated_file.xlsx')
    return render(request, 'upload/index.html')

def challenge3(request):
    data = pd.read_excel(r'C:\Users\theja\Desktop\django\Elucidata\elucidata\media\updated_file.xlsx')
    mean_data = {}
    count = -1
    for i in data['update_time']:
        count += 1
        if i in mean_data:
            mean_data[i][1] += 1
            mean_data[i][0] += data['Retention time (min)'][count]
        else:
            mean_data[i] = [data['Retention time (min)'][count], 1]
    count = 0
    data['Mean data'] = ''
    for i in data['update_time']:
        data['Mean data'][count] = mean_data[i][0] / mean_data[i][1]
        count += 1
    try:
        fs.delete('updated_file_final.xlsx')
    except:
        pass
    data.to_excel(r'C:\Users\theja\Desktop\django\Elucidata\elucidata\media\updated_file_final.xlsx')
    return render(request, 'upload/index.html')