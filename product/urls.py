from django.urls import path 
from .import views
urlpatterns =[
    path('',views.home),
    path('mycart',views.mycart,name="mycart"),
    path('base',views.base,name="base"),
    path('croptop',views.croptop,name="croptop"),
    path('tshirt',views.tshirt,name="tshirt"),
    path('shirt',views.shirt,name="shirt"),
    path('aline',views.aline,name="aline"),
    path('bodycon',views.bodycon,name="bodycon"),
   
   
    path('allitems',views.allitems,name="allitems"),
    path('buy/<int:id>/<price>/<av>/<str:cat>',views.buy,name="buy"),
    path('billing',views.bill,name="billing"),
    path('bills',views.bills,name="bills"),
    path('signup',views.signuppage,name='signup'),
    path('login',views.logInpage,name='login'),
    path('logout',views.LogOutpage,name='logout'),
    path('footwear',views.footwear,name="footwear"),
    path('search',views.search,name='search'),
    path('rating',views.rating,name="rating"),
    path('submitreview',views.submitreview,name="submitreview"),
    path('shoe',views.shoe,name="shoe"),
    
]