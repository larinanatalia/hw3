from pprint import pprint

from django.shortcuts import render
import csv
import os

from django.conf import settings


def inflation_view(request):
    template_name = 'inflation.html'
    with open(r'C:\Users\79035\Desktop\django_netology\dj-homeworks\dynamic-templates\task1\inflation_russia.csv', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        total_format = []
        for item in reader:
            for each_list in item:
                without_quotes = each_list.split(';')
                if '' in without_quotes:
                    spare = list()
                    for item in without_quotes:
                        if item == '':
                            item = item.replace("", "-")
                        spare.append(item)
                    total_format.append(spare)
                else:
                    total_format.append(without_quotes)


    # чтение csv-файла и заполнение контекста
    context = {'total_format': total_format[1:],
               'header': total_format[0]}

    return render(request, template_name,
                  context)