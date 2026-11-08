
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

from view.layout import Layout


class FileUpload:
    def __init__(self, parent):
        self.parent = parent
        self.file_path = None

        self.create_component()

    def create_component(self):
        """Cria a área de seleção de arquivo."""

        self.frame = tk.Frame(self.parent, bg=Layout.WHITE, padx=15, pady=15)
        self.frame.pack(fill="x", padx=40, pady=8)

        # Título
        self.title = tk.Label(self.frame, text="Importar planilha", font=("Arial", 11, "bold"), bg=Layout.WHITE, fg=Layout.TEXT_PRIMARY)
        self.title.pack(anchor="w")

        # Descrição
        self.description = tk.Label(self.frame, text="Selecione um arquivo Excel para começar.", font=("Arial", 10), bg=Layout.WHITE, fg=Layout.TEXT_SECONDARY)
        self.description.pack(anchor="w", pady=(5, 15), padx=(0, 0))

        # Botões
        self.buttons_frame = tk.Frame(self.frame, bg=Layout.WHITE)
        self.buttons_frame.pack(anchor="w")

        self.upload_button = tk.Button(self.buttons_frame, text="Selecionar arquivo Excel", font=("Arial", 10, "bold"), bg=Layout.SECONDARY, fg=Layout.WHITE, relief="flat", cursor="hand2", padx=7, pady=3, command=self.select_file)
        self.upload_button.pack(side="left")

        # Nome do arquivo selecionado
        self.file_label = tk.Label(self.frame, text="Nenhum arquivo selecionado", font=("Arial", 9), bg=Layout.WHITE, fg=Layout.TEXT_SECONDARY)
        self.file_label.pack(anchor="w", pady=(10, 0))

    def select_file(self):
        """Abre a janela para seleção de arquivo Excel."""

        file_path = filedialog.askopenfilename(title="Selecionar planilha Excel", filetypes=[("Arquivos Excel", "*.xlsx *.xls")])
        if file_path:
            self.file_path = file_path
            file_name = Path(file_path).name
            self.file_label.config(text=f"Arquivo selecionado: {file_name}", fg=Layout.TEXT_PRIMARY)
