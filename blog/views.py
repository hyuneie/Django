# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Photo
from .forms import CommentForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TestDataSerializer
from django.contrib.auth.decorators import login_required

class PostList(generic.ListView):
    model = Post
    paginate_by = 1
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def sport(request):
    return render(request, 'sport.html', {'member_reg': "ok"})

def minwon(request):
    return render(request, 'complaint.html', {'member_reg': "ok"})

def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.user = request.user
        post.save()
        # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다
        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = post
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
        return redirect('/post_detail/' + str(post.id))
    else:
        return render(request, 'index.html')

@api_view(['GET'])
def getTestDatas(request):
    datas = Post.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)
