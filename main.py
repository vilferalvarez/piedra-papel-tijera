import random


def get_choices():
  player = input("Elija una opcion (piedra, papel o tijera: )")
  opciones = ["piedra", "papel", "tijera"]
  computer = random.choice(opciones)
  return {"player": player, "computer": computer}



def check_win(player,computer):
  if player==computer:
    print("Es un empate")
  elif player.lower()=="piedra":
    if computer.lower()=="tijera":
      print ("¡ Gataste !")
    else:
      print ("Perdiste  :( \n")
  elif player.lower()=="papel":
    if computer.lower()=="piedra":
      print ("¡ Gataste !")
    else:
      print ("Perdiste  :( \n")
  elif player.lower()=="tijera":
    if computer.lower()=="papel":
      print ("¡ Gataste !")
    else:
      print ("Perdiste  :( \n")
  
  print (f"Jugador:{player}; Computador: {computer}")



next=True
while next==True:
  jugada=get_choices()
  check_win(jugada["player"],jugada["computer"])
  resp=input("Desea realizar otra jugada? (Y/N):")
  if resp.lower()=="y":
    next=True
  else:
    next=False
    print("! Adiós ¡")
  






