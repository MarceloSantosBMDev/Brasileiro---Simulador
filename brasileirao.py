import tkinter as tk
import random as rm
import random
from tkinter import messagebox
import os
from tkinter import font as tkFont
from PIL import Image, ImageTk


apostas_usuario = []  # Armazena as apostas do usuário
idioma_selecionado = 'Português'
bet_mode = 0
usuario_logado = 'inexistente da silva'
fichas_usuario = 0
# Variáveis globais



def select_edition(edition):
    global edicao, times, confrontos, rodadas, rodada_atual, jogos_por_time
    edicao = edition
#vitorias em casa = 10
#derrotas em casa = 11
#vitorias como visitante = 12
#o stats de valor 12, é a odd que o time paga se ganhar o campeonato
    if edicao == 2024:
      times = {
    "Atlético-GO":  [0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0 ,5],
    "Athletico-PR": [0, 0, 0, 4, 0, 0, 0, 0, 0, 3, 0, 0, 7],
    "Atlético-MG":  [0, 0, 0, 5, 0, 0, 0, 0, 0, 3, 0, 0, 8],
    "Bahia":        [0, 0, 0, 5, 0, 0, 0, 0, 0, 4, 0, 0, 9],
    "Botafogo":     [0, 0, 0, 7, 0, 0, 0, 0, 0, 6, 0, 0, 13],
    "Corinthians": [0, 0, 0, 4, 0,0,0,0,0,3, 0, 0, 7],
    "Vitória": [0, 0, 0, 3, 0,0,0,0,0,2, 0, 0, 5],
    "Cruzeiro": [0, 0, 0, 4, 0,0,0,0,0,5, 0, 0, 9],
    "Cuiabá": [0, 0, 0, 2, 0,0,0,0,0,4, 0, 0, 6],
    "Flamengo": [0, 0, 0, 6, 0,0,0,0,0,5, 0, 0, 11],
    "Fluminense": [0, 0, 0, 3, 0,0,0,0,0,5, 0, 0, 8],
    "Fortaleza": [0, 0, 0, 5, 0,0,0,0,0,4, 0, 0, 9],
    "Juventude": [0, 0, 0, 4, 0,0,0,0,0,4, 0, 0, 8],
    "Grêmio": [0, 0, 0, 4, 0,0,0,0,0,4, 0, 0, 8],
    "Internacional": [0, 0, 0, 5, 0,0,0,0,0,6, 0, 0, 11],
    "Palmeiras": [0, 0, 0, 6, 0,0,0,0,0,7, 0, 0, 13],
    "RB Bragantino": [0, 0, 0, 4, 0,0,0,0,0,4, 0, 0, 8],
    "Criciúma": [0, 0, 0, 5, 0,0,0,0,0,2, 0, 0, 7],
    "São Paulo": [0, 0, 0, 5, 0,0,0,0,0,3, 0, 0, 8],
    "Vasco da Gama": [0, 0, 0, 4, 0,0,0,0,0,2, 0, 0, 6]
}
    elif edicao == 2025:
        times = {
    "Ceará-SC":  [0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 5],
    "Sport-Recife": [0, 0, 0, 4, 0, 0, 0, 0, 0, 3, 0, 0, 7],
    "Atlético-MG":  [0, 0, 0, 5, 0, 0, 0, 0, 0, 4, 0, 0, 9],
    "Bahia":        [0, 0, 0, 5, 0, 0, 0, 0, 0, 4, 0, 0, 9],
    "Botafogo":     [0, 0, 0, 6, 0, 0, 0, 0, 0, 5, 0, 0, 8],
    "Corinthians": [0, 0, 0, 6, 0,0,0,0,0,4, 0, 0, 10],
    "Vitória": [0, 0, 0, 4, 0,0,0,0,0,2, 0, 0, 6],
    "Cruzeiro": [0, 0, 0, 5, 0,0,0,0,0,3, 0, 0, 8],
    "Mirassol": [0, 0, 0, 4, 0,0,0,0,0,3, 0, 0, 7],
    "Flamengo": [0, 0, 0, 6, 0,0,0,0,0,5, 0, 0, 11],
    "Fluminense": [0, 0, 0, 4, 0,0,0,0,0,5, 0, 0, 9],
    "Fortaleza": [0, 0, 0, 5, 0,0,0,0,0,4, 0, 0, 9],
    "Juventude": [0, 0, 0, 3, 0,0,0,0,0,4, 0, 0, 7],
    "Grêmio": [0, 0, 0, 5, 0,0,0,0,0,4, 0, 0, 9],
    "Internacional": [0, 0, 0, 5, 0,0,0,0,0,5, 0, 0, 10],
    "Palmeiras": [0, 0, 0, 5, 0,0,0,0,0,6, 0, 0, 11],
    "RB Bragantino": [0, 0, 0, 3, 0,0,0,0,0,3, 0, 0, 6],
    "Santos": [0, 0, 0, 5, 0,0,0,0,0,3, 0, 0, 8],
    "São Paulo": [0, 0, 0, 5, 0,0,0,0,0,5, 0, 0, 10],
    "Vasco da Gama": [0, 0, 0, 4, 0,0,0,0,0,3, 0, 0, 7]
}    
    
    jogos_por_time = {time: [] for time in times.keys()} 
    confrontos = criar_jogos()     
    rodadas = total_rodadas
    rodada_atual = 0 
    root.destroy()
    start_simulation() 
    
    
total_rodadas = 38
def carregar_jogos(nome_arquivo="placares_jogos.txt"):
  
    global jogos_por_time
    jogos_por_time = {time: [] for time in times.keys()} 

    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(" ")
                if len(partes) == 5:
                    time1, gols_time1, _, gols_time2, time2 = partes
                    gols_time1 = int(gols_time1)
                    gols_time2 = int(gols_time2)
                    jogos_por_time[time1].append(f"{time1} {gols_time1} x {gols_time2} {time2}")
                    jogos_por_time[time2].append(f"{time2} {gols_time2} x {gols_time1} {time1}")

    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de placares não encontrado!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))



def criar_tela_jogos():
    tela_times = tk.Tk()
    tela_times.title("Escolha um Time")
    tela_times.geometry("600x600")
    tela_times.configure(bg="#2c3e50")  

    frame_principal = tk.Frame(tela_times, bg="#2c3e50")
    frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = tk.Canvas(frame_principal, width=560, height=560, bg="#2c3e50", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview, 
                             troughcolor="#34495e", bg="#2980b9", activebackground="#3498db")
    scrollbar.pack(side="right", fill="y")

    frame_times = tk.Frame(canvas, bg="#2c3e50")
    canvas.create_window((0, 0), window=frame_times, anchor="nw", width=540)
    
    frame_times.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.configure(yscrollcommand=scrollbar.set)

    def on_enter(e):
        e.widget["bg"] = "#2980b9"

    def on_leave(e):
        e.widget["bg"] = "#3498db"

    for time in times.keys():
        botao_time = tk.Button(frame_times, text=time, command=lambda t=time: mostrar_jogos(t),
                               width=40, bg="#3498db", fg="white", font=("Helvetica", 12, "bold"),
                               relief="flat", overrelief="raised", bd=0, activebackground="#2980b9",
                               cursor="hand2", pady=5)
        botao_time.pack(pady=5, padx=10, fill="x")
        botao_time.bind("<Enter>", on_enter)
        botao_time.bind("<Leave>", on_leave)

    tela_times.mainloop()


def mostrar_jogos(time):
    global label_aviso, times, jogos, max_jogos
    tela_jogos = tk.Tk()
    tela_jogos.title(f"Jogos de {time}")
    tela_jogos.geometry("500x600")
    tela_jogos.configure(bg="#2c3e50")  

    jogos = jogos_por_time.get(time, [])
    max_jogos = 38

    frame_jogos = tk.Frame(tela_jogos, bg="#2c3e50")
    frame_jogos.pack(pady=20, padx=20, fill="both", expand=True)

    canvas = tk.Canvas(frame_jogos, bg="#34495e", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_jogos, orient="vertical", command=canvas.yview, bg="#2980b9", troughcolor="#34495e")
    scrollable_frame = tk.Frame(canvas, bg="#34495e")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    if idioma_selecionado == "Português":
         label_aviso = tk.Label(
            tela_jogos,
           text=f"Total de jogos: {len(jogos)} (Máximo: {max_jogos})\n Posição do time: {times[time][4]}\n Vitorias em casa: {times[time][10]}\n Derrotas em casa: {times[time][11]}",
           font=("Helvetica", 10, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    elif idioma_selecionado == "Inglês":
             label_aviso = tk.Label(
            tela_jogos,
           text=f"Total of games: {len(jogos)} (Max: {max_jogos})\n Team position: {times[time][4]}\n Wins in house: {times[time][10]}\n Loses in house: {times[time][11]}",
           font=("Helvetica", 10, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    
    elif idioma_selecionado == "Alemão":
      label_aviso = tk.Label(
        tela_jogos,
        text=f"Gesamtzahl der Spiele: {len(jogos)} (Maximal: {max_jogos})\n Teamposition: {times[time][4]}\n Heimsiege: {times[time][10]}\n Heimniederlagen: {times[time][11]}",
        font=("Helvetica", 10, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    
    label_aviso.pack(pady=(20, 10))

    if not jogos:
        label_aviso.config(text="Nenhum jogo encontrado.", font=("Helvetica", 10, "italic"), fg="#e74c3e")

    if jogos:
        for i, jogo in enumerate(jogos[:max_jogos]):
            label_jogo = tk.Label(
                scrollable_frame,
                text=jogo,
                font=("Helvetica", 9),
                fg="#ecf0f1",
                bg="#34495e",
                anchor="w",
                padx=10,
                pady=3,
                bd=0,
                highlightthickness=0
            )
            label_jogo.pack(fill="x", pady=2)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    btn_fechar = tk.Button(
        tela_jogos,
        text="Fechar",
        command=tela_jogos.destroy,
        bg="#e74c3c",
        fg="white",
        font=("Helvetica", 10, "bold"),
        relief="flat",
        width=20,
        bd=0,
        activebackground="#c0392b"
    )
    btn_fechar.pack(pady=20)

    tela_jogos.mainloop()

def criar_jogos():
    global edicao
    if edicao == 2024:
        confrontoss = [
    ('Corinthians', 'São Paulo'), ('Palmeiras', 'Criciúma'), ('Vasco da Gama', 'RB Bragantino'), ('Atlético-GO', 'Internacional'), ('Athletico-PR', 'Grêmio'), ('Atlético-MG', 'Juventude'), ('Bahia', 'Fortaleza'), ('Botafogo', 'Fluminense'), ('Vitória', 'Flamengo'), ('Cruzeiro', 'Cuiabá'),
    ('Corinthians', 'Criciúma'), ('São Paulo', 'RB Bragantino'), ('Palmeiras', 'Internacional'), ('Vasco da Gama', 'Grêmio'), ('Atlético-GO', 'Juventude'), ('Athletico-PR', 'Fortaleza'), ('Atlético-MG', 'Fluminense'), ('Bahia', 'Flamengo'), ('Botafogo', 'Cuiabá'), ('Vitória', 'Cruzeiro'),
    ('Corinthians', 'RB Bragantino'), ('Criciúma', 'Internacional'), ('São Paulo', 'Grêmio'), ('Palmeiras', 'Juventude'), ('Vasco da Gama', 'Fortaleza'), ('Atlético-GO', 'Fluminense'), ('Athletico-PR', 'Flamengo'), ('Atlético-MG', 'Cuiabá'), ('Bahia', 'Cruzeiro'), ('Botafogo', 'Vitória'),
    ('Corinthians', 'Internacional'), ('RB Bragantino', 'Grêmio'), ('Criciúma', 'Juventude'), ('São Paulo', 'Fortaleza'), ('Palmeiras', 'Fluminense'), ('Vasco da Gama', 'Flamengo'), ('Atlético-GO', 'Cuiabá'), ('Athletico-PR', 'Cruzeiro'), ('Atlético-MG', 'Vitória'), ('Bahia', 'Botafogo'),
    ('Corinthians', 'Grêmio'), ('Internacional', 'Juventude'), ('RB Bragantino', 'Fortaleza'), ('Criciúma', 'Fluminense'), ('São Paulo', 'Flamengo'), ('Palmeiras', 'Cuiabá'), ('Vasco da Gama', 'Cruzeiro'), ('Atlético-GO', 'Vitória'), ('Athletico-PR', 'Botafogo'), ('Atlético-MG', 'Bahia'),
    ('Corinthians', 'Juventude'), ('Grêmio', 'Fortaleza'), ('Internacional', 'Fluminense'), ('RB Bragantino', 'Flamengo'), ('Criciúma', 'Cuiabá'), ('São Paulo', 'Cruzeiro'), ('Palmeiras', 'Vitória'), ('Vasco da Gama', 'Botafogo'), ('Atlético-GO', 'Bahia'), ('Athletico-PR', 'Atlético-MG'),
    ('Corinthians', 'Fortaleza'), ('Juventude', 'Fluminense'), ('Grêmio', 'Flamengo'), ('Internacional', 'Cuiabá'), ('RB Bragantino', 'Cruzeiro'), ('Criciúma', 'Vitória'), ('São Paulo', 'Botafogo'), ('Palmeiras', 'Bahia'), ('Vasco da Gama', 'Atlético-MG'), ('Atlético-GO', 'Athletico-PR'),
    ('Corinthians', 'Fluminense'), ('Fortaleza', 'Flamengo'), ('Juventude', 'Cuiabá'), ('Grêmio', 'Cruzeiro'), ('Internacional', 'Vitória'), ('RB Bragantino', 'Botafogo'), ('Criciúma', 'Bahia'), ('São Paulo', 'Atlético-MG'), ('Palmeiras', 'Athletico-PR'), ('Vasco da Gama', 'Atlético-GO'),
    ('Corinthians', 'Flamengo'), ('Fluminense', 'Cuiabá'), ('Fortaleza', 'Cruzeiro'), ('Juventude', 'Vitória'), ('Grêmio', 'Botafogo'), ('Internacional', 'Bahia'), ('RB Bragantino', 'Atlético-MG'), ('Criciúma', 'Athletico-PR'), ('São Paulo', 'Atlético-GO'), ('Palmeiras', 'Vasco da Gama'),
    ('Corinthians', 'Cuiabá'), ('Flamengo', 'Cruzeiro'), ('Fluminense', 'Vitória'), ('Fortaleza', 'Botafogo'), ('Juventude', 'Bahia'), ('Grêmio', 'Atlético-MG'), ('Internacional', 'Athletico-PR'), ('RB Bragantino', 'Atlético-GO'), ('Criciúma', 'Vasco da Gama'), ('São Paulo', 'Palmeiras'),
    ('Corinthians', 'Cruzeiro'), ('Cuiabá', 'Vitória'), ('Flamengo', 'Botafogo'), ('Fluminense', 'Bahia'), ('Fortaleza', 'Atlético-MG'), ('Juventude', 'Athletico-PR'), ('Grêmio', 'Atlético-GO'), ('Internacional', 'Vasco da Gama'), ('RB Bragantino', 'Palmeiras'), ('Criciúma', 'São Paulo'),
    ('Corinthians', 'Vitória'), ('Cruzeiro', 'Botafogo'), ('Cuiabá', 'Bahia'), ('Flamengo', 'Atlético-MG'), ('Fluminense', 'Athletico-PR'), ('Fortaleza', 'Atlético-GO'), ('Juventude', 'Vasco da Gama'), ('Grêmio', 'Palmeiras'), ('Internacional', 'São Paulo'), ('RB Bragantino', 'Criciúma'),
    ('Corinthians', 'Botafogo'), ('Vitória', 'Bahia'), ('Cruzeiro', 'Atlético-MG'), ('Cuiabá', 'Athletico-PR'), ('Flamengo', 'Atlético-GO'), ('Fluminense', 'Vasco da Gama'), ('Fortaleza', 'Palmeiras'), ('Juventude', 'São Paulo'), ('Grêmio', 'Criciúma'), ('Internacional', 'RB Bragantino'),
    ('Corinthians', 'Bahia'), ('Botafogo', 'Atlético-MG'), ('Vitória', 'Athletico-PR'), ('Cruzeiro', 'Atlético-GO'), ('Cuiabá', 'Vasco da Gama'), ('Flamengo', 'Palmeiras'), ('Fluminense', 'São Paulo'), ('Fortaleza', 'Criciúma'), ('Juventude', 'RB Bragantino'), ('Grêmio', 'Internacional'),
    ('Corinthians', 'Atlético-MG'), ('Bahia', 'Athletico-PR'), ('Botafogo', 'Atlético-GO'), ('Vitória', 'Vasco da Gama'), ('Cruzeiro', 'Palmeiras'), ('Cuiabá', 'São Paulo'), ('Flamengo', 'Criciúma'), ('Fluminense', 'RB Bragantino'), ('Fortaleza', 'Internacional'), ('Juventude', 'Grêmio'),
    ('Corinthians', 'Athletico-PR'), ('Atlético-MG', 'Atlético-GO'), ('Bahia', 'Vasco da Gama'), ('Botafogo', 'Palmeiras'), ('Vitória', 'São Paulo'), ('Cruzeiro', 'Criciúma'), ('Cuiabá', 'RB Bragantino'), ('Flamengo', 'Internacional'), ('Fluminense', 'Grêmio'), ('Fortaleza', 'Juventude'),
    ('Corinthians', 'Atlético-GO'), ('Athletico-PR', 'Vasco da Gama'), ('Atlético-MG', 'Palmeiras'), ('Bahia', 'São Paulo'), ('Botafogo', 'Criciúma'), ('Vitória', 'RB Bragantino'), ('Cruzeiro', 'Internacional'), ('Cuiabá', 'Grêmio'), ('Flamengo', 'Juventude'), ('Fluminense', 'Fortaleza'),
    ('Corinthians', 'Vasco da Gama'), ('Atlético-GO', 'Palmeiras'), ('Athletico-PR', 'São Paulo'), ('Atlético-MG', 'Criciúma'), ('Bahia', 'RB Bragantino'), ('Botafogo', 'Internacional'), ('Vitória', 'Grêmio'), ('Cruzeiro', 'Juventude'), ('Cuiabá', 'Fortaleza'), ('Flamengo', 'Fluminense'),
    ('Corinthians', 'Palmeiras'), ('Vasco da Gama', 'São Paulo'), ('Atlético-GO', 'Criciúma'), ('Athletico-PR', 'RB Bragantino'), ('Atlético-MG', 'Internacional'), ('Bahia', 'Grêmio'), ('Botafogo', 'Juventude'), ('Vitória', 'Fortaleza'), ('Cruzeiro', 'Fluminense'), ('Cuiabá', 'Flamengo'),
    ('São Paulo', 'Corinthians'), ('Criciúma', 'Palmeiras'), ('RB Bragantino', 'Vasco da Gama'), ('Internacional', 'Atlético-GO'), ('Grêmio', 'Athletico-PR'), ('Juventude', 'Atlético-MG'), ('Fortaleza', 'Bahia'), ('Fluminense', 'Botafogo'), ('Flamengo', 'Vitória'), ('Cuiabá', 'Cruzeiro'),
    ('Criciúma', 'Corinthians'), ('RB Bragantino', 'São Paulo'), ('Internacional', 'Palmeiras'), ('Grêmio', 'Vasco da Gama'), ('Juventude', 'Atlético-GO'), ('Fortaleza', 'Athletico-PR'), ('Fluminense', 'Atlético-MG'), ('Flamengo', 'Bahia'), ('Cuiabá', 'Botafogo'), ('Cruzeiro', 'Vitória'),
    ('RB Bragantino', 'Corinthians'), ('Internacional', 'Criciúma'), ('Grêmio', 'São Paulo'), ('Juventude', 'Palmeiras'), ('Fortaleza', 'Vasco da Gama'), ('Fluminense', 'Atlético-GO'), ('Flamengo', 'Athletico-PR'), ('Cuiabá', 'Atlético-MG'), ('Cruzeiro', 'Bahia'), ('Vitória', 'Botafogo'),
    ('Internacional', 'Corinthians'), ('Grêmio', 'RB Bragantino'), ('Juventude', 'Criciúma'), ('Fortaleza', 'São Paulo'), ('Fluminense', 'Palmeiras'), ('Flamengo', 'Vasco da Gama'), ('Cuiabá', 'Atlético-GO'), ('Cruzeiro', 'Athletico-PR'), ('Vitória', 'Atlético-MG'), ('Botafogo', 'Bahia'),
    ('Grêmio', 'Corinthians'), ('Juventude', 'Internacional'), ('Fortaleza', 'RB Bragantino'), ('Fluminense', 'Criciúma'), ('Flamengo', 'São Paulo'), ('Cuiabá', 'Palmeiras'), ('Cruzeiro', 'Vasco da Gama'), ('Vitória', 'Atlético-GO'), ('Botafogo', 'Athletico-PR'), ('Bahia', 'Atlético-MG'),
    ('Juventude', 'Corinthians'), ('Fortaleza', 'Grêmio'), ('Fluminense', 'Internacional'), ('Flamengo', 'RB Bragantino'), ('Cuiabá', 'Criciúma'), ('Cruzeiro', 'São Paulo'), ('Vitória', 'Palmeiras'), ('Botafogo', 'Vasco da Gama'), ('Bahia', 'Atlético-GO'), ('Atlético-MG', 'Athletico-PR'),
    ('Fortaleza', 'Corinthians'), ('Fluminense', 'Juventude'), ('Flamengo', 'Grêmio'), ('Cuiabá', 'Internacional'), ('Cruzeiro', 'RB Bragantino'), ('Vitória', 'Criciúma'), ('Botafogo', 'São Paulo'), ('Bahia', 'Palmeiras'), ('Atlético-MG', 'Vasco da Gama'), ('Athletico-PR', 'Atlético-GO'),
    ('Fluminense', 'Corinthians'), ('Flamengo', 'Fortaleza'), ('Cuiabá', 'Juventude'), ('Cruzeiro', 'Grêmio'), ('Vitória', 'Internacional'), ('Botafogo', 'RB Bragantino'), ('Bahia', 'Criciúma'), ('Atlético-MG', 'São Paulo'), ('Athletico-PR', 'Palmeiras'), ('Atlético-GO', 'Vasco da Gama'),
    ('Flamengo', 'Corinthians'), ('Cuiabá', 'Fluminense'), ('Cruzeiro', 'Fortaleza'), ('Vitória', 'Juventude'), ('Botafogo', 'Grêmio'), ('Bahia', 'Internacional'), ('Atlético-MG', 'RB Bragantino'), ('Athletico-PR', 'Criciúma'), ('Atlético-GO', 'São Paulo'), ('Vasco da Gama', 'Palmeiras'),
    ('Cuiabá', 'Corinthians'), ('Cruzeiro', 'Flamengo'), ('Vitória', 'Fluminense'), ('Botafogo', 'Fortaleza'), ('Bahia', 'Juventude'), ('Atlético-MG', 'Grêmio'), ('Athletico-PR', 'Internacional'), ('Atlético-GO', 'RB Bragantino'), ('Vasco da Gama', 'Criciúma'), ('Palmeiras', 'São Paulo'),
    ('Cruzeiro', 'Corinthians'), ('Vitória', 'Cuiabá'), ('Botafogo', 'Flamengo'), ('Bahia', 'Fluminense'), ('Atlético-MG', 'Fortaleza'), ('Athletico-PR', 'Juventude'), ('Atlético-GO', 'Grêmio'), ('Vasco da Gama', 'Internacional'), ('Palmeiras', 'RB Bragantino'), ('São Paulo', 'Criciúma'),
    ('Vitória', 'Corinthians'), ('Botafogo', 'Cruzeiro'), ('Bahia', 'Cuiabá'), ('Atlético-MG', 'Flamengo'), ('Athletico-PR', 'Fluminense'), ('Atlético-GO', 'Fortaleza'), ('Vasco da Gama', 'Juventude'), ('Palmeiras', 'Grêmio'), ('São Paulo', 'Internacional'), ('Criciúma', 'RB Bragantino'),
    ('Botafogo', 'Corinthians'), ('Bahia', 'Vitória'), ('Atlético-MG', 'Cruzeiro'), ('Athletico-PR', 'Cuiabá'), ('Atlético-GO', 'Flamengo'), ('Vasco da Gama', 'Fluminense'), ('Palmeiras', 'Fortaleza'), ('São Paulo', 'Juventude'), ('Criciúma', 'Grêmio'), ('RB Bragantino', 'Internacional'),
    ('Bahia', 'Corinthians'), ('Atlético-MG', 'Botafogo'), ('Athletico-PR', 'Vitória'), ('Atlético-GO', 'Cruzeiro'), ('Vasco da Gama', 'Cuiabá'), ('Palmeiras', 'Flamengo'), ('São Paulo', 'Fluminense'), ('Criciúma', 'Fortaleza'), ('RB Bragantino', 'Juventude'), ('Internacional', 'Grêmio'),
    ('Atlético-MG', 'Corinthians'), ('Athletico-PR', 'Bahia'), ('Atlético-GO', 'Botafogo'), ('Vasco da Gama', 'Vitória'), ('Palmeiras', 'Cruzeiro'), ('São Paulo', 'Cuiabá'), ('Criciúma', 'Flamengo'), ('RB Bragantino', 'Fluminense'), ('Internacional', 'Fortaleza'), ('Grêmio', 'Juventude'),
    ('Athletico-PR', 'Corinthians'), ('Atlético-GO', 'Atlético-MG'), ('Vasco da Gama', 'Bahia'), ('Palmeiras', 'Botafogo'), ('São Paulo', 'Vitória'), ('Criciúma', 'Cruzeiro'), ('RB Bragantino', 'Cuiabá'), ('Internacional', 'Flamengo'), ('Grêmio', 'Fluminense'), ('Juventude', 'Fortaleza'),
    ('Atlético-GO', 'Corinthians'), ('Vasco da Gama', 'Athletico-PR'), ('Palmeiras', 'Atlético-MG'), ('São Paulo', 'Bahia'), ('Criciúma', 'Botafogo'), ('RB Bragantino', 'Vitória'), ('Internacional', 'Cruzeiro'), ('Grêmio', 'Cuiabá'), ('Juventude', 'Flamengo'), ('Fortaleza', 'Fluminense'),
    ('Vasco da Gama', 'Corinthians'), ('Palmeiras', 'Atlético-GO'), ('São Paulo', 'Athletico-PR'), ('Criciúma', 'Atlético-MG'), ('RB Bragantino', 'Bahia'), ('Internacional', 'Botafogo'), ('Grêmio', 'Vitória'), ('Juventude', 'Cruzeiro'), ('Fortaleza', 'Cuiabá'), ('Fluminense', 'Flamengo'),
    ('Palmeiras', 'Corinthians'), ('São Paulo', 'Vasco da Gama'), ('Criciúma', 'Atlético-GO'), ('RB Bragantino', 'Athletico-PR'), ('Internacional', 'Atlético-MG'), ('Grêmio', 'Bahia'), ('Juventude', 'Botafogo'), ('Fortaleza', 'Vitória'), ('Fluminense', 'Cruzeiro'), ('Flamengo', 'Cuiabá')
]
    elif edicao == 2025:
        confrontoss=[
    ('Mirassol', 'Fluminense'), ('Vasco da Gama', 'Flamengo'), ('Ceará-SC', 'Fortaleza'), ('São Paulo', 'Santos'), ('Atlético-MG', 'Juventude'), ('Sport-Recife', 'Cruzeiro'), ('Bahia', 'Grêmio'), ('RB Bragantino', 'Vitória'), ('Botafogo', 'Internacional'), ('Palmeiras', 'Corinthians'),
    ('Mirassol', 'Flamengo'), ('Fluminense', 'Fortaleza'), ('Vasco da Gama', 'Santos'), ('Ceará-SC', 'Juventude'), ('São Paulo', 'Cruzeiro'), ('Atlético-MG', 'Grêmio'), ('Sport-Recife', 'Vitória'), ('Bahia', 'Internacional'), ('RB Bragantino', 'Corinthians'), ('Botafogo', 'Palmeiras'),
    ('Mirassol', 'Fortaleza'), ('Flamengo', 'Santos'), ('Fluminense', 'Juventude'), ('Vasco da Gama', 'Cruzeiro'), ('Ceará-SC', 'Grêmio'), ('São Paulo', 'Vitória'), ('Atlético-MG', 'Internacional'), ('Sport-Recife', 'Corinthians'), ('Bahia', 'Palmeiras'), ('RB Bragantino', 'Botafogo'),
    ('Mirassol', 'Santos'), ('Fortaleza', 'Juventude'), ('Flamengo', 'Cruzeiro'), ('Fluminense', 'Grêmio'), ('Vasco da Gama', 'Vitória'), ('Ceará-SC', 'Internacional'), ('São Paulo', 'Corinthians'), ('Atlético-MG', 'Palmeiras'), ('Sport-Recife', 'Botafogo'), ('Bahia', 'RB Bragantino'),
    ('Mirassol', 'Juventude'), ('Santos', 'Cruzeiro'), ('Fortaleza', 'Grêmio'), ('Flamengo', 'Vitória'), ('Fluminense', 'Internacional'), ('Vasco da Gama', 'Corinthians'), ('Ceará-SC', 'Palmeiras'), ('São Paulo', 'Botafogo'), ('Atlético-MG', 'RB Bragantino'), ('Sport-Recife', 'Bahia'),
    ('Mirassol', 'Cruzeiro'), ('Juventude', 'Grêmio'), ('Santos', 'Vitória'), ('Fortaleza', 'Internacional'), ('Flamengo', 'Corinthians'), ('Fluminense', 'Palmeiras'), ('Vasco da Gama', 'Botafogo'), ('Ceará-SC', 'RB Bragantino'), ('São Paulo', 'Bahia'), ('Atlético-MG', 'Sport-Recife'),
    ('Mirassol', 'Grêmio'), ('Cruzeiro', 'Vitória'), ('Juventude', 'Internacional'), ('Santos', 'Corinthians'), ('Fortaleza', 'Palmeiras'), ('Flamengo', 'Botafogo'), ('Fluminense', 'RB Bragantino'), ('Vasco da Gama', 'Bahia'), ('Ceará-SC', 'Sport-Recife'), ('São Paulo', 'Atlético-MG'),
    ('Mirassol', 'Vitória'), ('Grêmio', 'Internacional'), ('Cruzeiro', 'Corinthians'), ('Juventude', 'Palmeiras'), ('Santos', 'Botafogo'), ('Fortaleza', 'RB Bragantino'), ('Flamengo', 'Bahia'), ('Fluminense', 'Sport-Recife'), ('Vasco da Gama', 'Atlético-MG'), ('Ceará-SC', 'São Paulo'),
    ('Mirassol', 'Internacional'), ('Vitória', 'Corinthians'), ('Grêmio', 'Palmeiras'), ('Cruzeiro', 'Botafogo'), ('Juventude', 'RB Bragantino'), ('Santos', 'Bahia'), ('Fortaleza', 'Sport-Recife'), ('Flamengo', 'Atlético-MG'), ('Fluminense', 'São Paulo'), ('Vasco da Gama', 'Ceará-SC'),
    ('Mirassol', 'Corinthians'), ('Internacional', 'Palmeiras'), ('Vitória', 'Botafogo'), ('Grêmio', 'RB Bragantino'), ('Cruzeiro', 'Bahia'), ('Juventude', 'Sport-Recife'), ('Santos', 'Atlético-MG'), ('Fortaleza', 'São Paulo'), ('Flamengo', 'Ceará-SC'), ('Fluminense', 'Vasco da Gama'),
    ('Mirassol', 'Palmeiras'), ('Corinthians', 'Botafogo'), ('Internacional', 'RB Bragantino'), ('Vitória', 'Bahia'), ('Grêmio', 'Sport-Recife'), ('Cruzeiro', 'Atlético-MG'), ('Juventude', 'São Paulo'), ('Santos', 'Ceará-SC'), ('Fortaleza', 'Vasco da Gama'), ('Flamengo', 'Fluminense'),
    ('Mirassol', 'Botafogo'), ('Palmeiras', 'RB Bragantino'), ('Corinthians', 'Bahia'), ('Internacional', 'Sport-Recife'), ('Vitória', 'Atlético-MG'), ('Grêmio', 'São Paulo'), ('Cruzeiro', 'Ceará-SC'), ('Juventude', 'Vasco da Gama'), ('Santos', 'Fluminense'), ('Fortaleza', 'Flamengo'),
    ('Mirassol', 'RB Bragantino'), ('Botafogo', 'Bahia'), ('Palmeiras', 'Sport-Recife'), ('Corinthians', 'Atlético-MG'), ('Internacional', 'São Paulo'), ('Vitória', 'Ceará-SC'), ('Grêmio', 'Vasco da Gama'), ('Cruzeiro', 'Fluminense'), ('Juventude', 'Flamengo'), ('Santos', 'Fortaleza'),
    ('Mirassol', 'Bahia'), ('RB Bragantino', 'Sport-Recife'), ('Botafogo', 'Atlético-MG'), ('Palmeiras', 'São Paulo'), ('Corinthians', 'Ceará-SC'), ('Internacional', 'Vasco da Gama'), ('Vitória', 'Fluminense'), ('Grêmio', 'Flamengo'), ('Cruzeiro', 'Fortaleza'), ('Juventude', 'Santos'),
    ('Mirassol', 'Sport-Recife'), ('Bahia', 'Atlético-MG'), ('RB Bragantino', 'São Paulo'), ('Botafogo', 'Ceará-SC'), ('Palmeiras', 'Vasco da Gama'), ('Corinthians', 'Fluminense'), ('Internacional', 'Flamengo'), ('Vitória', 'Fortaleza'), ('Grêmio', 'Santos'), ('Cruzeiro', 'Juventude'),
    ('Mirassol', 'Atlético-MG'), ('Sport-Recife', 'São Paulo'), ('Bahia', 'Ceará-SC'), ('RB Bragantino', 'Vasco da Gama'), ('Botafogo', 'Fluminense'), ('Palmeiras', 'Flamengo'), ('Corinthians', 'Fortaleza'), ('Internacional', 'Santos'), ('Vitória', 'Juventude'), ('Grêmio', 'Cruzeiro'),
    ('Mirassol', 'São Paulo'), ('Atlético-MG', 'Ceará-SC'), ('Sport-Recife', 'Vasco da Gama'), ('Bahia', 'Fluminense'), ('RB Bragantino', 'Flamengo'), ('Botafogo', 'Fortaleza'), ('Palmeiras', 'Santos'), ('Corinthians', 'Juventude'), ('Internacional', 'Cruzeiro'), ('Vitória', 'Grêmio'),
    ('Mirassol', 'Ceará-SC'), ('São Paulo', 'Vasco da Gama'), ('Atlético-MG', 'Fluminense'), ('Sport-Recife', 'Flamengo'), ('Bahia', 'Fortaleza'), ('RB Bragantino', 'Santos'), ('Botafogo', 'Juventude'), ('Palmeiras', 'Cruzeiro'), ('Corinthians', 'Grêmio'), ('Internacional', 'Vitória'),
    ('Mirassol', 'Vasco da Gama'), ('Ceará-SC', 'Fluminense'), ('São Paulo', 'Flamengo'), ('Atlético-MG', 'Fortaleza'), ('Sport-Recife', 'Santos'), ('Bahia', 'Juventude'), ('RB Bragantino', 'Cruzeiro'), ('Botafogo', 'Grêmio'), ('Palmeiras', 'Vitória'), ('Corinthians', 'Internacional'),
    ('Fluminense', 'Mirassol'), ('Flamengo', 'Vasco da Gama'), ('Fortaleza', 'Ceará-SC'), ('Santos', 'São Paulo'), ('Juventude', 'Atlético-MG'), ('Cruzeiro', 'Sport-Recife'), ('Grêmio', 'Bahia'), ('Vitória', 'RB Bragantino'), ('Internacional', 'Botafogo'), ('Corinthians', 'Palmeiras'),
    ('Flamengo', 'Mirassol'), ('Fortaleza', 'Fluminense'), ('Santos', 'Vasco da Gama'), ('Juventude', 'Ceará-SC'), ('Cruzeiro', 'São Paulo'), ('Grêmio', 'Atlético-MG'), ('Vitória', 'Sport-Recife'), ('Internacional', 'Bahia'), ('Corinthians', 'RB Bragantino'), ('Palmeiras', 'Botafogo'),
    ('Fortaleza', 'Mirassol'), ('Santos', 'Flamengo'), ('Juventude', 'Fluminense'), ('Cruzeiro', 'Vasco da Gama'), ('Grêmio', 'Ceará-SC'), ('Vitória', 'São Paulo'), ('Internacional', 'Atlético-MG'), ('Corinthians', 'Sport-Recife'), ('Palmeiras', 'Bahia'), ('Botafogo', 'RB Bragantino'),
    ('Santos', 'Mirassol'), ('Juventude', 'Fortaleza'), ('Cruzeiro', 'Flamengo'), ('Grêmio', 'Fluminense'), ('Vitória', 'Vasco da Gama'), ('Internacional', 'Ceará-SC'), ('Corinthians', 'São Paulo'), ('Palmeiras', 'Atlético-MG'), ('Botafogo', 'Sport-Recife'), ('RB Bragantino', 'Bahia'),
    ('Juventude', 'Mirassol'), ('Cruzeiro', 'Santos'), ('Grêmio', 'Fortaleza'), ('Vitória', 'Flamengo'), ('Internacional', 'Fluminense'), ('Corinthians', 'Vasco da Gama'), ('Palmeiras', 'Ceará-SC'), ('Botafogo', 'São Paulo'), ('RB Bragantino', 'Atlético-MG'), ('Bahia', 'Sport-Recife'),
    ('Cruzeiro', 'Mirassol'), ('Grêmio', 'Juventude'), ('Vitória', 'Santos'), ('Internacional', 'Fortaleza'), ('Corinthians', 'Flamengo'), ('Palmeiras', 'Fluminense'), ('Botafogo', 'Vasco da Gama'), ('RB Bragantino', 'Ceará-SC'), ('Bahia', 'São Paulo'), ('Sport-Recife', 'Atlético-MG'),
    ('Grêmio', 'Mirassol'), ('Vitória', 'Cruzeiro'), ('Internacional', 'Juventude'), ('Corinthians', 'Santos'), ('Palmeiras', 'Fortaleza'), ('Botafogo', 'Flamengo'), ('RB Bragantino', 'Fluminense'), ('Bahia', 'Vasco da Gama'), ('Sport-Recife', 'Ceará-SC'), ('Atlético-MG', 'São Paulo'),
    ('Vitória', 'Mirassol'), ('Internacional', 'Grêmio'), ('Corinthians', 'Cruzeiro'), ('Palmeiras', 'Juventude'), ('Botafogo', 'Santos'), ('RB Bragantino', 'Fortaleza'), ('Bahia', 'Flamengo'), ('Sport-Recife', 'Fluminense'), ('Atlético-MG', 'Vasco da Gama'), ('São Paulo', 'Ceará-SC'),
    ('Internacional', 'Mirassol'), ('Corinthians', 'Vitória'), ('Palmeiras', 'Grêmio'), ('Botafogo', 'Cruzeiro'), ('RB Bragantino', 'Juventude'), ('Bahia', 'Santos'), ('Sport-Recife', 'Fortaleza'), ('Atlético-MG', 'Flamengo'), ('São Paulo', 'Fluminense'), ('Ceará-SC', 'Vasco da Gama'),
    ('Corinthians', 'Mirassol'), ('Palmeiras', 'Internacional'), ('Botafogo', 'Vitória'), ('RB Bragantino', 'Grêmio'), ('Bahia', 'Cruzeiro'), ('Sport-Recife', 'Juventude'), ('Atlético-MG', 'Santos'), ('São Paulo', 'Fortaleza'), ('Ceará-SC', 'Flamengo'), ('Vasco da Gama', 'Fluminense'),
    ('Palmeiras', 'Mirassol'), ('Botafogo', 'Corinthians'), ('RB Bragantino', 'Internacional'), ('Bahia', 'Vitória'), ('Sport-Recife', 'Grêmio'), ('Atlético-MG', 'Cruzeiro'), ('São Paulo', 'Juventude'), ('Ceará-SC', 'Santos'), ('Vasco da Gama', 'Fortaleza'), ('Fluminense', 'Flamengo'),
    ('Botafogo', 'Mirassol'), ('RB Bragantino', 'Palmeiras'), ('Bahia', 'Corinthians'), ('Sport-Recife', 'Internacional'), ('Atlético-MG', 'Vitória'), ('São Paulo', 'Grêmio'), ('Ceará-SC', 'Cruzeiro'), ('Vasco da Gama', 'Juventude'), ('Fluminense', 'Santos'), ('Flamengo', 'Fortaleza'),
    ('RB Bragantino', 'Mirassol'), ('Bahia', 'Botafogo'), ('Sport-Recife', 'Palmeiras'), ('Atlético-MG', 'Corinthians'), ('São Paulo', 'Internacional'), ('Ceará-SC', 'Vitória'), ('Vasco da Gama', 'Grêmio'), ('Fluminense', 'Cruzeiro'), ('Flamengo', 'Juventude'), ('Fortaleza', 'Santos'),
    ('Bahia', 'Mirassol'), ('Sport-Recife', 'RB Bragantino'), ('Atlético-MG', 'Botafogo'), ('São Paulo', 'Palmeiras'), ('Ceará-SC', 'Corinthians'), ('Vasco da Gama', 'Internacional'), ('Fluminense', 'Vitória'), ('Flamengo', 'Grêmio'), ('Fortaleza', 'Cruzeiro'), ('Santos', 'Juventude'),
    ('Sport-Recife', 'Mirassol'), ('Atlético-MG', 'Bahia'), ('São Paulo', 'RB Bragantino'), ('Ceará-SC', 'Botafogo'), ('Vasco da Gama', 'Palmeiras'), ('Fluminense', 'Corinthians'), ('Flamengo', 'Internacional'), ('Fortaleza', 'Vitória'), ('Santos', 'Grêmio'), ('Juventude', 'Cruzeiro'),
    ('Atlético-MG', 'Mirassol'), ('São Paulo', 'Sport-Recife'), ('Ceará-SC', 'Bahia'), ('Vasco da Gama', 'RB Bragantino'), ('Fluminense', 'Botafogo'), ('Flamengo', 'Palmeiras'), ('Fortaleza', 'Corinthians'), ('Santos', 'Internacional'), ('Juventude', 'Vitória'), ('Cruzeiro', 'Grêmio'),
    ('São Paulo', 'Mirassol'), ('Ceará-SC', 'Atlético-MG'), ('Vasco da Gama', 'Sport-Recife'), ('Fluminense', 'Bahia'), ('Flamengo', 'RB Bragantino'), ('Fortaleza', 'Botafogo'), ('Santos', 'Palmeiras'), ('Juventude', 'Corinthians'), ('Cruzeiro', 'Internacional'), ('Grêmio', 'Vitória'),
    ('Ceará-SC', 'Mirassol'), ('Vasco da Gama', 'São Paulo'), ('Fluminense', 'Atlético-MG'), ('Flamengo', 'Sport-Recife'), ('Fortaleza', 'Bahia'), ('Santos', 'RB Bragantino'), ('Juventude', 'Botafogo'), ('Cruzeiro', 'Palmeiras'), ('Grêmio', 'Corinthians'), ('Vitória', 'Internacional'),
    ('Vasco da Gama', 'Mirassol'), ('Fluminense', 'Ceará-SC'), ('Flamengo', 'São Paulo'), ('Fortaleza', 'Atlético-MG'), ('Santos', 'Sport-Recife'), ('Juventude', 'Bahia'), ('Cruzeiro', 'RB Bragantino'), ('Grêmio', 'Botafogo'), ('Vitória', 'Palmeiras'), ('Internacional', 'Corinthians')
]
        
        
        
        
        
    todososjogos = []
    for confrontos in confrontoss:
     todososjogos.append(confrontos)
    return todososjogos
    
def tela_inicial():
    global frame_times, labels_times, rodadas_label, btn_simular, rodadas, abrir_tela_jogos, label_introducao, label_pontos

    tela_inicial = tk.Tk()
    tela_inicial.configure(bg="#1c1c1c")  
    tela_inicial.title("Simulator Brasileirão")
    tela_inicial.attributes("-fullscreen", True)
    
    # Fontes personalizadas
    font_titulo = tkFont.Font(family="Arial", size=24, weight="bold")
    font_btn = tkFont.Font(family="Arial", size=14, weight="bold")
    font_texto = tkFont.Font(family="Arial", size=12)

    frame_cabecalho = tk.Frame(tela_inicial, bg="#2c3e50")
    frame_cabecalho.pack(fill="x", pady=10)

    label_introducao = tk.Label(frame_cabecalho, text="Bem-vindo ao Simulador de Brasileirão", bg="#2c3e50", fg="white", font=font_titulo)
    label_introducao.pack(pady=10)

    btn_fechar = tk.Button(frame_cabecalho, text=" X ", command=tela_inicial.destroy, bg="#ff5c5c", fg="white", font=font_btn, relief="flat")
    btn_fechar.pack(side="right", padx=10)

    btn_config = tk.Button(frame_cabecalho, text="⚙️", command=config_tela, bg="#ffba08", fg="black", font=font_btn, relief="flat")
    btn_config.pack(side="right", padx=10)

    frame_principal = tk.Frame(tela_inicial, bg="#1c1c1c")
    frame_principal.pack(fill="both", expand=True, padx=20, pady=10)

    frame_times = tk.Frame(frame_principal, bg="#2c2c2c", bd=2, relief="groove")
    frame_times.pack(fill="both", expand=True, pady=10)

    canvas = tk.Canvas(frame_times, bg="#2c2c2c", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_times, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#2c2c2c")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    labels_times = {}  # Dicionário para armazenar os labels dos times

    frame_info = tk.Frame(frame_principal, bg="#1c1c1c")
    frame_info.pack(fill="x", pady=10)
    
    rodadas_label = tk.Label(frame_info, text=f"Rodadas restantes: {rodadas}", bg="#1c1c1c", fg="#d3d3d3", font=font_texto)
    rodadas_label.pack(side="left", padx=10)
    
    if bet_mode == 1:
        label_pontos = tk.Label(frame_info, text=f"Fichas de {usuario_logado}: {fichas_usuario}", bg="#1c1c1c", fg="#d3d3d3", font=font_texto)
        label_pontos.pack(side="left", padx=10)


    frame_botoes = tk.Frame(frame_principal, bg="#1c1c1c")
    frame_botoes.pack(fill="x", pady=10)

    btn_simular = tk.Button(frame_botoes, text="Simular Próxima Rodada", command=simular_rodada, bg="#00aaff", fg="white", font=font_btn, bd=0, padx=20, pady=5)
    btn_simular.pack(side="left", padx=10, fill="x", expand=True)

    abrir_tela_jogos = tk.Button(frame_botoes, text="Abrir Tela de Jogos", command=criar_tela_jogos, bg="#ff8c42", fg="white", font=font_btn, bd=0, padx=20, pady=5)
    abrir_tela_jogos.pack(side="left", padx=10, fill="x", expand=True)

    if bet_mode == 1:
        btn_apostar = tk.Button(frame_botoes, text="Apostar em Jogos", bg="#2980b9", fg="white", font=font_btn, command=tela_escolher_jogos)
        btn_apostar.pack(side="left", padx=10, fill="x", expand=True)

    frame_rodape = tk.Frame(tela_inicial, bg="#2c3e50")
    frame_rodape.pack(fill="x", pady=10)

    label_rodape = tk.Label(frame_rodape, text="Desenvolvido por Marcelo", bg="#2c3e50", fg="white", font=font_texto)
    label_rodape.pack(pady=5)

    tela_inicial.mainloop()


def iniciar_simulacao(nome_arquivo="placares_jogos.txt"):
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print(f"Arquivo '{nome_arquivo}' excluído para nova simulação.")
iniciar_simulacao()



def organizar_tabela():
    global frame_times, label_time
 
   
    for widget in frame_times.winfo_children():
        widget.destroy()

    
    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)

   
    for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao  
        saldo_gols = stats[1] - stats[0] 

       
        if posicao <= 4:
            bg_color = "#2980b9"  
        elif posicao <= 6:
            bg_color = "#f39c12"  
        elif posicao <= 12:
            bg_color = "#27ae60"  
        elif posicao < 17:
            bg_color = "#1c1c1c"  
        else:
            bg_color = "#c0392b"  

        
        

       
        if idioma_selecionado == 'Inglês':
            texto_base = f"{posicao}º {time} | Games: {stats[8]} | Points: {stats[2]} | Wins: {stats[5]} | Draws: {stats[6]} | Loses: {stats[7]} | Goal difference: {saldo_gols} | Goals For: {stats[1]} | Goals Against: {stats[0]}"
        elif idioma_selecionado == 'Alemão':
            texto_base = f"{posicao}º {time} | Spiele: {stats[8]} | Punkte: {stats[2]} | Siege: {stats[5]} | Unentschieden: {stats[6]} | Niederlagen: {stats[7]} | Tordifferenz: {saldo_gols} | Tore: {stats[1]} | Gegentore: {stats[0]}"
        elif idioma_selecionado == 'Português':
            texto_base = f"{posicao}º {time} | Jogos: {stats[8]} | Pontos: {stats[2]} | Vitórias: {stats[5]} | Empates: {stats[6]} | Derrotas: {stats[7]} | Saldo: {saldo_gols} | Gols Feitos: {stats[1]} | Gols Tomados: {stats[0]}"
       
        label_time = tk.Label(
            frame_times,
            text=texto_base,
            bg=bg_color,
            fg="#ecf0f1", 
            font=("Helvetica", 10, "bold"),  
            padx=5,
            pady=2,
            relief="flat"
        )
        label_time.pack(anchor="w", fill="x", padx=5, pady=1)

        label_time.config(
            borderwidth=1,
            highlightbackground="#34495e",
            highlightcolor="#34495e",
            highlightthickness=1
        )
            
def parabenizar_campeao():
    global btn_simular
    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)
    if idioma_selecionado == 'Português':
      for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao
        if posicao == 1:
            messagebox.showinfo(
                title="Campeão definido",
                message=f"🎉 Parabéns! O campeão foi **{time}**! 🎉",
                icon='info'
            )
        btn_simular.config(
        text="Informações do campeonato",
        command=lambda: Informar(),
        bg='red',
        fg='white',  
        font=('Arial', 12, 'bold')
    )
    elif idioma_selecionado == 'Inglês':
      for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao
        if posicao == 1:
            messagebox.showinfo(
                title="Champion decided",
                message=f"🎉 Congratiulation! The Champion is **{time}**! 🎉",
                icon='info'
            )
        btn_simular.config(
        text="Champioship infomations",
        command=lambda: Informar(),
        bg='red',
        fg='white',  
        font=('Arial', 12, 'bold')
    )
    elif idioma_selecionado == 'Alemão':
     for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao
        if posicao == 1:
            messagebox.showinfo(
                title="Meister entschieden",
                message=f"🎉 Glückwunsch! Der Meister ist **{time}**! 🎉",
                icon='info'
            )
        btn_simular.config(
        text="Meisterschaftsinformationen",
        command=lambda: Informar(),
        bg='red',
        fg='white',  
        font=('Arial', 12, 'bold')
    )

"""def calcular_odd(time1, time2):
    odd = float
    if time1[12] > time2[12] - 1:
        odd = 1.7
    if time1[12] > time2[12] - 1:
        odd = 1.7
    m  if time1[12] > time2[12] - 1:
        odd = 1.7
"""

def Informar():
    tela_informativa = tk.Tk()
    tela_informativa.configure(bg="#2c3e50")  
    tela_informativa.title("Informações da Simulação")
    tela_informativa.geometry('600x600')  
    titulo = tk.Label(tela_informativa, text="Resultados da Simulação", bg="#2c3e50", fg="#ecf0f1", font=('Arial', 18, 'bold'))
    titulo.pack(pady=(20, 10))

    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)
    
    maiortomados = -1
    Golstomados = ""
    maior = -1  
    Artilheiro = ""
    maiorsaldo = -1
    saldoo = ""
    melhor_mandante = ""
    maior_mandante = -1
    for posicao, (time, stats) in enumerate(sorted_times, start=1):
        if stats[1] - stats[0] > maiorsaldo:
            maiorsaldo = stats[1] - stats[0]
            saldoo = time
        if stats[1] > maior: 
            maior = stats[1]
            Artilheiro = time  
        if stats[0] > maiortomados: 
            maiortomados = stats[0]
            Golstomados = time  
        if stats[10] > maior_mandante:
            maior_mandante = stats[10]
            melhor_mandante = time
    if idioma_selecionado == 'Português':
      for posicao, (time, stats) in enumerate(sorted_times, start=1):
        if posicao <= 4:
            label = tk.Label(tela_informativa, text=f"{posicao}° lugar: {time} com {stats[2]} pontos", bg="#27ae60", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))
        if posicao >= 17:
            label = tk.Label(tela_informativa, text=f"O time que caiu no Z{(21 - posicao)} foi o {time} com {stats[2]} pontos", bg="#e74c3c", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))
            
        
      stats_title = tk.Label(tela_informativa, text="Estatísticas Finais", bg="#34495e", fg="#ecf0f1", font=('Arial', 16, 'underline'))
      stats_title.pack(pady=(20, 10))
      
      labelArtilheiro = tk.Label(tela_informativa, text=f"O artilheiro do campeonato foi {Artilheiro} com {maior} gols", bg="#f39c12", fg="white", font=('Arial', 12))
      labelArtilheiro.pack(pady=(5, 5))
    
      labelTomados = tk.Label(tela_informativa, text=f"O time que tomou mais gols foi o {Golstomados} com {maiortomados} gols tomados", bg="#e67e22", fg="white", font=('Arial', 12))
      labelTomados.pack(pady=(5, 5))
    
      labelSaldo = tk.Label(tela_informativa, text=f"O time com maior saldo de gols foi {saldoo} com {maiorsaldo} de saldo de gols", bg="#8e44ad", fg="white", font=('Arial', 12))
      labelSaldo.pack(pady=(5, 5))
    
      labelMandante = tk.Label(tela_informativa, text=f"O time que ficou como melhor mandante foi {melhor_mandante} com {maior_mandante} vitórias em casa", bg="#2980b9", fg="white", font=('Arial', 12))
      labelMandante.pack(pady=(5, 5))

      fechar_btn = tk.Button(tela_informativa, text="Fechar", command=tela_informativa.destroy, bg="#c0392b", fg="white", font=('Arial', 12, 'bold'))
      fechar_btn.pack(pady=(20, 10))

      tela_informativa.mainloop()
    elif idioma_selecionado == 'Inglês':
        for posicao, (time, stats) in enumerate(sorted_times, start=1):
         if posicao <= 4:
            label = tk.Label(tela_informativa, text=f"{posicao}° place: {time} with {stats[2]} points", bg="#27ae60", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))
         if posicao >= 17:
           label = tk.Label(tela_informativa, text=f"The team that was relegated to Z{(21 - posicao)} was {time} with {stats[2]} points", bg="#e74c3c", fg="white", font=('Arial', 12))
           label.pack(pady=(5, 5))
        

        stats_title = tk.Label(tela_informativa, text="Final Statistics", bg="#34495e", fg="#ecf0f1", font=('Arial', 16, 'underline'))
        stats_title.pack(pady=(20, 10))

        labelArtilheiro = tk.Label(tela_informativa, text=f"The top scorer of the championship was {Artilheiro} with {maior} goals", bg="#f39c12", fg="white", font=('Arial', 12))
        labelArtilheiro.pack(pady=(5, 5))

        labelTomados = tk.Label(tela_informativa, text=f"The team that conceded the most goals was {Golstomados} with {maiortomados} goals conceded", bg="#e67e22", fg="white", font=('Arial', 12))
        labelTomados.pack(pady=(5, 5))

        labelSaldo = tk.Label(tela_informativa, text=f"The team with the best goal difference was {saldoo} with {maiorsaldo} goal difference", bg="#8e44ad", fg="white", font=('Arial', 12))
        labelSaldo.pack(pady=(5, 5))

        labelMandante = tk.Label(tela_informativa, text=f"The best home team was {melhor_mandante} with {maior_mandante} home wins", bg="#2980b9", fg="white", font=('Arial', 12))
        labelMandante.pack(pady=(5, 5))

        fechar_btn = tk.Button(tela_informativa, text="Close", command=tela_informativa.destroy, bg="#c0392b", fg="white", font=('Arial', 12, 'bold'))
        fechar_btn.pack(pady=(20, 10))

        tela_informativa.mainloop()

      
    if idioma_selecionado == 'Alemão':
          for posicao, (time, stats) in enumerate(sorted_times, start=1):
           if posicao <= 4:
            label = tk.Label(tela_informativa, text=f"{posicao}. Platz: {time} mit {stats[2]} Punkten", bg="#27ae60", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))

           if posicao >= 17:
            label = tk.Label(tela_informativa, text=f"Das Team, das in die Z{(21 - posicao)} abgestiegen ist, war {time} mit {stats[2]} Punkten", bg="#e74c3c", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))
    
          stats_title = tk.Label(tela_informativa, text="Endstatistiken", bg="#34495e", fg="#ecf0f1", font=('Arial', 16, 'underline'))
          stats_title.pack(pady=(20, 10))

          labelArtilheiro = tk.Label(tela_informativa, text=f"Der Torschützenkönig des Turniers war {Artilheiro} mit {maior} Toren", bg="#f39c12", fg="white", font=('Arial', 12))
          labelArtilheiro.pack(pady=(5, 5))
    
          labelTomados = tk.Label(tela_informativa, text=f"Das Team, das die meisten Gegentore kassiert hat, war {Golstomados} mit {maiortomados} Gegentoren", bg="#e67e22", fg="white", font=('Arial', 12))
          labelTomados.pack(pady=(5, 5))
    
          labelSaldo = tk.Label(tela_informativa, text=f"Das Team mit der besten Tordifferenz war {saldoo} mit {maiorsaldo} Toren", bg="#8e44ad", fg="white", font=('Arial', 12))
          labelSaldo.pack(pady=(5, 5))
    
          labelMandante = tk.Label(tela_informativa, text=f"Das beste Heimteam war {melhor_mandante} mit {maior_mandante} Heimsiegen", bg="#2980b9", fg="white", font=('Arial', 12))
          labelMandante.pack(pady=(5, 5))

          fechar_btn = tk.Button(tela_informativa, text="Schließen", command=tela_informativa.destroy, bg="#c0392b", fg="white", font=('Arial', 12, 'bold'))
          fechar_btn.pack(pady=(20, 10))

          tela_informativa.mainloop()

def Abrir_Perfil():
    global usuario_logado

    tela_de_perfil = tk.Toplevel()
    tela_de_perfil.title("User")
    tela_de_perfil.configure(bg="#2c3e50")
    tela_de_perfil.geometry('600x600')
    
    try:
        caminho_imagem = r"C:\Users\Marceloo\Desktop\python book\brasileira-sim\images\17004.png"
        imagem = Image.open(caminho_imagem)
        imagem = imagem.resize((100, 100), Image.Resampling.LANCZOS)  # Redimensiona a imagem
        foto = ImageTk.PhotoImage(imagem)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        foto = None
    
    if foto:
        label_imagem = tk.Label(tela_de_perfil, image=foto, bg='#2c3e50')
        label_imagem.image = foto  # Mantém uma referência para evitar que a imagem seja coletada pelo garbage collector
        label_imagem.pack(pady=(50, 10))
    else:
        label_erro = tk.Label(tela_de_perfil, text="Imagem não encontrada", fg="white", bg='#2c3e50')
        label_erro.pack(pady=(50, 10))
    
    label_nome_user = tk.Label(tela_de_perfil, text=f"Nome: {usuario_logado}", fg="white", bg='#2c3e50', font=('Arial', 12, 'bold'))
    label_nome_user.pack(pady=(5, 5))
    
    label_fixas_usuario = tk.Label(tela_de_perfil, text=f"Fixas: {fichas_usuario}", fg="white", bg='#2c3e50', font=('Arial', 12, 'bold'))
    label_fixas_usuario.pack(pady=(5, 5))
    tela_de_perfil.mainloop()


Abrir_Perfil()





def statsteams():
  if bet_mode == 0:
    global tela_times
    tela_times = tk.Toplevel()
    tela_times.title("Status dos Times")
    tela_times.configure(bg="#2c3e50")  
    tela_times.geometry("500x640")

    times_por_pagina = 5
    pagina_atual = [0]

    def exibir_times():
        global btn_anterior, btn_atualizar, btn_proximo
        for widget in tela_times.winfo_children():
            widget.destroy()

        inicio = pagina_atual[0] * times_por_pagina
        fim = inicio + times_por_pagina
        times_pagina = list(times.items())[inicio:fim]

        for nome_time, stats in times_pagina:
            frame_time = tk.Frame(tela_times, bg="#34495e")
            frame_time.pack(pady=5, padx=10, fill="x")

            tk.Label(frame_time, text=nome_time, bg="#34495e", fg="#ecf0f1", font=("Arial", 14, 'bold')).grid(row=0, column=0, sticky="w")
            if idioma_selecionado == "Português":
             tk.Label(frame_time, text="Ataque:", bg="#34495e", fg="white").grid(row=1, column=0, sticky="w")
             ataque = tk.Entry(frame_time, width=5)
             ataque.insert(0, stats[3])
             ataque.grid(row=1, column=1)

             tk.Label(frame_time, text="Defesa:", bg="#34495e", fg="white").grid(row=2, column=0, sticky="w")
             defesa = tk.Entry(frame_time, width=5)
             defesa.insert(0, stats[9])
             defesa.grid(row=2, column=1)

            elif idioma_selecionado == "Inglês":
                 tk.Label(frame_time, text="Attack:", bg="#34495e", fg="white").grid(row=1, column=0, sticky="w")
                 ataque = tk.Entry(frame_time, width=5)
                 ataque.insert(0, stats[3])
                 ataque.grid(row=1, column=1)

                 tk.Label(frame_time, text="Defense:", bg="#34495e", fg="white").grid(row=2, column=0, sticky="w")
                 defesa = tk.Entry(frame_time, width=5)
                 defesa.insert(0, stats[9])
                 defesa.grid(row=2, column=1)

            elif idioma_selecionado == "Alemão":
                 tk.Label(frame_time, text="Angriff:", bg="#34495e", fg="white").grid(row=1, column=0, sticky="w")
                 ataque = tk.Entry(frame_time, width=5)
                 ataque.insert(0, stats[3])
                 ataque.grid(row=1, column=1)

                 tk.Label(frame_time, text="Verteidigung:", bg="#34495e", fg="white").grid(row=2, column=0, sticky="w")
                 defesa = tk.Entry(frame_time, width=5)
                 defesa.insert(0, stats[9])
                 defesa.grid(row=2, column=1)

            global textt
            def atualizar_stats(nome=nome_time, atk_entry=ataque, def_entry=defesa):
                times[nome][3] = int(atk_entry.get())
                times[nome][9] = int(def_entry.get())
                if idioma_selecionado == 'Português':
                  times[nome][3] = int(atk_entry.get())
                  times[nome][9] = int(def_entry.get())
                  print(f"Time {nome}: Ataque = {times[nome][3]}, Defesa = {times[nome][9]}")
                elif idioma_selecionado == 'Inglês':
                  times[nome][3] = int(atk_entry.get())
                  times[nome][9] = int(def_entry.get())
                  print(f"Time {nome}: Attack = {times[nome][3]}, Defense = {times[nome][9]}")
                elif idioma_selecionado == "Alemão":
                  print(f"Mannschaft {nome}: Angriff = {times[nome][3]}, Verteidigung = {times[nome][9]}")
            if idioma_selecionado == 'Português':
             btn_atualizar = tk.Button(frame_time, text=f"Atualizar", command=atualizar_stats, bg="#f39c12", fg="black", font=("Arial", 10))
             btn_atualizar.grid(row=3, column=0, columnspan=2, pady=(5, 0))
            elif idioma_selecionado == 'Inglês':
             btn_atualizar = tk.Button(frame_time, text=f"Update", command=atualizar_stats, bg="#f39c12", fg="black", font=("Arial", 10))
             btn_atualizar.grid(row=3, column=0, columnspan=2, pady=(5, 0))  
            elif idioma_selecionado == "Alemão":
             btn_atualizar = tk.Button(frame_time, text=f"Aktualisieren", command=atualizar_stats, bg="#f39c12", fg="black", font=("Arial", 10))
             btn_atualizar.grid(row=3, column=0, columnspan=2, pady=(5, 0))    
                
        btn_frame = tk.Frame(tela_times, bg="#2c3e50")
        btn_frame.pack(pady=10)
        if idioma_selecionado == "Português":
          if pagina_atual[0] > 0:
            btn_anterior = tk.Button(btn_frame, text="Anterior", command=lambda: mudar_pagina(-1), bg="#2980b9", fg="white", font=("Arial", 12))
            btn_anterior.pack(side="left", padx=20)

          if fim < len(times):
            btn_proximo = tk.Button(btn_frame, text="Próximo", command=lambda: mudar_pagina(1), bg="#2980b9", fg="white", font=("Arial", 12))
            btn_proximo.pack(side="right", padx=20)
            
        if idioma_selecionado == "Inglês":
          if pagina_atual[0] > 0:
            btn_anterior = tk.Button(btn_frame, text="Previous", command=lambda: mudar_pagina(-1), bg="#2980b9", fg="white", font=("Arial", 12))
            btn_anterior.pack(side="left", padx=20)

          if fim < len(times):
            btn_proximo = tk.Button(btn_frame, text="Next", command=lambda: mudar_pagina(1), bg="#2980b9", fg="white", font=("Arial", 12))
            btn_proximo.pack(side="right", padx=20)
            
                   
        if idioma_selecionado == "Alemão":
          if pagina_atual[0] > 0:
           btn_anterior = tk.Button(btn_frame, text="Zurück", command=lambda: mudar_pagina(-1), bg="#2980b9", fg="white", font=("Arial", 12))
           btn_anterior.pack(side="left", padx=20)

          if fim < len(times):
              btn_proximo = tk.Button(btn_frame, text="Weiter", command=lambda: mudar_pagina(1), bg="#2980b9", fg="white", font=("Arial", 12))
              btn_proximo.pack(side="right", padx=20)

    def mudar_pagina(direcao):
        pagina_atual[0] += direcao
        exibir_times()

    exibir_times()
  else: 
    messagebox.showinfo(
                title="Impossivel alterar status",
                message=f"Impossivel alterar os status dos times com o modo aposta ativo",
                icon='info'
            )
    
def selecionar_linguagem():
    global idioma_selecionado
    
    tela_linguagem = tk.Toplevel()
    tela_linguagem.title("Seleção de Idioma")
    tela_linguagem.geometry("400x300")
    tela_linguagem.configure(bg="#2c3e50")
    
    lbl_instrucao = tk.Label(tela_linguagem, text="Escolha um idioma:", font=("Arial", 16), bg="#2c3e50", fg="#ecf0f1")
    lbl_instrucao.pack(pady=20)
    def definir_idioma(idioma):
        global idioma_selecionado
        idioma_selecionado = idioma
        if idioma == "Inglês":
            btn_config_teams.config(text="Change team status")
            btn_colocar_time_5.config(text="Status 5 in teams")
            btn_colocar_time_6.config(text="Randomize Status")
            btn_colocar_time_7.config(text="Language")
            labelconfig1.config(text="Settings")
            label_introducao.config(text="Welcome to Brasileirão Simulator")
            if rodada_atual == 38:
               btn_simular.config(text="Championship Information")
            else:
               btn_simular.config(text="Simulate next round")
            abrir_tela_jogos.config(text="Open match history screen")
            rodadas_label.config(text=f"Rounds remaining: {rodadas}")
            organizar_tabela()
        elif idioma == "Alemão":
            btn_config_teams.config(text="Team-Status ändern")
            btn_colocar_time_5.config(text="Status 5 in Teams")
            btn_colocar_time_6.config(text="Status randomisieren")
            btn_colocar_time_7.config(text="Sprache")
            labelconfig1.config(text="Einstellungen")
            label_introducao.config(text="Willkommen im Brasileirão-Simulator")
            if rodada_atual == 38:
              btn_simular.config(text="Meisterschaftsinformationen")
            else:
              btn_simular.config(text="Nächste Runde simulieren")
            abrir_tela_jogos.config(text="Öffnen Sie die Spielbildschirme")
            rodadas_label.config(text=f"verbleibende Runden: {rodadas}")
            organizar_tabela()
        elif idioma == "Português":
            btn_config_teams.config(text="Mudar status dos times")
            btn_colocar_time_5.config(text="Status 5 em times")
            btn_colocar_time_6.config(text="Randomizar Status")
            btn_colocar_time_7.config(text="Linguagem")
            labelconfig1.config(text="Configurações")
            label_introducao.config(text="Bem-vindo ao Simulador de Brasileirão")
            if rodada_atual == 38:
               btn_simular.config(text="Informações do campeonato")
            else:
               btn_simular.config(text="Simular proxima rodada")
            abrir_tela_jogos.config(text="Abrir telas De Jogos")
            rodadas_label.config(text=f"Rodadas restantes: {rodadas}")
            organizar_tabela()
        tela_linguagem.destroy()
        fechar_tela_times()
        
        
    idiomas = ["Inglês", "Português", "Alemão"]
    for idioma in idiomas:
        btn = tk.Button(tela_linguagem, text=idioma, command=lambda i=idioma: [definir_idioma(i), organizar_tabela()],
                        bg="#2980b9", fg="white", font=("Arial", 14), relief="solid", bd=2)
        btn.pack(pady=10, fill="x", padx=40)
        

def config_tela():
    global tela_configuracao, btn_config_teams, labelconfig1, btn_colocar_time_5, btn_colocar_time_6, btn_colocar_time_7
        
        
    tela_configuracao = tk.Toplevel()
    tela_configuracao.configure(bg="#2c3e50")  
    tela_configuracao.title("Configurações")
    tela_configuracao.geometry('500x500')
    
    labelconfig1 = tk.Label(tela_configuracao, text="Configurações", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 24, 'bold'))
    labelconfig1.pack(pady=20)
    
    btn_config_teams = tk.Button(tela_configuracao, text="Mudar status dos times", bg="#2980b9", fg="white", font=("Arial", 14), command=statsteams)
    btn_config_teams.pack(pady=20)
    
    btn_colocar_time_5 = tk.Button(tela_configuracao, text="Status 5 em times", bg="#2980b9", fg="white", font=("Arial", 14), command=stats5teams)
    btn_colocar_time_5.pack(pady=20)
    
    btn_colocar_time_6 = tk.Button(tela_configuracao, text="Randomizar Status", bg="#2980b9", fg="white", font=("Arial", 14), command=randomizestats)
    btn_colocar_time_6.pack(pady=20)
    
    btn_colocar_time_7 = tk.Button(tela_configuracao, text="Linguagem", bg="#2980b9", fg="white", command=selecionar_linguagem, font=("Arial", 14))
    btn_colocar_time_7.pack(pady=20)
    if idioma_selecionado == "Inglês":
         btn_config_teams.config(text="Change team status")
         btn_colocar_time_5.config(text="Status 5 in teams")
         btn_colocar_time_6.config(text="Randomize Status")
         btn_colocar_time_7.config(text="Language")
         labelconfig1.config(text="Settings")
         label_introducao.config(text="Welcome to Brasileirão Simulator")
         if rodada_atual == 38:
          btn_simular.config(text="Championship Information")
         else:
          btn_simular.config(text="Simulate next round")
         abrir_tela_jogos.config(text="Open match history screen")
         rodadas_label.config(text=f"Rounds remaining: {rodadas}")
    elif idioma_selecionado == "Alemão":
        btn_config_teams.config(text="Team-Status ändern")
        btn_colocar_time_5.config(text="Status 5 in Teams")
        btn_colocar_time_6.config(text="Status randomisieren")
        btn_colocar_time_7.config(text="Sprache")
        labelconfig1.config(text="Einstellungen")
        label_introducao.config(text="Willkommen im Brasileirão-Simulator")
        if rodada_atual == 38:
              btn_simular.config(text="Meisterschaftsinformationen")
        else:
              btn_simular.config(text="Nächste Runde simulieren")
        abrir_tela_jogos.config(text="Öffnen Sie die Spielbildschirme")
        rodadas_label.config(text=f"verbleibende Runden: {rodadas}")
    elif idioma_selecionado == "Português":
        btn_colocar_time_5.config(text="Status 5 em times")
        btn_colocar_time_6.config(text="Randomizar Status")
        btn_colocar_time_7.config(text="Linguagem")
        labelconfig1.config(text="Configurações")
        label_introducao.config(text="Bem-vindo ao Simulador de Brasileirão")
        btn_simular.config(text="Simular Proxima Rodada")
        abrir_tela_jogos.config(text="Abrir telas De Jogos")
        rodadas_label.config(text=f"Rodadas restantes: {rodadas}")
        

    tela_configuracao.mainloop()

def randomizestats():
    global times
    for team, stats in times.items():
        stats[3] = random.randint(1, 10)
        stats[9] = random.randint(1, 10)
        print(f"{team} updated - Attack: {stats[3]}, Defense: {stats[9]}")

def stats5teams():
    global times
    for team, stats in times.items():
        stats[3] = 5  
        stats[9] = 5 
        print(f"{team} updated - Attack: {stats[3]}, Defense: {stats[9]}")


def start_simulation():
    if bet_mode == 1: 
        tela_login()  
    else:
        tela_inicial() 

def fechar_tela_times():
    global tela_times
    if tela_times is not None and tela_times.winfo_exists(): 
        tela_times.destroy()  
        tela_times = None 

def toggle_bet_mode():
    global bet_mode
    bet_mode = 1 if bet_mode == 0 else 0
    btn_modo_aposta.config(text="Modo Aposta: ATIVADO" if bet_mode else "Modo Aposta: DESATIVADO")



jogos_selecionados = []



global Label_escolha_edicao
def tela_selecao_edicao():
    global root, btn_modo_aposta

    root = tk.Tk()
    root.title("Seleção de Edição")
    root.geometry("500x400")
    root.configure(bg="#2c3e50")

    font_titulo = tkFont.Font(family="Arial", size=18, weight="bold")
    font_btn = tkFont.Font(family="Arial", size=14, weight="bold")

    frame_central = tk.Frame(root, bg="#2c3e50")
    frame_central.pack(expand=True, pady=20)

    tk.Label(frame_central, text="Escolha a Edição do Campeonato:", bg="#2c3e50", fg="#ecf0f1", font=font_titulo).pack(pady=20)

    btn_2024 = tk.Button(frame_central, text="2024", font=font_btn, bg="#27AE60", fg="white", width=15, bd=0, relief="flat", command=lambda: select_edition(2024))
    btn_2024.pack(pady=10, ipady=5)
    btn_2024.config(highlightbackground="#27AE60", highlightthickness=2, highlightcolor="#27AE60", bd=0)

    btn_2025 = tk.Button(frame_central, text="2025", font=font_btn, bg="#E74C3C", fg="white", width=15, bd=0, relief="flat", command=lambda: select_edition(2025))
    btn_2025.pack(pady=10, ipady=5)
    btn_2025.config(highlightbackground="#E74C3C", highlightthickness=2, highlightcolor="#E74C3C", bd=0)

    btn_modo_aposta = tk.Button(frame_central, text="Modo Aposta: DESATIVADO", font=font_btn, bg="#2980b9", fg="white", width=25, bd=0, relief="flat", command=toggle_bet_mode)
    btn_modo_aposta.pack(pady=20, ipady=5)
    btn_modo_aposta.config(highlightbackground="#2980b9", highlightthickness=2, highlightcolor="#2980b9", bd=0)

    canvas = tk.Canvas(root, width=500, height=400, bg="#2c3e50", highlightthickness=0)
    canvas.create_rectangle(0, 0, 500, 400, fill="#2c3e50", outline="#2c3e50")
    canvas.create_rectangle(0, 0, 500, 200, fill="#34495e", outline="#34495e")
    canvas.pack()

    root.mainloop()

import random as rm

def simular_jogo(time1, time2, nome_arquivo="placares_jogos.txt"):
    chances_time1 = times[time1][3]  
    chances_time2 = times[time2][3]  
    gols_defendidos1 = times[time1][9]
    gols_defendidos2 = times[time2][9]
#here I add inspiration method, the team have 1% of chance of have each stats to 8
    if rm.random() <= 0.02:
        inspirationatack1 = chances_time1 * 2
        inspirationdefense1 = gols_defendidos1 * 2
        chances_time1 = inspirationatack1
        gols_defendidos1 = inspirationdefense1
        print(f"o time {time1} se inpirou na rodada {rodada_atual}")

    if rm.random() <= 0.01:
        inspirationatack2 = chances_time1 * 2
        inspirationdefense2 = gols_defendidos1 * 2
        chances_time2 = inspirationatack2
        gols_defendidos2 = inspirationdefense2
        print(f"o time {time2} se inpirou na rodada {rodada_atual}")

    gols_time1 = 0
    gols_time2 = 0
    defesas1 = 0
    defesas2 = 0

    for _ in range(chances_time1):
        if rm.choices([True, False], weights=[0.35, 0.65])[0]:  
            gols_time1 += 1

    for _ in range(chances_time2):
        if rm.choices([True, False], weights=[0.30, 0.70])[0]: 
            gols_time2 += 1

    for _ in range(gols_defendidos1):
        if rm.choices([True, False], weights=[0.2, 0.8])[0]:  
            defesas1 += 1

    for _ in range(gols_defendidos2):
        if rm.choices([True, False], weights=[0.15, 0.85])[0]: 
            defesas2 += 1

    if gols_time1 == 0:
        defesas2 = 0
    if gols_time2 == 0:
        defesas1 = 0

    gols_time1 = max(0, gols_time1 - defesas2)
    gols_time2 = max(0, gols_time2 - defesas1)

    times[time1][1] += gols_time1  
    times[time1][0] += gols_time2  
    times[time2][1] += gols_time2  
    times[time2][0] += gols_time1  

    if gols_time1 > gols_time2:
        times[time1][10] += 1
        times[time1][2] += 3  
        times[time1][5] += 1  
        times[time2][7] += 1  
    elif gols_time1 < gols_time2:
        times[time1][11] += 1
        times[time2][2] += 3  
        times[time2][5] += 1  
        times[time1][7] += 1 
    else:
        times[time1][2] += 1  
        times[time2][2] += 1  
        times[time1][6] += 1  
        times[time2][6] += 1  

    times[time1][8] += 1  
    times[time2][8] += 1  

    with open(nome_arquivo, "a") as arquivo:
        resultado = f"{time1} {gols_time1} x {gols_time2} {time2}\n"
        arquivo.write(resultado)

    resultado_time1 = f"{time1} {gols_time1} x {gols_time2} {time2}"
    resultado_time2 = f"{time1} {gols_time1} x {gols_time2} {time2}"
    jogos_por_time[time2].append(resultado_time1)
    jogos_por_time[time1].append(resultado_time2)


def organizar_tabela():
    global frame_times, label_time
 
   
    for widget in frame_times.winfo_children():
        widget.destroy()

    
    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)

   
    for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao  
        saldo_gols = stats[1] - stats[0] 

       
        if posicao <= 4:
            bg_color = "#2980b9"  
        elif posicao <= 6:
            bg_color = "#f39c12"  
        elif posicao <= 12:
            bg_color = "#27ae60"  
        elif posicao < 17:
            bg_color = "#1c1c1c"  
        else:
            bg_color = "#c0392b"  

        
        

       
        if idioma_selecionado == 'Inglês':
            texto_base = f"{posicao}º {time} | Games: {stats[8]} | Points: {stats[2]} | Wins: {stats[5]} | Draws: {stats[6]} | Loses: {stats[7]} | Goal difference: {saldo_gols} | Goals For: {stats[1]} | Goals Against: {stats[0]}"
        elif idioma_selecionado == 'Alemão':
            texto_base = f"{posicao}º {time} | Spiele: {stats[8]} | Punkte: {stats[2]} | Siege: {stats[5]} | Unentschieden: {stats[6]} | Niederlagen: {stats[7]} | Tordifferenz: {saldo_gols} | Tore: {stats[1]} | Gegentore: {stats[0]}"
        elif idioma_selecionado == 'Português':
            texto_base = f"{posicao}º {time} | Jogos: {stats[8]} | Pontos: {stats[2]} | Vitórias: {stats[5]} | Empates: {stats[6]} | Derrotas: {stats[7]} | Saldo: {saldo_gols} | Gols Feitos: {stats[1]} | Gols Tomados: {stats[0]}"
       
        label_time = tk.Label(
            frame_times,
            text=texto_base,
            bg=bg_color,
            fg="#ecf0f1", 
            font=("Helvetica", 10, "bold"),  
            padx=5,
            pady=2,
            relief="flat"
        )
        label_time.pack(anchor="w", fill="x", padx=5, pady=1)

        label_time.config(
            borderwidth=1,
            highlightbackground="#34495e",
            highlightcolor="#34495e",
            highlightthickness=1
        )


def atualizar_fichas_usuario(nome, novas_fichas):
    """Atualiza as fichas do usuário no arquivo."""
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("usuarios.txt", "w") as arquivo:
        for linha in linhas:
            dados = linha.strip().split(":")
            if dados[0] == nome:
                arquivo.write(f"{dados[0]}:{dados[1]}:{novas_fichas}\n")  # Atualizar as fichas
            else:
                arquivo.write(linha)


def comparar_apostas_com_resultados():
    global apostas_usuario, fichas_usuario

    resultados = []

    with open("placares_jogos.txt", "r") as arquivo:
        linhas = [linha.strip() for linha in arquivo.readlines()]

    resultados_dict = {}
    for linha in linhas:
        
        if "x" in linha.lower(): 
            partes = linha.split()
            try:
                indice_x = partes.index("x") if "x" in partes else partes.index("X")
                time1 = " ".join(partes[:indice_x - 1]).strip()  # Nome do time 1
                gols_time1 = int(partes[indice_x - 1])           # Gols do time 1
                gols_time2 = int(partes[indice_x + 1])           # Gols do time 2
                time2 = " ".join(partes[indice_x + 2:]).strip()  # Nome do time 2

                resultados_dict[(time1, time2)] = (gols_time1, gols_time2)
                resultados_dict[(time2, time1)] = (gols_time2, gols_time1) 
            except (ValueError, IndexError):
                continue  

    
    for aposta in apostas_usuario:
        time1, time2, aposta_escolhida, fichas_apostadas = aposta["time1"], aposta["time2"], aposta["aposta"], aposta["fichas"]

        if (time1, time2) in resultados_dict:
            gols_time1, gols_time2 = resultados_dict[(time1, time2)]

            if (gols_time1 > gols_time2 and aposta_escolhida == time1) or \
               (gols_time2 > gols_time1 and aposta_escolhida == time2) or \
               (gols_time1 == gols_time2 and aposta_escolhida == "empate"):
                resultado = "ganhou"
                fichas_usuario += fichas_apostadas  # Usuário ganha a aposta
            else:
                resultado = "perdeu"
                fichas_usuario -= fichas_apostadas  # Usuário perde a aposta

            resultados.append(f"{time1} {gols_time1} x {gols_time2} {time2} - Você {resultado} {fichas_apostadas} fichas.")
        else:
            resultados.append(f"{time1} x {time2} - Resultado não encontrado.")

    messagebox.showinfo("Resultados das Apostas", "\n".join(resultados) if resultados else "Nenhuma aposta foi processada.")

    atualizar_fichas_usuario(usuario_logado, fichas_usuario)
    label_pontos.config(text=f"Fichas de {usuario_logado}: {fichas_usuario}")

    apostas_usuario.clear()

    messagebox.showinfo("Saldo Atual", f"Seu saldo atual é de {fichas_usuario} fichas.")




def simular_rodada():
    global rodadas, rodada_atual, fichas_usuario

    if rodada_atual < total_rodadas:
        with open("placares_jogos.txt", "a") as arquivo:
            arquivo.write(f"Rodada {rodada_atual + 1}\n")
        
        for i in range(10): 
            index = rodada_atual * 10 + i
            if index < len(confrontos):
                time1, time2 = confrontos[index]
                simular_jogo(time1, time2)
        
        organizar_tabela()
        rodada_atual += 1
        rodadas -= 1

        if idioma_selecionado == 'Português':
            rodadas_label.config(text=f"Rodadas restantes: {rodadas}")
        elif idioma_selecionado == 'Inglês':
            rodadas_label.config(text=f"Rounds remaining: {rodadas}")
        elif idioma_selecionado == 'Alemão':
            rodadas_label.config(text=f"verbleibende Runden: {rodadas}")
        
        if rodadas == 0:
            parabenizar_campeao()
            if idioma_selecionado == 'Português':
                btn_simular.config(text="Informações do campeonato", command=Informar, bg='red', fg='white', font=('Arial', 12, 'bold'))
            elif idioma_selecionado == 'Inglês':
                btn_simular.config(text="Championship information", command=Informar, bg='red', fg='white', font=('Arial', 12, 'bold'))
            elif idioma_selecionado == 'Alemão':
                btn_simular.config(text="Meisterschaftsinformationen", command=Informar, bg='red', fg='white', font=('Arial', 12, 'bold'))

        if bet_mode == 1 and apostas_usuario:
            comparar_apostas_com_resultados()
    else:
        messagebox.showinfo("Fim do Campeonato", "O campeonato chegou ao fim!")
        


def tela_escolher_jogos():
    """Tela para o usuário escolher em quais jogos deseja apostar."""
    global jogos_selecionados

    tela_escolha = tk.Toplevel()
    tela_escolha.title("Escolher Jogos para Apostar")
    tela_escolha.geometry("400x600")
    tela_escolha.configure(bg="#2c3e50")

    font_label = tkFont.Font(family="Arial", size=12)
    font_btn = tkFont.Font(family="Arial", size=12, weight="bold")

    tk.Label(tela_escolha, text="Selecione os jogos para apostar:", bg="#2c3e50", fg="#ecf0f1", font=font_label).pack(pady=10)

    frame_jogos = tk.Frame(tela_escolha, bg="#2c3e50")
    frame_jogos.pack(fill="both", expand=True)

    # Variáveis para armazenar as seleções
    selecoes = []
    for i in range(10):
        index = rodada_atual * 10 + i
        if index >= len(confrontos):
            break

        time1, time2 = confrontos[index]
        var = tk.BooleanVar(value=False)  # Checkbox para selecionar o jogo
        selecoes.append((time1, time2, var))

        frame_jogo = tk.Frame(frame_jogos, bg="#34495e", bd=2, relief="groove")
        frame_jogo.pack(pady=5, padx=10, fill="x")

        tk.Checkbutton(frame_jogo, text=f"{time1} x {time2}", variable=var, bg="#34495e", fg="#ecf0f1", font=font_label, selectcolor="#2c3e50").pack()

    btn_confirmar = tk.Button(tela_escolha, text="Confirmar Seleção", bg="#2980b9", fg="white", font=font_btn, command=lambda: confirmar_selecao(selecoes, tela_escolha))
    btn_confirmar.pack(pady=20)

def confirmar_selecao(selecoes, tela_escolha):
    """Armazena os jogos selecionados e fecha a tela de escolha."""
    global jogos_selecionados

    jogos_selecionados = []
    for time1, time2, var in selecoes:
        if var.get():  # Se o jogo foi selecionado
            jogos_selecionados.append((time1, time2))

    if not jogos_selecionados:
        messagebox.showinfo("Aviso", "Nenhum jogo selecionado. Você pode apostar depois.")
    else:
        messagebox.showinfo("Sucesso", f"{len(jogos_selecionados)} jogos selecionados para apostar.")

    tela_escolha.destroy()
    tela_apostas_rodada()  # Abre a tela de apostas



def tela_apostas_rodada():
    """Tela para o usuário fazer as apostas nos jogos selecionados."""
    global fichas_usuario, usuario_logado, jogos_selecionados
    apostas_usuario.clear()
    tela_apostas = tk.Toplevel()
    tela_apostas.title("Apostas da Rodada")
    tela_apostas.geometry("600x600")
    tela_apostas.configure(bg="#2c3e50")

    font_label = tkFont.Font(family="Arial", size=12)
    font_btn = tkFont.Font(family="Arial", size=12, weight="bold")

    tk.Label(tela_apostas, text="Faça suas apostas:", bg="#2c3e50", fg="#ecf0f1", font=font_label).pack(pady=10)

    # Adicionar um Canvas com barra de rolagem
    canvas = tk.Canvas(tela_apostas, bg="#2c3e50")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(tela_apostas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame_conteudo = tk.Frame(canvas, bg="#2c3e50")
    canvas.create_window((0, 0), window=frame_conteudo, anchor="nw")

    apostas = []

    for time1, time2 in jogos_selecionados:
        frame_jogo = tk.Frame(frame_conteudo, bg="#34495e", bd=2, relief="groove")
        frame_jogo.pack(pady=5, padx=10, fill="x")

        tk.Label(frame_jogo, text=f"{time1} x {time2}", bg="#34495e", fg="#ecf0f1", font=font_label).pack(pady=5)

        var_aposta = tk.StringVar(value="nenhuma")

        aposta_frame = tk.Frame(frame_jogo, bg="#34495e")
        aposta_frame.pack()

        tk.Radiobutton(aposta_frame, text=time1, variable=var_aposta, value=time1, bg="#34495e", fg="#ecf0f1", font=font_label, selectcolor="#2c3e50").pack(side="left", padx=5)
        tk.Radiobutton(aposta_frame, text=time2, variable=var_aposta, value=time2, bg="#34495e", fg="#ecf0f1", font=font_label, selectcolor="#2c3e50").pack(side="left", padx=5)
        tk.Radiobutton(aposta_frame, text="Empate", variable=var_aposta, value="empate", bg="#34495e", fg="#ecf0f1", font=font_label, selectcolor="#2c3e50").pack(side="left", padx=5)

        tk.Label(frame_jogo, text="Fichas:", bg="#34495e", fg="#ecf0f1", font=font_label).pack(side="left", padx=5)
        entry_fichas = tk.Entry(frame_jogo, font=font_label, width=10)
        entry_fichas.pack(side="left", padx=5)

        apostas.append((time1, time2, var_aposta, entry_fichas))

    btn_confirmar = tk.Button(tela_apostas, text="Confirmar Apostas", bg="#2980b9", fg="white", font=font_btn, command=lambda: processar_apostas(apostas, tela_apostas))
    btn_confirmar.pack(pady=20)

def processar_apostas(apostas, tela_apostas):
    """Processa as apostas feitas pelo usuário."""
    global fichas_usuario, usuario_logado, apostas_usuario

    total_apostado = 0

    # Verificar se o usuário tem fichas suficientes antes de processar as apostas
    for aposta in apostas:
        time1, time2, var_aposta, entry_fichas = aposta
        fichas_apostadas = entry_fichas.get().strip()  # Remover espaços extras

        # Verifica se o campo de fichas está vazio ou não é um número
        if not fichas_apostadas:
            continue  # Ignora se o campo estiver vazio

        if not fichas_apostadas.isdigit():  # Verifica se é um número inteiro válido
            messagebox.showerror("Erro", f"Aposta inválida para {time1} x {time2}. Insira um valor numérico.")
            return
        
        fichas_apostadas = int(fichas_apostadas)

        if fichas_apostadas < 0:
            messagebox.showerror("Erro", f"Aposta inválida para {time1} x {time2}. O valor deve ser positivo.")
            return

        total_apostado += fichas_apostadas

    # Verificar se o usuário tem fichas suficientes para todas as apostas
    if total_apostado > fichas_usuario:
        messagebox.showerror("Erro", "Você não tem fichas suficientes para todas as apostas.")
        return

    # Processar as apostas
    for aposta in apostas:
        time1, time2, var_aposta, entry_fichas = aposta
        fichas_apostadas = entry_fichas.get().strip()

        if not fichas_apostadas:
            continue

        fichas_apostadas = int(fichas_apostadas)

        # Armazenar a aposta do usuário
        aposta_usuario = {
            "time1": time1,
            "time2": time2,
            "aposta": var_aposta.get(),
            "fichas": fichas_apostadas
        }
        apostas_usuario.append(aposta_usuario)

    # Atualizar o saldo de fichas
    label_pontos.config(text=f"Fichas de {usuario_logado}: {fichas_usuario}")

    # Fechar a tela de apostas
    tela_apostas.destroy()

    # Mostrar mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Apostas realizadas com sucesso! Total apostado: {total_apostado} fichas.")

#parte referente ao login
def verificar_usuario_existe(nome):
    if not os.path.exists("usuarios.txt"):
        return False
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            if linha.split(":")[0] == nome:
                return True
    return False

def cadastrar_usuario(nome, senha):
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome}:{senha}:100\n")  # Novo usuário começa com 100 fichas

def fazer_login():
    global fichas_usuario, usuario_logado  # Acessa as variáveis globais
    nome = entry_nome.get()
    senha = entry_senha.get()

    if not nome or not senha:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
        return

    if verificar_usuario_existe(nome):
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(":")
                if dados[0] == nome and dados[1] == senha:
                    usuario_logado = nome  # Armazena o nome do usuário logado
                    fichas_usuario = int(dados[2])  # Recupera as fichas do usuário
                    tela_login.destroy()
                    tela_inicial()
                    return
            messagebox.showerror("Erro", "Senha incorreta.")
    else:
        cadastrar_usuario(nome, senha)
        usuario_logado = nome  # Armazena o nome do usuário logado
        fichas_usuario = 100  # Novo usuário começa com 100 fichas
        messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso! Você recebeu 100 fichas.")
        tela_login.destroy()
        tela_inicial()

def tela_login():
    global tela_login, entry_nome, entry_senha

    tela_login = tk.Tk()
    tela_login.title("Login")
    tela_login.geometry("400x300")
    tela_login.configure(bg="#2c3e50")

    font_titulo = tkFont.Font(family="Arial", size=18, weight="bold")
    font_label = tkFont.Font(family="Arial", size=12)
    font_entry = tkFont.Font(family="Arial", size=12)

    tk.Label(tela_login, text="Login", bg="#2c3e50", fg="#ecf0f1", font=font_titulo).pack(pady=20)

    tk.Label(tela_login, text="Nome:", bg="#2c3e50", fg="#ecf0f1", font=font_label).pack()
    entry_nome = tk.Entry(tela_login, font=font_entry)
    entry_nome.pack(pady=5)

    tk.Label(tela_login, text="Senha:", bg="#2c3e50", fg="#ecf0f1", font=font_label).pack()
    entry_senha = tk.Entry(tela_login, show="*", font=font_entry)
    entry_senha.pack(pady=5)

    btn_login = tk.Button(tela_login, text="Login", bg="#2980b9", fg="white", font=font_label, command=fazer_login)
    btn_login.pack(pady=20)

    tela_login.mainloop()
    
#fim da parte do login


tela_selecao_edicao()
  
    
