from django.shortcuts import render
from datetime import date


# all_posts =[
#  {
#     "slug": "hike-in-the-mountains",
#     "image": "Rara.jpg",
#     "author": "Aasis",
#     "date" :date(2024,8,23),
#     "title": "Rara Lake",
#     "excerpt":"the best place to spend your holidays! this is the heaven",
#     "content":"""Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus rerum quos, rem non tempore fugiat, 
#     repudiandae repellat optio dolores dolore repellendus eligendi? Odio nemo voluptates, earum veritatis sequi et beatae!
    
#     Lorem ipsum dolor sit amet consectetur, 
#     adipisicing elit. Necessitatibus rerum quos, rem non tempore fugiat, 
#     repudiandae repellat optio dolores dolore repellendus eligendi? Odio nemo voluptates, 
#     earum veritatis sequi et beatae!
    
#     Lorem ipsum dolor sit amet consectetur, 
#     adipisicing elit. Necessitatibus rerum quos, rem non tempore fugiat, 
#     repudiandae repellat optio dolores dolore repellendus eligendi? Odio nemo voluptates, 
#     earum veritatis sequi et beatae!
#     """,
    
#   },
#   {
#     "slug": "hike-in-the-mountains",
#     "image": "Rara.jpg",
#     "author": "Aasis",
#     "date" :date(2024,8,23),
#     "title": "Rara Lake",
#     "excerpt":"the best place to spend your holidays! this is the heaven",
#     "content":"""Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus rerum quos, rem non tempore fugiat, 
#     repudiandae repellat optio dolores dolore repellendus eligendi? Odio nemo voluptates, earum veritatis sequi et beatae!
    
#     Lorem ipsum dolor sit amet consectetur, 
#     adipisicing elit. Necessitatibus rerum quos, rem non tempore fugiat, 
#     repudiandae repellat optio dolores dolore repellendus eligendi? Odio nemo voluptates, 
#     earum veritatis sequi et beatae!
    
#     Lorem ipsum dolor sit amet consectetur, 
#     adipisicing elit. Necessitatibus rerum quos, rem non tempore fugiat, 
#     repudiandae repellat optio dolores dolore repellendus eligendi? Odio nemo voluptates, 
#     earum veritatis sequi et beatae!
#     """,
    
#   },
#   {
#     "slug": "hike-in-the-mountains",
#     "image": "Rara.jpg",
#     "author": "Aasis",
#     "date" :date(2024,8,23),
#     "title": "Rara Lake",
#     "excerpt":"the best place to spend your holidays! this is the heaven",
#     "content":"""Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus rerum quos, rem non tempore fugiat, 
#     repudiandae repellat optio dolores dolore repellendus eligendi? Odio nemo voluptates, earum veritatis sequi et beatae!
    
#     Lorem ipsum dolor sit amet consectetur, 
#     adipisicing elit. Necessitatibus rerum quos, rem non tempore fugiat, 
#     repudiandae repellat optio dolores dolore repellendus eligendi? Odio nemo voluptates, 
#     earum veritatis sequi et beatae!
    
#     Lorem ipsum dolor sit amet consectetur, 
#     adipisicing elit. Necessitatibus rerum quos, rem non tempore fugiat, 
#     repudiandae repellat optio dolores dolore repellendus eligendi? Odio nemo voluptates, 
#     earum veritatis sequi et beatae!
#     """,
    
#   }
# ]

# def get_date(post):
#   return post['date']

# Create your views here.

def starting_page(request):
  # sorted_posts = sorted(all_posts,key=get_date) 
  # latest_post = sorted_posts[-3:]
  return render(request,"Blog/index.html")


def posts(request):
  return render(request,"Blog/all-posts.html")

def post_detail(request,slug):
  return render(request, "Blog/post-detail.html")


