class WikidataProperty():
    def __init__(self, pid, name=None):
        if not pid.startswith('P'):
            raise ValueError('Properties must begin with a P')
        try:
            int(pid[1:])
        except ValueError:
            raise ValueError('Properties must be of the format P<number>')

        self._pid = pid
        self._name = name

    @property
    def pid(self):
        return self._pid

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'{self._pid} ({self.name})'

    def __repr__(self):
        return self.__str__()

INSTANCE_OF = WikidataProperty('P31', 'instance of')
TITLE = WikidataProperty('P1476', 'title')
PART_OF_THE_SERIES = WikidataProperty('P179', 'part of the series')
ORIGINAL_NETWORK = WikidataProperty('P449', 'original network')
COUNTRY_OF_ORIGIN = WikidataProperty('P495', 'country of origin')
ORIGNAL_LANGUAGE_OF_FILM_OR_TV_SHOW = WikidataProperty('P364', 'original language of film or tv show')
PRODUCTION_COMPANY = WikidataProperty('P272', 'production company')
PUBLICATION_DATE = WikidataProperty('P577', 'publication date')
DIRECTOR = WikidataProperty('P57', 'director')
SEASON = WikidataProperty('P4908', 'season')
NUMBER_OF_EPISODES = WikidataProperty('P1113', 'number of episodes')
HAS_PART = WikidataProperty('P527', 'has part')

FOLLOWS = WikidataProperty('P155', 'follows')
FOLLOWED_BY = WikidataProperty('P156', 'followed by')

TELEVISION_SERIES_EPISODE = 'Q21191270'
TELEVISION_SERIES_SEASON = 'Q3464665'
TELEVISION_SERIES = 'Q5398426'