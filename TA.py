import tkinter as tk
from tkinter import messagebox

class InflationCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Inflasi")
        
        self._inflation_rate = 3.03  # Private attribute for inflation rate

        # Membuat label dan entry untuk jumlah uang awal
        self.label_initial_amount = tk.Label(root, text="Masukkan jumlah uang awal (dalam Rupiah):")
        self.label_initial_amount.pack()
        self.entry_initial_amount = tk.Entry(root)
        self.entry_initial_amount.pack()

        # Membuat label dan entry untuk jumlah tahun
        self.label_years = tk.Label(root, text="Masukkan jumlah tahun:")
        self.label_years.pack()
        self.entry_years = tk.Entry(root)
        self.entry_years.pack()

        # Membuat tombol untuk menghitung inflasi
        self.calculate_button = tk.Button(root, text="Hitung Inflasi", command=self.calculate)
        self.calculate_button.pack()

        # Label untuk menampilkan hasil
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def get_inflation_rate(self):
        return self._inflation_rate

    def set_inflation_rate(self, rate):
        if rate > 0:
            self._inflation_rate = rate
        else:
            raise ValueError("Tingkat inflasi harus lebih besar dari 0")

    def calculate_inflation(self, initial_amount, years):
        future_value = initial_amount
        for _ in range(years):
            future_value *= (1 + self._inflation_rate / 100)
        return future_value

    def calculate(self):
        try:
            initial_amount = float(self.entry_initial_amount.get())
            years = int(self.entry_years.get())
            if initial_amount <= 0 or years <= 0:
                raise ValueError

            future_value = self.calculate_inflation(initial_amount, years)
            self.result_label.config(text=f"Nilai uang sebesar Rp{initial_amount:,.2f} setelah {years} tahun dengan tingkat inflasi 3,03% per tahun adalah Rp{future_value:,.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Masukkan nilai yang valid untuk jumlah uang dan jumlah tahun (harus lebih dari 0).")

if __name__ == "__main__":
    root = tk.Tk()
    app = InflationCalculator(root)
    root.mainloop()
