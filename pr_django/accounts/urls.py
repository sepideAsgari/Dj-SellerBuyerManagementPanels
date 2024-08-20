# from django.urls import path, include
# from django.urls import path
# from accounts import views


# urlpatterns = [
#     path('get-user-info/', views.get_user_info)
# ]
from django.urls import path
from accounts.views import UserInfoView, VendorRegisterView

urlpatterns = [
    path('get/', UserInfoView.as_view()),
    path('vendors/', VendorRegisterView.as_view()),
    # سایر مسیرها
]