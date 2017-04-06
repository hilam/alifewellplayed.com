from __future__ import absolute_import
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django import template

from coreExtend.models import Account
from replica.pulse.models import Entry, Media, Channel, Topic, Draft, MenuPosition, MenuItem

register = template.Library()

@register.inclusion_tag('replica/pulse/templatetags/render_latest_entries.html')
def render_latest_entries(channel_type=None, num=25):
    if channel_type:
        objects = Entry.objects.published().filter(channel__slug=channel_type)[:num]
    else:
        objects = Entry.objects.published()[:num]
    return { 'objects': objects }

@register.inclusion_tag('replica/pulse/templatetags/month_links_snippet.html')
def render_month_links(channel_type=None,):
    if channel_type:
        dates = Entry.objects.published().filter(channel__slug=channel_type).dates('pub_date', 'month')
    else:
        dates = Entry.objects.published().dates('pub_date', 'month')
    return { 'dates': dates, }

@register.inclusion_tag('replica/pulse/templatetags/render_menu.html')
def render_menu(menu_name=None, num=25):
    if menu_name:
        menu = MenuPosition.objects.get(slug=menu_name)
        menu_items = MenuItem.objects.filter(position=menu)[:num]
    else:
        menu = ''
        menu_items = MenuItem.objects.all()[:num]
    return { 'menu': menu, 'objects': menu_items }