def ajax(url, **user_settings):
    settings = {
        'method': user_settings.get('method', 'Get'),
        'contents': user_settings.get('contents', ''),
        'datatype': user_settings.get('datatype', 'text/plain')
    }
    print('請求{}'.format(url))
    print('設定{}'.format(settings))

my_settings = {'method': 'POST', 'contents': 'book=python'}
ajax('http://openhome.cc', **my_settings)