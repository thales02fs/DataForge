from view.layout import Layout
from view.components.header import Header
from view.components.file_upload import FileUpload
from view.components.processing import Processing
from view.components.database_export import DatabaseExport

import tkinter as tk

class Window:
    def __init__(self, root):
        self.root = root
        self.configure_window()
        self.create_layout()

    def configure_window(self):
        """Configura a janela principal."""

        self.root.title("DataForge")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - Layout.WINDOW_WIDTH) // 2
        y = (screen_height - Layout.WINDOW_HEIGHT) // 2

        self.root.geometry(f"{Layout.WINDOW_WIDTH}x{Layout.WINDOW_HEIGHT}+{x}+{y}")
        self.root.minsize(Layout.MIN_WIDTH, Layout.MIN_HEIGHT)
        self.root.configure(bg=Layout.BACKGROUND)

    def create_layout(self):
        """Organiza as regiões principais da aplicação."""

        # Área principal
        self.content_area = tk.Frame(self.root,bg=Layout.BACKGROUND)
        self.content_area.pack(fill="both", expand=True)

        # Header
        Header(self.content_area)

        # FileUpload
        FileUpload(self.content_area)

        # DataProcessing
        Processing(self.content_area)

        # DatabaseExport
        DatabaseExport(self.content_area)