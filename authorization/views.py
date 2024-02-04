from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Hello'])
class HelloView(APIView): 
    """ 
    Наследуется от класса APIView, представление будет обрабатывать различные 
    типы запросов (GET, POST, PUT, DELETE)
    """    
    permission_classes = (IsAuthenticated,) # Свойство, которое указывает,
                                                                    # что для доступа необходима аутентификация

    def get(self, request):
        """
        Это метод для обработки HTTP GET-запроса. В случае данного представления, 
        когда отправляется GET-запрос будет получен словарь content с сообщением "Hello, World!".
        """        
        content = {'message': 'Hello, World!'}
        return Response(content)
