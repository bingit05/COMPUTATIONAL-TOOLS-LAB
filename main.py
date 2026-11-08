import tkinter as tk
from tkinter import messagebox, ttk
from database import init_db
import operations


class LibraryApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Library Management System")
    self.root.geometry("800x600")
    self.root.config(bg="#f4f4f4")

    # Initialize Database
    init_db()

    # Create Notebook (Tabs)
    self.notebook = ttk.Notebook(self.root)
    self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # Tabs
    self.tab_add_book = ttk.Frame(self.notebook)
    self.tab_issue_book = ttk.Frame(self.notebook)
    self.tab_return_book = ttk.Frame(self.notebook)
    self.tab_search = ttk.Frame(self.notebook)

    self.notebook.add(self.tab_add_book, text="Add Book")
    self.notebook.add(self.tab_issue_book, text="Issue Book")
    self.notebook.add(self.tab_return_book, text="Return Book")
    self.notebook.add(self.tab_search, text="Search Records")

    self.setup_add_book_ui()
    self.setup_issue_book_ui()
    self.setup_return_book_ui()
    self.setup_search_ui()

  def setup_add_book_ui(self):
    frame = ttk.LabelFrame(
        self.tab_add_book, text="Add New Book Details", padding=20
    )
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ttk.Label(frame, text="Book Title:").grid(
        row=0, column=0, sticky="w", pady=5
    )
    self.title_entry = ttk.Entry(frame, width=30)
    self.title_entry.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Author:").grid(row=1, column=0, sticky="w", pady=5)
    self.author_entry = ttk.Entry(frame, width=30)
    self.author_entry.grid(row=1, column=1, pady=5)

    ttk.Label(frame, text="ISBN:").grid(row=2, column=0, sticky="w", pady=5)
    self.isbn_entry = ttk.Entry(frame, width=30)
    self.isbn_entry.grid(row=2, column=1, pady=5)

    ttk.Label(frame, text="Total Copies:").grid(
        row=3, column=0, sticky="w", pady=5
    )
    self.copies_entry = ttk.Entry(frame, width=30)
    self.copies_entry.grid(row=3, column=1, pady=5)

    ttk.Button(
        frame, text="Add Book", command=self.add_book_action
    ).grid(row=4, column=0, columnspan=2, pady=20)

  def add_book_action(self):
    success, msg = operations.add_book(
        self.title_entry.get().strip(),
        self.author_entry.get().strip(),
        self.isbn_entry.get().strip(),
        self.copies_entry.get().strip(),
    )
    if success:
      messagebox.showinfo("Success", msg)
      self.title_entry.delete(0, tk.END)
      self.author_entry.delete(0, tk.END)
      self.isbn_entry.delete(0, tk.END)
      self.copies_entry.delete(0, tk.END)
    else:
      messagebox.showerror("Error", msg)

  def setup_issue_book_ui(self):
    frame = ttk.LabelFrame(
        self.tab_issue_book, text="Issue Book to Borrower", padding=20
    )
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ttk.Label(frame, text="Book ISBN:").grid(row=0, column=0, sticky="w", pady=5)
    self.issue_isbn_entry = ttk.Entry(frame, width=30)
    self.issue_isbn_entry.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Borrower Name:").grid(
        row=1, column=0, sticky="w", pady=5
    )
    self.borrower_entry = ttk.Entry(frame, width=30)
    self.borrower_entry.grid(row=1, column=1, pady=5)

    ttk.Button(
        frame, text="Issue Book", command=self.issue_book_action
    ).grid(row=2, column=0, columnspan=2, pady=20)

  def issue_book_action(self):
    success, msg = operations.issue_book(
        self.issue_isbn_entry.get().strip(), self.borrower_entry.get().strip()
    )
    if success:
      messagebox.showinfo("Success", msg)
      self.issue_isbn_entry.delete(0, tk.END)
      self.borrower_entry.delete(0, tk.END)
    else:
      messagebox.showerror("Error", msg)

  def setup_return_book_ui(self):
    frame = ttk.LabelFrame(
        self.tab_return_book, text="Return Issued Book", padding=20
    )
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ttk.Label(frame, text="Book ISBN:").grid(row=0, column=0, sticky="w", pady=5)
    self.return_isbn_entry = ttk.Entry(frame, width=30)
    self.return_isbn_entry.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Borrower Name:").grid(
        row=1, column=0, sticky="w", pady=5
    )
    self.return_borrower_entry = ttk.Entry(frame, width=30)
    self.return_borrower_entry.grid(row=1, column=1, pady=5)

    ttk.Button(
        frame, text="Return Book", command=self.return_book_action
    ).grid(row=2, column=0, columnspan=2, pady=20)

  def return_book_action(self):
    success, msg = operations.return_book(
        self.return_isbn_entry.get().strip(),
        self.return_borrower_entry.get().strip(),
    )
    if success:
      messagebox.showinfo("Success", msg)
      self.return_isbn_entry.delete(0, tk.END)
      self.return_borrower_entry.delete(0, tk.END)
    else:
      messagebox.showerror("Error", msg)

  def setup_search_ui(self):
    frame = ttk.LabelFrame(
        self.tab_search, text="Search Inventory & Transactions", padding=10
    )
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    ttk.Label(frame, text="Search Type:").grid(
        row=0, column=0, sticky="w", pady=5
    )
    self.search_type_combo = ttk.Combobox(
        frame, values=["Books Inventory", "Active Transactions"], state="readonly"
    )
    self.search_type_combo.grid(row=0, column=1, pady=5)
    self.search_type_combo.current(0)

    ttk.Label(frame, text="Keyword:").grid(row=1, column=0, sticky="w", pady=5)
    self.search_entry = ttk.Entry(frame, width=30)
    self.search_entry.grid(row=1, column=1, pady=5)

    ttk.Button(frame, text="Search", command=self.perform_search).grid(
        row=1, column=2, padx=10
    )

    self.tree = ttk.Treeview(frame, columns=(), show="headings", height=15)
    self.tree.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=15)

    scrollbar = ttk.Scrollbar(
        frame, orient="vertical", command=self.tree.yview
    )
    scrollbar.grid(row=2, column=3, sticky="ns", pady=15)
    self.tree.configure(yscrollcommand=scrollbar.set)

    frame.rowconfigure(2, weight=1)
    frame.columnconfigure(1, weight=1)

  def perform_search(self):
    search_type = self.search_type_combo.get()
    keyword = self.search_entry.get().strip()

    for item in self.tree.get_children():
      self.tree.delete(item)

    rows = operations.search_records(search_type, keyword)

    if search_type == "Books Inventory":
      self.tree["columns"] = (
          "ID",
          "Title",
          "Author",
          "ISBN",
          "Total",
          "Available",
      )
      for col in self.tree["columns"]:
        self.tree.heading(col, text=col)
        self.tree.column(col, width=110, anchor="center")
    elif search_type == "Active Transactions":
      self.tree["columns"] = (
          "ID",
          "ISBN",
          "Borrower",
          "Issue Date",
          "Status",
      )
      for col in self.tree["columns"]:
        self.tree.heading(col, text=col)
        self.tree.column(col, width=130, anchor="center")

    for row in rows:
      self.tree.insert("", tk.END, values=row)


if __name__ == "__main__":
  root = tk.Tk()
  app = LibraryApp(root)
  root.mainloop()