from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def firstApp(request):
    if request.method == "POST":
        name = request.data['name']
        age = request.data['age']
        print("name: "+name+" age: "+age)
        postContext = {"name": name,"age": age}
        return Response(postContext)
    getContext = {"name": "Alex Smith","university": "MIST"}
    return Response(getContext)
