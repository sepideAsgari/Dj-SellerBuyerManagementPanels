# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password



class User(AbstractUser):
    SUPERUSER = 'superuser'
    ADMIN = 'admin'
    CUSTOMER = 'customer'
    VENDOR = 'vendor'

    USER_TYPE_CHOICES = [
        (SUPERUSER, 'Superuser'),
        (ADMIN, 'Admin'),
        (CUSTOMER, 'Customer'),
        (VENDOR, 'Vendor')
    ]

    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=CUSTOMER,
    )

    province = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    REQUIRED_FIELDS = ["email", "user_type", "full_name"]

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'user_type'], name='unique_email_per_user_type')
        ]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.user_type = self.SUPERUSER
        super().save(*args, **kwargs)


class Vendor(User):
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    mini_description = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='vendor_profile_pictures/', blank=True, null=True)
    bank_account_number = models.CharField(max_length=50, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    visit_count = models.IntegerField(default=0)
    sales_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"

    def __str__(self):
        return self.username

    def get_last_login_time(self):
        return self.last_login.strftime("%Y-%m-%d %H:%M:%S") if self.last_login else "User hasn't logged in yet."

    def save(self, *args, **kwargs):
        # Ensure password is hashed properly before saving
        if self.pk is None or 'password' in self.__dict__ and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

# class User(AbstractUser):
#     SUPERUSER = 'superuser'
#     ADMIN = 'admin'
#     CUSTOMER = 'customer'
#     VENDOR = 'vendor'

#     USER_TYPE_CHOICES = [
#         (SUPERUSER, 'Superuser'),
#         (ADMIN, 'Admin'),
#         (CUSTOMER, 'Customer'),
#         (VENDOR, 'Vendor')
#     ]

#     full_name = models.CharField(max_length=100, null=True)
#     email = models.EmailField()
#     user_type = models.CharField(
#         max_length=20,
#         choices=USER_TYPE_CHOICES,
#         default=CUSTOMER,
#     )

#     # Add selectedProvince and selectedCity fields
#     province = models.CharField(max_length=100, null=True, blank=True)
#     city = models.CharField(max_length=100, null=True, blank=True)
#     REQUIRED_FIELDS = ["email", "user_type", "full_name"]

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['email', 'user_type'], name='unique_email_per_user_type')
#         ]

#     def save(self, *args, **kwargs):
#         if self.is_superuser:
#             self.user_type = self.SUPERUSER
#         super().save(*args, **kwargs)


# class Vendor(models.Model):
#     VENDOR = 'vendor'
#     ADMIN = 'admin'

#     USER_TYPE_CHOICES = [
#         (ADMIN, 'Admin'),
#         (VENDOR, 'Vendor')
#     ]

#     username_validator = UnicodeUsernameValidator()
#     user = models.ForeignKey(get_user_model(
#     ), null=True, on_delete=models.CASCADE, limit_choices_to={'user_type': 'vendor'})

#     first_name = models.CharField(max_length=100, null=True)
#     last_name = models.CharField(max_length=100, null=True)
#     address = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=20, null=True)
#     email = models.EmailField(null=True)
#     user_type = models.CharField(
#         max_length=20,
#         choices=USER_TYPE_CHOICES,
#         default=VENDOR,
#     )
#     mini_description = models.TextField(blank=True)

#     profile_picture = models.ImageField(
#         upload_to='vendor_profile_pictures/', blank=True, null=True)

#     bank_account_number = models.CharField(max_length=50, blank=True)
#     latitude = models.FloatField(null=True, blank=True)
#     longitude = models.FloatField(null=True, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True, null=True)
#     last_login = models.DateTimeField(null=True, blank=True)
#     visit_count = models.IntegerField(default=0)
#     sales_count = models.IntegerField(default=0)
#     is_active = models.BooleanField(default=True)

#     # Add selectedProvince and selectedCity fields
#     province = models.CharField(max_length=100, null=True, blank=True)
#     city = models.CharField(max_length=100, null=True, blank=True)

#     username = models.CharField(("username"), max_length=150, unique=True, help_text=("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."), validators=[username_validator],
#                                 error_messages={"unique": (
#                                     "کاربری با این شناسه در سایت عضو می باشد"), },
#                                 )
#     password = models.CharField(max_length=64, null=True, blank=True)

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
