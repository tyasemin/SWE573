from django.contrib import admin

from django.contrib import admin
from .models import User, Board, Node, Connection, Tag, BoardTag, Discussion, Media, Attachment, Vote, EditHistory

admin.site.register(User)
admin.site.register(Board)
admin.site.register(Node)
admin.site.register(Connection)
admin.site.register(Tag)
admin.site.register(BoardTag)
admin.site.register(Discussion)
admin.site.register(Media)
admin.site.register(Attachment)
admin.site.register(Vote)
admin.site.register(EditHistory)

