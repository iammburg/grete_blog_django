from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Blog dari file grete_blog/models.py
from .models import Blog


# membuat class BlogForm untuk membuat Blog
class BlogForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Blog
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ("title", "slug", "content")
        # mengatur teks label untuk setiap field
        labels = {
            "title": _("Judul"),
            "slug": _("Slug"),
            "content": _("Konten"),
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            "title": {
                "required": _("Judul harus diisi."),
            },
            "content": {
                "required": _("Konten harus diisi."),
            },
        }
