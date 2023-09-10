from django.urls import path
from users.views import login_ajax, register_ajax, ProfileView, AdvertView, OrdersView, FairsView, CreateAdvertisementView

urlpatterns = [
    path('accounts/ajax/login/', login_ajax, name='login_ajax'),
    path('accounts/ajax/register/', register_ajax, name='register_ajax'),
    path('profile', ProfileView.as_view(), name="profile"),
    path('profile/advert', AdvertView.as_view(), name="advert"),
    path('profile/orders', OrdersView.as_view(), name="orders"),
    path('profile/fairs', FairsView.as_view(), name="fairs"),
    path('profile/advertisement/create', CreateAdvertisementView.as_view(), name="create_advertisement"),
]
