from django.shortcuts import render

# Create your views here.
def alunos_list(request):
    return render(request, 'alunos/alunos_list.html')