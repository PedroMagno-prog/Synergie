from core.dice_roller import roll_XdY, roll_XdY_eZ

print("Rolando 1d10 com Vantagem/Explosão: ")

print(f"Rolando dano entre 1 a 8d6: \n"
      f"1d6 = {roll_XdY(1, 6)}"
      f"2d6 = {roll_XdY(2, 6)}"
      f"3d6 = {roll_XdY(3, 6)}"
      f"4d6 = {roll_XdY(4, 6)}"
      f"5d6 = {roll_XdY(5, 6)}"
      f"6d6 = {roll_XdY(6, 6)}"
      f"7d6 = {roll_XdY(7, 6)}"
      f"8d6 = {roll_XdY(8, 6)}")