from system import control as sys


def show_inst():
    sys.clrscr()
    print('1. 新游戏')
    print('2. 读取游戏')
    print('3. 设置')
    print('4. 离开')

def move_guide():
    sys.clrscr()
    print('移动到: ')
    print('1.家')
    print('2.神社')
    print('3.河边')
    print('4.学校')
    print('5.街道')

def house_guide():
    sys.clrscr()
    print('现在在家')
    print('1. 保存')
    print('2. 移动')
    print('3. 学习')
    print('4. 睡觉')
    print('5. 查看信息')

def repair_shop_guide():
    sys.clrscr()
    print('这里有一家修理店')
    print('1. 进去看看')
    print('2. 离开')

def jinja_guide():
    sys.clrscr()
    print('这里是神社')
    print('1. 向巫女搭话')
    print('2. 拜神')
    print('3. 移动')

def school_guide():
    sys.clrscr()
    print('这里是学校')
    print('1. 向同学搭话')
    print('2. 去图书馆')
    print('3. 存档')
    print('4. 移动')

def school_talk_guide():
    sys.clrscr()
    print('和谁谈话？')
    print('1. 春树')
    print('2. 离开')

def river_guide():
    sys.clrscr()
    print('这里是河边')
    print('1. 去修理店')
    print('2. 离开')

def repair_shop_guide():
    sys.clrscr()
    print('这里是修理店')
    print('1. 购买')
    print('2. 修理')
    print('3. 出售')
    print('4. 离开')
    print('5. 交谈')

def street_guide():
    sys.clrscr()
    print('这里是街道')
    print('1. 诊所')
    print('2. 快餐店')
    print('3. 离开')
    print('4. 对话')

def stranger_talk_guide():
    sys.clrscr()
    print('和谁说话？')
    print('1. 紫苑')
    print('2. 离开')

def clinic_guide():
    sys.clrscr()
    print('这里是诊所')
    print('1. 买药')
    print('2. 离开')
    print('3. 交谈')

def fast_food_guide():
    sys.clrscr()
    print('这里是快餐店')
    print('1. 买东西')
    print('2. 快餐店挑战活动')
    print('3. 离开')
