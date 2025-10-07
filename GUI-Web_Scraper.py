import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup

def scrape_website():
    url = url_entry.get().strip()
    keyword = keyword_entry.get().strip().lower()

    if not url:
        messagebox.showwarning("Input Error", "Please enter a website URL.")
        return

    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load the website:\n{e}")
        return

    results_box.delete("1.0", tk.END)

    # Search all visible text elements
    found = False
    for tag in soup.find_all(text=True):
        text = tag.strip()
        if keyword and keyword in text.lower():
            results_box.insert(tk.END, f"👉 {text}\n\n")
            found = True

    if not found:
        results_box.insert(tk.END, "No matches found for the keyword.\n")


root = tk.Tk()
root.title("Web Scraper GUI")
root.geometry("700x500")

tk.Label(root, text="Website URL:").pack(pady=5)
url_entry = tk.Entry(root, width=80)
url_entry.pack(pady=5)

tk.Label(root, text="Keyword to search:").pack(pady=5)
keyword_entry = tk.Entry(root, width=40)
keyword_entry.pack(pady=5)

tk.Button(root, text="Scrape", command=scrape_website, bg="#4CAF50", fg="white", width=15).pack(pady=10)

tk.Label(root, text="Results:").pack()
results_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
results_box.pack(padx=10, pady=10)

root.mainloop()
