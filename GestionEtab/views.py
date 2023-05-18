from django.shortcuts import render
import matplotlib.pyplot as plt
from .models import *
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.paginator import *

import pandas as pd

def home(request):
    return render(request, 'base.html')

def excel_view(request):
    p = request.GET.get("page",1)
    groupe = 'GR'+str(p)
    file_path = './' + str(groupe) + '.xlsx'
    try:
        df = pd.read_excel(file_path)
        html_table = df.to_html(classes='table table-striped')
        return render(request, 'data.html', {'data': html_table,'groupe':p})
    except FileNotFoundError:
        return render(request, 'data.html', {'data': 'File not found'})
    
    
def chart_view(request, grp):
    groupe = 'GR'+str(grp)
    df = pd.read_excel('./'+str(groupe)+'.xlsx')
    fig, ax = plt.subplots(figsize=(12, 6))

    df = pd.read_excel('./' + str(groupe) + '.xlsx')
    plt.figure(figsize=(10, 6))
    plt.bar(df['Name'], df['Total Hours/Week'])
    plt.xlabel('Name')
    plt.ylabel('Total Hours/Week')
    plt.title('Attendance')
    plt.savefig('GestionEtab/static/GestionEtab/' + str(groupe) + '.png')

    df2 = pd.read_excel('./' + str(groupe) + '.xlsx')
    genre_counts = df2['Genre'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%')
    plt.title('Genre Distribution')
    plt.savefig('GestionEtab/static/GestionEtab/' + str(groupe) + 'P.png')
    Files = attendenceFile.objects.all()
    return render(request, 'chart.html', {'chartB': 'GestionEtab/'+str(groupe)+'.png','groupe':grp, 'chartP': 'GestionEtab/'+str(groupe)+'P.png','files':Files})

def Login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('recipe_list')
    return render(request, 'login.html')

def Logout_user(request):
    logout(request)
    return redirect('login')