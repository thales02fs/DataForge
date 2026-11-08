
import tkinter as tk

from view.layout import Layout

class Processing:
    def __init__(self, parent):
        self.parent = parent
        self.create_component()

    def create_component(self):
        """Cria a área de tratamento dos dados."""

        self.frame = tk.Frame(self.parent, bg=Layout.WHITE, padx=25, pady=25)
        self.frame.pack(fill="x", padx=40, pady=0)

        # Título
        self.title = tk.Label(self.frame, text="Tratamento de dados", font=("Arial", 11, "bold"), bg=Layout.WHITE, fg=Layout.TEXT_PRIMARY)
        self.title.pack(anchor="w")

        # Descrição
        self.description = tk.Label(self.frame, text="Identifique inconsistências e prepare sua planilha para armazenamento.", font=("Arial", 10), bg=Layout.WHITE, fg=Layout.TEXT_SECONDARY)
        self.description.pack(anchor="w", pady=(5, 15), padx=(0, 0))

        # Botão de tratamento
        self.process_button = tk.Button(self.frame, text="Limpar e tratar dados", font=("Arial", 10, "bold"), bg=Layout.SECONDARY, fg=Layout.WHITE, relief="flat", cursor="hand2", padx=7, pady=3)
        self.process_button.pack(anchor="w")

        # Resultado do processamento
        self.result_label = tk.Label(self.frame, text="Aguardando processamento...", font=("Arial", 9), bg=Layout.WHITE, fg=Layout.TEXT_SECONDARY)
        self.result_label.pack(anchor="w", pady=(15, 0))
