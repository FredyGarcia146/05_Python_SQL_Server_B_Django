
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
    
urlpatterns = [
    path('postulant/', views.PostulantsViewSet.as_view(),name='postulants_list'),
    path('postulant/<int:Id>', views.PostulantDetail.as_view(),name='postulant_detail'),
    #/Api/postulant/<int:id>     PostulantDetail
]

urlpatterns= format_suffix_patterns(urlpatterns)