from django.urls import path
from . import views
app_name='pics'
urlpatterns =[

    path('create',views.CreatePic.as_view(),name='createPic'),
    path('pic/<int:pk>',views.PicDetails.as_view(),name='pic_details'),
    path('pic/<int:pk>/update',views.UpdatePic.as_view(),name='updatePic'),
    path('',views.PicListView.as_view(),name='picList'),
    path('pic/<int:pk>/delete',views.DeletePic.as_view(),name='deletePic'),
    path('pic_picture/<int:pk>',views.file_stream,name='pic_picture'),
    path('pic/<int:pk>/create_comment',views.CreateCommentView.as_view(),name='create_comment'),
    path('pic/<int:pk1>/comment/<int:pk2>/delete',views.DeleteCmmentView.as_view(),name='Delete_comment')
]