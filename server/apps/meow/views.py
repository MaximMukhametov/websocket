from django.shortcuts import render


def start_task(request):
    return render(request, "index.html", {})

def table(request):
    return render(request, "index_table.html", {})
