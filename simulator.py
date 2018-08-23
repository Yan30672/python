import lol_model1
import lol_model2
import numpy as np

health = int(input('請輸入敵方血量:'))
armor = int(input('請輸入敵方物防:'))
mr = int(input('請輸入敵方魔防:'))
lv = int(input('請輸入等級:'))

cham = lol_model1.champion(lv, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
bot = lol_model2.Enemy(health, armor, mr)

#使用英雄
cham.Jayce(1)

#寫入裝備 無盡需放最後
cham.blade_of_ruined_king(1)
cham.lord_dominiks_regards(0)
cham.youmuus_ghostblade(0)
cham.duskblade(0)
cham.edge_of_night(0)
cham.deaths_dance(0)
cham.the_bloodthirster(0)
cham.essence_reaver(0)
cham.phantom_dancer(0)
cham.rapid_firecannon(0)
cham.statikk_shiv(0)
cham.infinity_edge(0)

# 計算面板攻速、物理攻擊以及敵方實際物防
cham.AS += (cham.lv - 1) * 0.03 * cham.AS
cham.ad += (cham.lv - 1) * 3.5
bot.armor = bot.armor*(1-cham.pen)-cham.le

#調整爆擊溢出
def p(cham):
    if cham.crit > 1:
        return 1
    else:
        return cham.crit


print('總花費：{}'.format(cham.cost))
print('物理攻擊：{}，物理致命：{}，物理穿透：{}，攻速：{}，爆擊機率：{}'.format(cham.ad,cham.le,cham.pen,cham.AS,p(cham)))

n = int(input('請輸入攻擊次數:'))
times = n / cham.AS

# 設計傷害函數
damage = 0
number = 0

while number != n:
    c = np.random.binomial(1, p(cham), size = None)
    if c == 1:
        print('第{}下爆擊了!'.format(number+1))
        if cham.ie == 1:
            damage += 2*cham.ad*0.15 \
                      +2*cham.ad*0.85*(100/(100+bot.armor)) \
                      +2*cham.ex1 * 0.15 \
                      +2*cham.ex2*0.85*(100/(100+bot.mr)) \
                      +cham.chd*health*(100/(100+bot.armor)) \
                      +cham.ex1 * (100/(100+bot.mr))
            print('第{}下傷害為{}'.format(number+1, 2*cham.ad*0.15 \
                      +2*cham.ad*0.85*(100/(100+bot.armor)) \
                      +2*cham.ex1 * 0.15 \
                      +2*cham.ex2*0.85*(100/(100+bot.mr)) \
                      +cham.chd*health*(100/(100+bot.armor)) \
                      +cham.ex1 * (100/(100+bot.mr))))
            health -= 2*cham.ad*0.15 \
                      +2*cham.ad*0.85*(100/(100+bot.armor)) \
                      +2*cham.ex1 * 0.15 \
                      +2*cham.ex2*0.85*(100/(100+bot.mr)) \
                      +cham.chd*health*(100/(100+bot.armor)) \
                      +cham.ex1 * (100/(100+bot.mr))
            if health <= 0:
                health = 0
            else:
                health += 0
            print('第{}下傷害後，敵方剩下{}血量'.format(number+1,health))
        else:
            damage += 2*cham.ad*(100/(100+bot.armor)) \
                      + cham.ex1 * (100 / (100 + bot.mr)) \
                      + 2*cham.ex2 * (100 / (100 + bot.mr)) \
                      + cham.chd * health * (100 / (100 + bot.armor))
            print('第{}下傷害為{}'.format(number + 1, 2*cham.ad*(100/(100+bot.armor)) \
                      + cham.ex1 * (100 / (100 + bot.mr)) \
                      + 2*cham.ex2 * (100 / (100 + bot.mr)) \
                      + cham.chd * health * (100 / (100 + bot.armor))))
            health -= 2*cham.ad*(100/(100+bot.armor)) \
                      + cham.ex1 * (100 / (100 + bot.mr)) \
                      + 2*cham.ex2 * (100 / (100 + bot.mr)) \
                      + cham.chd * health * (100 / (100 + bot.armor))
            if health <= 0:
                health = 0
            else:
                health += 0
            print('第{}下傷害後，敵方剩下{}血量'.format(number + 1, health))
    else:
        print('第{}下沒爆擊!'.format(number + 1))
        damage += cham.ad*(100/(100+bot.armor)) \
                      + cham.ex1 * (100 / (100 + bot.mr)) \
                      + cham.ex2 * (100 / (100 + bot.mr)) \
                      + cham.chd * health * (100 / (100 + bot.armor))
        print('第{}下傷害為{}'.format(number + 1, cham.ad*(100/(100+bot.armor)) \
                      + cham.ex1 * (100 / (100 + bot.mr)) \
                      + cham.ex2 * (100 / (100 + bot.mr)) \
                      + cham.chd * health * (100 / (100 + bot.armor))))
        health -= cham.ad*(100/(100+bot.armor)) \
                      + cham.ex1 * (100 / (100 + bot.mr)) \
                      + cham.ex2 * (100 / (100 + bot.mr)) \
                      + cham.chd * health * (100 / (100 + bot.armor))
        if health <= 0:
            health = 0
        else:
            health += 0
        print('第{}下傷害後，敵方剩下{}血量'.format(number + 1, health))

    number += 1

dps = damage / times

print('攻擊歷時{}秒鐘'.format(times))
print('一共對敵人造成{}傷害'.format(damage))
print('敵人最後剩下{}血量'.format(health))
print('每秒傷害量：{}'.format(dps))
print('每單位金錢買到的dps；{}'.format(dps / cham.cost))