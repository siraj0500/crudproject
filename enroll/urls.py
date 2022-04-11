from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.add_show, name='addandshow'),
    # (2) created path of index page [ kept the single quot to enter in to the index directly
    # then import views from enroll app, views.add_show (added add_show function from views),
    # gave a name for the path for future uses ]


    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    # delete path:  first delete will be coming from the html, and convert the id into integer,
    # specify the delete function path from views.py , finally gave a name for the path for future uses.


    path('<int:id>', views.update_data, name='updatedata')
    # update path:update function can have a name as edit/update accordingly or even if there isn't any name,
    # it can work with id also it should work dynamically so this is a better way to do it,
    # convert the id into integer,specify the update function path from views.py ,
    # finally gave a name for the path for future uses.
]
