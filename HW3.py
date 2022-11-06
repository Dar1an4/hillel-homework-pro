class Url:

    def __init__(self, scheme='', authority='', path='', query='', fragment=''):
        self.scheme: str = scheme
        self.authority: str = authority
        self.path: list or str = path if type(path) is str else ('/'+'/'.join(path))
        self.query = Url.fquery(query)
        self.fragment = fragment

    def __str__(self):
        answer = f'{self.scheme}://{self.authority}{self.path}{self.query}{self.fragment}'
        return answer

    def __eq__(self, arg):
        if str(self) == str(arg):
            return True
        else:
            return False

    @staticmethod
    def fquery(query):
        list_query = []
        if type(query) is str and query != '':
            return f'?q={query}'
        elif type(query) is dict:
            for i, k in query.items():
                list_query.append(i)
                list_query.append('=')
                list_query.append(k)
                list_query.append('&')
            return f"?{''.join(list_query)[0:-1]}"
        return ''


class HttpsUrl(Url):

    def __init__(self, scheme='https', authority='', path='', query='', fragment=''):
        super().__init__(scheme, authority, path, query, fragment)


class HttpUrl(Url):

    def __init__(self, scheme='http', authority='', path='', query='', fragment=''):
        super().__init__(scheme, authority, path, query, fragment)


class GoogleUrl(HttpsUrl):

    def __init__(self, scheme='https', authority='google.com', path='', query='', fragment=''):
        super().__init__(scheme, authority, path, query, fragment)


class WikiUrl(HttpsUrl):

    def __init__(self, scheme='https', authority='wikipedia.org', path='', query='', fragment=''):
        super().__init__(scheme, authority, path, query, fragment)


class UrlCreator(Url):
    get_attr_list = []
    callable_list = []

    def __init__(self, scheme='', authority='', path='', query='', fragment=''):
        super().__init__(scheme, authority, path, query, fragment)

    def __call__(self, *args, **kwargs):
        if args:
            UrlCreator.callable_list.clear()
            for i in args:
                UrlCreator.callable_list.append(i)
                self.path = '/' + '/'.join(self.callable_list)
        if kwargs:
            list_query = []
            for i, k in kwargs.items():
                list_query.append(i)
                list_query.append('=')
                list_query.append(k)
                list_query.append('&')
            self.query = f"?{''.join(list_query)[0:-1]}"
        return self

    def _create(self):
        return self.__str__()

    def __getattr__(self, attr):
        self.callable_list.append(attr)
        self.path = '/' + '/'.join(self.callable_list)
        return self


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'

url_creator = UrlCreator(scheme='https', authority='docs.python.org')
assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
assert url_creator('api', 'v1', 'list') == 'https://docs.python.org/api/v1/list'
assert url_creator('api', 'v1', 'list', q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'
assert url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create() == 'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default'



