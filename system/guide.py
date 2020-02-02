from system import control


def show_inst():
    control.clrscr()
    print('1. 新游戏')
    print('2. 读取游戏')
    print('3. 设置')
    print('4. 离开')

def move_guide():
    control.clrscr()
    print('移动到: ')
    print('1.家')
    print('2.神社')
    print('3.河边')
    print('4.学校')
    print('5.街道')

def house_guide():
    control.clrscr()
    print('现在在家')
    print('1. 保存')
    print('2. 移动')
    print('3. 学习')
    print('4. 睡觉')
    print('5. 查看信息')

def repair_shop_guide():
    control.clrscr()
    print('这里有一家修理店')
    print('1. 进去看看')
    print('2. 离开')

def jinja_guide():
    control.clrscr()
    print('这里是神社')
    print('1. 向巫女搭话')
    print('2. 拜神')
    print('3. 移动')

def school_guide():
    control.clrscr()
    print('这里是学校')
    print('1. 向同学搭话')
    print('2. 去图书馆')
    print('3. 存档')
    print('4. 移动')

def school_talk_guide():
    control.clrscr()
    print('和谁谈话？')
    print('1. 春树')
    print('2. 离开')

def river_guide():
    control.clrscr()
    print('这里是河边')
    print('1. 去修理店')
    print('2. 离开')

def repair_shop_guide():
    control.clrscr()
    print('这里是修理店')
    print('1. 购买')
    print('2. 修理')
    print('3. 出售')
    print('4. 离开')
    print('5. 交谈')

def street_guide():
    control.clrscr()
    print('这里是街道')
    print('1. 诊所')
    print('2. 快餐店')
    print('3. 离开')
    print('4. 对话')

def stranger_talk_guide():
    control.clrscr()
    print('和谁说话？')
    print('1. 紫苑')
    print('2. 离开')

def clinic_guide():
    control.clrscr()
    print('这里是诊所')
    print('1. 买药')
    print('2. 离开')
    print('3. 交谈')

def fast_food_guide():
    control.clrscr()
    print('这里是快餐店')
    print('1. 买东西')
    print('2. 快餐店挑战活动')
    print('3. 离开')

def star_event_1_guide():
    print('看到了巫女灵梦一个人在空地窝着不知道在干什么')
    print('从后面走近了...')
    print('被灵梦注意到了')
    control.press()
    print('灵梦：没看到过的脸啊，新来的？')
    print('点了点头')
    print('灵梦：我是这的巫女，如你所见，这神社基本没人来的')
    print('所以也没什么香火钱，我都穷的吃土了')
    print('要是你愿意捐助我1w块我就很高兴了')
    print('要捐款嘛?')

def star_event_2_guide():
    print('看到了巫女灵梦一个人在空地窝着不知道在干什么')
    print('从后面走近了...')
    print('被灵梦注意到了')
    control.press()
    print('灵梦：又是你啊')
    print('现在经济不景气，神社开销又很大，这不，又要吃土了')
    print('所以你愿意再捐助我3w块嘛？')

def star_event_3_guide():
    print('看到了巫女灵梦一个人在空地窝着不知道在干什么')
    print('从后面走近了...')
    print('被灵梦注意到了')
    control.press()
    print('灵梦：你又来啦')
    print('哎，又发生了很多事。。。')
    print('所以你愿意再捐助我6w块嘛？')

def star_get_coop_guide():
    print('怎么有你这种烂好人呢，也不怕被人骗嘛')
    print('没办法，既然你帮我这么多次，我也得照顾照顾你')
    print('遇到什么麻烦可以跟我说，钱的事我解决不了')
    print('其它事大体上还是能解决的，别小看了巫女啊')
    print('-----结识了巫女：灵梦-----')