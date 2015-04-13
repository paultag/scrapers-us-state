# Copyright (c) Sunlight Foundation, 2014, under the terms of the BSD-3
# license, a copy of which is in the root level LICENSE file.
#   Paul R. Tagliamonte <paultag@sunlightfoundation.com>

from pupa.scrape import Jurisdiction, Post, Organization
from .contributions import MichiganRegistrationScraper


class Michigan(Jurisdiction):
    division_id = 'ocd-division/country:us/state:ak'
    classification = 'government'
    name = "Michigan State Government"
    url = 'http://www.michigan.gov/'

    scrapers = {
        "registrations": MichiganRegistrationScraper,
    }

    def get_organizations(self):
        org = Organization(name='Michigan Executive Branch',
                           classification='executive')
        yield org
