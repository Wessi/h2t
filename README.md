# [h2t](http://www.github.com/wessi/ExtractTextsFromHtml/)

H2T is a Python script to convert a page of HTML into clean text file and extract all the sentences within paragraph from HTML file.

Usage: `h2t.py [(filename|url) [encoding]]`

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      --ignore-links        don't include any formatting for links
      --ignore-images       don't include any formatting for images
      -g, --google-doc      convert an html-exported Google Document
      -d, --dash-unordered-list
                            use a dash rather than a star for unordered list items
      -b BODY_WIDTH, --body-width=BODY_WIDTH
                            number of characters per output line, 0 for no wrap
      -i LIST_INDENT, --google-list-indent=LIST_INDENT
                            number of pixels Google indents nested lists
      -s, --hide-strikethrough
                            hide strike-through text. only relevent when -g is
                            specified as well

Or you can use it from within Python:

    import h2t
    print h2t.h2t("<p>Hello, world.</p>")

Or with some configuration options:

    import h2t
    h = h2t.HTML2Text()
    h.ignore_links = True
    print h.handle("<p>Hello, <a href='http://earth.google.com/'>world</a>!")

