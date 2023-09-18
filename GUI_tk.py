import tkinter as tk
from ttkthemes import ThemedTk
from utility import labels as lbl
from utility import client_settup as cst

def connect():
    port = entry_port.get()
    baud = entry_baud.get()
    bytesize = 8
    pairity = entry_pair.get()
    stopbits = entry_stopb.get()
    print(f'port: {port}, baudrate: {baud}, bytesize: {bytesize}, pairity {pairity}, stop {stopbits}')

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




# Create Buttons,



root.mainloop()