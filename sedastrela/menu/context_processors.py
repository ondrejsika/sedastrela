from sedastrela.menu.models import Menu


def menus(request):
    menus = {}

    for menu in Menu.objects.all():
        menus[menu.uid] = menu

    return {
        'menus': menus,
    }
