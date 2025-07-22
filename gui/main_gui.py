# gui/main_gui.py
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from converter.core import convert_image_to_jpg, is_supported_image
from tkinter import PhotoImage

def run_gui():
    def convert_files(file_paths):
        output_dir = filedialog.askdirectory(title="Select Output Folder")
        if not output_dir:
            return

        result_box.delete(0, tk.END)
        result_text.set("Converting...")
        progress['maximum'] = len(file_paths)
        progress['value'] = 0
        root.update_idletasks()

        for i, path in enumerate(file_paths):
            result = convert_image_to_jpg(path, output_dir)
            result_box.insert(tk.END, result)
            progress['value'] = i + 1
            root.update_idletasks()

        result_text.set(f"Done! Converted {len(file_paths)} files.")

    def select_and_convert():
        file_paths = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=[("Image files", "*.heic *.png *.bmp *.tiff *.tif *.gif *.webp *.jpeg *.jpg")]
        )
        if file_paths:
            convert_files(file_paths)

    def drop(event):
        raw_paths = root.tk.splitlist(event.data)
        file_paths = [p for p in raw_paths if is_supported_image(p)]
        if file_paths:
            convert_files(file_paths)

    # TkinterDnD GUI
    global root
    root = TkinterDnD.Tk()
    root.title("ImageMelt- Any Image to JPG Converter")
    root.geometry("520x430")
    root.resizable(False, False)

    style = ttk.Style(root)
    style.theme_use("clam")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Load and resize the logo
    logo_path = os.path.join("assets", "logo.png")
    original_logo = PhotoImage(file=logo_path)
    # Resize if logo is too large (optional)
    max_logo_width = 40  # Adjust as needed
    if original_logo.width() > max_logo_width:
        scale = max_logo_width / original_logo.width()
        logo_img = original_logo.subsample(int(1/scale))
    else:
        logo_img = original_logo

    # Add a label with image and text
    title_label = tk.Label(
        main_frame,
        text="  ImgMorph: Convert Images to JPG",
        image=logo_img,
        compound="left",  # Image on left, text on right
        font=("Segoe UI", 16, "bold"),
        anchor="w",
        padx=10
    )
    title_label.image = logo_img  # Keep reference to avoid garbage collection
    title_label.pack(pady=(0, 10), anchor="center")


    convert_button = ttk.Button(main_frame, text="📂 Select and Convert", command=select_and_convert)
    convert_button.pack(pady=10)

    global progress
    progress = ttk.Progressbar(main_frame, mode='determinate', length=450)
    progress.pack(pady=10)

    global result_text
    result_text = tk.StringVar(value="Select or drop files to start.")
    status_label = ttk.Label(main_frame, textvariable=result_text, font=("Segoe UI", 10, "italic"), foreground="green")
    status_label.pack(pady=5)

    drop_label = tk.Label(main_frame, text="⬇ Drag & Drop Image Files Here ⬇", relief="ridge",
                          borderwidth=2, background="#f0f0f0", height=3, font=("Arial", 12))
    drop_label.pack(pady=10, fill=tk.X)
    drop_label.drop_target_register(DND_FILES)
    drop_label.dnd_bind('<<Drop>>', drop)

    global result_box
    result_box = tk.Listbox(main_frame, height=10, font=("Courier New", 10))
    result_box.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
