from tkinter import ttk
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
    label = ttk.Label(popup, text=lbl.connect_error, justify='left')
    label.pack(padx=20, pady=20)

    # Create a close button
    button = ttk.Button(popup, text="Zamknij", command=popup.destroy)
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

root = ThemedTk(theme="radiance")

root.title('ASKR')
root.geometry('600x600')

# Create Frame Model
settings_frame = ttk.Frame(root, width=580, height=150, relief='ridge', borderwidth=2)
settings_frame.grid(row=0, column=0, padx=10, pady=5, sticky='ew')

drive_frame = ttk.Frame(root, width=580, height=150, relief='ridge', borderwidth=2)
drive_frame.grid(row=1, column=0, padx=10, pady=5, sticky='ew')


func_frame = ttk.Frame(root, width=580, height=150, relief='ridge', borderwidth=2)
func_frame.grid(row=2, column=0, padx=10, pady=5, sticky='ew')
# Setting frame gutts
# ROW 0
ttk.Label(settings_frame, text='Ustawienia klienta', relief='sunken').grid(row=0, column=0, padx=2, pady=10, sticky='NW')
ttk.Label(settings_frame, text='PORT').grid(row=0, column=1, padx=20, pady=10)
ttk.Label(settings_frame, text='transmisja').grid(row=0, column=2, padx=20, pady=10)
ttk.Label(settings_frame, text='parzystość').grid(row=0, column=3, padx=20, pady=10)
ttk.Label(settings_frame, text='bity stopu').grid(row=0, column=4, padx=20, pady=10)

# ROW 1
# Block entry checkbox
block_var = tk.IntVar()
block_var.set(1)
block = ttk.Checkbutton(settings_frame, text='blokuj', variable=block_var, command=toggle_settings)
block.grid(row=1, column=0, padx=2, pady=10)
# tk.Label(settings_frame, text='blokuj').grid(row=1, column=0, padx=2, pady=10, sticky='W')

# Port entry
entry_port = tk.StringVar()
entry_port.set(cst.default_port)
port_en = ttk.Entry(settings_frame, textvariable=entry_port, width=8)
port_en.grid(row=1, column=1, padx=2, pady=10)
port_en.config(state='disabled')

# Baudrate entry
entry_baud = tk.IntVar()
entry_baud.set(cst.default_baudrate)
baud_en = ttk.Entry(settings_frame, textvariable=entry_baud, width=8)
baud_en.grid(row=1, column=2, padx=2, pady=10)
baud_en.config(state='disabled')

# Pairity entry
entry_pair = tk.StringVar()
entry_pair.set(cst.default_pairity)
pair_en = ttk.Entry(settings_frame, textvariable=entry_pair, width=8)
pair_en.grid(row=1, column=3, padx=2, pady=10)
pair_en.config(state='disabled')

# Stopbits entry
entry_stopb = tk.IntVar()
entry_stopb.set(cst.default_stopbits)
stopb_en = ttk.Entry(settings_frame, textvariable=entry_stopb, width=8)
stopb_en.grid(row=1, column=4, padx=2, pady=10)
stopb_en.config(state='disabled')

# ROW 2
# Connect button
conn_but = ttk.Button(settings_frame, text='POŁĄCZ', command=connect)
conn_but.grid(row=2, column=0, padx=2, pady=10)

# Connection status entry
connection_status = tk.StringVar()
connection_status.set('Sprawdź parametry klienta i naciśnij: POŁĄCZ')
connection_entry = ttk.Entry(settings_frame, textvariable=connection_status, width=50)
connection_entry.grid(row=2, column=1, columnspan=4, pady=10)

# Drive frame gutts
ttk.Label(drive_frame, text='Ustawienia napędu', relief='sunken').grid(row=0, column=0, padx=3, pady=10, sticky='w')
ttk.Label(drive_frame, text='slave').grid(row=0, column=1, padx=10, pady=10)
ttk.Label(drive_frame, text='prędkość docelowa').grid(row=0, column=2, padx=10, pady=10)
ttk.Label(drive_frame, text='rozpędzanie').grid(row=0, column=3, padx=10, pady=10)
ttk.Label(drive_frame, text='hamowanie').grid(row=0, column=4, padx=10, pady=10)


# Slave combo
slaves = [1, 2, 3, 4]
selected_slave = tk.IntVar()
selected_slave.set(slaves[0])
combo = ttk.Combobox(drive_frame, textvariable=selected_slave, values=slaves, width=5)
combo.grid(row=1, column=1, padx=10, pady=10)


# Set Button
set_but = ttk.Button(drive_frame, text='USTAW') #### Dodaj command
set_but.grid(row=1, column=0, padx=2, pady=10)

# Velocity
entry_vel = tk.IntVar()
entry_vel.set(cst.default_velocity)
velocity_en = ttk.Entry(drive_frame, textvariable=entry_vel, width=8)
velocity_en.grid(row=1, column=2, pady=10)

# Acceleration
entry_acc = tk.IntVar()
entry_acc.set(cst.default_acceleration)
acceleration_en = ttk.Entry(drive_frame, textvariable=entry_acc, width=8)
acceleration_en.grid(row=1, column=3, pady=10)

# Break
entry_break = tk.IntVar()
entry_break.set(cst.default_acceleration)
break_en = ttk.Entry(drive_frame, textvariable=entry_break, width=8)
break_en.grid(row=1, column=4, pady=10)



root.mainloop()