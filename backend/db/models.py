from django.db import models
import pycountry

COUNTRY_CHOICES = [(country.name, country.name) for country in pycountry.countries]

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password_hash = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    occupation = models.CharField(max_length=255)
    registration_date = models.DateTimeField()
    def __str__(self):
        return self.username


class Board(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    number_of_nodes = models.IntegerField()
    number_of_connections = models.IntegerField()
    number_of_contributors = models.IntegerField()


class Node(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    wikidata_id = models.CharField(max_length=255)
    wikidata_description = models.TextField()
    wikidata_image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField()


class Connection(models.Model):
    source_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='source_connections')
    target_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='target_connections')
    connection_type = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()


class Tag(models.Model):
    name = models.CharField(max_length=255)


class BoardTag(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Discussion(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField()


class Media(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    media_url = models.CharField(max_length=255)
    media_type = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField()


class Attachment(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_url = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField()


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=255)
    voted_at = models.DateTimeField()


class EditHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    edit_description = models.TextField()
    edited_at = models.DateTimeField()
