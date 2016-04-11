#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^$', view=views.HomeTemplateView.as_view(), name='home'),

    url(regex=r'^servicios',
        view=views.ServicesTemplateView.as_view(), name='services'),

    url(regex=r'^faq',
        view=views.FAQTemplateView.as_view(), name='faq'),

    url(regex=r'^acerca',
        view=views.AboutTemplateView.as_view(), name='about'),

    url(regex=r'^login', view=views.LoginTemplateView.as_view(), name='login'),

    url(regex=r'^hecho',
        view=views.SuccessTemplateView.as_view(), name='success'),

    url(regex=r'^unete', view=views.JoinEmailView.as_view(), name='join'),

    url(regex=r'^agendar', view=views.DateEmailView.as_view(), name='date'),

    url(regex=r'^quienes-somos',
        view=views.WhoTemplateView.as_view(), name='who'),

    url(regex=r'^enviar-mail',
        view=views.ContactEmailView.as_view(), name='send_contact_mail'),
]