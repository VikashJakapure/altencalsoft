from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from . cms_menu import BooksMenu


class BooksApphook(CMSApp):
    app_name = "book_app"
    name = ("Books Application")
    menus = [BooksMenu, ]

    def get_urls(self, page=None, language=None, **kwargs):
        return ["book.urls"]


apphook_pool.register(BooksApphook)
