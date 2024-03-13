from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from authorization.models import UserManager
from products.models import Category
from rest_framework_simplejwt.tokens import AccessToken

class CategoryApiTestCase(APITestCase):
    
    def setUp(self):
        Category.objects.create(name_category='ААА')
    
    def test_category_list(self):
        response = self.client.get(reverse('categories'))
        print(response.data)
    
    
    
    
    
    # def setUp(self):
    #     self.user = UserManager().create_user(email='testuser@example.com', 
    #                                          first_name='Test', 
    #                                          last_name='User', 
    #                                          password='12345')
        
    #     self.access_token = str(AccessToken.for_user(self.user))

    # def test_list_categories(self):
    #     url = '/api/categories/' 
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
    #     response = self.client.get(url)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # Проверьте, что вернутые данные соответствуют ожидаемому формату
    #     expected_data = [
    #     {
    #         "id": 2,
    #         "name_category": "Витамины и БАДы"
    #     },
    #     {
    #         "id": 3,
    #         "name_category": "Косметика"
    #     },
    #     {
    #         "id": 4,
    #         "name_category": "Красота и здоровье"
    #     },
    #     {
    #         "id": 1,
    #         "name_category": "Детство"
    #     },
    #     {
    #         "id": 5,
    #         "name_category": "Лекарства"
    #     }
    #     ]
    #     self.assertEqual(response.data, expected_data)
