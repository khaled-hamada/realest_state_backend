from django.contrib.auth import  get_user_model
User = get_user_model()  ## this how to get the user when creating a custom user model , you cannot use import 

from rest_framework.response import Response
from rest_framework.views import APIView ## generic class based view 
from rest_framework import permissions
# from django.views.decorators.csrf import csrf_exempt


class SignupView(APIView):
    """  thid class view used to create users first time they visit our website
        in order to do so, we allow all people to reach this view so that they can
        signup bu setting permissions to allow any

        after that we validate both email to be unique and passward to be 6 chars at least 
        in case of any validation we return an error response to the requested page 
     """
    permission_classes = (permissions.AllowAny, )

    ## def get , post ... methods that will come from your api 
    def post(self, request, format=None):
        data = self.request.data
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password2 == password:
        ## i will also validate form data in the frontend  using validator lib 
            if User.objects.filter(email = email).exists():
                ##error duplicate email 
                return Response({"error": "Email already exists"})
            else:
                ##if pass < 6 
                if len(password) < 6:
                    return Response({"error": "Password is very weak , length must be at least six chars"})
                else:
                    user = User.objects.create_user(email = email , name= name ,password = password )
                    user.save()
                    return Response({"success": "User created successfully"})
                
        else :
            return Response({"error":"password does not match"})
