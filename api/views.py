from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, _get_displayed_page_numbers, _get_page_links
from rest_framework.utils.urls import remove_query_param, replace_query_param


from api.serializers import MessageSerializer
from api.models import Message
from collections import namedtuple

#Added custom pagination class for url style /api/messages/list/1
class ListPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    
    #Need to override this function to read page number from url
    def get_page_number(self, request, paginator):
        page_number = int(request.path.split('/')[-1], 10)
        page_number = page_number if page_number > 0 else 1
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number
    
    #Service function to make url style /api/messages/list/1
    def build_url(self, page_number=1):
        url = self.request.build_absolute_uri()
        new_url = url.split('/')
        new_url[-1] = '1' if page_number == 1 else str(page_number)
        return '/'.join(new_url)

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        
        return self.build_url(page_number)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()

        return self.build_url(page_number)

    #Need to override this function for returning appropriate links for web browser pagination
    def get_html_context(self):

        def page_number_to_url(page_number):
            return self.build_url(page_number)   

        current = self.page.number
        final = self.page.paginator.num_pages
        page_numbers = _get_displayed_page_numbers(current, final)
        page_links = _get_page_links(page_numbers, current, page_number_to_url)

        return {
            'previous_url': self.get_previous_link(),
            'next_url': self.get_next_link(),
            'page_links': page_links
        }


# Create your views here.

class MessageList(generics.ListAPIView):
    queryset = Message.objects.all().order_by('-create_date')
    serializer_class = MessageSerializer
    pagination_class = ListPagination


class MessageDetail(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


#All request validation done in MessageSerializator class, also default validators will be proceed in the first place
class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageSerializer
