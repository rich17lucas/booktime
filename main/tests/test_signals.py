from django.test import TestCase
from main import models
from django.core.files.images import ImageFile
from decimal import Decimal

class TestSignal(TestCase):
    def test_thumbnails_are_generated_on_save(self):
        product = models.Product(
            name = "The cathedral the bazaar",
            price = Decimal("10.00"),
        )
        product.save()

    with open(
        "main/fixtures/the-catheral-the-bazaar.thumb.jpg"
        "rb"
    ) as f:
        expected_content = f.read()
        assert image.thumbnail.read() == expected_content

    image.thumbnail.delete(save=False)
    image.image.delete(save=False)