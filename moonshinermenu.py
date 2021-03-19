class MoonshineMenuItem(object):
    def __init__(self, title, parent=None):
        self.parent = parent
        self.title = title
        self.items = None

    def add_submenu(self, menu_item):
        if not self.items:
            self.items = list()
        self.items.append(menu_item)
        menu_item.parent = self


class MoonshinerMenu(object):
    def __init__(self, root_menu_item):
        self.root_item = root_menu_item
        self.active_item = root_menu_item
        self.selected_item = None

    @property
    def selected_item_id(self):
        if self.selected_item and self.selected_item.parent:
            return self.selected_item.parent.items.index(self.selected_item)
        else:
            return None

    @selected_item_id.setter
    def selected_item_id(self, value):
        if self.selected_item and self.selected_item.parent:
            self.selected_item = self.selected_item.parent.items[value]

    def enter_key_pressed(self):
        if self.selected_item:
            self.root_item = self.selected_item
            self.selected_item = None

    def up_key_pressed(self):
        if self.selected_item_id is not None and self.selected_item_id > 0:
            self.selected_item_id = self.selected_item_id - 1

    def down_key_pressed(self):
        if self.selected_item_id is not None and ((self.selected_item_id+1) < self.selected_item.parent.items.length()):
            self.selected_item_id = self.selected_item_id + 1

    def cancel_key_pressed(self):
        if self.selected_item and self.selected_item.parent:
            self.selected_item = self.selected_item.parent
