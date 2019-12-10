from django.shortcuts import render, get_object_or_404, redirect, get_object_or_404, resolve_url
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.views.generic import (
    ListView, DetailView, FormView
    ArchiveIndexView, YearArchiveView, MonthArchiveView,
    WeekArchiveView,DayArchiveView, TodayArchiveView,DateDetailView,
    CreateView, UpdateView, DeleteView,

)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import PostForm


from django.http import Http404, HttpResponse


class PostListView(ListView):
    model = Post

    def head(self, *args, **kwargs):
        try:
            post = self.get_queryset().latest('id')
        except Post.DoesNotExist:
            raise Http404



        time = post.updated_at.strftime('%a, %d %b %Y %H:%M:%S GMT')
        response = HttpResponse()
        response['Last-Modified'] = time
        return response





post_list = PostListView.as_view()


def greeting_view(message):
    def view_fn(request):
        return HttpResponse(message)
    return view_fn

greeting = greeting_view('Good Day')
morning_greeting = greeting_view('Morning to ya')
evening_greeting = greeting_view('Evenign to ya')

from django.views import View


@method_decorator(login_required, name='dispatch')
class EditFormView(View):
    model = None
form_class =None
    success_url = None
    template_name = None

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.model, id=pk)

    def get_success_url(self):
        return self.success_url  # 없다면 클래스 변수를 가져옴

    def get_template_name(self):
        return self.template_name  # 없다면 클래스 변수를 가져옴

    def get_form(self):
        form_kwargs = {
            'instance': self.get_object(),
        }
        if self.request.method == 'POST':
            form_kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
            return self.form_class(**form_kwargs)


    def get_context_data(self, **kwargs):  # 폼에넘길 인자들 사전현태로 만들기
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return kwargs


    def get(self, *args, **kwargs):  # get요청일때 실행되는 함수
        return render(self.request, self.get_template_name(), self.get_context_data())


    def post(self, *args, **kwargs):  # post요청일떄 실행되는 함수
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        return render(self.request, self.get_template_name(), self.get_context_data(form=form))




post_edit = EditFormView.as_view(
     model=Post,
     form_class=PostForm,
     success_url='/',
     template_name='blog/post_form.html')


index = ListView.as_view(model=Post, allow_empty=True, paginate_by=1)
'''
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'object':post,
        'post': post,
    })
'''
class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dummy'] = 'Django'
        return context


post_detail = PostDetailView.as_view(model=Post)

post_archive = ArchiveIndexView.as_view(model=Post, date_field='updated_at')

class PostYearArchiveView(YearArchiveView):
    model = Post
    date_field = 'updated_at'

class PostMonthArchiveView(MonthArchiveView):
    model = Post
    date_field = 'updated_at'
    month_format = '%m'

class PostWeekArchiveView(WeekArchiveView):
    model = Post
    date_field = 'updated_at'

class PostDayArchiveView(DayArchiveView):
    model = Post
    date_field = 'updated_at'
    month_format = '%m'

class PostTodayArchiveView(TodayArchiveView):
    model = Post
    date_field = 'updated_at'

class PostDateDetailView(DateDetailView):
    model = Post
    date_field = 'created_at'
    month_format = '%m'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = reverse_lazy('blog:post_index') 경로 변경 불가 detail로 이동하고싶다

    def get_success_url(self):
        return resolve_url('blog:post_detail', self.object.id)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_index')