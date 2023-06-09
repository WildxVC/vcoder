from django.shortcuts import render,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.
def blogHome(request):
    allpost = Post.objects.order_by("-timestamp")
    context={'allpost': allpost}
    return render(request,"blog/blogHome.html",context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict:
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)            

    context={'post': post,'comments':comments,'replyDict':replyDict}
    return render(request,"blog/blogPost.html",context)

def postComment(request):
    if request.method=='POST':
        comment=request.POST['comment']
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno) 
        parentSno=request.POST.get("parentSno")
        if parentSno == "":    
            comment=BlogComment(user=user,comment=comment,post=post)
            comment.save()
            messages.success(request,"Your comment has been successfully posted!")
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(user=user,comment=comment,post=post,parent=parent)    
            comment.save()
            messages.success(request,"Your reply has been successfully posted!")

    return redirect(f"/blog/{post.slug}")
