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
  In this code part, I put the function for add the matchs of the teams, first have the global variable 'jogos_por_time' in this variable have the dictionary of the determined team, this dictionary is responsible for save all matchs of the teams, it appared in the function responsible for matchs simulate, is there that save the results.

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
