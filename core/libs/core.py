from math import ceil


class paging():
    def __init__(self, model, page, page_size, page_per_block):
        self.page_size = page_size or 10
        self.page_per_block = page_per_block or 10

        self.total = model.objects.count()
        self.page_count = ceil(self.total / self.page_size)

        self.page = int(page or 1)

        if self.page < 1:
            self.page = 1
        elif self.page > self.page_count:
            self.page = self.page_count

        page_index = self.page - 1

        self.limit = self.page_size * self.page
        self.offset = self.limit - self.page_size
        self.lists = model.objects.all()[self.offset:self.limit]

        self.now_block = int(page_index / self.page_per_block)
        self.total_block = int((self.page_count - 1) / self.page_per_block)

        self.page_start = int(self.now_block * self.page_per_block) + 1
        self.page_end = self.page_start + self.page_per_block - 1

        if self.page_end > self.page_count:
            self.page_end = self.page_count

        self.page_range = range(self.page_start, self.page_end + 1)

        if self.page > 1:
            self.previous_page = self.page - 1

        if self.page < self.page_count:
            self.next_page = self.page + 1

        if self.now_block > 0:
            self.previous_page_block = self.page_start - 1

        if self.now_block < self.total_block:
            self.next_page_block = self.page_end + 1
