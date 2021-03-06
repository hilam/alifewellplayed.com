from __future__ import absolute_import
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django import template

from coreExtend.models import Account
from replica.pulse.models import Entry, Media, Channel, Topic, Draft, MenuPosition, MenuItem

register = template.Library()

@register.inclusion_tag('replica/pulse/templatetags/render_latest_entries.html', takes_context=True)
def render_latest_entries(context, channel_type=None, num=25):
    request = context['request']
    u = request.user
    if u.is_staff:
        entries = Entry.objects.posts()
    else:
        entries = Entry.objects.published()
    if channel_type:
        objects = entries.filter(channel__slug=channel_type)[:num]
    else:
        objects = entries[:num]
    return { 'objects': objects }

@register.inclusion_tag('replica/pulse/templatetags/month_links_snippet.html', takes_context=True)
def render_month_links(context, channel_type=None,):
    request = context['request']
    u = request.user
    if u.is_staff:
        entries = Entry.objects.posts()
    else:
        entries = Entry.objects.published()
    if channel_type:
        dates = entries.filter(channel__slug=channel_type).dates('pub_date', 'month')
    else:
        dates = entries.dates('pub_date', 'month')
    return { 'dates': dates, }

@register.inclusion_tag('replica/pulse/templatetags/render_menu.html', takes_context=True)
def render_menu(context, menu_name=None, num=25):
    request = context['request']
    if menu_name:
        menu = MenuPosition.objects.get(slug=menu_name)
        menu_items = MenuItem.objects.filter(position=menu).order_by('weight')[:num]
    else:
        menu = ''
        menu_items = MenuItem.objects.all()[:num]
    return { 'menu': menu, 'objects': menu_items, 'request':request }
