import random
import time
import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class RandomPairGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Pair Generator")
        
        self.names = []
        self.generated_pairs = []
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_frame = tk.Frame(self.root)
        self.label_frame.pack(pady=10)
        
        self.random_pair_label = tk.Label(self.label_frame, text="Random Pair", font=("Helvetica", 16))
        self.random_pair_label.pack()
        
        self.author_label = tk.Label(self.label_frame, text="by Nur Dwi P.", font=("Helvetica", 12))
        self.author_label.pack()
        
        self.add_name_button = ttk.Button(self.root, text="Tambah Nama", command=self.show_add_name_window)
        self.add_name_button.pack(pady=5, padx=10, fill=tk.BOTH)
        
        self.generate_pairs_button = ttk.Button(self.root, text="Buat Pasangan", command=self.generate_pairs)
        self.generate_pairs_button.pack(pady=5, padx=10, fill=tk.BOTH)
        
        self.reset_button = ttk.Button(self.root, text="Reset", command=self.reset_names)
        self.reset_button.pack(pady=5, padx=10, fill=tk.BOTH)
        
        self.quit_button = ttk.Button(self.root, text="Keluar", command=self.root.destroy)
        self.quit_button.pack(pady=10, padx=10, fill=tk.BOTH)
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        
    def show_add_name_window(self):
        self.main_frame.destroy()
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        
        self.name_label = tk.Label(self.main_frame, text="Masukkan Nama:")
        self.name_label.pack(anchor="w", padx=10, pady=5)
        
        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.pack(anchor="w", padx=10, pady=5, fill=tk.BOTH)
        
        self.names_label = tk.Label(self.main_frame, text="Nama yang telah dimasukkan:")
        self.names_label.pack(padx=10, pady=5)
        
        self.names_text = tk.Text(self.main_frame, height=5, width=30, state="disabled")
        self.names_text.pack(padx=10, pady=5, fill=tk.BOTH)
        
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)
        
        self.submit_button = ttk.Button(self.button_frame, text="Submit", command=self.add_name_and_close)
        self.submit_button.pack(side="left", padx=5, fill=tk.BOTH)
        
        self.name_entry.bind("<Return>", lambda event: self.add_name())
        
    def add_name_and_close(self):
        self.add_name()
        self.main_frame.destroy()
        
    def add_name(self):
        name = self.name_entry.get()
        if name:
            self.names.append(name)
            self.name_entry.delete(0, tk.END)  # Membersihkan kotak masukan
            self.names_text.config(state="normal")  # Aktifkan mode edit
            self.names_text.delete("1.0", tk.END)  # Membersihkan teks sebelumnya
            self.names_text.insert(tk.END, "\n".join(self.names))
            
    def generate_pairs(self):
        if len(self.names) < 2:
            messagebox.showerror("Kesalahan", "Harap masukkan setidaknya dua nama peserta.")
            return
        
        random.shuffle(self.names)
        self.generated_pairs = [(self.names[i], self.names[i+1]) for i in range(0, len(self.names), 2)]
        
        self.show_generated_pairs()
        
    def show_generated_pairs(self):
        self.main_frame.destroy()
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        
        if not self.generated_pairs:
            pairs_label = tk.Label(self.main_frame, text="Belum ada pasangan yang dibuat.")
            pairs_label.pack(padx=10, pady=10)
        else:
            pairs_text = "\n".join([f"{pair[0]} - {pair[1]}" for pair in self.generated_pairs])
            pairs_label = tk.Label(self.main_frame, text=pairs_text)
            pairs_label.pack(padx=10, pady=10)
        
        ulangi_button = ttk.Button(self.main_frame, text="Ulangi", command=self.generate_pairs)
        ulangi_button.pack(pady=5, padx=10, fill=tk.BOTH)
        
        simpan_button = ttk.Button(self.main_frame, text="Simpan", command=self.reset_names)
        simpan_button.pack(pady=5, padx=10, fill=tk.BOTH)
        
    def reset_names(self):
        self.names = []
        self.generated_pairs = []
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = RandomPairGeneratorApp(root)
    root.geometry("360x640")  # Ukuran tampilan ponsel
    root.mainloop()
