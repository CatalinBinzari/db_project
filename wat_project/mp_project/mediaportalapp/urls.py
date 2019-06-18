from django.conf.urls import url
from mediaportalapp.views import CategoryDetailView, CategoryListView, ArticleDetailView, DynamicArticleImageView, CreateCommentView, DisplayArticlesByCategoryView, UserReactionView, RegistrationView, LoginView, UserAccountView,AddArticleToFavorites

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name ='base_view'),
    url(r'^user_account/(?P<user>[-\w]+)/$', UserAccountView.as_view(), name = 'account_view'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^show_article_image/$',DynamicArticleImageView.as_view(), name='article_image'),
    url(r'^add_comment/$' , CreateCommentView.as_view(), name = 'add_comment'),
    url(r'^display_articles_by_category/$', DisplayArticlesByCategoryView.as_view(), name = 'articles_by_category'),
    url(r'^user_reaction/$', UserReactionView.as_view(), name= 'user_reaction'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^login/$', LoginView.as_view(), name='login_view'),
    url(r'^add_to_favorites/$', AddArticleToFavorites.as_view(), name='add_to_favorites')
] 