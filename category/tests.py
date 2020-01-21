from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from category.api.serializers import CategorySerializer
from category.models import Category


class CategoryTestCase(TestCase):
    client = Client()

    def setUp(self):
        user = User.objects.create_user('test', 'test@test.com', 'secret')
        Category.objects.create(name="Sports", slug="sports", created_by=user, updated_by=user, created_at=timezone.now(), updated_at=timezone.now())

    def test_category_created(self):
        category = Category.objects.get(name="Sports")
        self.assertEqual(category.__str__(), "Sports")

    def test_get_all_category(self):
        response = self.client.get(reverse('category')) #@todo : find corrent url to reverse
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
