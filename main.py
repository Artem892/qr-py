import qrcode
import tkinter as tk
from PIL import ImageTk, Image

# Функція для генерації QR-коду
def generate_qrcode():
    # Отримати URL з поля введення
    url = url_entry.get()
    # Створити QR-код
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    # Зберегти QR-код у форматі PNG
    img.save('qrcode.png')
    # Відображення QR-коду в графічному інтерфейсі
    img = ImageTk.PhotoImage(Image.open('qrcode.png'))
    qr_label.config(image=img)
    qr_label.image = img

# Створення графічного інтерфейсу

root = tk.Tk()
root.title("QR Code Generator")

# Створення елементів графічного інтерфейсу
url_label = tk.Label(root, text="URL:")
url_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qrcode)
qr_label = tk.Label(root)

# Розміщення елементів графічного інтерфейсу
url_label.pack()
url_entry.pack()
generate_button.pack()
qr_label.pack()

# Запуск головного циклу графічного інтерфейсу
root.mainloop()
