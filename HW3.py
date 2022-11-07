class Url:

    def __init__(self, scheme='', authority='', path='', query='', fragment=''):
        self.scheme: str = scheme
        self.authority: str = authority
        self.path: list or str = path if type(path) is str else ('/'+'/'.join(path))  # check given arg and rewrite if it not default and if it list
        self.query = Url.fquery(query)  # check given arg and rewrite if it not default and if it dict
        self.fragment = fragment

    def __str__(self) -> str:
        answer = f'{self.scheme}://{self.authority}{self.path}{self.query}{self.fragment}'
        return answer

    def __eq__(self, arg) -> bool:
        return str(self) == str(arg)

    @staticmethod
    def fquery(query: str | dict) -> str:
        list_query = [i + '=' + k + '&' for i, k in query.items()] if type(query) is dict \
            else '' if query == '' else f'?q={query}'
        answer = ('?' + ''.join(list_query)[0:-1]) if type(list_query) is list else list_query
        return answer


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
    attr_list = []

    def __init__(self, scheme='', authority='', path='', query='', fragment=''):
        super().__init__(scheme, authority, path, query, fragment)

    def __call__(self, *args: str, **kwargs: dict):
        if args:
            UrlCreator.attr_list.clear()
            for i in args:
                UrlCreator.attr_list.append(i)
                self.path = '/' + '/'.join(self.attr_list)
        if kwargs:
            list_query = [i + '=' + k + '&' for i, k in kwargs.items()]
            self.query = f"?{''.join(list_query)[0:-1]}"
        return self

    def _create(self) -> str:
        return self.__str__()

    def __getattr__(self, attr):
        self.attr_list.append(attr)
        self.path = '/' + '/'.join(self.attr_list)
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
assert url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create() == \
       'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default'


print(url_creator.scheme)
print(url_creator.authority)
print(url_creator.path)
print(url_creator.query)
