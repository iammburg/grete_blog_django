from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.contrib import messages

# import class BLog dari file grete_blog
from .models import Blog

# import class BlogForm dari file grete_blog/forms.py
from .forms import BlogForm


# Membuat View untuk halaman daftar blog
def index_view(request):
    # Mengambil semua data blog
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    # memparsing data blog ke template grete_blog/index.html dan merender nya
    return render(request, "grete_blog/index.html", context)


def detail_view(request, blog_slug):
    # Mengambil data blog berdasarkan slug
    # Fungsi GET harus spesifik gini ya
    blog = get_object_or_404(Blog, slug=blog_slug)

    context = {"blog": blog}

    # parsing data blog ke template grete_blog/detail.html dan merendernya
    return render(request, "grete_blog/detail.html", context)


def create_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == "POST":
        # membuat objek dari class BlogForm
        new_blog = BlogForm(request.POST)
        # Mengecek validasi form
        if new_blog.is_valid():
            # Simpan data ke dalam table Blogs
            new_blog.save()
            # mengeset pesan sukses dan redirect ke halaman daftar blog
            messages.success(request, "Sukses Menambah Blog baru.")
            return redirect("blog:index")
        else:
            # Jika form tidak valid, kembalikan objek form ke template untuk ditampilkan
            return render(request, "grete_blog/form.html", {"form": new_blog})
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class BlogForm
        form = BlogForm()
        # merender template form dengan memparsing data form
        return render(request, "grete_blog/form.html", {"form": form})


# Membuat View untuk halaman form ubah Blog
def update_view(request, blog_slug):
    try:
        # mengambil data Blog yang akan diubah berdasarkan Blog id
        # Fungsi GET harus spesifik gini ya
        blog = Blog.objects.get(slug=blog_slug)
    except Blog.DoesNotExist:
        # Jika data blog tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("blog tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == "POST":
        editForm = BlogForm(request.POST, instance=blog)
        if editForm.is_valid():
            # Simpan perubahan data ke dalam table blogs
            editForm.save()
            # mengeset pesan sukses dan redirect ke halaman daftar blog
            messages.success(request, "Sukses Mengubah blog.")
            return redirect("blog:index")
        else:
            # Jika form tidak valid, kembalikan objek form ke template untuk ditampilkan
            return render(request, "grete_blog/form.html", {"form": editForm})
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class BlogForm
        form = BlogForm(instance=blog)
    # merender template form dengan memparsing data form
    return render(request, "grete_blog/form.html", {"form": form})


# Membuat View untuk menghapus data Blog
def delete_view(request, blog_slug):
    try:
        # mengambil data Blog yang akan dihapus berdasarkan Blog id
        deleteBlog = Blog.objects.get(slug=blog_slug)
        # menghapus data dari table blogs
        deleteBlog.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar Blog
        messages.success(request, "Sukses Menghapus Blog.")
        return redirect("blog:index")
    except Blog.DoesNotExist:
        # Jika data Blog tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Blog tidak ditemukan.")


def custom_404(request, exception):
    return render(request, "grete_blog/404.html", status=404)
