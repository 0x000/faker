from __future__ import unicode_literals
from . import BaseProvider


class Provider(BaseProvider):
    formats = ['{{last_name}} {{company_suffix}}', 
               '{{last_name}}, {{last_name}} og {{last_name}}',
               '{{last_name}}-{{last_name}}'
              ]

    company_suffixes = ['Gruppen', 'AS', 'ASA', 'BA', 'RFH', 'og Sønner']

    def company(self):
        """
        :example 'Acme Ltd'
        """
        pattern = self.random_element(self.formats)
        return self.generator.parse(pattern)

    @classmethod
    def company_suffix(cls):
        """
        :example 'Ltd'
        """
        return cls.random_element(cls.company_suffixes)
