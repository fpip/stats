class SimpleTable(object):

    def __init__(self, data=None, headers=None, first_row_headers=False,
                    padding=10):
        self.data = data
        self.headers = headers
        self.padding = padding
        self.col_widths = []
        self.first_row_headers = first_row_headers

    def __str__(self):
        if self.first_row_headers and not self.headers:
            self.headers = self.data.pop(0)

        self.col_widths = self._get_column_widths()
        self.template = self._build_row_template()

        buffer = ""
        if self.headers:
            buffer += self._format_headers()

        return buffer + self._format_table()

    def _format_table(self):
        return ''.join([self.template % row for row in self.data])

    def _build_row_template(self):
        return ''.join(["%%-%ss" % width for width in self.col_widths]) + "\n"

    def _get_column_widths(self):
        maxlen = max([len(row) for row in self.data])
        widths = [0 for _ in range(maxlen)]

        for row in self.data:
            for i, column in enumerate(row):
                header_length = len(self.headers[i])
                column_length = len(str(column))
                widths[i] = max(header_length, column_length) + self.padding

        return widths

    def _format_headers(self):
        table_width = sum(self.col_widths) + len(self.col_widths)
        return self.template % self.headers + '%s\n' % ('-' * table_width)
