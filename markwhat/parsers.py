from docutils.core import publish_parts
from markdown import markdown
from textile import textile


def parse_textile(text):
    """
    :type text: basestring

    :rtype: basestring
    """
    return textile(text=text, encoding='utf-8', output='utf-8')


def parse_markdown(text, args=''):
    """
    :type text: basestring
    :type args: basestring

    :rtype: basestring
    """
    extensions = [e for e in args.split(',') if e]
    if len(extensions) > 0 and extensions[0] == "safe":
        extensions = extensions[1:]
        safe_mode = True
    else:
        safe_mode = False

    extensions.extend([
        'extra',
        'admonition',
        'codehilite',
        'headerid',
        'meta',
        'nl2br',
        'sane_lists',
        'smarty',
        'toc',
        'wikilinks',
        'tables',
    ])

    return markdown(
        text,
        extensions,
        safe_mode=safe_mode,
        enable_attributes=(not safe_mode)
    )


def parse_restructuredtext(text):
    """
    :type text: basestring

    :rtype: basestring
    """
    parts = publish_parts(
        source=text,
        writer_name="html4css1",
    )

    return parts["fragment"]
