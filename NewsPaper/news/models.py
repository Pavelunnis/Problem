from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
#from django.db.models.functions import Coalesce если None коментов или постов


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.IntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get("postRating")

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get("commentRating")
        self.ratingAuthor = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=64)
    def __str__(self):
        return self.category


class Post(models.Model):
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    news = 'NW'
    article = "AC"

    NamePost = [
        (news, 'новость'),
        (article, 'статья')
    ]
    namePost = models.CharField(max_length=2, choices=NamePost, default='NW')
    timeCreate = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through="PostCategory")
    heading = models.CharField(max_length=128)
    textPost = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.textpost[0:123] + "..."

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )