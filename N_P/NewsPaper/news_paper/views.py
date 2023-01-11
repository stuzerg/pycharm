# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post, Author


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    #model = Post

    queryset = Post.objects.all().order_by('-creation_date')
    # Поле, которое будет использоваться для сортировки объектов
   # ordering = 'pk'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)


        return context



class PostDetail(DetailView):

    model = Post


    template_name = 'post.html'

    context_object_name = 'post'