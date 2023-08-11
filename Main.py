import subprocess
import customtkinter
import pandas as pd
import time

subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\BoltRefresh.py'])
df = pd.read_excel(r'C:\Users\Iago Piai\Desktop\StatusBolt\Main\BoltsOFF.xlsx')
df['Ultima Transmissão'] = pd.to_datetime(df['Ultima Transmissão'], format='%d/%m/%Y %H:%M')
df = df.sort_values(by='Ultima Transmissão', ascending=False)
max_empresa_lengths = df['Empresa'].apply(len)
df['Empresa'] = df.apply(lambda row: row['Empresa'].ljust(max_empresa_lengths.max()), axis=1)
df['custom_string'] = df['Empresa']
df['custom_data'] = df['Ultima Transmissão'].dt.strftime('%d/%m/%Y %H:%M')
custom_string_with_space = '\n\n'.join(df['custom_string'])
custom_data_with_space = '\n\n'.join(df['custom_data'])


customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")
button_font = ('Lexend', 13, 'bold')
tile_font = ('Lexend', 14, 'bold')

app = customtkinter.CTk()
app.geometry("880x730")

def refresh():
    subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\BoltRefresh.py'])
    df = pd.read_excel(r'C:\Users\Iago Piai\Desktop\StatusBolt\Main\BoltsOFF.xlsx')
    df['Ultima Transmissão'] = pd.to_datetime(df['Ultima Transmissão'], format='%d/%m/%Y %H:%M')
    df = df.sort_values(by='Ultima Transmissão', ascending=False)
    max_empresa_lengths = df['Empresa'].apply(len)
    df['Empresa'] = df.apply(lambda row: row['Empresa'].ljust(max_empresa_lengths.max()), axis=1)
    df['custom_string'] = df['Empresa'] + '                                ' + df['Ultima Transmissão'].dt.strftime('%d/%m/%Y %H:%M').str.ljust(16)
    custom_string_with_space = '\n\n'.join(df['custom_string'])
    textbox.delete("1.0", customtkinter.END)
    textbox.insert(customtkinter.END, custom_string_with_space)

# Functions
def button_callback():
    print("button pressed")

def auth_retina():
    subprocess.run(r'C:\Users\Iago Piai\Desktop\StatusBolt\Autorization.txt', shell=True)

def auth_infra_retina():
    subprocess.run(r'C:\Users\Iago Piai\Desktop\StatusBolt\Autorization_Infra.txt', shell=True)
    
def dir():
    subprocess.run(['explorer' ,r'C:\Users\Iago Piai\Desktop\StatusBolt'], shell=True)

def vscode():
    subprocess.run(r'C:\Users\Iago Piai\AppData\Local\Programs\Microsoft VS Code\Code.exe', shell=True)

def bolt_discord():
    subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\Bolt2.py'])

def ativos():
    subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\Ativos2.py'])

def BoltsOff():
    subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\BoltsOff.py'])

def TotalBolts():
    subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\TotalBolts.py'])

def pontos():
    subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\Position.py'])

def pontosoff():
    subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\PontosOFF.py'])

def recall():
    subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\Recall.py'])

def log_refresh():
    subprocess.run(['python', r'C:\Users\Iago Piai\PycharmProjects\Flame\venv\APPS\logrefresh.py'])

def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)

# Frame Textbox
textbox_frame = customtkinter.CTkFrame(app)
textbox_frame.grid(row=0, column=0, padx=10, pady=10)

# Frame Buttons
buttons_frame = customtkinter.CTkFrame(app)
buttons_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')

# Frame Under Text
under_text = customtkinter.CTkFrame(app)
under_text.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="w")

# Frame Under Buttons
under_buttons = customtkinter.CTkFrame(app)
under_buttons.grid(row=1, column=1, padx=10, pady=10, sticky="e")

# Layout
textbox = customtkinter.CTkTextbox(textbox_frame, font=button_font, corner_radius=4, height=220, width=300)
textbox.grid(row=1,column=0, padx=10, pady=10)

textbox = customtkinter.CTkTextbox(under_text, font=button_font, corner_radius=4, height=280, width=250)
textbox.grid(row=1, column=0, padx=10, pady=10)

textbox2 = customtkinter.CTkTextbox(under_text, font=button_font, corner_radius=4, height=280, width=200)
textbox2.grid(row=1, column=1, padx=10, pady=10)

tile_under_button_2 = customtkinter.CTkLabel(buttons_frame, text=' SCRIPTS ', font=tile_font, text_color="white", bg_color="gray32", padx=40, pady=(10))
tile_under_button_2.grid(row=0, column=0, columnspan=4,padx=15, pady=10, sticky="nsew")

tile_under_button_2 = customtkinter.CTkLabel(textbox_frame, text=' LOG ', font=tile_font, text_color="white", bg_color="gray32", padx=40, pady=(10))
tile_under_button_2.grid(row=0, column=0, columnspan=4,padx=10, pady=10,sticky="nsew")

tile_under_button_2 = customtkinter.CTkLabel(under_text, text=' BOLTS OFF ', font=tile_font, text_color="white", bg_color="gray32", padx=40, pady=(10))
tile_under_button_2.grid(row=0, column=0, columnspan=4,padx=10, pady=10,sticky="nsew")

button = customtkinter.CTkButton(buttons_frame, command=pontosoff, text='Pontos Off', height= 50, font = button_font,hover_color="dark gray", corner_radius=2)
button.grid(row=1, column=1, padx=15, pady=15)
button = customtkinter.CTkButton(buttons_frame, command=pontos, text='Pontos Total', height= 50, font = button_font,hover_color="dark gray", corner_radius=2)
button.grid(row=1, column=2, padx=15, pady=15)
button = customtkinter.CTkButton(buttons_frame, command=ativos, text='Pontos Log', height= 50, font = button_font,hover_color="dark gray", corner_radius=2)
button.grid(row=1, column=3, padx=15, pady=15)

# Pontos Buttons
button = customtkinter.CTkButton(buttons_frame, command=BoltsOff, text='Bolts Off', height= 50, font = button_font,hover_color="dark gray", corner_radius=2)
button.grid(row=2, column=1, padx=15, pady=15)
button = customtkinter.CTkButton(buttons_frame, command=TotalBolts, text='Bolts Total', height= 50, font = button_font,hover_color="dark gray", corner_radius=2)
button.grid(row=2, column=2, padx=15, pady=15)
button = customtkinter.CTkButton(buttons_frame, command=bolt_discord, text='Bolt Discord', height= 50, font = button_font,hover_color="dark gray", corner_radius=2)
button.grid(row=2, column=3, padx=15, pady=15)

# Gambiarras
button = customtkinter.CTkButton(buttons_frame, command=log_refresh, text='Log Refresh', height= 50, font = button_font,hover_color="dark gray", corner_radius=2)
button.grid(row=3, column=1, padx=15, pady=15)
button = customtkinter.CTkButton(buttons_frame, command=recall, text='Recall', height= 50, font = button_font,hover_color="dark gray", corner_radius=2)
button.grid(row=3, column=2, padx=15, pady=15)
button = customtkinter.CTkButton(buttons_frame, command=button_callback, text='Desenvolvimento', height= 50, font=button_font,hover_color="dark gray", corner_radius=2)
button.grid(row=3, column=3, padx=15, pady=15)
# End Buttons

# Options / Config
tile_under_button = customtkinter.CTkLabel(under_buttons, text=' CONFIG ', font=tile_font, text_color="white", padx=40, pady=(10), corner_radius=1, fg_color="gray32")
tile_under_button.grid(row=0, column=1, padx=15, pady=15)

tile_under_button = customtkinter.CTkLabel(under_buttons, text=' OPTIONS ', font=tile_font, text_color="white", padx=40, pady=(10), corner_radius=1, fg_color="gray32")
tile_under_button.grid(row=0, column=2, padx=15, pady=15)

button = customtkinter.CTkButton(under_buttons, command=auth_retina, text='Auth Retina', height= 28, font=button_font,hover_color="gray32", corner_radius=2, text_color='white', fg_color="dark gray")
button.grid(row=1, column=1, padx=15, pady=15)

button = customtkinter.CTkButton(under_buttons, command=auth_infra_retina, text='Auth Infra', height= 28, font=button_font, hover_color="gray32", corner_radius=2,text_color='white', fg_color="dark gray")
button.grid(row=2, column=1, padx=15, pady=15)

button = customtkinter.CTkButton(under_buttons, command=refresh, text='Refresh', height= 28, font=button_font, hover_color="gray32", corner_radius=2,text_color='white', fg_color="dark gray")
button.grid(row=3, column=1, padx=15, pady=15)

button = customtkinter.CTkButton(under_buttons, command=dir, text='Diretório', height= 28, font=button_font, hover_color="gray32", corner_radius=2,text_color='white', fg_color="dark gray")
button.grid(row=4, column=1, padx=15, pady=15)

button = customtkinter.CTkButton(under_buttons, command=vscode, text='Abrir Vscode : >', height= 28, font=button_font, hover_color="gray32", corner_radius=2,text_color='white', fg_color="dark gray")
button.grid(row=5, column=1, columnspan=4, sticky="nsew", padx=15, pady=15)

appearance_mode_label = customtkinter.CTkLabel(under_buttons, text="Appearance Mode:", anchor="w", font=button_font)
appearance_mode_label.grid(row=1, column=2,padx=15, pady=15)

appearance_mode_optionemenu = customtkinter.CTkOptionMenu(under_buttons, values=["Light", "Dark"],command=change_appearance_mode_event,font=button_font, corner_radius=2, fg_color='dark gray', text_color='white')
appearance_mode_optionemenu.grid(row=2, column=2, padx=15, pady=15)

scaling_label = customtkinter.CTkLabel(under_buttons, text="UI Scaling:", anchor="w", font=button_font)
scaling_label.grid(row=3, column=2, padx=15, pady=15)

scaling_optionemenu = customtkinter.CTkOptionMenu(under_buttons, values=["80%", "90%", "100%"],command=change_scaling_event, font=button_font, corner_radius=2, fg_color='dark gray', text_color='white')
scaling_optionemenu.grid(row=4, column=2, padx=15, pady=15)
# End Options / Config

# Progress Bar
sidebar_button_event = customtkinter.CTkProgressBar(app, height = 8)
sidebar_button_event.grid(row=3, column=0, columnspan=3,  padx=10, pady=10 ,sticky="nsew")

textbox.delete("1.0", customtkinter.END)
textbox.insert(customtkinter.END, custom_string_with_space)

textbox2.delete("1.0", customtkinter.END)
textbox2.insert(customtkinter.END, custom_data_with_space)

app.mainloop()

