from django.shortcuts import render
from .models import Owner, ReposDetail
from .serializers import ReposDetailSerializer
from rest_framework.views import APIView
from .git_apis import get_repos, get_followers
from rest_framework.response import Response
from rest_framework import status
from IPython import embed

# Create your views here.

class ReposList(APIView):

    def get_object(self, username):
        try:
            return ReposDetail.objects.get(user=username)
        except ReposDetail.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        resp = get_repos(username)
        if resp.get('status') and isinstance(resp.get('data'), list):
            serializer = ReposDetailSerializer(data=resp.get('data'))
            if serializer.is_valid():
                serializer.save()
        return Response(resp)

    def put(self, request, username, format=None):
        repos = self.get_object(pk)
        serializer = SnippetSerializer(repos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)