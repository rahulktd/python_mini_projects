from django.urls import path

from core import views, admin_views, student_views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login_view',views.login_view,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),



    path('view_students',admin_views.view_students,name='view_students'),
    path('complaints_to',admin_views.complaints_to,name='complaints_to'),
    path('reply_to_complaint/<int:id>/',admin_views.reply_to_complaint,name='reply_to_complaint'),
    path('activate_student/<int:id>/', admin_views.activate_student, name='activate_student'),
    path('send_notification', admin_views.send_notification, name='send_notification'),



    path('create_complaint', student_views.create_complaint, name='create_complaint'),
    path('reported_complaints', student_views.reported_complaints, name='reported_complaints'),
    path('view_reply', student_views.view_reply, name='view_reply'),
]