from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User

# Create your views here.
@api_view(['POST'])
def Signup(request):

    myInfo = request.data



    return Response(data = myInfo)


@api_view(['POST'])
def Login(request):

    return Response(data= request.data)
