This Code is one Simulator of Brazil Soccer Championship, in this code we have some interesting things, like the goal method, all teams have a number in dictionary, this number represent the goal chances of this team, like, see the team 'Botafogo', he have 6 chance of goal, but, chance of goal dont mean is goal, is just a chance, in function 'Simular_Jogo', the team is placed in situation of goal, and one command random with 30% of chance of goal decide it, if True = goal of team, if False = the team lose the goal.
  # The docs with all matchs
  - This code too create one docs with result of all match of the championship, this docs going to updated all times after one round, and you can see the results of this round, all rounds have they number on top her, please, after the execution, delete de docx, because I didn´t create one method of automatic delete, thx ^^
# Problems
- Of course, this code have some problems, and I can see it, but look, I really tried create one code with a minimum problem possible, now I´m going to list the problems I found in this code, if you want help me, fell free and you have my grateful ^^
- the first problem I found is the incorrect assignment of round, have teams playing two times in the round, all knows the teams can´t play two times. I didn´t create one function that checks if the team played, because is more difficulty than you think, if you write a code that verifies if the teams played, one moment you will stay with one round with just teams that played, and your code go stop work or return just some games, like, we need 10 games in all rounds, imagine your code return all 10 games, but in round 33 (just imagine kappa) dont have enouth teams for play, your code will stop working or return just some games, in test that I made, in the round 12 my code return just 8 games, because or the other teams go play 2 games for round or dont have teams enough, with this, I just want make you knows, it is difficulty, but you think you a better coder than me, fell free again ^^
- Another problems is the organization of front-end tabble, like, see the team 'America-MG', it´s going to be in top in all simulations, it happens because I didn´t make something for organization of this. Actually, I didn´t try and I dont have idea for how to make this, if you want make this for me, I would be very grateful.  // it is fixed, I did change in functions, now, the code put the labels of team after get the position of team - fixed
- Look, if you se other problem, you report for my email 'nagatofx3@hotmail.com', not so problem, you can tell me about one thing you think is good for code or one change, all things about code, if you want ask me about code, fell free too ^^^

I know, probaly the code have more problems, but I dont found. The frond-end is simple, I think in python is difficulty for beautiful front end HAHA.

# Changes I want make

- I really liked of the result of this code and I want make some changes in this, I´m gonna list some changes that I thought:
- I want to make the option after the simulator, the user can simulator the Libertadores Cup too, but for this, I need one simulation of Argentina League, because the Libertadores Cup use teams of all country of south america, I just want to put the teams of Argentina, in the moment I think to put the teams generics of other countrys, (real teams only for Brazil and Argentica)
- Another change I was think is the put one system of defense of the teams, for this I need a buff in number of goals, I think about this because some teams have good defensive stats, with it in mind, I can devolper one system of this, is just a some changes in function "Simular_Jogo", actually, I was change this, I think in final of today, this will be uptade


# Changes I made (octuber)
- In this month I did make some changes, for exemple, the exit button, I put one button in first screen for user can exit the app, actually, I made this after one friend report this for me, he talked "exit the aplication using alt + f4 is bad", this is simple function and I dont cast much time for make this HAHA
- Another change I did make is the screen of all games of the selected team, the user can go in button write "Abrir tela de Jogos", after this, one screen with buttons white all teams going to appared, User click in one team and all matchs of the selected team will appear in him screen
- In another commit I remember I talked about one system of defense of the team, I made this and now the teams have too one system of defense, I inspired of the real Brazil League and the most strong system defense of the teams are of 'Palmeiras', In real league is the team with less goals taked, actually, I try balanced the all teams, for all team have a real chance of win the League, but its not possible, we know that have stronger teams, like 'Palmeiras', 'Botafogo', 'Flamengo', 'Internacional', have too weaker teams like 'Atletico-GO', 'Vitoria', 'RB Bragantino', I referenced of the real league and is the more strongs and more weaks of the real league. But have one great point, the simulator is very similar of the real table, in this moment of I commited this the teams "Botafogo" is the first of league, if you simulate 3 times you will see the "Botafogo" will win one time, and the 'Palmeiras' and 'Flamengo' will be G4 almost ever time.
- Now I put some sytem of the count of wins of the home wins of the teams, is will appear in infromation of league also the screen of teams matchs

# code explanation
  # carregar_jogos
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
  In this code part, I put the function for add the matchs of the teams, first have the global variable 'jogos_por_time' in this variable have the dictionary of the determined team, this dictionary is responsible for save all matchs of the teams, it appear in the function responsible for matchs simulate, is there that save the results.

# criar_telas_jogos
    def criar_tela_jogos():
      tela_times = tk.Tk()
      tela_times.title("Escolha um Time")
      tela_times.geometry("400x750")
    
      for time in times.keys():
          botao_time = tk.Button(tela_times, text=time, command=lambda t=time: mostrar_jogos(t))
          botao_time.pack(pady=5)
      
      tela_times.mainloop()
Here, I put the function that make screen with buttons with all teams, have one button of each team,, if you know about tk library, I have sure you know the command geomatry, title, tk, button and mainloop, the loop in 'for' is for creat one button for all teams.
# mostrar_jogos
    def mostrar_jogos(time):
        tela_jogos = tk.Tk()
        tela_jogos.title(f"Jogos de {time}")
        tela_jogos.geometry("400x500")

        jogos = jogos_por_time.get(time, [])
    
        max_jogos = 38
        label_aviso = tk.Label(tela_jogos, text=f"Total de jogos: {len(jogos)} (Máximo: {max_jogos})\n Posição do time: {times[time][0]}\n Vitorias em casa: {times[time][10]}\n Derrotas em casa: {times[time]      [11]}", font=("Arial", 10), fg="red")
        label_aviso.pack(pady=(10, 0))

        if len(jogos) < max_jogos:
                label_aviso.config(text=f"Total de jogos: {len(jogos)} (Máximo: {max_jogos})\n Posição do time: {times[time][4]}\n Vitorias em casa: {times[time][10]}\n Derrotas em casa: {times[time][11]}", font=("Arial", 10), fg="red")
        if not jogos:
            label_aviso = tk.Label(tela_jogos, text="Nenhum jogo encontrado.", font=("Arial", 10), fg="red")
            label_aviso.pack(pady=(10, 0))
        if jogos:
            for i, jogo in enumerate(jogos[:max_jogos]):
                label_jogo = tk.Label(tela_jogos, text=jogo, font=("Arial", 6))
                label_jogo.pack(anchor="w")

        btn_fechar = tk.Button(tela_jogos, text="Fechar", command=tela_jogos.destroy)
        btn_fechar.pack(pady=10)


This function is for screen the matchs of each team, all times the user click in one button with team, this function start work, look, if the user click more times in button, this function screen the matchs screen very times, actually, I was thinking to make a way check if the screen of the one team already open, the other (if it had been opened, obviously) close, but I did´nt make this because I have laziness HAHA ^^

# tela_inicial
    def tela_inicial():
        global frame_times, labels_times, rodadas_label, btn_simular, rodadas

        tela_inicial = tk.Tk()
        tela_inicial.configure(bg="black")
        tela_inicial.title("Simulator Brasileirão")
        tela_inicial.attributes("-fullscreen", True)
        btn_fechar = tk.Button(tela_inicial, text=" X ", command=tela_inicial.destroy, bg="white", fg="black")
        btn_fechar.place(relx=1.0, y=10, anchor='ne')
        label_introducao = tk.Label(tela_inicial, text="Bem-vindo ao Simulador de Brasileirão", bg="black", fg="white", font=("Comic Sans", 16))
        label_introducao.pack(pady=20)

        frame_times = tk.Frame(tela_inicial, bg="black")
        frame_times.pack(pady=20)

        labels_times = {}

        rodadas_label = tk.Label(tela_inicial, text=f"Rodadas restantes: {rodadas}", bg="black", fg="white", font=("Arial", 14))
        rodadas_label.pack(pady=10)

        btn_simular = tk.Button(tela_inicial, text="Simular Próxima Rodada", command=simular_rodada, bg="white", fg="black", font=("Arial", 14))
        btn_simular.pack(pady=10)

        abrir_tela_jogos = tk.Button(tela_inicial, text="Abrir telas De Jogos", command=criar_tela_jogos, bg="orange", fg="black", font=("Arial", 14))
        abrir_tela_jogos.pack(pady=10)
    
        tela_inicial.mainloop()
This function is the first screen that appear for the user, in this, is list all teams and they stats, the labels that have will be update all times the user click int he button "Simular Proxima Rodada", this screen have the close button too and the the button "Abrir telas De Jogos" this button open the screen of function "criar_telas_jogos".
In this screen, if the user simulate all rounds, will go trade the button "Simular Proxima Rodada" for "Mostrar Informações do Campeonato", if the user click in this button, will appear the screen with the simulate informations.

# iniciar_simulacao
    def iniciar_simulacao(nome_arquivo="placares_jogos.txt"):
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)
            print(f"Arquivo '{nome_arquivo}' excluído para nova simulação.")
Here, is the function of the start of the simulation, actually, this don´t make much things for the simulate, just delete the arquive with the matchs, look, this function just make something if the file for the games already existing

# simular_rodada
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
This function is for simulate the round, here the round is simulate, the function for tabble organization is called. If the variable that keeper the number of all round is arrive 0, the function call the function for send congratiluation for the champion team.
# simular_jogo
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
This function is the most complex of the code, here the system of the goal and defense start work, the system of home team too, some variable with the information of team are added, here determine what team win, if you wanna the simulate have more goals, you can change the chances of goal and defense, but look, I put this numbers because I think in this form the number of goals of the winner team is so realist, if you see the four last team, you can see they made so few goals, I was thinking one form to make they make more, I know this is desbalanced.

