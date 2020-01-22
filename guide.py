import system as sys

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

def repair_shop_guide():
    sys.clrscr()
    print('这里有一家修理店')
    print('1. 进去看看')
    print('2. 离开')

def jinja_guide():
    sys.clrscr()
    print('这里是神社')
    print('1. 向巫女搭话')
    print('2. 抽签')
    print('3. 移动')

def school_guide():
    sys.clrscr()
    print('这里是学校')
    print('1. 向同学搭话')
    print('2. 存档')
    print('3. 移动')

def school_talk_guide():
    sys.clrscr()
    print('和谁谈话？')
    print('1. 春树')
    print('2. 离开')