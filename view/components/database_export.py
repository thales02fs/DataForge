from view.layout import Layout

import tkinter as tk

class DatabaseExport:
    def __init__(self, parent):
        self.parent = parent
        self.create_component()

    def create_component(self):
        """Cria a área de geração do banco de dados."""

        self.frame = tk.Frame(self.parent, bg=Layout.WHITE, padx=25, pady=25)
        self.frame.pack(fill="x", padx=40, pady=8)

        # Título
        self.title = tk.Label(self.frame, text="Gerar banco de dados", font=("Arial", 11, "bold"), bg=Layout.WHITE, fg=Layout.TEXT_PRIMARY)
        self.title.pack(anchor="w")

        # Descrição
        self.description = tk.Label(self.frame, text="Armazene os dados tratados em um banco SQLite.", font=("Arial", 10), bg=Layout.WHITE, fg=Layout.TEXT_SECONDARY)
        self.description.pack(anchor="w", pady=(5, 15), padx=(0, 0))

        # Botão
        self.generate_button = tk.Button(self.frame, text="Gerar banco de dados", font=("Arial", 10, "bold"), bg=Layout.SECONDARY, fg=Layout.WHITE, relief="flat", cursor="hand2", padx=7, pady=3, command=self.generate_database)
        self.generate_button.pack(anchor="w")

    def generate_database(self):
        """Inicia a geração do banco de dados."""
        pass