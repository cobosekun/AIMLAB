import pyxel
import pyautogui as pag

class App:
  def __init__(self, target_size, target_color) -> None:
    self.width, self.height = self.get_windowsize(magnification=6)
    pyxel.init(self.width, self.height, title="AIMLAB", fps=120)
    pyxel.load("assets/aimlab.pyxres")
    pyxel.mouse(True)
    self.target_x, self.target_y = self.random_coordinates()
    self.target_size = target_size
    self.target_color = target_color
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

  def draw(self):
    
    # 起動画面
    pyxel.cls(0)
    pyxel.text(self.width/2 - 22, self.height/2 - 10, "A I M L A B", 12)
    pyxel.text(self.width/2 - 50, self.height/2 + 5, "- PRESS Enter to START -", 12)
    
    if pyxel.btnp(pyxel.KEY_RETURN) is True: # ToDo returnの瞬間だけしか分岐に入らない
      pyxel.cls(7)
      pyxel.circ(self.target_x, self.target_y, self.target_size, self.target_color)
      pyxel.circ(160 / 2, 120 / 2, 10, 14)


  def get_windowsize(self, magnification: int = 1):
    self.target_x, self.target_y = pag.size()
    return self.target_x//magnification, self.target_y//magnification

  def random_coordinates(self):
    self.x = pyxel.rndi(100, self.height - 100)
    self.y = pyxel.rndi(100, self.width - 100)
    return self.x, self.y
  
  # @staticmethod
  # def color_palette(color: str) -> int:
  #   color_palette = {
  #     "Black" : 0,
  #     "" : 1,
  #     "" : 2,
  #     "" : 3,
  #     "" : 4,
  #     "" : 5,
  #     "" : 6,
  #     "" : 7,
  #     "" : 8,
  #     "" : 9,
  #     "" : 10,
  #     "" : 11,
  #     "" : 12,
  #     "" : 13,
  #     "" : 14,
  #     "" : 15,
  #   }
  

if __name__ == "__main__":
  App(5, 8)
  
# 起動画面を作る。