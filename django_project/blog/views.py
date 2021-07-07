from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def home(request):
    print([post.author for post in Post.objects.all()])
    context ={
        'posts':Post.objects.all()
    }
    return render(request,'blog/index.html',context=context)

class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date_posted')
    template_name="blog/index.html"
    context_object_name = 'posts'
    # ordering = 

def about(request):
    return render(request,'blog/about.html')

class PostDetailView(DetailView):
    model = Post
    template_name='blog/post_detail.html'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form): # add author before the form is created..
        # form is valid only if ..

        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form): # add author before the form is created..
        # form is valid only if ..

        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    # template_name='blog/post_detail.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False





