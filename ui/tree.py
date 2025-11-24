from component.tree_component import TreeComponent

from PySide6.QtWidgets import (QTreeWidget, QTreeWidgetItem, QMainWindow,
                               QVBoxLayout, QWidget, QApplication)
from PySide6.QtCore import Qt


class Tree(QMainWindow, TreeComponent):
    def __init__(self, site):
        super().__init__()
        self.setWindowTitle("Tree View")
        # Set window size. Quearter of screen
        screen = QApplication.primaryScreen().geometry()
        width = screen.width() // 2
        height = screen.height() // 2
        self.resize(width, height)

        # Set column
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(4)
        self.tree_widget.setHeaderLabels(['', 'Link',
                                          'Dork', 'Category'])
        self.tree_widget.setSortingEnabled(True)

        # Set column size
        self.tree_widget.setColumnWidth(0, 45)
        self.tree_widget.setColumnWidth(1, 200)
        self.tree_widget.setColumnWidth(2, 200)
        self.tree_widget.setColumnWidth(3, 150)

        # Set column header to align center
        header = self.tree_widget.header()
        header.setDefaultAlignment(Qt.AlignCenter)
        # Set tootltip for header
        header.setToolTip("Tip: Double click row to open link on browser")

        # Get data
        data = self.get_data(site)

        # Populate row based on data
        for item in data:
            row = QTreeWidgetItem([
                "\n",  # Empty double line for increase row height workaround
                item["link"],
                item["dork"],
                item["category"]
            ])
            # Set checkbox
            row.setCheckState(0, Qt.Unchecked)
            # Set tooltip for each column
            row.setToolTip(0, "You can use this to mark vulnerable link")
            row.setToolTip(1, item["link"])
            row.setToolTip(2, item["dork"])
            row.setToolTip(3, item["category"])
            # Add row
            self.tree_widget.addTopLevelItem(row)

        # Open link on browser if double clicked
        self.tree_widget.itemDoubleClicked.connect(self.open_link)

        # Set link as default sorting
        self.tree_widget.sortByColumn(1, Qt.AscendingOrder)

        # Set layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.tree_widget)
        self.setCentralWidget(central_widget)
