import tkinter as tk

class BoasVindasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bem-Vindos, FERAS 2024!!!")
        self.centralizarJanela()

        self.label = tk.Label(master, text="Bem-vindo ao Curso de Ciências da Computação!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.buttonProxima = tk.Button(master, text="Mensagenzinha", command=self.abrirSegundaJanela, font=("Arial", 12))
        self.buttonProxima.pack(pady=10)

        self.buttonInformativo = tk.Button(master, text="Informativos", command=self.abrirTerceiraJanela,font=("Arial", 12))
        self.buttonInformativo.pack(pady=10)

    def centralizarJanela(self):
        larguraJanela = 500
        alturaJanela = 200

        larguraTela = self.master.winfo_screenwidth()
        alturaTela = self.master.winfo_screenheight()

        posicaoX = (larguraTela - larguraJanela) // 2
        posicaoY = (alturaTela - alturaJanela) // 2

        self.master.geometry(f"{larguraJanela}x{alturaJanela}+{posicaoX}+{posicaoY}")

    def abrirSegundaJanela(self):
        self.novaJanela = tk.Toplevel(self.master)
        self.novaJanela.title("Mensagenzinha")
        self.centralizarJanelaNova()

        curso = "Ciências da Computação"
        instituicao = "UEPB"

        mensagem = f"""
            Nós do mais recente Centro Acadêmico (CA) de {curso} da {instituicao} 
        gostaríamos de receber nossos primeiros calouros com muito carinho! É um
        prazer ter em nossa comunidade acadêmica vocês que estão prestes a iniciar uma 
        jornada emocionante e desafiadora no campo da computação. 
            Durante este curso, vocês terão a oportunidade de explorar conceitos fundamentais,
        desenvolver habilidades práticas e colaborar em projetos inovadores. O conhecimento
        empírico adquirido ao longo do curso é inestimável! Este é o momento perfeito para se
        envolverem, fazerem perguntas e explorarem novas ideias. Lembrem-se sempre de que estão
        cercados por uma rede de apoio, incluindo professores, monitores e colegas de classe.
            Não hesitem em buscar ajuda quando necessário e aproveitem ao máximo
        todas as oportunidades disponíveis. 
            A galera do Centro Acadêmico está disposta a lhes apoiar durante sua jornada 
        acadêmica. Desejamos a todos um excelente primeiro semestre!
            Bem-vindos novamente! E boa sorte :)
        """

        labelMensagem = tk.Label(self.novaJanela, text=mensagem, justify="left", font=("Arial", 12))
        labelMensagem.pack(padx=1, pady=1)

    def abrirTerceiraJanela(self):
        self.novaJanela = tk.Toplevel(self.master)
        self.novaJanela.title("Dicas")
        self.centralizarJanelaNova()

        mensagem = f"""
           Algumas dicas:

           1. Explore a grade curricular
            ● Antes mesmo das aulas de suas futuras cadeiras começarem, dê uma olhada na 
              introdução dos assuntos, seja por vídeos no YouTube ou PDF's online. Quanto
              mais você se habitua, menos penosas serão as avaliações 

           2. Participe de grupos de estudo e projetos
            ● Encontre grupos que compartilhem interesses semelhantes aos seus. Isso pode
              lhe ajudar não só a entender melhor os conceitos, mas também a formar conexões
              valiosas ao longo do curso e até mesmo além da universidade.
            
           3. Não seja dependente do ChatGPT 
            ● É fato que isso é uma ferramenta fenomenal que nos poupa montes de paciência
              e tempo. Mas não passa de uma ferramenta. O hábito de copiar e colar o que o
              ChatGPT indica é prejudicial para o seu aprendizado, e faz a sua intuição perante
              problemas corriqueiros ficar voltada sempre a recorrer ao Chat e perder cada vez
              mais seu discernimento tão necessário.
            ● Quando seu código rodar, 
            
           4. Participe de eventos e palestras.
            ● Horas complementares são ouro para os universitários. Além de eventos e palestras
              relacionados especificamente à computação, explore também eventos interdisciplinares.
              Muitas vezes, ideias inovadoras surgem da interseção de diferentes áreas do 
              conhecimento.
            
           5. NÃO tenha uma linguagem de estimação!
            ● Sua linguagem favorita não é especial. Todos temos uma que gostamos mais.
              Não se limite desta forma, ok? Questione, pesquise, experimente. O mercado
              é favorável àqueles mais criativos.
            
           6. Busque oportunidades de estágio e trabalho voluntário.
            ● Amenos que você seja um expert cheio de títulos e com um extenso portfólio,
              as oportunidades não irão atrás de você, há menos vagas do que pessoas para
              preenchê-las, por isso, demonstre interesse.
              
           7. Procure orientação acadêmica.
            ● Converse com os professores ao final das aulas, mostre questões que buscou
              resolver se possível, esclareça dúvidas. Isso pode fazer a diferença para uma
              indicação futuramente, viu. Não confie só no Guanabara pra te ajudar nesse começo.
            
           8. Crie e alimente seu portfólio.
            ● Github, Linkedin, etc.
            ● A maioria vai atrás de montar um portfólio quando está desesperada por trabalho,
              evite isso. Ponha no LinkedIn sobre o que está estudando e no GitHub os projetos
              que está desenvolvendo. 
            
        """

        # Cria o widget de texto
        texto = tk.Text(self.novaJanela, wrap="word", font=("Arial", 12))
        texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Adiciona a mensagem ao widget de texto
        texto.insert(tk.END, mensagem)

        # Cria a barra de rolagem
        scrollbar = tk.Scrollbar(self.novaJanela, command=texto.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Vincula a barra de rolagem ao widget de texto
        texto.config(yscrollcommand=scrollbar.set)

    def centralizarJanelaNova(self):
        larguraJanela = 700
        alturaJanela = 300

        larguraTela = self.novaJanela.winfo_screenwidth()
        alturaTela = self.novaJanela.winfo_screenheight()

        posicaoX = (larguraTela - larguraJanela) // 2
        posicaoY = (alturaTela - alturaJanela) // 2

        self.novaJanela.geometry(f"{larguraJanela}x{alturaJanela}+{posicaoX}+{posicaoY}")

def main():
    root = tk.Tk()
    app = BoasVindasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
