import tkinter as tk
import random as rm
from tkinter import messagebox

times = {
    "América-MG": [0, 0, 0, 2, 0, 0, 0 ,0 ,0],
    "Athletico-PR": [0, 0, 0, 3, 0, 0, 0, 0, 0],
    "Atlético-MG": [0, 0, 0, 3, 0, 0 , 0,0,0],
    "Bahia": [0, 0, 0, 4, 0,0,0,0,0],
    "Botafogo": [0, 0, 0, 6, 0,0,0,0,0],
    "Corinthians": [0, 0, 0, 3, 0,0,0,0,0],
    "Vitória": [0, 0, 0, 3, 0,0,0,0,0],
    "Cruzeiro": [0, 0, 0, 3, 0,0,0,0,0],
    "Cuiabá": [0, 0, 0, 2, 0,0,0,0,0],
    "Flamengo": [0, 0, 0, 5, 0,0,0,0,0],
    "Fluminense": [0, 0, 0, 3, 0,0,0,0,0],
    "Fortaleza": [0, 0, 0, 4, 0,0,0,0,0],
    "Juventude": [0, 0, 0, 4, 0,0,0,0,0],
    "Grêmio": [0, 0, 0, 3, 0,0,0,0,0],
    "Internacional": [0, 0, 0, 5, 0,0,0,0,0],
    "Palmeiras": [0, 0, 0, 5, 0,0,0,0,0],
    "RB Bragantino": [0, 0, 0, 3, 0,0,0,0,0],
    "Criciúma": [0, 0, 0, 3, 0,0,0,0,0],
    "São Paulo": [0, 0, 0, 4, 0,0,0,0,0],
    "Vasco da Gama": [0, 0, 0, 4, 0,0,0,0,0]
}
total_rodadas = 38
def criar_jogos():
    confrontoss = [
        ("América-MG", "Athletico-PR"),
    ("América-MG", "Atlético-MG"),
    ("América-MG", "Bahia"),
    ("América-MG", "Botafogo"),
    ("América-MG", "Corinthians"),
    ("América-MG", "Vitória"),
    ("América-MG", "Cruzeiro"),
    ("América-MG", "Cuiabá"),
    ("América-MG", "Flamengo"),
    ("América-MG", "Fluminense"),
    ("América-MG", "Fortaleza"),
    ("América-MG", "Juventude"),
    ("América-MG", "Grêmio"),
    ("América-MG", "Internacional"),
    ("América-MG", "Palmeiras"),
    ("América-MG", "RB Bragantino"),
    ("América-MG", "Criciúma"),
    ("América-MG", "São Paulo"),
    ("América-MG", "Vasco da Gama"),
    ("Athletico-PR", "Atlético-MG"),
    ("Athletico-PR", "Bahia"),
    ("Athletico-PR", "Botafogo"),
    ("Athletico-PR", "Corinthians"),
    ("Athletico-PR", "Vitória"),
    ("Athletico-PR", "Cruzeiro"),
    ("Athletico-PR", "Cuiabá"),
    ("Athletico-PR", "Flamengo"),
    ("Athletico-PR", "Fluminense"),
    ("Athletico-PR", "Fortaleza"),
    ("Athletico-PR", "Juventude"),
    ("Athletico-PR", "Grêmio"),
    ("Athletico-PR", "Internacional"),
    ("Athletico-PR", "Palmeiras"),
    ("Athletico-PR", "RB Bragantino"),
    ("Athletico-PR", "Criciúma"),
    ("Athletico-PR", "São Paulo"),
    ("Athletico-PR", "Vasco da Gama"),
    ("Atlético-MG", "Bahia"),
    ("Atlético-MG", "Botafogo"),
    ("Atlético-MG", "Corinthians"),
    ("Atlético-MG", "Vitória"),
    ("Atlético-MG", "Cruzeiro"),
    ("Atlético-MG", "Cuiabá"),
    ("Atlético-MG", "Flamengo"),
    ("Atlético-MG", "Fluminense"),
    ("Atlético-MG", "Fortaleza"),
    ("Atlético-MG", "Juventude"),
    ("Atlético-MG", "Grêmio"),
    ("Atlético-MG", "Internacional"),
    ("Atlético-MG", "Palmeiras"),
    ("Atlético-MG", "RB Bragantino"),
    ("Atlético-MG", "Criciúma"),
    ("Atlético-MG", "São Paulo"),
    ("Atlético-MG", "Vasco da Gama"),
    ("Bahia", "Botafogo"),
    ("Bahia", "Corinthians"),
    ("Bahia", "Vitória"),
    ("Bahia", "Cruzeiro"),
    ("Bahia", "Cuiabá"),
    ("Bahia", "Flamengo"),
    ("Bahia", "Fluminense"),
    ("Bahia", "Fortaleza"),
    ("Bahia", "Juventude"),
    ("Bahia", "Grêmio"),
    ("Bahia", "Internacional"),
    ("Bahia", "Palmeiras"),
    ("Bahia", "RB Bragantino"),
    ("Bahia", "Criciúma"),
    ("Bahia", "São Paulo"),
    ("Bahia", "Vasco da Gama"),
    ("Botafogo", "Corinthians"),
    ("Botafogo", "Vitória"),
    ("Botafogo", "Cruzeiro"),
    ("Botafogo", "Cuiabá"),
    ("Botafogo", "Flamengo"),
    ("Botafogo", "Fluminense"),
    ("Botafogo", "Fortaleza"),
    ("Botafogo", "Juventude"),
    ("Botafogo", "Grêmio"),
    ("Botafogo", "Internacional"),
    ("Botafogo", "Palmeiras"),
    ("Botafogo", "RB Bragantino"),
    ("Botafogo", "Criciúma"),
    ("Botafogo", "São Paulo"),
    ("Botafogo", "Vasco da Gama"),
    ("Corinthians", "Vitória"),
    ("Corinthians", "Cruzeiro"),
    ("Corinthians", "Cuiabá"),
    ("Corinthians", "Flamengo"),
    ("Corinthians", "Fluminense"),
    ("Corinthians", "Fortaleza"),
    ("Corinthians", "Juventude"),
    ("Corinthians", "Grêmio"),
    ("Corinthians", "Internacional"),
    ("Corinthians", "Palmeiras"),
    ("Corinthians", "RB Bragantino"),
    ("Corinthians", "Criciúma"),
    ("Corinthians", "São Paulo"),
    ("Corinthians", "Vasco da Gama"),
    ("Vitória", "Cruzeiro"),
    ("Vitória", "Cuiabá"),
    ("Vitória", "Flamengo"),
    ("Vitória", "Fluminense"),
    ("Vitória", "Fortaleza"),
    ("Vitória", "Juventude"),
    ("Vitória", "Grêmio"),
    ("Vitória", "Internacional"),
    ("Vitória", "Palmeiras"),
    ("Vitória", "RB Bragantino"),
    ("Vitória", "Criciúma"),
    ("Vitória", "São Paulo"),
    ("Vitória", "Vasco da Gama"),
    ("Cruzeiro", "Cuiabá"),
    ("Cruzeiro", "Flamengo"),
    ("Cruzeiro", "Fluminense"),
    ("Cruzeiro", "Fortaleza"),
    ("Cruzeiro", "Juventude"),
    ("Cruzeiro", "Grêmio"),
    ("Cruzeiro", "Internacional"),
    ("Cruzeiro", "Palmeiras"),
    ("Cruzeiro", "RB Bragantino"),
    ("Cruzeiro", "Criciúma"),
    ("Cruzeiro", "São Paulo"),
    ("Cruzeiro", "Vasco da Gama"),
    ("Cuiabá", "Flamengo"),
    ("Cuiabá", "Fluminense"),
    ("Cuiabá", "Fortaleza"),
    ("Cuiabá", "Juventude"),
    ("Cuiabá", "Grêmio"),
    ("Cuiabá", "Internacional"),
    ("Cuiabá", "Palmeiras"),
    ("Cuiabá", "RB Bragantino"),
    ("Cuiabá", "Criciúma"),
    ("Cuiabá", "São Paulo"),
    ("Cuiabá", "Vasco da Gama"),
    ("Flamengo", "Fluminense"),
    ("Flamengo", "Fortaleza"),
    ("Flamengo", "Juventude"),
    ("Flamengo", "Grêmio"),
    ("Flamengo", "Internacional"),
    ("Flamengo", "Palmeiras"),
    ("Flamengo", "RB Bragantino"),
    ("Flamengo", "Criciúma"),
    ("Flamengo", "São Paulo"),
    ("Flamengo", "Vasco da Gama"),
    ("Fluminense", "Fortaleza"),
    ("Fluminense", "Juventude"),
    ("Fluminense", "Grêmio"),
    ("Fluminense", "Internacional"),
    ("Fluminense", "Palmeiras"),
    ("Fluminense", "RB Bragantino"),
    ("Fluminense", "Criciúma"),
    ("Fluminense", "São Paulo"),
    ("Fluminense", "Vasco da Gama"),
    ("Fortaleza", "Juventude"),
    ("Fortaleza", "Grêmio"),
    ("Fortaleza", "Internacional"),
    ("Fortaleza", "Palmeiras"),
    ("Fortaleza", "RB Bragantino"),
    ("Fortaleza", "Criciúma"),
    ("Fortaleza", "São Paulo"),
    ("Fortaleza", "Vasco da Gama"),
    ("Juventude", "Grêmio"),
    ("Juventude", "Internacional"),
    ("Juventude", "Palmeiras"),
    ("Juventude", "RB Bragantino"),
    ("Juventude", "Criciúma"),
    ("Juventude", "São Paulo"),
    ("Juventude", "Vasco da Gama"),
    ("Grêmio", "Internacional"),
    ("Grêmio", "Palmeiras"),
    ("Grêmio", "RB Bragantino"),
    ("Grêmio", "Criciúma"),
    ("Grêmio", "São Paulo"),
    ("Grêmio", "Vasco da Gama"),
    ("Internacional", "Palmeiras"),
    ("Internacional", "RB Bragantino"),
    ("Internacional", "Criciúma"),
    ("Internacional", "São Paulo"),
    ("Internacional", "Vasco da Gama"),
    ("Palmeiras", "RB Bragantino"),
    ("Palmeiras", "Criciúma"),
    ("Palmeiras", "São Paulo"),
    ("Palmeiras", "Vasco da Gama"),
    ("RB Bragantino", "Criciúma"),
    ("RB Bragantino", "São Paulo"),
    ("RB Bragantino", "Vasco da Gama"),
    ("Criciúma", "São Paulo"),
    ("Criciúma", "Vasco da Gama"),
    ("São Paulo", "Vasco da Gama"),
    ("América-MG", "Athletico-PR"),
    ("América-MG", "Atlético-MG"),
    ("América-MG", "Bahia"),
    ("América-MG", "Botafogo"),
    ("América-MG", "Corinthians"),
    ("América-MG", "Vitória"),
    ("América-MG", "Cruzeiro"),
    ("América-MG", "Cuiabá"),
    ("América-MG", "Flamengo"),
    ("América-MG", "Fluminense"),
    ("América-MG", "Fortaleza"),
    ("América-MG", "Juventude"),
    ("América-MG", "Grêmio"),
    ("América-MG", "Internacional"),
    ("América-MG", "Palmeiras"),
    ("América-MG", "RB Bragantino"),
    ("América-MG", "Criciúma"),
    ("América-MG", "São Paulo"),
    ("América-MG", "Vasco da Gama"),
    ("Athletico-PR", "Atlético-MG"),
    ("Athletico-PR", "Bahia"),
    ("Athletico-PR", "Botafogo"),
    ("Athletico-PR", "Corinthians"),
    ("Athletico-PR", "Vitória"),
    ("Athletico-PR", "Cruzeiro"),
    ("Athletico-PR", "Cuiabá"),
    ("Athletico-PR", "Flamengo"),
    ("Athletico-PR", "Fluminense"),
    ("Athletico-PR", "Fortaleza"),
    ("Athletico-PR", "Juventude"),
    ("Athletico-PR", "Grêmio"),
    ("Athletico-PR", "Internacional"),
    ("Athletico-PR", "Palmeiras"),
    ("Athletico-PR", "RB Bragantino"),
    ("Athletico-PR", "Criciúma"),
    ("Athletico-PR", "São Paulo"),
    ("Athletico-PR", "Vasco da Gama"),
    ("Atlético-MG", "Bahia"),
    ("Atlético-MG", "Botafogo"),
    ("Atlético-MG", "Corinthians"),
    ("Atlético-MG", "Vitória"),
    ("Atlético-MG", "Cruzeiro"),
    ("Atlético-MG", "Cuiabá"),
    ("Atlético-MG", "Flamengo"),
    ("Atlético-MG", "Fluminense"),
    ("Atlético-MG", "Fortaleza"),
    ("Atlético-MG", "Juventude"),
    ("Atlético-MG", "Grêmio"),
    ("Atlético-MG", "Internacional"),
    ("Atlético-MG", "Palmeiras"),
    ("Atlético-MG", "RB Bragantino"),
    ("Atlético-MG", "Criciúma"),
    ("Atlético-MG", "São Paulo"),
    ("Atlético-MG", "Vasco da Gama"),
    ("Bahia", "Botafogo"),
    ("Bahia", "Corinthians"),
    ("Bahia", "Vitória"),
    ("Bahia", "Cruzeiro"),
    ("Bahia", "Cuiabá"),
    ("Bahia", "Flamengo"),
    ("Bahia", "Fluminense"),
    ("Bahia", "Fortaleza"),
    ("Bahia", "Juventude"),
    ("Bahia", "Grêmio"),
    ("Bahia", "Internacional"),
    ("Bahia", "Palmeiras"),
    ("Bahia", "RB Bragantino"),
    ("Bahia", "Criciúma"),
    ("Bahia", "São Paulo"),
    ("Bahia", "Vasco da Gama"),
    ("Botafogo", "Corinthians"),
    ("Botafogo", "Vitória"),
    ("Botafogo", "Cruzeiro"),
    ("Botafogo", "Cuiabá"),
    ("Botafogo", "Flamengo"),
    ("Botafogo", "Fluminense"),
    ("Botafogo", "Fortaleza"),
    ("Botafogo", "Juventude"),
    ("Botafogo", "Grêmio"),
    ("Botafogo", "Internacional"),
    ("Botafogo", "Palmeiras"),
    ("Botafogo", "RB Bragantino"),
    ("Botafogo", "Criciúma"),
    ("Botafogo", "São Paulo"),
    ("Botafogo", "Vasco da Gama"),
    ("Corinthians", "Vitória"),
    ("Corinthians", "Cruzeiro"),
    ("Corinthians", "Cuiabá"),
    ("Corinthians", "Flamengo"),
    ("Corinthians", "Fluminense"),
    ("Corinthians", "Fortaleza"),
    ("Corinthians", "Juventude"),
    ("Corinthians", "Grêmio"),
    ("Corinthians", "Internacional"),
    ("Corinthians", "Palmeiras"),
    ("Corinthians", "RB Bragantino"),
    ("Corinthians", "Criciúma"),
    ("Corinthians", "São Paulo"),
    ("Corinthians", "Vasco da Gama"),
    ("Vitória", "Cruzeiro"),
    ("Vitória", "Cuiabá"),
    ("Vitória", "Flamengo"),
    ("Vitória", "Fluminense"),
    ("Vitória", "Fortaleza"),
    ("Vitória", "Juventude"),
    ("Vitória", "Grêmio"),
    ("Vitória", "Internacional"),
    ("Vitória", "Palmeiras"),
    ("Vitória", "RB Bragantino"),
    ("Vitória", "Criciúma"),
    ("Vitória", "São Paulo"),
    ("Vitória", "Vasco da Gama"),
    ("Cruzeiro", "Cuiabá"),
    ("Cruzeiro", "Flamengo"),
    ("Cruzeiro", "Fluminense"),
    ("Cruzeiro", "Fortaleza"),
    ("Cruzeiro", "Juventude"),
    ("Cruzeiro", "Grêmio"),
    ("Cruzeiro", "Internacional"),
    ("Cruzeiro", "Palmeiras"),
    ("Cruzeiro", "RB Bragantino"),
    ("Cruzeiro", "Criciúma"),
    ("Cruzeiro", "São Paulo"),
    ("Cruzeiro", "Vasco da Gama"),
    ("Cuiabá", "Flamengo"),
    ("Cuiabá", "Fluminense"),
    ("Cuiabá", "Fortaleza"),
    ("Cuiabá", "Juventude"),
    ("Cuiabá", "Grêmio"),
    ("Cuiabá", "Internacional"),
    ("Cuiabá", "Palmeiras"),
    ("Cuiabá", "RB Bragantino"),
    ("Cuiabá", "Criciúma"),
    ("Cuiabá", "São Paulo"),
    ("Cuiabá", "Vasco da Gama"),
    ("Flamengo", "Fluminense"),
    ("Flamengo", "Fortaleza"),
    ("Flamengo", "Juventude"),
    ("Flamengo", "Grêmio"),
    ("Flamengo", "Internacional"),
    ("Flamengo", "Palmeiras"),
    ("Flamengo", "RB Bragantino"),
    ("Flamengo", "Criciúma"),
    ("Flamengo", "São Paulo"),
    ("Flamengo", "Vasco da Gama"),
    ("Fluminense", "Fortaleza"),
    ("Fluminense", "Juventude"),
    ("Fluminense", "Grêmio"),
    ("Fluminense", "Internacional"),
    ("Fluminense", "Palmeiras"),
    ("Fluminense", "RB Bragantino"),
    ("Fluminense", "Criciúma"),
    ("Fluminense", "São Paulo"),
    ("Fluminense", "Vasco da Gama"),
    ("Fortaleza", "Juventude"),
    ("Fortaleza", "Grêmio"),
    ("Fortaleza", "Internacional"),
    ("Fortaleza", "Palmeiras"),
    ("Fortaleza", "RB Bragantino"),
    ("Fortaleza", "Criciúma"),
    ("Fortaleza", "São Paulo"),
    ("Fortaleza", "Vasco da Gama"),
    ("Juventude", "Grêmio"),
    ("Juventude", "Internacional"),
    ("Juventude", "Palmeiras"),
    ("Juventude", "RB Bragantino"),
    ("Juventude", "Criciúma"),
    ("Juventude", "São Paulo"),
    ("Juventude", "Vasco da Gama"),
    ("Grêmio", "Internacional"),
    ("Grêmio", "Palmeiras"),
    ("Grêmio", "RB Bragantino"),
    ("Grêmio", "Criciúma"),
    ("Grêmio", "São Paulo"),
    ("Grêmio", "Vasco da Gama"),
    ("Internacional", "Palmeiras"),
    ("Internacional", "RB Bragantino"),
    ("Internacional", "Criciúma"),
    ("Internacional", "São Paulo"),
    ("Internacional", "Vasco da Gama"),
    ("Palmeiras", "RB Bragantino"),
    ("Palmeiras", "Criciúma"),
    ("Palmeiras", "São Paulo"),
    ("Palmeiras", "Vasco da Gama"),
    ("RB Bragantino", "Criciúma"),
    ("RB Bragantino", "São Paulo"),
    ("RB Bragantino", "Vasco da Gama"),
    ("Criciúma", "São Paulo"),
    ("Criciúma", "Vasco da Gama"),
    ("São Paulo", "Vasco da Gama")
    ]
    rm.shuffle(confrontoss)
    todososjogos = []
# Imprime os confrontos randomizados
    for confrontos in confrontoss:
     todososjogos.append(confrontos)
    return todososjogos
    
    
   
    
    
    
    confrontos = criar_jogos()
confrontos = criar_jogos()     
rodadas = total_rodadas
rodada_atual = 0
def tela_inicial():
    global frame_times, labels_times, rodadas_label, rodada_atual, btn_simular, total_rodadas
    
    tela_inicial = tk.Tk()
    tela_inicial.configure(bg="black")
    tela_inicial.title("Simulator Brasileirão")
    tela_inicial.attributes("-fullscreen", True)

    label_introducao = tk.Label(tela_inicial, text="Bem-vindo ao Simulador de Brasileirão", bg="black", fg="white", font=("Arial", 16))
    label_introducao.pack(pady=20)

    frame_times = tk.Frame(tela_inicial, bg="black")
    frame_times.pack(pady=20)

    labels_times = {}

    for time in times.keys():
        label_time = tk.Label(frame_times, bg="black", fg="white", font=("Arial", 12))
        label_time.pack(anchor="w")
        labels_times[time] = label_time

    rodadas_label = tk.Label(tela_inicial, text=f"Rodadas restantes: {rodadas}", bg="black", fg="white", font=("Arial", 14))
    rodadas_label.pack(pady=20)
    
    btn_simular = tk.Button(tela_inicial, text="Simular Próxima Rodada", command=simular_rodada, bg="white", fg="black", font=("Arial", 14))
    btn_simular.pack(pady=20)
    
    tela_inicial.mainloop()

def simular_rodada():
    global rodadas, rodada_atual
    if rodada_atual < total_rodadas:
        for i in range(10): 
            index = rodada_atual * 10 + i
            if index < len(confrontos):
                time1, time2 = confrontos[index]
                simular_jogo(time1, time2)

        organizar_tabela()
        rodada_atual += 1
        rodadas -= 1
        rodadas_label.config(text=f"Rodadas restantes: {rodadas}")
        if rodadas == 0:
            parabenizar_campeao()
    else:
        messagebox.showinfo("Fim do Campeonato", "O campeonato chegou ao fim!")

import random as rm

def simular_rodada():
    global rodadas, rodada_atual
    if rodada_atual < total_rodadas:
        # Escrever "Rodada X" uma vez antes de começar a simular os jogos da rodada
        with open("placares_jogos.txt", "a") as arquivo:
            arquivo.write(f"Rodada {rodada_atual + 1}\n")
        
        # Simular os jogos da rodada
        for i in range(10): 
            index = rodada_atual * 10 + i
            if index < len(confrontos):
                time1, time2 = confrontos[index]
                simular_jogo(time1, time2)

        # Atualizar a tabela e a rodada
        organizar_tabela()
        rodada_atual += 1
        rodadas -= 1
        rodadas_label.config(text=f"Rodadas restantes: {rodadas}")
        
        # Verificar se o campeonato terminou
        if rodadas == 0:
            parabenizar_campeao()
    else:
        messagebox.showinfo("Fim do Campeonato", "O campeonato chegou ao fim!")

def simular_jogo(time1, time2, nome_arquivo="placares_jogos.txt"):
    chances_time1 = times[time1][3]  
    chances_time2 = times[time2][3]  
    gols_time1 = 0
    gols_time2 = 0

    for _ in range(chances_time1):
        if rm.choices([True, False], weights=[0.3, 0.7])[0]:  
            gols_time1 += 1

    for _ in range(chances_time2):
        if rm.choices([True, False], weights=[0.3, 0.7])[0]: 
            gols_time2 += 1

    times[time1][1] += gols_time1  
    times[time1][0] += gols_time2  
    times[time2][1] += gols_time2  
    times[time2][0] += gols_time1  

    if gols_time1 > gols_time2:
        times[time1][2] += 3  
        times[time1][5] += 1  
        times[time2][7] += 1  
    elif gols_time1 < gols_time2:
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

    # Escrever o placar do jogo
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(f"{time1} {gols_time1} x {gols_time2} {time2}\n")



def organizar_tabela():
    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)

    for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao
        saldo_gols = stats[1] - stats[0]
        labels_times[time].config(text=f"{posicao}º {time} | Jogos: {stats[8]} | Pontos: {stats[2]} | Vitorias: {stats[5]} | Empate: {stats[6]} | Derrota: {stats[7]} | Saldo: {saldo_gols} | Gols Feitos: {stats[1]} | Gols Tomados: {stats[0]} ")
def parabenizar_campeao():
    global btn_simular
    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)
    
    for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao
        if posicao == 1:
            messagebox.showinfo(f"Campeão definido", f"Parabéns o campeão foi {time}")
        btn_simular.config(text="Informações do campeonato", command=lambda: Informar(), bg = 'red')
def Informar():
    tela_informativa = tk.Tk()
    tela_informativa.configure(bg="black")
    tela_informativa.title("Informações da Simulação")
    tela_informativa.geometry('500x500')
    
    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)
    maiortomados = -1
    Golstomados = ""
    maior = -1  
    Artilheiro = ""
    
    for posicao, (time, stats) in enumerate(sorted_times, start=1):
        if posicao == 1:
            labelZ1 = tk.Label(tela_informativa, text=f"O time vencedor do campeonato foi o {time} com {stats[2]} pontos", bg='green')
            labelZ1.pack(pady=(10, 10))
        elif posicao == 2:
            labelZ2 = tk.Label(tela_informativa, text=f"O segundo lugar foi para o {time} com {stats[2]} pontos", bg='green')
            labelZ2.pack(pady=(10, 10))
        elif posicao == 3:
            labelZ3 = tk.Label(tela_informativa, text=f"O terceiro lugar foi para o {time} com {stats[2]} pontos", bg='green')
            labelZ3.pack(pady=(10, 10))
        elif posicao == 4: 
            labelZ4 = tk.Label(tela_informativa, text=f"O quarto lugar foi para o {time} com {stats[2]} pontos", bg='green')
            labelZ4.pack(pady=(10, 10))
        
        if posicao == 20:
            labelG4 = tk.Label(tela_informativa, text=f"O time que caiu no G4 foi o {time} com {stats[2]} pontos", bg='red')
            labelG4.pack(pady=(10, 10))
        elif posicao == 19:
            labelG3 = tk.Label(tela_informativa, text=f"O time que caiu no G3 foi o {time} com {stats[2]} pontos", bg='red')
            labelG3.pack(pady=(10, 10))
        elif posicao == 18:
            labelG2 = tk.Label(tela_informativa, text=f"O time que caiu no G2 foi o {time} com {stats[2]} pontos", bg='red')
            labelG2.pack(pady=(10, 10))
        elif posicao == 17: 
            labelG1 = tk.Label(tela_informativa, text=f"O time que caiu no G1 foi o {time} com {stats[2]} pontos", bg='red')
            labelG1.pack(pady=(10, 10))
        
        if stats[1] > maior: 
            maior = stats[1]
            Artilheiro = time  
        if stats[2] > maiortomados: 
            maiortomados = stats[1]
            Golstomados = time  
    labelArtilheiro = tk.Label(tela_informativa, text=f"O artilheiro do campeonato foi {Artilheiro} com {maior} gols", bg='yellow')
    labelArtilheiro.pack(pady=(10, 10))
    labelTomados = tk.Label(tela_informativa, text=f"O artilheiro do campeonato foi {Golstomados} com {maiortomados} gols", bg='orange')
    labelTomados.pack(pady=(10, 10))

    tela_informativa.mainloop()  


tela_inicial()
