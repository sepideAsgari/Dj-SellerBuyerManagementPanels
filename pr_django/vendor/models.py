# from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from PIL import Image
from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.utils.text import slugify
from django.contrib.auth import get_user_model
from accounts.models import Vendor
# from .utils import resize_image
import os


# class Vendor(models.Model):
#     username_validator = UnicodeUsernameValidator()
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL,
#     #                          on_delete=models.CASCADE)
#     user = models.ForeignKey(get_user_model(
#     ),null=True, on_delete=models.CASCADE, limit_choices_to={'user_type': 'vendor'})
#     full_name = models.CharField(max_length=100, null=True)
#     first_name = models.CharField(max_length=100, null=True)
#     last_name = models.CharField(max_length=100, null=True)
#     address = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=20, null=True)
#     email = models.EmailField(null=True)
#     mini_description = models.TextField(blank=True)
#     #
#     profile_picture = models.ImageField(
#         upload_to='vendor_profile_pictures/', blank=True, null=True)
#     #
#     bank_account_number = models.CharField(max_length=50, blank=True)
#     #
#     latitude = models.FloatField(null=True, blank=True)
#     longitude = models.FloatField(null=True, blank=True)
#     #
#     date_joined = models.DateTimeField(auto_now_add=True, null=True)
#     last_login = models.DateTimeField(null=True, blank=True)
#     #
#     visit_count = models.IntegerField(default=0)
#     sales_count = models.IntegerField(default=0)
#     #
#     is_active = models.BooleanField(default=True)

#     username = models.CharField(("username"), max_length=150, unique=True, help_text=("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),validators=[username_validator],
#     error_messages={"unique": ("کاربری با این شناسه در سایت عضو می باشد"),},
#     )
#     password = models.CharField(max_length=64,null=True, blank=True)

#     def __str__(self):
#         return self.username

#     def get_last_login_time(self):
#         return self.last_login.strftime("%Y-%m-%d %H:%M:%S") if self.last_login else "User hasn't logged in yet."

#     # def save(self, *args, **kwargs):
#     #     # چک کنید که تصویر جدید آپلود شده است
#     #     if self.pk:  # چک کنید که این یک ذخیره جدید یا تغییر وضعیت فیلد است
#     #         try:
#     #             vendor = Vendor.objects.get(pk=self.pk)
#     #             if vendor.profile_picture != self.profile_picture:  # چک کنید که تصویر قبلی با تصویر جدید متفاوت است
#     #                 # تصویر جدید آپلود شده است، بنابراین آن را تبدیل کرده و در پوشه مورد نظر ذخیره کنید
#     #                 input_image_path = self.profile_picture.path
#     #                 output_image_path = os.path.join(
#     #                     'media', 'vendor_profile_pictures', os.path.basename(input_image_path))
#     #                 if resize_image(input_image_path, output_image_path):
#     #                     # ذخیره مسیر تصویر تغییر یافته
#     #                     self.profile_picture = os.path.relpath(
#     #                         output_image_path, 'media')
#     #         except Vendor.DoesNotExist:
#     #             pass
#     #     super(Vendor, self).save(*args, **kwargs)
#     # def save(self, *args, **kwargs):
#     #     super().save(*args, **kwargs)

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    # سایر فیلدهای مربوط به محصول

    def __str__(self):
        return self.name
