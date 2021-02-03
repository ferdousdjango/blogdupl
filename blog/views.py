from django.shortcuts import redirect,render
from blog.models import Post,BlogComment,HomePost
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def bloghome(request):
    allposts= Post.objects.all()
    context = {'allposts':allposts}
    
    return render(request,'blog/bloghome.html',context)
@login_required
def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    
    #comments= BlogComment.objects.filter(post=post,parent=None)
    #replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    #replyDict={}
#
    #for reply in replies:
        #if reply.parent.sno not in replyDict.keys():
            #replyDict[reply.parent.sno]=[reply]
       # else:
            #replyDict[reply.parent.sno].append(reply)

    context={'post':post} #'comments': comments, 'user': request.user, 'replyDict': replyDict#}
    return render(request,'blog/blogpost.html',context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")


def HomePost(request):
    homeposts= HomePost.objects.all()
    context = {'homeposts':homeposts}
    
    return render(request,'blog/bloghome.html',context)
def HomeDetail(request,slug):
    homepost = HomePost.objects.filter(slug=slug).first()
    homepost.views= homepost.views +1
    homepost.save()