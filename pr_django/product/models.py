from io import BytesIO
import uuid
from django_jalali.db import models as jmodels  # type: ignore
from PIL import Image
import random
# from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg, F, FloatField, ExpressionWrapper, Count
from django.core.files import File
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from unidecode import unidecode
from django.utils.crypto import get_random_string


def create_new_serial_number():
    return str(random.randint(1000000, 9999999))


class Category(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

    # def get_category_name(self):
    #     return f'/{self.name}'


def custom_slugify(value):
    value = unidecode(value)
    return slugify(value, allow_unicode=True)


def unique_slugify(instance, value, slug_field_name='slug'):
    slug = custom_slugify(value)
    model_class = instance.__class__
    queryset = model_class.objects.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)
    unique_slug = slug
    counter = 1
    while queryset.filter(**{slug_field_name: unique_slug}).exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1
    return unique_slug


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    serial = models.CharField(
        max_length=7, unique=True, editable=False, default=create_new_serial_number)
    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=0)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_category_name(self):
        return self.category.name

    def averageReview(self):
        reviews = Review.objects.filter(
            product=self, is_active=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(round(reviews['average'], 1))
        return avg

    def countReview(self):
        reviews = Review.objects.filter(
            product=self, is_active=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

    @staticmethod
    # def top_rated_products():
    #     top_rated = Product.objects.annotate(
    #         avg_rating=Avg('review__rating'),
    #         num_reviews=Count('review')
    #     ).filter(is_active=True).order_by('-avg_rating', '-num_reviews')[:4]
    #     return top_rated
    def top_rated_products():
        weight_avg_rating = 0.4
        weight_num_reviews = 0.6

        top_rated = Product.objects.annotate(
            avg_rating=ExpressionWrapper(
                F('review__rating') * weight_avg_rating,
                output_field=FloatField()
            ),
            num_reviews=ExpressionWrapper(
                F('review') * weight_num_reviews,
                output_field=FloatField()
            )
        ).filter(is_active=True).order_by(
            '-avg_rating', '-num_reviews'
        )[:4]

        return top_rated

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            # print('http://127.0.0.1:8000' + self.thumbnail.url)
            # print('1')
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                # print('2')
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                # print('4')
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        print(thumbnail)
        return thumbnail

    def get_make_product_image(self):
        if self.thumbnail:
            # print('http://127.0.0.1:8000' + self.thumbnail.url)
            # print('1')
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_product_image(self.image)
                print('1111')
                self.save()
                # print('2')
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                # print('4')
                return ''

    def make_product_image(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        print(thumbnail)
        return thumbnail


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0, validators=[
                                 MinValueValidator(0), MaxValueValidator(5)])
    avg_rate = models.DecimalField(
        max_digits=2, decimal_places=1, editable=False, default=0.0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, max_length=36,
                          unique=True, primary_key=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=False)

    class Meta:
        ordering = ('-createdAt',)

    def __str__(self):
        return f'{self.user} ID for {self.product}'


@receiver(post_save, sender=Review)
def update_review(sender, instance, created, **kwargs):
    if created:
        reviews = Review.objects.filter(product=instance.product)
        total_rating = sum(
            review.rating for review in reviews if review.rating is not None)
        if reviews.count() > 0:
            avg_rate = total_rating / reviews.count()
            total_rating = total_rating
            instance.avg_rate = avg_rate
            instance.total_rating = total_rating
            instance.save(update_fields=['avg_rate'])

    # def get_rating_stars(self):
    #     if self.rating is not None:
    #         return '★' * self.rating + '☆' * (5 - self.rating)
    #     else:
    #         return ''


# class ProductRate(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     rate = models.IntegerField(null=True, blank=True, default=0, validators=[
#                                MinValueValidator(0), MaxValueValidator(5)])
#     # rate = models.DecimalField(
#     #     max_digits=2, null=True, blank=True, default=0.0, decimal_places=1)
#     avg_rate = models.DecimalField(max_digits=2, decimal_places=1, editable=False,default=0.0)
#     total_rate = models.IntegerField(default=0, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, max_length=36,
#                           unique=True, primary_key=True, editable=False)

#     class Meta:
#         ordering = ('-created_at',)

#     def __str__(self):
#         return f'{self.id} review for {self.product}'
#     # def __str__(self):
#     #     return self.user
