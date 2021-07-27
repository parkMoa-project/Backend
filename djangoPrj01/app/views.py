from django.utils.functional import partition
from parkmoa.settings import ALLOWED_HOSTS
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

class SearchView(APIView):
    #  default: 세션기반, http basic기반 인증 제거 => auth 없이 접근 가능
    authentication_classes = []

    def get(self, request):
        es = Elasticsearch([{
            'cloud_id': 'team-parkMoa:YXAtbm9ydGhlYXN0LTIuYXdzLmVsYXN0aWMtY2xvdWQuY29tOjkyNDMkNjc2ODhhNjFmOTZiNDNjNTlkZWFiNDUwMzUwMmQ2YTckZGM4Y2EyMTg4N2FlNDM1Nzg2OTkxMTI2YmZmNzJmZTY=',
            'http_auth': 'elastic:IaPpgyeCkU38iytPPHn4jQny',
        }])

        # 검색어
        search_word = request.query_params.get('search')
       
        # 검색어 없을시 전체 검색
        if not search_word:
            docs = es.search(index='parkmoa', body={"size":2000})
            data_list = docs['hits'] #json 타입 반환

            return Response(data_list)


        docs = es.search(index='parkmoa',
                         body={
                             "query": {
                                 "multi_match": {
                                     "query": search_word,
                                    #  "fields": ["공원명"]
                                 }
                             }
                         })

        data_list = docs['hits']

        return Response(data_list)
