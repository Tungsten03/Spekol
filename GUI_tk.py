import tkinter as tk
from ttkthemes import ThemedTk
from utility import labels as lbl
from utility import client_settup as cst
from func import *
from pymodbus.client import ModbusSerialClient


def show_err():
    """
    Display a help popup window with instructions.

    This function creates a new 'Pomoc' popup window using `Toplevel()`. It adds a label to the
    popup window with the help text obtained from `lbl.gui_help`.

    :return: None
    """
    # Create a new popup window with 'Pomoc' title
    popup = tk.Toplevel()
    popup.title('Pomoc')

    # Create a label with help text
    label = tk.Label(popup, text=lbl.connect_error, justify='left')
    label.pack(padx=20, pady=20)

    # Create a close button
    button = tk.Button(popup, text="Zamknij", command=popup.destroy)
    button.pack(pady=10)

def connect():
    port = entry_port.get()
    baudrate = entry_baud.get()
    bytesize = 8
    pairity = entry_pair.get()
    stopbits = entry_stopb.get()
    client = ModbusSerialClient(port=port, baudrate=baudrate, bytesize=bytesize, pairity=pairity,
                                sopbits=stopbits)
    connection = client.connect()
    if connection:
        connection_status.set('Połączono z klientem')
        connection_entry.config(background='green')
    else:
        show_err()
        connection_status.set('Nie udało się połączyć z klientem')
        connection_entry.config(background='red')

def toggle_settings():
    if block_var.get():
        port_en.config(state='disabled')
        baud_en.config(state='disabled')
        pair_en.config(state='disabled')
        stopb_en.config(state='disabled')
    else:
        port_en.config(state='normal')
        baud_en.config(state='normal')
        pair_en.config(state='normal')
        stopb_en.config(state='normal')

root = ThemedTk(theme="plastic")

root.title('ASKR')
root.geometry('640x600')

# Create Frame Model
settings_frame = tk.Frame(root, width=580, height=150, relief='ridge', borderwidth=2)
settings_frame.grid(row=0, column=0, padx=10, pady=5)

drive_frame = tk.Frame(root, width=580, height=150, relief='ridge', borderwidth=2)
drive_frame.grid(row=1, column=0, padx=10, pady=5)

func_frame = tk.Frame(root, width=580, height=150, relief='ridge', borderwidth=2)
func_frame.grid(row=2, column=0, padx=10, pady=5)

# Setting frame gutts
# ROW 0
tk.Label(settings_frame, text='Ustawienia klienta').grid(row=0, column=0, padx=2, pady=10, sticky='NW')
tk.Label(settings_frame, text='PORT').grid(row=0, column=1, padx=2, pady=10)
tk.Label(settings_frame, text='transmisja').grid(row=0, column=2, padx=2, pady=10)
tk.Label(settings_frame, text='parzystość').grid(row=0, column=3, padx=2, pady=10)
tk.Label(settings_frame, text='bity stopu').grid(row=0, column=4, padx=2, pady=10)

# ROW 1
block_var = tk.IntVar()
block_var.set(1)
block = tk.Checkbutton(settings_frame, text='blokuj', variable=block_var, command=toggle_settings)
block.grid(row=1, column=0, padx=2, pady=10, sticky='E')
# tk.Label(settings_frame, text='blokuj').grid(row=1, column=0, padx=2, pady=10, sticky='W')

entry_port = tk.StringVar()
entry_port.set(cst.default_port)
port_en = tk.Entry(settings_frame, textvariable=entry_port)
port_en.grid(row=1, column=1, padx=2, pady=10)
port_en.config(state='disabled')

entry_baud = tk.IntVar()
entry_baud.set(cst.default_baudrate)
baud_en = tk.Entry(settings_frame, textvariable=entry_baud)
baud_en.grid(row=1, column=2, padx=2, pady=10)
baud_en.config(state='disabled')

entry_pair = tk.StringVar()
entry_pair.set(cst.default_pairity)
pair_en = tk.Entry(settings_frame, textvariable=entry_pair)
pair_en.grid(row=1, column=3, padx=2, pady=10)
pair_en.config(state='disabled')

entry_stopb = tk.IntVar()
entry_stopb.set(cst.default_stopbits)
stopb_en = tk.Entry(settings_frame, textvariable=entry_stopb)
stopb_en.grid(row=1, column=4, padx=2, pady=10)
stopb_en.config(state='disabled')

# ROW 2
conn_but = tk.Button(settings_frame, text='POŁĄCZ', command=connect)
conn_but.grid(row=2, column=0, padx=2, pady=10)
connection_status = tk.StringVar()
connection_status.set('Sprawdź parametry klienta i naciśnij: POŁĄCZ')
connection_entry = tk.Entry(settings_frame, textvariable=connection_status)
connection_entry.grid(row=2, column=1, columnspan=3, pady=10, sticky='WE')

# Drive frame gutts
acc_entry = tk.Entry(drive_frame)
acc_entry.pack()


root.mainloop()