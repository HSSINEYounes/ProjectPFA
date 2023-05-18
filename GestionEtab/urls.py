from django.urls import path
from .views import excel_view, chart_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('excel/', excel_view, name='excel_view'),
    path('chart/<int:grp>', chart_view, name='chart_view'),
    # path('login/', Login_user, name='login'),
    # path('logout/', Logout_user, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)