import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer


class UserViewSet(viewsets.ModelViewSet): # 特定のmodelを指定すると、modelのCRUD操作がViewSetのアクションとして暗黙的に実装される
    queryset = User.objects.all() # userテーブルのオブジェクト全権取得
    serializer_class = UserSerializer # 先ほど指定したserializerを指定


class EntryViewSet(viewsets.ModelViewSet): # modelViewSet is to get the complete set of default read and write operations.
    queryset = Entry.objects.all() # Entryテーブルのオブジェクト全権取得
    serializer_class = EntrySerializer # userテーブルのオブジェクト全権取得
    filter_fields = ('author', 'status') # authorとstatusでfilterできるようになる。 ?author=1のようにつければUserのid=1が書いた記事のみがとれる