"""
Creates the default Site object.
"""

from django.db.models import signals
from django.contrib.sites.models import Site
from django.contrib.sites import models as site_app
from django.conf import settings
from urlparse import urlparse

def create_default_site(app, created_models, verbosity, db, **kwargs):
    if Site in created_models:
        host = urlparse(settings.CURRENT_URL)[1]
        if verbosity >= 2:
            print "Creating %s Site object" % host
        s = Site(domain=host, name=host)
        s.save(using=db)
    Site.objects.clear_cache()

signals.post_syncdb.connect(create_default_site, sender=site_app)
