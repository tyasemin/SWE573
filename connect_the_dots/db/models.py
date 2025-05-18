from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField 
from django.db.models import JSONField

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, blank=True, null=True)

class Board(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def number_of_nodes(self):
        return self.nodes.count()  

    @property
    def number_of_connections(self):
        return self.connections.count()  

    @property
    def number_of_contributors(self):
        return self.nodes.values('created_by').distinct().count()  
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
    wikidata_selected_properties = JSONField(blank=True, null=True)
    manual_properties = JSONField(blank=True, null=True)
    

class Connection(models.Model):
    from_node = models.ForeignKey(
        Node, on_delete=models.CASCADE, related_name='outgoing_connections'
    )
    to_node = models.ForeignKey(
        Node, on_delete=models.CASCADE, related_name='incoming_connections'
    )
    label = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='connections')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

User = get_user_model()

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.description}"
