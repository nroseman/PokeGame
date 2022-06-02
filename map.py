class Map:
    def __init__(self, mag, s_w, s_h, t_s) -> None:
        self.image = './img/testMap.png'
        self.width = 40
        self.height = 40
        self.offset = ((s_w/2 - 15 * t_s), (s_h/2 - (5 * t_s)))  # (screen/2)

    def render(self, mag):
        pass
