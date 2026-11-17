# 1-m
class Hayvon:
    def __init__(self, nom, yosh):
        self.nom = nom
        self.yosh = yosh

    def malumot(self):
        print(f"Nomi: {self.nom}")
        print(f"Yoshi: {self.yosh}")


class It(Hayvon):
    def __init__(self, nom, yosh, zot):
        super().__init__(nom, yosh)
        self.zot = zot

    def malumot(self):
        super().malumot()
        print(f"Zoti: {self.zot}")


it = It("REX", 3, "Ovcharka")
it.malumot()
