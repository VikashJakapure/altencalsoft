from cms.menu_bases import CMSAttachMenu
from django.urls import reverse
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from .models import Book


class BooksMenu(CMSAttachMenu):
    name = ("Books Menu")

    def get_nodes(self, request):
        nodes = []
        for book in Book.objects.all():
            node = NavigationNode(
                title=book.name,
                url=reverse('polls:detail', args=(book.pk,)),
                id=book.pk,
            )
            nodes.append(node)
        return nodes


menu_pool.register_menu(BooksMenu)
