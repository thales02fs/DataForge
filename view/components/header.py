from view.layout import Layout

import tkinter as tk

class Header:
    def __init__(self, parent):
        self.parent = parent
        self.create_header()

    def create_header(self):
        """Cria o cabeçalho da aplicação."""

        self.frame = tk.Frame(self.parent, bg=Layout.BACKGROUND)
        self.frame.pack(fill="x", padx=40, pady=(35, 25))

        # Nome da aplicação
        self.title = tk.Label(self.frame, text="DataForge", font=("Arial", 26, "bold"), bg=Layout.BACKGROUND, fg=Layout.PRIMARY)
        self.title.pack(anchor="w")

        # Descrição
        self.subtitle = tk.Label(self.frame,text="Da planilha ao banco sem complicação.",font=("Arial", 11),bg=Layout.BACKGROUND,fg=Layout.TEXT_SECONDARY)
        self.subtitle.pack(anchor="w", pady=(5, 0))
