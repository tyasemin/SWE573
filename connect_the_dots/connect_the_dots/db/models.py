from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, blank=True, null=True)

class Board(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_nodes = models.IntegerField(null=True, blank=True)
    number_of_connections = models.IntegerField(null=True, blank=True)
    number_of_contributors = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.title} - {self.owner.username}"

class Node(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='nodes')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    wikidata_id = models.CharField(max_length=255,blank=True)
    wikidata_description = models.TextField(blank=True)
    wikidata_image_url = models.CharField(max_length=255,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=255,blank=True)

class Connection(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='connections')
    from_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='outgoing')
    to_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='incoming')
    label = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
