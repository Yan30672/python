class champion:
    def __init__(self, lv, ad, le, pen, AS, crit, chd, ex1, ex2, ie, cost):
        self.lv = lv
        self.ad = ad
        self.le = le
        self.pen = pen
        self.AS = AS
        self.crit = crit
        self.chd = chd
        self.ex1 = ex1
        self.ex2 = ex2
        self.ie = ie
        self.cost = cost

    # 英雄列表
    def Jayce(self, item):
        if item == 1:
            self.ad += 58
            self.AS += 0.658
        else:
            pass

    # 裝備屬性
    def blade_of_ruined_king(self, item):
        if item == 1:
            self.ad += 40
            self.chd += 0.08
            self.cost += 3200
            self.AS = 1.25 * self.AS
        else:
            pass

    def lord_dominiks_regards(self, item):
        if item == 1:
            self.ad += 40
            self.pen += 0.35
            self.cost += 2800
        else:
            pass

    def youmuus_ghostblade(self, item):
        if item == 1:
            self.ad += 55
            self.le += 18
            self.cost += 2900
        else:
            pass

    def duskblade(self, item):
        if item == 1:
            self.ad += 55
            self.le += 18
            self.cost += 2900
        else:
            pass

    def edge_of_night(self, item):
        if item == 1:
            self.ad += 55
            self.le += 18
            self.cost += 3100
        else:
            pass

    def deaths_dance(self, item):
        if item == 1:
            self.ad += 80
            self.cost += 3500
        else:
            pass

    def the_bloodthirster(self, item):
        if item == 1:
            self.ad += 80
            self.cost += 3500
        else:
            pass

    def essence_reaver(self, item):
        if item == 1:
            self.ad += 70
            self.cost += 3200
        else:
            pass

    def infinity_edge(self, item):
        if item == 1:
            self.ad += 80
            self.crit = 2 * self.crit
            self.cost += 3600
            self.ie += 1
        else:
            pass

    def phantom_dancer(self, item):
        if item == 1:
            self.crit += 0.3
            self.AS = 1.45 * self.AS
            self.cost += 2800
        else:
            pass

    def rapid_firecannon(self, item):
        if item == 1:
            self.AS = 1.3 * self.AS
            self.crit += 0.3
            self.ex1 += 60 + (80 / 17) * self.lv
            self.cost += 2900
        else:
            pass

    def statikk_shiv(self, item):
        if item == 1:
            self.AS = 1.35 * self.AS
            self.crit += 0.3
            self.ex2 += 60 + (80 / 17) * self.lv
            self.cost += 2900
        else:
            pass