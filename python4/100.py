from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:#kazanın olmadığı ve hiçbir bölmeye tıklanmadığı durumda

        if player == players[0]:#oyuncu eğer x ise

            buttons[row][column]['text'] = player# x i bölmeye yazdır

            if check_winner() is False:#eğer x kazanmazsa diğer oyuncuyu çağır
                player = players[1]
                label.config(text=(players[1]+" turn"))#üstteki ekranda yazdır

            elif check_winner() is True:#eğer x kazanırsa kazandığını yazdır(true ve false değerleri check_winner fonkisyonundaki sonuçla gelecek)
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":#hiçkimsenin kazanamadığı durum
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player#oyuncu 'o' ise

            if check_winner() is False:#eğer kazanamazsa 'x' i yazdır
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:#eğer kazanırsa 'o' yazdır
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":#eğer yazanan yoksa 'tie'
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":#yatay durumdaki blokların eşleşme durumu
            buttons[row][0].config(bg="green")#eşleşiyorsa yeşile çevir
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":#düşey durumdaki blokların eşleşme durumu
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":#çarpraz durumdaki blokların eşleşme durumu
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":#sağ çapraz durumdaki blokların eşleşme durumu
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:#açılmamış blok olmadığı durumda

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")#butonları sarıya çevir
        return "Tie"

    else:#diğer durumlar için false döndür
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:#eğer tüm bloklar doluysa false döndür
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")#yeni oyun oluştur ve en alt satıra git işlemi tekrarla


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]#oyuncular
player = random.choice(players)
buttons = [[0,0,0],#ekran şekli
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")#en üstteki oyuncu sırası

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")#oyunu sıfırlama butonu

frame=Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))#fonksiyonu çağır
        buttons[row][column].grid(row=row,column=column)#her bir bölmeyi ayarla

window.mainloop()





















