from django.urls import path
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'lists', Student_Viewset, basename = 'listdata')
urlpatterns = router.urls



'''
urlpatterns = [
    path('list/', Student_Viewset.as_view({
        'get':'list',
    })),
    path('list/<pk>/', Student_Viewset.as_view({
        'get':'retrieve',
    }))
]
'''            
    # path('list/', student_list.as_view() , name='student_list'),
    # path('view/<pk>', student_view, name='student_view'),
    # path('list/<pk>', student_details.as_view(), name='student_view'),
# ]
