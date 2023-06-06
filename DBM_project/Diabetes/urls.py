from django.urls import path
from . import views

urlpatterns = [
    path('Diabetes/',views.Diabetes, name = 'Diabetes'),
    path('takeatest/',views.takeatest, name = 'takeatest'),
    path('submit-form/', views.your_form_submission_view, name = 'submit_form'),
    path('import-csv/', views.import_csv, name = 'import-csv'),
    path('import-stats-data/', views.import_stats_data, name = 'stats-data'),
    path('map/', views.map, name='map'),
    path('information/', views.Diabetesinformation, name = 'information'),
]

