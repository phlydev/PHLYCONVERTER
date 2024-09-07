import os
from tkinter import filedialog, messagebox
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk
from moviepy.editor import VideoFileClip


# Funktion zum Auswählen der Datei
def select_file():
    file_path = filedialog.askopenfilename(title="Datei auswählen",
                                           filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.mov;*.flv;*.wmv")])
    if file_path:
        file_label.config(text=file_path)


# Funktion zur Umwandlung der Datei
def convert_file():
    input_file = file_label.cget("text")
    if not input_file:
        messagebox.showerror("Fehler", "Bitte eine Datei auswählen.")
        return

    output_format = format_var.get()
    if not output_format:
        messagebox.showerror("Fehler", "Bitte ein Zielformat auswählen.")
        return

    try:
        clip = VideoFileClip(input_file)

        # Standardmäßig setzen wir den Codec je nach gewähltem Format
        if output_format == "mp4":
            codec = "libx264"
        elif output_format == "avi":
            codec = "png"
        elif output_format == "mkv":
            codec = "libx264"
        elif output_format == "mov":
            codec = "libx264"
        elif output_format == "flv":
            codec = "flv"
        elif output_format == "wmv":
            codec = "libx264"  # Du kannst "wmv2" versuchen, falls Probleme auftreten

        output_file = filedialog.asksaveasfilename(defaultextension=f".{output_format}",
                                                   filetypes=[(f"{output_format.upper()} file", f"*.{output_format}")])
        if output_file:
            clip.write_videofile(output_file, codec=codec)
            messagebox.showinfo("Erfolg", "Datei wurde erfolgreich umgewandelt!")
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler bei der Umwandlung: {e}")


# Hauptfenster der Anwendung
root = ThemedTk(theme="equilux")  # Dark Mode durch ttkthemes
root.title("PHLY VIDEO CONVERTER")
root.geometry("600x400")
root.config(bg="#2C2C2C")  # Hintergrund dunkelgrau

# Stil-Verbesserungen für ttk Widgets
style = ttk.Style()
style.configure("TLabel", background="#2C2C2C", foreground="white", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 10, "bold"), padding=6, background="#4A4A4A", foreground="white")
style.configure("TOptionMenu", background="#2C2C2C", foreground="white", font=("Helvetica", 12))
style.map("TButton", background=[("active", "#00BFFF"), ("!active", "#4A4A4A")])

# Benutzerdefinierter Stil für Buttons (abgerundet und Hover-Effekte)
style.configure("RoundedButton.TButton", relief="flat", padding=6, font=("Helvetica", 10, "bold"),
                background="#4A4A4A", foreground="white", borderwidth=2)
style.map("RoundedButton.TButton", background=[("active", "#00BFFF")])

# Label und Button zur Dateiauswahl
file_label = ttk.Label(root, text="Keine Datei ausgewählt", anchor="center", borderwidth=0, relief="solid", padding=10)
file_label.pack(pady=20, padx=20, fill="x")

file_button = ttk.Button(root, text="Datei auswählen", style="RoundedButton.TButton", command=select_file)
file_button.pack(pady=10)

# Dropdown für Zielformat-Auswahl
format_var = tk.StringVar()
formats = ["mp4", "avi", "mkv", "mov", "flv", "wmv"]
format_menu = ttk.OptionMenu(root, format_var, formats[0], *formats)
format_menu.pack(pady=20)

# Button zum Starten der Konvertierung
convert_button = ttk.Button(root, text="Datei umwandeln", style="RoundedButton.TButton", command=convert_file)
convert_button.pack(pady=20)

# Fußzeile
footer_label = ttk.Label(root, text="PHLY VIDEO CONVERTER © 2024", font=("Helvetica", 10), background="#2C2C2C",
                         foreground="gray")
footer_label.pack(side="bottom", pady=10)

# Hauptschleife
root.mainloop()
