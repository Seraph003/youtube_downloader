from tkinter import Tk
from tkinter.filedialog import askdirectory

try:
    print("Tkinter...")
    root = Tk()
    root.withdraw()
    print("Membuka file explorer untuk memilih path penyimpanan...")
    output_path = askdirectory(title="Pilih path")
    print(f"Path yang dipilih: {output_path}")
    root.destroy()
except Exception as e:
    print(f"Error file explorer: {e}")
