# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'email': 'geeklab@spb.ru',
                'address': 'территория Петропавловская крепость, 3Ж',
            },             {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@kz.ru',
                'address': 'территория Кремль, 11, Казань, Республика Татарстан, Россия',
            },             {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email': 'geeklab@msk.ru',
                'address': 'Красная площадь, 7, Москва, Россия',
            },
        ]
        return context_data


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
                'title': 'Новость раз',
                'preview': 'Превью к новости раз',
                'date': '2022-01-01'
            },  {
                'title': 'Новость два',
                'preview': 'Превью к новости два',
                'date': '2022-01-02'
            },  {
                'title': 'Новость три',
                'preview': 'Превью к новости три',
                'date': '2022-01-03'
            },  {
                'title': 'Новость четыре',
                'preview': 'Превью к новости четыре',
                'date': '2022-01-04'
            },  {
                'title': 'Новость пять',
                'preview': 'Превью к новости пять',
                'date': '2022-01-05'
            }
        ]
        return context_data
