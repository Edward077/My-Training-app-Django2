from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# create a post disctionary to be fetch  by the htmel
posts = [
    {
    "ID": 0,
    "Title": 'Let explore python in details ',
    "Content": 'Python is intepreted, High level, general purpose programming languag'
    'widly uses in the field of web development, data science and machine learning'

    },

    {
    "ID": 1,
    "Title": 'Let explore java in details ',
    "Content": 'Java is a static language, High level, general purpose programming languag'
    'widly uses in the field of web development, data science and machine learning'
    },

    {
     "ID": 2,
    "Title": 'Let explore react in details ',
    "Content": 'React is intepreted, High level, general purpose programming languag'
    'widly uses in the field of web development, data science and machine learning'

    },
]
# posts=[] # when the post is empty
# def helloword(request):
# def home(request, name):

def home(request): 

# Implementing the reverse function 
    # print(reverse('home', args=['edt'])),
    html = ""
    for post in posts:
        html += f'''
            <div>
            <a href ="/post/{post['ID']}/">
                <h1>{post['ID']}-{post['Title']}</h1></a>
                <p>{post['Content']}</p>
            </div>
'''
    # return HttpResponse(html)
    return render(request,'sub/home.html',{'posts': posts, 'username': 'edward'})
    # return render(request,'sub/home.html', {"name": "Edward", 'list': ['carrot']})

def post(request, ID):
    # To implement the HttpNotFound Found
    valid_id = False

    # print(type(id)) # print the datatypeID
    for post in posts:
        if post['ID'] == ID:
            post_dict =post
            valid_id = True
            break
    if valid_id:
    #     html = f'''
    #             <h1>{post_dict['Title']}</h1>
    #             <p>{post_dict['Content']}</p>
    # '''
        return render(request, "sub/post.html", {'post_dict':post})
        # return HttpResponse(f" {ID} ")
        # return HttpResponse(html)
    else:
        return HttpResponseNotFound("Wrong Post")
    
    # Implementing the RedirectResponse
def google(request, id):
        url = reverse("post", args=[id])
        # return HttpResponseRedirect('https://www.google.com')

        # return HttpResponseRedirect(f'/post/{id}')
        return HttpResponseRedirect(url)

def global_temp(request):
     return render(request, 'global.html')