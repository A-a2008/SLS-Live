from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('problems/', views.problems, name='problems'),
    path('consequences/', views.consequences, name='consequences'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('career-goals/', views.career_goals, name='career-goals'),
    path("story/each-story/<int:id>", views.get_by_id, name='each_story'),
    path("stories/write/", views.write_stories, name="write_stories"),
    path("stories/how-to/", views.how_to_write_stories, name="how_to_write_stories"),
]
