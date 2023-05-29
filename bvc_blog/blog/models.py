from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    comments_enabled = models.BooleanField()

class BlogPostCategory(models.Model):
    name = models.CharField(max_length=255)

class BlogPostTag(models.Model):
    name = models.CharField(max_length=255)

class BlogPostLike(models.Model):
    blog_post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)

class BlogPostFavorite(models.Model):
    blog_post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

class Comment(models.Model):
    blog_post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    content = models.TextField()

class CommentLike(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)

class Inquiry(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    reason_for_contact = models.CharField(max_length=255)
    message_subject = models.CharField(max_length=255)
    message = models.TextField()
    opened = models.BooleanField()

class SocialMediaPlatform(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    description = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.PasswordField(max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_description = models.TextField()
    profile_image = models.CharField(max_length=255)

class UserSocialMedia(models.Model):
    platform_id = models.ForeignKey(SocialMediaPlatform, on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    url = models.TextField()