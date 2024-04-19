import pyxel

class App:
  def __init__(self) -> None:
    pyxel.init(160,120)
    self.x = 0
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

  def draw(self):
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

if __name__ == "__main__":
  import pyxel
  pyxel.init(160, 120)
  pyxel.cls(1)
  pyxel.circb(60, 60, 40, 7)
  pyxel.show()