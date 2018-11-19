from nntplib import NNTP
with NNTP('news.gmane.org') as n:
     n.group('gmane.comp.python.committers')
