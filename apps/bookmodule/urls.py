from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.formatting, name="books.formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('search/', views.search),
    path('simple/query/', views.simple_query),
    path('complex/query/', views.complex_query),
    path('lab8/task1/', views.task1),
    path('lab8/task2/', views.task2),
    path('lab8/task3/', views.task3),
    path('lab8/task4/', views.task4),
    path('lab8/task5/', views.task5),
    path('lab8/task7/', views.task7),
    path('lab9/task22', views.task22),
    path('lab9/task33', views.task33),  
    path('lab9/task44', views.task44),  
    path('lab9/task55', views.task55),  
    path('lab9_part1/listbooks', views.listbooks, name="list_books"),     
    path('lab9_part1/addbook', views.addbook, name= "add_book"),    
    path('lab9_part1/editbook/<int:id>', views.editbook, name= "edit_book"),    
    path('lab9_part1/deletebook/<int:id>', views.deletebook, name= "delete_book"),
    path('lab9_part2/listbooks2', views.listbooks2, name="list_books2"),     
    path('lab9_part2/addbook2', views.addbook2, name= "add_book2"),    
    path('lab9_part2/editbook2/<int:id>', views.editbook2, name= "edit_book2"),    
    path('lab9_part2/deletebook2/<int:id>', views.deletebook2, name= "delete_book2"), 
    path('students/list/', views.list_students, name="list_students"),
    path('students/add/', views.addstudent, name="add_student"),
    path('students/edit/<int:id>/', views.editstudent, name="edit_student"),
    path('students/delete/<int:id>/', views.deletestudent, name="delete_student"),
    path('students/list2/', views.list_students2, name="list_students2"),
    path('students/add2/', views.addstudent2, name="add_student2"),
    path('students/edit2/<int:id>/', views.editstudent2, name="edit_student2"),
    path('students/delete2/<int:id>/', views.deletestudent2, name="delete_student2"),
    path('profiles/list', views.list_profiles, name='list_profiles'),
    path('profiles/add/', views.add_profile, name='add_profile'),
    path('profiles/edit/<int:id>/', views.edit_profile, name='edit_profile'),
    path('profiles/delete/<int:id>/', views.delete_profile, name='delete_profile'),

] 


