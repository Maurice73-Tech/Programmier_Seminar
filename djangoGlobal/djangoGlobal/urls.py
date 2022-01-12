from django.contrib import admin
from django.urls import path
from app_1.views import (registrieren, benutzer_logout, benutzer_login, profile, impressum,authentifizieren_view,add_block_view,LikesPostView,UpdateBlogView, DislikePostView,LikeKommentar,DislikeKommentar,LikeUnterkommentare,DislikeUnterkommentare,ForumView, BlogDetailView, AddKommentarView,AddUnterkommentarView,profile_edit, Passwords_View)
from app_1.models import Post,Kommentar,UnterKommentar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',benutzer_login,name='startseite'),
    path('impressum/', impressum,name='impressum'),
    path('forum/', ForumView.as_view (model=Post),name='forum'),
    path('blog-details/<int:pk>', BlogDetailView.as_view (model=Post),name='blog-details'),
    path('blog-details/update/<int:pk>', UpdateBlogView.as_view (model=Post),name='update-blog'),
    path('addpost/', add_block_view ,name='addpost'),
    path('admin/', admin.site.urls),
    path('login/', benutzer_login, name='login'),
    path('logout/', benutzer_logout,name='logout'),
    path('registrieren/', registrieren ,name='registrieren'),
    path('authentifizieren/', authentifizieren_view ,name='authentifizieren'),
    path('profile/', profile ,name='profile'),
    path('profile_edit/', profile_edit.as_view() ,name='profile_edit'),
    path('password/', Passwords_View.as_view(template_name='password_edit.html')),
    path('likes/<int:pk>', LikesPostView, name='like_post'),
    path('blog-details/<int:pk>/kommentieren', AddKommentarView.as_view(model=Post), name='addcomment'),
    path('dislike/<int:pk>', DislikePostView, name='dislike_post'),
    path('Klikes/<int:pkPost>/<int:pkKommentar>', LikeKommentar, name='kommentar_likes'),
    path('Kdislikes/<int:pkPost>/<int:pkKommentar>',DislikeKommentar,name='kommentar_dislikes'),
    path('uklikes/<int:pkPost>/<int:pkUnterkommentar>',LikeUnterkommentare, name='unterkommentar_likes'),
    path('ukdislikes/<int:pkPost>/<int:pkUnterkommentar>',DislikeUnterkommentare, name='unterkommentare_dislikes'),
    path('blog-details/<int:post>/<int:kommentar>/unterkommentar', AddUnterkommentarView.as_view(model=Kommentar), name ='addsubcomment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)