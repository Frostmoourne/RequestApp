from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .serializers import *
# Create your tests here.


class GetTest(TestCase):
    """Тест get-запросов"""
    def setUp(self) -> None:

        self.client = APIClient()
        self.new_client = Client.objects.create(name='Ivanov Ivan', phone='+7999999999')
        self.employee = Employee.objects.create(name='Vasiliev Vasiliy', position='admin')
        self.request_1 = Request.objects.create(text='Заявка 1', responsible=self.employee, client=self.new_client)
        self.request_2 = Request.objects.create(text='Заявка 2', responsible=self.employee, client=self.new_client)

    def test_get_request(self):
        request_1 = Request.objects.get(text='Заявка 1')
        request_2 = Request.objects.get(text='Заявка 2')
        response = Request.objects.all()
        self.assertIn(request_1, response)
        self.assertIn(request_2, response)

    def test_url(self):
        """Тест urls"""
        response = self.client.get(f'/api/requests/{self.request_1.pk}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(f'/api/requests/create')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class CreateNewRequest(TestCase):
    """Тест post-запросов"""
    def setUp(self):
        self.new_client = Client.objects.create(name='Ivanov Ivan', phone='+7999999999')
        self.employee = Employee.objects.create(name='Vasiliev Vasiliy', position='admin')
        self.valid_request = {
            'text': 'Заявка 123',
            'responsible': self.employee,
            'client': self.new_client,
        }

    def test_create_request(self):
        self.serializer = RequestUpdateSerializer(instance=self.valid_request)
        data = self.serializer.data
        new_requests = self.client.post(f'/api/requests/create', data=data)

        self.assertEqual(data['text'], new_requests.data['text'])
        self.assertEqual(data['client'], new_requests.data['client'])


class UpdateRequest(TestCase):
    """Тест put-запросов"""
    def setUp(self):
        self.client = APIClient()
        self.new_client = Client.objects.create(name='Ivanov Ivan', phone='+7999999999')
        self.employee = Employee.objects.create(name='Vasiliev Vasiliy', position='admin')
        self.valid_request = {
            'text': 'Заявка 123',
            'responsible': self.employee,
            'client': self.new_client,
        }
        self.new_request = {
            'text': 'Заявка 12345',
            'responsible': self.employee,
            'client': self.new_client,
        }
        self.request = Request.objects.create(**self.valid_request)

    def test_update_request(self):
        self.serializer = RequestUpdateSerializer(instance=self.new_request)
        data = self.serializer.data
        response = self.client.put(f'/api/requests/{self.request.pk}', data=data)
        self.assertEqual(data['text'], response.data['text'])
        self.assertEqual(data['responsible'], response.data['responsible'])


class DeleteRequest(TestCase):
    """Тест delete-запросов"""
    def setUp(self):
        self.new_client = Client.objects.create(name='Ivanov Ivan', phone='+7999999999')
        self.employee = Employee.objects.create(name='Vasiliev Vasiliy', position='admin')
        self.valid_request = {
            'text': 'Заявка 123',
            'responsible': self.employee,
            'client': self.new_client,
        }
        self.request = Request.objects.create(**self.valid_request)

    def test_create_request(self):
        new_request = self.client.delete(f'/api/requests/{self.request.pk}/delete')
        self.assertEqual(new_request.status_code, status.HTTP_204_NO_CONTENT)

