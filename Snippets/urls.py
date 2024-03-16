from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='add_snippet_page'),
    path('snippets/list', views.snippets_page, name = 'snippets_page'),
    path('snippets/dell/<int:snip_id>', views.deleteSnippet, name='deleteSnippet'),
#    path('snippets/create_snippet', views.create_snippet, name='create_snippet'),
    path('snippets/<int:snip_id>', views.get_snippets_info_page, name='snippets_info_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
