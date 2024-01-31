# app/testPosts.py

from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My Title", description="Blurb", wiki="Post Body")
        post.save()
        assert post.title == "My Title"
        assert post.description == "Blurb"
        assert post.wiki == "Post Body"
