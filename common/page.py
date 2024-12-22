class Page:
    def __init__(self, items=None, total: int = 0, currentPage: int = 1, size: int = 10):
        if items is None:
            items = []
        self.items = items
        self.total = total
        self.currentPage = currentPage
        self.size = size
        if total % size == 0:
            self.pages = int(total / size)
        else:
            self.pages = int(total / size) + 1
