from datetime import datetime
import sqlite3
from database import get_connection


def add_book(title, author, isbn, copies):
  if not title or not author or not isbn or not copies:
    return False, "All fields are required!"
  try:
    copies = int(copies)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, isbn, total_copies, available_copies)"
        " VALUES (?, ?, ?, ?, ?)",
        (title, author, isbn, copies, copies),
    )
    conn.commit()
    conn.close()
    return True, "Book added successfully!"
  except sqlite3.IntegrityError:
    return False, "Book with this ISBN already exists!"
  except ValueError:
    return False, "Total copies must be a valid integer."


def issue_book(isbn, borrower):
  if not isbn or not borrower:
    return False, "All fields are required!"

  conn = get_connection()
  cursor = conn.cursor()

  cursor.execute("SELECT available_copies FROM books WHERE isbn = ?", (isbn,))
  result = cursor.fetchone()

  if not result:
    conn.close()
    return False, "Book not found with this ISBN!"

  available_copies = result[0]
  if available_copies > 0:
    issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "UPDATE books SET available_copies = available_copies - 1 WHERE isbn ="
        " ?",
        (isbn,),
    )
    cursor.execute(
        "INSERT INTO transactions (isbn, borrower_name, issue_date, status)"
        " VALUES (?, ?, ?, ?)",
        (isbn, borrower, issue_date, "Issued"),
    )
    conn.commit()
    conn.close()
    return True, f"Book issued successfully to {borrower}!"
  else:
    conn.close()
    return False, "No copies available to issue!"


def return_book(isbn, borrower):
  if not isbn or not borrower:
    return False, "All fields are required!"

  conn = get_connection()
  cursor = conn.cursor()

  cursor.execute(
      "SELECT id FROM transactions WHERE isbn = ? AND borrower_name = ? AND"
      " status = 'Issued'",
      (isbn, borrower),
  )
  transaction = cursor.fetchone()

  if not transaction:
    conn.close()
    return False, "No active issue record found for this user and book!"

  return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  cursor.execute(
      "UPDATE transactions SET return_date = ?, status = 'Returned' WHERE id ="
      " ?",
      (return_date, transaction[0]),
  )
  cursor.execute(
      "UPDATE books SET available_copies = available_copies + 1 WHERE isbn = ?",
      (isbn,),
  )
  conn.commit()
  conn.close()
  return True, "Book returned successfully!"


def search_records(search_type, keyword):
  conn = get_connection()
  cursor = conn.cursor()
  keyword_pattern = f"%{keyword}%"

  rows = []
  if search_type == "Books Inventory":
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?",
        (keyword_pattern, keyword_pattern, keyword_pattern),
    )
    rows = cursor.fetchall()
  elif search_type == "Active Transactions":
    cursor.execute(
        "SELECT id, isbn, borrower_name, issue_date, status FROM transactions"
        " WHERE (isbn LIKE ? OR borrower_name LIKE ?) AND status = 'Issued'",
        (keyword_pattern, keyword_pattern),
    )
    rows = cursor.fetchall()

  conn.close()
  return rows