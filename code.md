Here, I will write about the code and the functions of it, I will try explain how the code work exactly, I will go write in the code in the screen appear order.

# Bet mode and edition selector
The first thing that you go see in the code is the screen of edition selector, over there, you can select the year of the championchip that you want simulate and turn on or turn down the bet mode

![image](https://github.com/user-attachments/assets/cf9ffe4e-7934-4b59-adf1-67bdc0d01243) 

- Check it, this is the first screen of the software, you can click in the year which you want, until now, have only 2 years, 2024 and 2025.
  
- In this screen you can turn on the bet mode, just click and the bet mode will go turn on, if you change your mind and turn down this, just click again.
  
  tela_selecao_edicao
  ---
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
  # If the bet mode is activated
  After the user turn on the bet mode, will appaer a login screen, the user need make the login

This function is responsible to open the first screen of the code, actually, this function start the work of code. with this functions work, the user can choose which year want simulate and if the user want or no the bet mode turned on, actually this function is very simple and after it call the function select_edition, this function must recive a parameter, about the year of the edition, if the user click in 2024, the parameter will be 2024, if click in 2025, parameter will be 2025.
This function also is responsible to turn on the bet mode, look the variable 'btn_modo_aposta' in the code, this variable talk about the bet mode, if the user click, the function 'toggle_bet_mode' will turn on, if the user click again, the function will change the boolan number of bet mode, after I say more about this function.

