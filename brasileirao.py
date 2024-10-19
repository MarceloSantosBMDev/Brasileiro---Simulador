import tkinter as tk
import random as rm
from tkinter import messagebox
import os


#max gols = 7
times = {
    "América-MG":  [0, 0, 0, 2, 0, 0, 0, 0, 0, 2],
    "Athletico-PR": [0, 0, 0, 4, 0, 0, 0, 0, 0, 3],
    "Atlético-MG":  [0, 0, 0, 5, 0, 0, 0, 0, 0, 3],
    "Bahia":        [0, 0, 0, 5, 0, 0, 0, 0, 0, 4],
    "Botafogo":     [0, 0, 0, 7, 0, 0, 0, 0, 0, 6],
    "Corinthians": [0, 0, 0, 4, 0,0,0,0,0,3],
    "Vitória": [0, 0, 0, 3, 0,0,0,0,0,2],
    "Cruzeiro": [0, 0, 0, 4, 0,0,0,0,0,5],
    "Cuiabá": [0, 0, 0, 2, 0,0,0,0,0,4],
    "Flamengo": [0, 0, 0, 6, 0,0,0,0,0,5],
    "Fluminense": [0, 0, 0, 3, 0,0,0,0,0,5],
    "Fortaleza": [0, 0, 0, 5, 0,0,0,0,0,4],
    "Juventude": [0, 0, 0, 4, 0,0,0,0,0,4],
    "Grêmio": [0, 0, 0, 4, 0,0,0,0,0,4],
    "Internacional": [0, 0, 0, 5, 0,0,0,0,0,6],
    "Palmeiras": [0, 0, 0, 6, 0,0,0,0,0,7],
    "RB Bragantino": [0, 0, 0, 4, 0,0,0,0,0,4],
    "Criciúma": [0, 0, 0, 5, 0,0,0,0,0,2],
    "São Paulo": [0, 0, 0, 5, 0,0,0,0,0,3],
    "Vasco da Gama": [0, 0, 0, 4, 0,0,0,0,0,2]
}
total_rodadas = 38


def criar_jogos():
    confrontoss = [
("Corinthians", "Palmeiras"),
("Palmeiras", "Corinthians"),
("Corinthians", "Vasco da Gama"),
("Vasco da Gama", "Corinthians"),
("Corinthians", "América-MG"),
("América-MG", "Corinthians"),
("Corinthians", "Athletico-PR"),
("Athletico-PR", "Corinthians"),
("Corinthians", "Atlético-MG"),
("Atlético-MG", "Corinthians"),
("Corinthians", "Bahia"),
("Bahia", "Corinthians"),
("Corinthians", "Botafogo"),
("Botafogo", "Corinthians"),
("Corinthians", "Vitória"),
("Vitória", "Corinthians"),
("Corinthians", "Cruzeiro"),
("Cruzeiro", "Corinthians"),
("Corinthians", "Cuiabá"),
("Cuiabá", "Corinthians"),
("Corinthians", "Flamengo"),
("Flamengo", "Corinthians"),
("Corinthians", "Fluminense"),
("Fluminense", "Corinthians"),
("Corinthians", "Fortaleza"),
("Fortaleza", "Corinthians"),
("Corinthians", "Juventude"),
("Juventude", "Corinthians"),
("Corinthians", "Grêmio"),
("Grêmio", "Corinthians"),
("Corinthians", "Internacional"),
("Internacional", "Corinthians"),
("Corinthians", "RB Bragantino"),
("RB Bragantino", "Corinthians"),
("Corinthians", "Criciúma"),
("Criciúma", "Corinthians"),
("Corinthians", "São Paulo"),
("São Paulo", "Corinthians"),
("Palmeiras", "Vasco da Gama"),
("Vasco da Gama", "Palmeiras"),
("Palmeiras", "América-MG"),
("América-MG", "Palmeiras"),
("Palmeiras", "Athletico-PR"),
("Athletico-PR", "Palmeiras"),
("Palmeiras", "Atlético-MG"),
("Atlético-MG", "Palmeiras"),
("Palmeiras", "Bahia"),
("Bahia", "Palmeiras"),
("Palmeiras", "Botafogo"),
("Botafogo", "Palmeiras"),
("Palmeiras", "Vitória"),
("Vitória", "Palmeiras"),
("Palmeiras", "Cruzeiro"),
("Cruzeiro", "Palmeiras"),
("Palmeiras", "Cuiabá"),
("Cuiabá", "Palmeiras"),
("Palmeiras", "Flamengo"),
("Flamengo", "Palmeiras"),
("Palmeiras", "Fluminense"),
("Fluminense", "Palmeiras"),
("Palmeiras", "Fortaleza"),
("Fortaleza", "Palmeiras"),
("Palmeiras", "Juventude"),
("Juventude", "Palmeiras"),
("Palmeiras", "Grêmio"),
("Grêmio", "Palmeiras"),
("Palmeiras", "Internacional"),
("Internacional", "Palmeiras"),
("Palmeiras", "RB Bragantino"),
("RB Bragantino", "Palmeiras"),
("Palmeiras", "Criciúma"),
("Criciúma", "Palmeiras"),
("Palmeiras", "São Paulo"),
("São Paulo", "Palmeiras"),
("Vasco da Gama", "América-MG"),
("América-MG", "Vasco da Gama"),
("Vasco da Gama", "Athletico-PR"),
("Athletico-PR", "Vasco da Gama"),
("Vasco da Gama", "Atlético-MG"),
("Atlético-MG", "Vasco da Gama"),
("Vasco da Gama", "Bahia"),
("Bahia", "Vasco da Gama"),
("Vasco da Gama", "Botafogo"),
("Botafogo", "Vasco da Gama"),
("Vasco da Gama", "Vitória"),
("Vitória", "Vasco da Gama"),
("Vasco da Gama", "Cruzeiro"),
("Cruzeiro", "Vasco da Gama"),
("Vasco da Gama", "Cuiabá"),
("Cuiabá", "Vasco da Gama"),
("Vasco da Gama", "Flamengo"),
("Flamengo", "Vasco da Gama"),
("Vasco da Gama", "Fluminense"),
("Fluminense", "Vasco da Gama"),
("Vasco da Gama", "Fortaleza"),
("Fortaleza", "Vasco da Gama"),
("Vasco da Gama", "Juventude"),
("Juventude", "Vasco da Gama"),
("Vasco da Gama", "Grêmio"),
("Grêmio", "Vasco da Gama"),
("Vasco da Gama", "Internacional"),
("Internacional", "Vasco da Gama"),
("Vasco da Gama", "RB Bragantino"),
("RB Bragantino", "Vasco da Gama"),
("Vasco da Gama", "Criciúma"),
("Criciúma", "Vasco da Gama"),
("Vasco da Gama", "São Paulo"),
("São Paulo", "Vasco da Gama"),
("América-MG", "Athletico-PR"),
("Athletico-PR", "América-MG"),
("América-MG", "Atlético-MG"),
("Atlético-MG", "América-MG"),
("América-MG", "Bahia"),
("Bahia", "América-MG"),
("América-MG", "Botafogo"),
("Botafogo", "América-MG"),
("América-MG", "Vitória"),
("Vitória", "América-MG"),
("América-MG", "Cruzeiro"),
("Cruzeiro", "América-MG"),
("América-MG", "Cuiabá"),
("Cuiabá", "América-MG"),
("América-MG", "Flamengo"),
("Flamengo", "América-MG"),
("América-MG", "Fluminense"),
("Fluminense", "América-MG"),
("América-MG", "Fortaleza"),
("Fortaleza", "América-MG"),
("América-MG", "Juventude"),
("Juventude", "América-MG"),
("América-MG", "Grêmio"),
("Grêmio", "América-MG"),
("América-MG", "Internacional"),
("Internacional", "América-MG"),
("América-MG", "RB Bragantino"),
("RB Bragantino", "América-MG"),
("América-MG", "Criciúma"),
("Criciúma", "América-MG"),
("América-MG", "São Paulo"),
("São Paulo", "América-MG"),
("Athletico-PR", "Atlético-MG"),
("Atlético-MG", "Athletico-PR"),
("Athletico-PR", "Bahia"),
("Bahia", "Athletico-PR"),
("Athletico-PR", "Botafogo"),
("Botafogo", "Athletico-PR"),
("Athletico-PR", "Vitória"),
("Vitória", "Athletico-PR"),
("Athletico-PR", "Cruzeiro"),
("Cruzeiro", "Athletico-PR"),
("Athletico-PR", "Cuiabá"),
("Cuiabá", "Athletico-PR"),
("Athletico-PR", "Flamengo"),
("Flamengo", "Athletico-PR"),
("Athletico-PR", "Fluminense"),
("Fluminense", "Athletico-PR"),
("Athletico-PR", "Fortaleza"),
("Fortaleza", "Athletico-PR"),
("Athletico-PR", "Juventude"),
("Juventude", "Athletico-PR"),
("Athletico-PR", "Grêmio"),
("Grêmio", "Athletico-PR"),
("Athletico-PR", "Internacional"),
("Internacional", "Athletico-PR"),
("Athletico-PR", "RB Bragantino"),
("RB Bragantino", "Athletico-PR"),
("Athletico-PR", "Criciúma"),
("Criciúma", "Athletico-PR"),
("Athletico-PR", "São Paulo"),
("São Paulo", "Athletico-PR"),
("Atlético-MG", "Bahia"),
("Bahia", "Atlético-MG"),
("Atlético-MG", "Botafogo"),
("Botafogo", "Atlético-MG"),
("Atlético-MG", "Vitória"),
("Vitória", "Atlético-MG"),
("Atlético-MG", "Cruzeiro"),
("Cruzeiro", "Atlético-MG"),
("Atlético-MG", "Cuiabá"),
("Cuiabá", "Atlético-MG"),
("Atlético-MG", "Flamengo"),
("Flamengo", "Atlético-MG"),
("Atlético-MG", "Fluminense"),
("Fluminense", "Atlético-MG"),
("Atlético-MG", "Fortaleza"),
("Fortaleza", "Atlético-MG"),
("Atlético-MG", "Juventude"),
("Juventude", "Atlético-MG"),
("Atlético-MG", "Grêmio"),
("Grêmio", "Atlético-MG"),
("Atlético-MG", "Internacional"),
("Internacional", "Atlético-MG"),
("Atlético-MG", "RB Bragantino"),
("RB Bragantino", "Atlético-MG"),
("Atlético-MG", "Criciúma"),
("Criciúma", "Atlético-MG"),
("Atlético-MG", "São Paulo"),
("São Paulo", "Atlético-MG"),
("Bahia", "Botafogo"),
("Botafogo", "Bahia"),
("Bahia", "Vitória"),
("Vitória", "Bahia"),
("Bahia", "Cruzeiro"),
("Cruzeiro", "Bahia"),
("Bahia", "Cuiabá"),
("Cuiabá", "Bahia"),
("Bahia", "Flamengo"),
("Flamengo", "Bahia"),
("Bahia", "Fluminense"),
("Fluminense", "Bahia"),
("Bahia", "Fortaleza"),
("Fortaleza", "Bahia"),
("Bahia", "Juventude"),
("Juventude", "Bahia"),
("Bahia", "Grêmio"),
("Grêmio", "Bahia"),
("Bahia", "Internacional"),
("Internacional", "Bahia"),
("Bahia", "RB Bragantino"),
("RB Bragantino", "Bahia"),
("Bahia", "Criciúma"),
("Criciúma", "Bahia"),
("Bahia", "São Paulo"),
("São Paulo", "Bahia"),
("Botafogo", "Vitória"),
("Vitória", "Botafogo"),
("Botafogo", "Cruzeiro"),
("Cruzeiro", "Botafogo"),
("Botafogo", "Cuiabá"),
("Cuiabá", "Botafogo"),
("Botafogo", "Flamengo"),
("Flamengo", "Botafogo"),
("Botafogo", "Fluminense"),
("Fluminense", "Botafogo"),
("Botafogo", "Fortaleza"),
("Fortaleza", "Botafogo"),
("Botafogo", "Juventude"),
("Juventude", "Botafogo"),
("Botafogo", "Grêmio"),
("Grêmio", "Botafogo"),
("Botafogo", "Internacional"),
("Internacional", "Botafogo"),
("Botafogo", "RB Bragantino"),
("RB Bragantino", "Botafogo"),
("Botafogo", "Criciúma"),
("Criciúma", "Botafogo"),
("Botafogo", "São Paulo"),
("São Paulo", "Botafogo"),
("Vitória", "Cruzeiro"),
("Cruzeiro", "Vitória"),
("Vitória", "Cuiabá"),
("Cuiabá", "Vitória"),
("Vitória", "Flamengo"),
("Flamengo", "Vitória"),
("Vitória", "Fluminense"),
("Fluminense", "Vitória"),
("Vitória", "Fortaleza"),
("Fortaleza", "Vitória"),
("Vitória", "Juventude"),
("Juventude", "Vitória"),
("Vitória", "Grêmio"),
("Grêmio", "Vitória"),
("Vitória", "Internacional"),
("Internacional", "Vitória"),
("Vitória", "RB Bragantino"),
("RB Bragantino", "Vitória"),
("Vitória", "Criciúma"),
("Criciúma", "Vitória"),
("Vitória", "São Paulo"),
("São Paulo", "Vitória"),
("Cruzeiro", "Cuiabá"),
("Cuiabá", "Cruzeiro"),
("Cruzeiro", "Flamengo"),
("Flamengo", "Cruzeiro"),
("Cruzeiro", "Fluminense"),
("Fluminense", "Cruzeiro"),
("Cruzeiro", "Fortaleza"),
("Fortaleza", "Cruzeiro"),
("Cruzeiro", "Juventude"),
("Juventude", "Cruzeiro"),
("Cruzeiro", "Grêmio"),
("Grêmio", "Cruzeiro"),
("Cruzeiro", "Internacional"),
("Internacional", "Cruzeiro"),
("Cruzeiro", "RB Bragantino"),
("RB Bragantino", "Cruzeiro"),
("Cruzeiro", "Criciúma"),
("Criciúma", "Cruzeiro"),
("Cruzeiro", "São Paulo"),
("São Paulo", "Cruzeiro"),
("Cuiabá", "Flamengo"),
("Flamengo", "Cuiabá"),
("Cuiabá", "Fluminense"),
("Fluminense", "Cuiabá"),
("Cuiabá", "Fortaleza"),
("Fortaleza", "Cuiabá"),
("Cuiabá", "Juventude"),
("Juventude", "Cuiabá"),
("Cuiabá", "Grêmio"),
("Grêmio", "Cuiabá"),
("Cuiabá", "Internacional"),
("Internacional", "Cuiabá"),
("Cuiabá", "RB Bragantino"),
("RB Bragantino", "Cuiabá"),
("Cuiabá", "Criciúma"),
("Criciúma", "Cuiabá"),
("Cuiabá", "São Paulo"),
("São Paulo", "Cuiabá"),
("Flamengo", "Fluminense"),
("Fluminense", "Flamengo"),
("Flamengo", "Fortaleza"),
("Fortaleza", "Flamengo"),
("Flamengo", "Juventude"),
("Juventude", "Flamengo"),
("Flamengo", "Grêmio"),
("Grêmio", "Flamengo"),
("Flamengo", "Internacional"),
("Internacional", "Flamengo"),
("Flamengo", "RB Bragantino"),
("RB Bragantino", "Flamengo"),
("Flamengo", "Criciúma"),
("Criciúma", "Flamengo"),
("Flamengo", "São Paulo"),
("São Paulo", "Flamengo"),
("Fluminense", "Fortaleza"),
("Fortaleza", "Fluminense"),
("Fluminense", "Juventude"),
("Juventude", "Fluminense"),
("Fluminense", "Grêmio"),
("Grêmio", "Fluminense"),
("Fluminense", "Internacional"),
("Internacional", "Fluminense"),
("Fluminense", "RB Bragantino"),
("RB Bragantino", "Fluminense"),
("Fluminense", "Criciúma"),
("Criciúma", "Fluminense"),
("Fluminense", "São Paulo"),
("São Paulo", "Fluminense"),
("Fortaleza", "Juventude"),
("Juventude", "Fortaleza"),
("Fortaleza", "Grêmio"),
("Grêmio", "Fortaleza"),
("Fortaleza", "Internacional"),
("Internacional", "Fortaleza"),
("Fortaleza", "RB Bragantino"),
("RB Bragantino", "Fortaleza"),
("Fortaleza", "Criciúma"),
("Criciúma", "Fortaleza"),
("Fortaleza", "São Paulo"),
("São Paulo", "Fortaleza"),
("Juventude", "Grêmio"),
("Grêmio", "Juventude"),
("Juventude", "Internacional"),
("Internacional", "Juventude"),
("Juventude", "RB Bragantino"),
("RB Bragantino", "Juventude"),
("Juventude", "Criciúma"),
("Criciúma", "Juventude"),
("Juventude", "São Paulo"),
("São Paulo", "Juventude"),
("Grêmio", "Internacional"),
("Internacional", "Grêmio"),
("Grêmio", "RB Bragantino"),
("RB Bragantino", "Grêmio"),
("Grêmio", "Criciúma"),
("Criciúma", "Grêmio"),
("Grêmio", "São Paulo"),
("São Paulo", "Grêmio"),
("Internacional", "RB Bragantino"),
("RB Bragantino", "Internacional"),
("Internacional", "Criciúma"),
("Criciúma", "Internacional"),
("Internacional", "São Paulo"),
("São Paulo", "Internacional"),
("RB Bragantino", "Criciúma"),
("Criciúma", "RB Bragantino"),
("RB Bragantino", "São Paulo"),
("São Paulo", "RB Bragantino"),
("Criciúma", "São Paulo"),
("São Paulo", "Criciúma"),
    ]
    rm.shuffle(confrontoss)
    todososjogos = []
    for confrontos in confrontoss:
     todososjogos.append(confrontos)
    return todososjogos
    
confrontos = criar_jogos()     
rodadas = total_rodadas
rodada_atual = 0
def tela_inicial():
    global frame_times, labels_times, rodadas_label, btn_simular, rodadas

    tela_inicial = tk.Tk()
    tela_inicial.configure(bg="black")
    tela_inicial.title("Simulator Brasileirão")
    tela_inicial.attributes("-fullscreen", True)

    label_introducao = tk.Label(tela_inicial, text="Bem-vindo ao Simulador de Brasileirão", bg="black", fg="white", font=("Arial", 16))
    label_introducao.pack(pady=20)

    frame_times = tk.Frame(tela_inicial, bg="black")
    frame_times.pack(pady=20)

    labels_times = {}

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

def iniciar_simulacao(nome_arquivo="placares_jogos.txt"):
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print(f"Arquivo '{nome_arquivo}' excluído para nova simulação.")
iniciar_simulacao()
def simular_rodada():
    global rodadas, rodada_atual
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
        rodadas_label.config(text=f"Rodadas restantes: {rodadas}")
        
        if rodadas == 0:
            parabenizar_campeao()
    else:
        messagebox.showinfo("Fim do Campeonato", "O campeonato chegou ao fim!")

def simular_jogo(time1, time2, nome_arquivo="placares_jogos.txt"):
    chances_time1 = times[time1][3]  
    chances_time2 = times[time2][3]  
    gols_defendidos1 = times[time1][9]
    gols_defendidos2 = times[time2][9]
    
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
        if rm.choices([True, False], weights=[0.2, 0.9])[0]:  
            defesas1 += 1

    for _ in range(gols_defendidos2):
        if rm.choices([True, False], weights=[0.05, 0.95])[0]: 
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

    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(f"{time1} {gols_time1} x {gols_time2} {time2}\n")

def organizar_tabela():
    global frame_times

    for widget in frame_times.winfo_children():
        widget.destroy()

    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)

    for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao  
        saldo_gols = stats[1] - stats[0]

        if posicao == 1:
            bg_color = "blue" 
        elif posicao == 2:
            bg_color = "blue"  
        elif posicao == 3:
            bg_color = "blue"  
        elif posicao == 4:
            bg_color = "blue"  
        elif posicao == 5:
            bg_color = "orange"
        elif posicao == 6:
            bg_color = "orange"
        elif posicao == 7:
            bg_color = "green"
        elif posicao == 8:
            bg_color = "green"
        elif posicao == 9:
            bg_color = "green"
        elif posicao == 10:
            bg_color = "green"
        elif posicao == 11:
            bg_color = "green"
        elif posicao == 12:
            bg_color = "green"
        elif posicao == 17:
            bg_color = "red" 
        elif posicao == 18:
            bg_color = "red"  
        elif posicao == 19:
            bg_color = "red"  
        elif posicao == 20:
            bg_color = "red"
        else:
            bg_color = "black"  

        label_time = tk.Label(frame_times, text=f"{posicao}º {time} | Jogos: {stats[8]} | Pontos: {stats[2]} | Vitórias: {stats[5]} | Empates: {stats[6]} | Derrotas: {stats[7]} | Saldo: {saldo_gols} | Gols Feitos: {stats[1]} | Gols Tomados: {stats[0]}", bg=bg_color, fg="white", font=("Arial", 12))
        label_time.pack(anchor="w")

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
    maiorsaldo = -1
    saldoo = ""
    
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
        if stats[1] - stats[0] > maiorsaldo:
            maiorsaldo = stats[1] - stats[0]
            saldoo = time
        if stats[1] > maior: 
            maior = stats[1]
            Artilheiro = time  
        if stats[0] > maiortomados: 
            maiortomados = stats[0]
            Golstomados = time  
    labelArtilheiro = tk.Label(tela_informativa, text=f"O artilheiro do campeonato foi {Artilheiro} com {maior} gols", bg='yellow')
    labelArtilheiro.pack(pady=(10, 10))
    labelTomados = tk.Label(tela_informativa, text=f"O time que tomou mais gols foi o {Golstomados} com {maiortomados} gols tomados", bg='orange')
    labelTomados.pack(pady=(10, 10))
    labelSaldo = tk.Label(tela_informativa, text=f"O time com maior saldo de gols foi {saldoo} com {maiorsaldo} de saldo de gols", bg='purple')
    labelSaldo.pack(pady=(10, 10))
    tela_informativa.mainloop()  

tela_inicial()
