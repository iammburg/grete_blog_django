from django.urls import path

# import View dari grete_blog Application
from .views import index_view, detail_view, create_view, update_view, delete_view


app_name = "blog"
urlpatterns = [
    # route untuk halaman daftar blog
    path("", index_view, name="index"),
    # route untuk halaman detail blog
    path("<str:blog_slug>", detail_view, name="detail"),
    # url untuk halaman tambah blog
    path("create/", create_view, name="create"),
    # url untuk halaman ubah blog
    path("update/<str:blog_slug>", update_view, name="update"),
    # url untuk menghapus blog
    path("delete/<str:blog_slug>", delete_view, name="delete"),
]
