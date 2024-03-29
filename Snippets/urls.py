from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='add_snippet_page'),
    path('snippets/<int:snip_id>/update',
         views.update_snippet_page, name='update_snippet_page'),
    path('snippets/list', views.snippets_page, name = 'snippets_page'),
    path('snippets/<int:snip_id>/delete', views.deleteSnippet, name='deleteSnippet'),
#    path('snippets/create_snippet', views.create_snippet, name='create_snippet'),
    path('snippets/<int:snip_id>', views.get_snippets_info_page, name='snippets_info_page'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('comment/add', views.comment_add, name="comment_add"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
