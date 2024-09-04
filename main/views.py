from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306201861',
        'name': 'Rahardi Salim',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)