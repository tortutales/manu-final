from django.shortcuts import render

# def login(request):
#     return 

def index(request):
    latest_question_list = []
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'webproject/admin/index.html', context)