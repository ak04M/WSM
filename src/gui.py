import tkinter as tk
from tkinter import ttk


class SearchGUI:
    def __init__(self, query_processor, wildcard_processor, filenames):
        self.query_processor = query_processor
        self.wildcard_processor = wildcard_processor
        self.filenames = filenames

        self.root = tk.Tk()
        self.root.title("Web Search Mining")
        self.root.geometry("850x600")
        self.root.minsize(700, 500)

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=30)
        main_frame.pack(fill="both", expand=True)

        title = tk.Label(
            main_frame,
            text="WEB SEARCH MINING",
            font=("Helvetica", 24, "bold")
        )
        title.pack(anchor="w")

        subtitle = tk.Label(
            main_frame,
            text="Information Retrieval System",
            font=("Helvetica", 12)
        )
        subtitle.pack(anchor="w", pady=(2, 5))

        student = tk.Label(
            main_frame,
            text="Ankush  •  B524012",
            font=("Helvetica", 10)
        )
        student.pack(anchor="w", pady=(0, 25))

        search_label = tk.Label(
            main_frame,
            text="Search",
            font=("Helvetica", 11, "bold")
        )
        search_label.pack(anchor="w", pady=(0, 8))

        search_frame = ttk.Frame(main_frame)
        search_frame.pack(fill="x")

        self.search_entry = ttk.Entry(
            search_frame,
            font=("Helvetica", 13)
        )
        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=7
        )

        self.search_button = ttk.Button(
            search_frame,
            text="Search",
            command=self.perform_search
        )
        self.search_button.pack(
            side="left",
            padx=(10, 0),
            ipadx=15,
            ipady=5
        )

        self.search_entry.bind(
            "<Return>",
            lambda event: self.perform_search()
        )

        hint = tk.Label(
            main_frame,
            text="Examples: information   |   retrieval AND index   |   search OR ranking   |   retriev*",
            font=("Helvetica", 9)
        )
        hint.pack(anchor="w", pady=(8, 25))

        results_label = tk.Label(
            main_frame,
            text="Results",
            font=("Helvetica", 11, "bold")
        )
        results_label.pack(anchor="w", pady=(0, 8))

        result_frame = ttk.Frame(main_frame)
        result_frame.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            result_frame,
            orient="vertical"
        )
        scrollbar.pack(side="right", fill="y")

        self.result_area = tk.Text(
            result_frame,
            font=("Helvetica", 11),
            wrap="word",
            padx=15,
            pady=12,
            state="disabled",
            yscrollcommand=scrollbar.set,
            relief="solid",
            borderwidth=1
        )
        self.result_area.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.config(command=self.result_area.yview)

        footer = tk.Label(
            main_frame,
            text="Ankush  •  B524012",
            font=("Helvetica", 10)
        )
        footer.pack(anchor="e", pady=(15, 0))

    def perform_search(self):
        query = self.search_entry.get().strip()

        if not query:
            self.display_results("Please enter a search query.")
            return

        try:
            if "*" in query:
                document_ids = self.wildcard_processor(
                    query.lower()
                )
            else:
                document_ids = self.query_processor.search(
                    query
                )

            if not document_ids:
                self.display_results(
                    f'No documents found for "{query}".'
                )
                return

            results = []

            for doc_id in document_ids:
                filename = self.filenames.get(
                    doc_id,
                    f"Document {doc_id}"
                )
                results.append(f"• {filename}")

            output = (
                f'Query: {query}\n'
                f'Results found: {len(document_ids)}\n'
                f'{"─" * 55}\n\n'
                + "\n".join(results)
            )

            self.display_results(output)

        except Exception as error:
            self.display_results(
                f"Error while processing query:\n{error}"
            )

    def display_results(self, text):
        self.result_area.config(state="normal")
        self.result_area.delete("1.0", tk.END)
        self.result_area.insert("1.0", text)
        self.result_area.config(state="disabled")

    def run(self):
        self.root.mainloop()