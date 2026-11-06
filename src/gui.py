
import tkinter as tk
from tkinter import ttk


class SearchGUI:
    # Professional color palette
    NAVY = "#14213D"
    BLUE = "#2563EB"
    BLUE_HOVER = "#1D4ED8"
    BG = "#F3F6FB"
    WHITE = "#FFFFFF"
    TEXT = "#1E293B"
    MUTED = "#64748B"
    BORDER = "#E2E8F0"
    GREEN = "#16A34A"

    def __init__(self, query_processor, wildcard_processor, filenames):
        self.query_processor = query_processor
        self.wildcard_processor = wildcard_processor
        self.filenames = filenames

        self.root = tk.Tk()
        self.root.title("Web Search Mining | Information Retrieval System")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        self.root.configure(bg=self.BG)

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Search.TButton",
            font=("Helvetica", 11, "bold"),
            foreground=self.WHITE,
            background=self.BLUE,
            borderwidth=0,
            padding=(20, 12)
        )

        style.map(
            "Search.TButton",
            background=[("active", self.BLUE_HOVER)]
        )

        style.configure(
            "Clear.TButton",
            font=("Helvetica", 10),
            foreground=self.MUTED,
            background=self.WHITE,
            borderwidth=1,
            padding=(12, 8)
        )

        style.configure(
            "Vertical.TScrollbar",
            background="#CBD5E1",
            troughcolor=self.WHITE,
            borderwidth=0,
            arrowsize=14
        )

    def create_widgets(self):
        # ================= HEADER =================
        header = tk.Frame(self.root, bg=self.NAVY, height=155)
        header.pack(fill="x")
        header.pack_propagate(False)

        header_content = tk.Frame(header, bg=self.NAVY)
        header_content.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=25
        )

        # Project title
        tk.Label(
            header_content,
            text="WEB SEARCH MINING",
            font=("Helvetica", 26, "bold"),
            fg=self.WHITE,
            bg=self.NAVY
        ).pack(anchor="w")

        tk.Label(
            header_content,
            text="Information Retrieval System",
            font=("Helvetica", 12),
            fg="#CBD5E1",
            bg=self.NAVY
        ).pack(anchor="w", pady=(5, 12))

        # Student information
        tk.Label(
            header_content,
            text="ACADEMIC PROJECT   |   ANKUSH   |   B524012",
            font=("Helvetica", 9, "bold"),
            fg="#93C5FD",
            bg=self.NAVY
        ).pack(anchor="w")

        # ================= MAIN CONTENT =================
        main_frame = tk.Frame(self.root, bg=self.BG)
        main_frame.pack(fill="both", expand=True, padx=40, pady=25)

        # Search section
        search_card = tk.Frame(
            main_frame,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        search_card.pack(fill="x", pady=(0, 20))

        search_content = tk.Frame(search_card, bg=self.WHITE)
        search_content.pack(fill="x", padx=25, pady=22)

        tk.Label(
            search_content,
            text="Search Documents",
            font=("Helvetica", 15, "bold"),
            fg=self.TEXT,
            bg=self.WHITE
        ).pack(anchor="w")

        tk.Label(
            search_content,
            text="Enter keywords, Boolean expressions, or wildcard queries.",
            font=("Helvetica", 10),
            fg=self.MUTED,
            bg=self.WHITE
        ).pack(anchor="w", pady=(5, 15))

        # Search entry and button
        search_row = tk.Frame(search_content, bg=self.WHITE)
        search_row.pack(fill="x")

        self.search_entry = tk.Entry(
            search_row,
            font=("Helvetica", 13),
            bg="#F8FAFC",
            fg=self.TEXT,
            insertbackground=self.BLUE,
            relief="flat",
            highlightthickness=1,
            highlightbackground=self.BORDER,
            highlightcolor=self.BLUE
        )

        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=12,
            padx=(0, 12)
        )

        self.search_entry.insert(0, "Enter your search query...")

        self.search_entry.bind(
            "<FocusIn>",
            self.clear_placeholder
        )

        self.search_entry.bind(
            "<Return>",
            lambda event: self.perform_search()
        )

        self.search_button = ttk.Button(
            search_row,
            text="SEARCH  →",
            style="Search.TButton",
            command=self.perform_search
        )
        self.search_button.pack(side="right")

        # Query examples
        tk.Label(
            search_content,
            text=(
                "Examples:  information   |   "
                "retrieval AND index   |   "
                "search OR ranking   |   retriev*"
            ),
            font=("Helvetica", 9),
            fg=self.MUTED,
            bg=self.WHITE
        ).pack(anchor="w", pady=(12, 0))

        # ================= RESULTS SECTION =================
        results_header = tk.Frame(main_frame, bg=self.BG)
        results_header.pack(fill="x", pady=(0, 12))

        tk.Label(
            results_header,
            text="Search Results",
            font=("Helvetica", 16, "bold"),
            fg=self.TEXT,
            bg=self.BG
        ).pack(side="left")

        self.result_count = tk.Label(
            results_header,
            text="0 DOCUMENTS",
            font=("Helvetica", 9, "bold"),
            fg=self.BLUE,
            bg="#DBEAFE",
            padx=12,
            pady=6
        )
        self.result_count.pack(side="right")

        # Results container
        result_card = tk.Frame(
            main_frame,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        result_card.pack(fill="both", expand=True)

        result_content = tk.Frame(result_card, bg=self.WHITE)
        result_content.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            result_content,
            orient="vertical",
            style="Vertical.TScrollbar"
        )
        scrollbar.pack(side="right", fill="y")

        # Results text area
        self.result_area = tk.Text(
            result_content,
            font=("Helvetica", 11),
            wrap="word",
            padx=15,
            pady=15,
            bg=self.WHITE,
            fg=self.TEXT,
            state="disabled",
            relief="flat",
            borderwidth=0,
            yscrollcommand=scrollbar.set,
            spacing1=5,
            spacing3=5
        )

        self.result_area.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.config(command=self.result_area.yview)

        # Text formatting
        self.result_area.tag_configure(
            "heading",
            font=("Helvetica", 13, "bold"),
            foreground=self.NAVY
        )

        self.result_area.tag_configure(
            "document",
            font=("Helvetica", 11),
            foreground=self.BLUE,
            lmargin1=10,
            lmargin2=25
        )

        self.result_area.tag_configure(
            "info",
            font=("Helvetica", 10),
            foreground=self.MUTED
        )

        self.result_area.tag_configure(
            "success",
            font=("Helvetica", 11, "bold"),
            foreground=self.GREEN
        )

        # Initial welcome message
        self.display_results(
            "Welcome to Web Search Mining\n\n"
            "Your Information Retrieval System is ready.\n\n"
            "Enter a query above to retrieve relevant documents.",
            count=0
        )

        # ================= FOOTER =================
        footer = tk.Frame(self.root, bg=self.BG)
        footer.pack(fill="x", padx=40, pady=(0, 15))

        tk.Label(
            footer,
            text="INFORMATION RETRIEVAL SYSTEM",
            font=("Helvetica", 8, "bold"),
            fg=self.MUTED,
            bg=self.BG
        ).pack(side="left")

        tk.Label(
            footer,
            text="IIIT BHUBANESWAR  •  B524012",
            font=("Helvetica", 8),
            fg=self.MUTED,
            bg=self.BG
        ).pack(side="right")

    def clear_placeholder(self, event):
        if self.search_entry.get() == "Enter your search query...":
            self.search_entry.delete(0, tk.END)

    def perform_search(self):
        query = self.search_entry.get().strip()

        if query == "Enter your search query..." or not query:
            self.display_results(
                "Please enter a search query.",
                count=0
            )
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
                    f'No documents found for "{query}".',
                    count=0
                )
                return

            self.result_area.config(state="normal")
            self.result_area.delete("1.0", tk.END)

            self.result_area.insert(
                tk.END,
                f"QUERY: {query}\n",
                "heading"
            )

            self.result_area.insert(
                tk.END,
                f"\n{len(document_ids)} matching documents found\n\n",
                "info"
            )

            self.result_area.insert(
                tk.END,
                "─" * 55 + "\n\n",
                "info"
            )

            for index, doc_id in enumerate(document_ids, 1):
                filename = self.filenames.get(
                    doc_id,
                    f"Document {doc_id}"
                )

                self.result_area.insert(
                    tk.END,
                    f"{index:02d}.  {filename}\n\n",
                    "document"
                )

            self.result_area.config(state="disabled")

            self.result_count.config(
                text=f"{len(document_ids)} DOCUMENTS"
            )

        except Exception as error:
            self.display_results(
                f"Error while processing query:\n\n{error}",
                count=0
            )

    def display_results(self, text, count=0):
        self.result_area.config(state="normal")
        self.result_area.delete("1.0", tk.END)
        self.result_area.insert("1.0", text)
        self.result_area.config(state="disabled")

        self.result_count.config(
            text=f"{count} DOCUMENTS"
        )

    def run(self):
        self.root.mainloop()
