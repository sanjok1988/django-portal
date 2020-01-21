from django.test import TestCase

from model_bakery import baker
from category.models import Category


class CategoryTestModel(TestCase):

    def setUp(self):
        category = baker.make(Category, _quantity=3)
        assert len(category) == 3

