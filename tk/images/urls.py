from django.conf.urls import url
from . import views

urlpatterns = [
    # url(
    #     regex=r'^all/$',
    #     view=views.ListAllImages.as_view(),
    #     name='all_images',
    # ),
    # url(
    #     regex=r'^comments/$',
    #     view=views.ListAllComments.as_view(),
    #     name='all_images',
    # ),
    # url(
    #     regex=r'^likes/$',
    #     view=views.ListAllLikes.as_view(),
    #     name='all_images',
    # )
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/like/$',
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/unlike/$',
        view=views.UnLikeImage.as_view(),
        name='like_image'
    ),
    url(
        # regex=r'comments/(?P<comment_id>[0-9]+)/$',
        regex=r'^(?P<image_id>[0-9]+)/comments/$',
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    ),
    url(
        regex=r'comments/(?P<comment_id>[0-9]+)/$',
        view=views.Comment.as_view(),
        name='comment'
    )
]
