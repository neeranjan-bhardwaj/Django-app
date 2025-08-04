from django.http import HttpResponse
from django.template import loader

def index(request):
    temp=loader.get_template('index.html')
    objects = [
        {
            'name': 'Naruto',
            'id': 1
        },
        {
            'name': 'One Piece',
            'id': 2
        },
        {
            'name': 'Attack on Titan',
            'id': 3
        },
        {
            'name': 'My Hero Academia',
            'id': 4
        },
    ]
constx={
        'x':objects
    }
    # print(objects)
    return HttpResponse(temp.render(constx,request))

def y(request, id):
    template = loader.get_template('y.html')
    return HttpResponse(template.render())