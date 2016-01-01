from os import path
from suite_parser_vars import get_resource_path
import copy


def get_variables():
    root_dir = path.dirname(path.abspath(__file__))
    resource_dir = get_resource_path(root_dir)
    var = {}
    var['SCREENSHOT_KW'] = get_screenshot()
    var['MYLIBRARY_KW'] = get_mylibrary(resource_dir)
    var['OTHERMYLIBRARY_KW'] = get_othermylibrary(resource_dir)
    var['MYLIBRARY_XML'] = get_mylibrary_xml(var['MYLIBRARY_KW'])
    var['SELENIUM2LIBRARY_KEYS_LIST'] = ['keywords', 'library_module']
    var['ADDCOOKIE_KEYS_LILST'] = ['keyword_name',
                                   'keyword_arguments',
                                   'documentation',
                                   'tags']
    return var


def get_mylibrary(resource_dir):
    data = {}
    data['library_module'] = 'MyLibrary'
    data['file_path'] = path.normpath(path.join(
        resource_dir,
        '..',
        'library',
        'MyLibrary.py'))
    data['file_name'] = path.basename(data['file_path'])
    kws = {}
    kw = {}
    kw['keyword_name'] = 'Keyword 2'
    kw['keyword_arguments'] = ['arg2', 'arg3']
    kw['documentation'] = 'kw 2 doc'
    kw['tags'] = []
    kws['keyword2'] = kw
    kw = {}
    kw['keyword_name'] = 'Keyword 1'
    kw['keyword_arguments'] = ['arg1']
    kw['documentation'] = 'kw 1 doc'
    kw['tags'] = ['tag1', 'tag2']
    kws['keyword1'] = kw
    data['keywords'] = kws
    return data


def get_othermylibrary(resource_dir):
    data = get_mylibrary(resource_dir)
    data['library_module'] = 'OtherMyLibrary'
    data['file_path'] = path.normpath(path.join(
        resource_dir,
        '..',
        'library',
        'OtherMyLibrary.py'))
    data['file_name'] = path.basename(data['file_path'])
    return data


def get_mylibrary_xml(data):
    n_data = copy.copy(data)
    n_data['file_path'] = data['file_path'].replace('.py', '.xml')
    n_data['file_name'] = data['file_name'].replace('.py', '.xml')
    return n_data


def get_screenshot():
    data = {}
    data['library_module'] = 'Screenshot'
    data['keywords'] = screenshot_keywords()
    return data


def screenshot_keywords():
    kws = {}
    kw = {}
    kw['keyword_name'] = 'Set Screenshot Directory'
    kw['tags'] = []
    kw['documentation'] = 'Sets the directory where screenshots are saved.'
    kw['keyword_arguments'] = ['path']
    kws[kw['keyword_name'].lower().replace(' ', '')] = kw
    kw = {}
    kw['keyword_name'] = 'Take Screenshot'
    kw['tags'] = []
    kw['documentation'] = \
        'Takes a screenshot in JPEG format and embeds it into the log file.'
    kw['keyword_arguments'] = ['name=screenshot', 'width=800px']
    kws[kw['keyword_name'].lower().replace(' ', '')] = kw
    kw = {}
    kw['keyword_name'] = 'Take Screenshot Without Embedding'
    kw['tags'] = []
    kw['documentation'] = 'Takes a screenshot and links it from the log file.'
    kw['keyword_arguments'] = ['name=screenshot']
    kws[kw['keyword_name'].lower().replace(' ', '')] = kw
    return kws
