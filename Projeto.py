from PySimpleGUI import PySimpleGUI as sg
#layout
def interface():
    sg.theme('DarkBlue7')
    x = input()
    y = input()
    layout = [
        [sg.Text('E-mail'),sg.Input(key=x,size=(20,1))],
        [sg.Text('Senha'),sg.Input(key=y,password_char="*",size=(20,1))],
        [sg.Checkbox('Salvar o Login?')],
        [sg.Button('Entrar')]
    ]
    #janela
    janela = sg.Window('Tela de Login', layout)
    #ler os eventos 
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Entrar':
            print("Bem vindo")

if(__name__ == "__main__"):        
    interface()

