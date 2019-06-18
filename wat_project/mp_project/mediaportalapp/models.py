from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.conf import settings
class Category(models.Model):

	name = models.CharField(max_length=60)
	slug = models.SlugField(max_length=200)#cand duci cu mausul pe un link a unei staii, tu vei vedea id-ul statii
	#omul sa stie unde se va duce
	def __str__(self):
		return self.name#in admin noi vom vedea obiectele categoriei ca denumiri
		#adica nu o vom vedea ca object number one , ci Arcade ,etc ..(numele categoriei)
	def get_absolute_url(self):
		return reverse('category-detail', kwargs={'slug':self.slug })

def generate_filename(instance,filename):
	filename = instance.slug + '.jpg'
	return "{}/{}".format(instance.slug, filename)
	
class ArticleManager(models.Manager):
	def all(self, *args, **kwargs):
		return super(ArticleManager,self).get_queryset().filter(pk__in=[1,2])


class Article(models.Model):
	#ce trebuie sa aiba statiaua noastra

	category = models.ForeignKey(Category)#la o singura categorie pot fi multe articule ,
	#dar la un articul nu poate fi mai multe categorii
	title = models.CharField(max_length=160)
	slug = models.SlugField()#vezi mai sus 
	image = models.ImageField(upload_to=generate_filename) #vom adauga o imagine TODO vreaau un trailer de la joc
	content = models.TextField()
	likes = models.PositiveIntegerField(default=0) #laikuri care trebuie sa fiem ai mult decat 0
	dislikes = models.PositiveIntegerField(default=0)
	objects = models.Manager()
	custom_manager = ArticleManager()
	comments = GenericRelation('comments')

	def __str__(self):
		return "Articol '{}' from category '{}'".format(self.title,self.category.name)

	def get_absolute_url(self):
		return reverse('article-detail', kwargs={'category': self.category.slug, 'slug': self.slug })

class Comments(models.Model):

	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	comment = models.TextField()
	timestamp= models.DateTimeField(auto_now_add=True, auto_now=False)# eletrebuie sa fie mereu opuse ,daca unul e true, altul e false
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type','object_id')

class UserAccount(models.Model):

	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	favorite_articles = models.ManyToManyField(Article, blank=True)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('account_view', kwargs={'user': self.user.username })