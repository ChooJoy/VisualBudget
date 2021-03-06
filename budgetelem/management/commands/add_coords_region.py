# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from budgetelem.models import Region
import urllib
from xml.etree import ElementTree as ET

import re, urlparse

def iriToUri(iri):
    parts= urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )

def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)



class Command(BaseCommand):

    def handle(self, *args, **options):
    
        docs = Region.objects.all()
        print len(docs)
        count = 1
        for elem in docs:
            print str(count)+'.', elem.capital
            count += 1

            url_utf = 'https://maps.googleapis.com/maps/api/geocode/xml?address='+ u'город ' + elem.capital +'&sensor=false&language=ru'
            
            feed = urllib.urlopen(iriToUri(url_utf))
            tree = ET.parse(feed)
            root = tree.getroot()

            result = root.find('result')
            geometry = result.find('geometry')
            location = geometry.find('location')
            lat = location.find('lat').text
            lng = location.find('lng').text

            elem.capital_coords_lat = lat
            elem.capital_coords_lng = lng
            elem.save()










