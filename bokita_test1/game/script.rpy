# 游戏的脚本可置于此文件中。

# 声明使用到的人物立绘

layeredimage kita1:
    
    group base:
        attribute s1 default:
            "kita base1"
        attribute s2:
            "kita base2"

    group flush:
        attribute f0 default:
            "kita f0"
        attribute f1:
            "kita f1"

    group leftarm:
        attribute a1 default:
            "kita a1"
        attribute a2:
            "kita a2"
        attribute a3:
            "kita a3"

    group mouth:
        attribute m1 default:
            "kita m1"
        attribute m2:
            "kita m2"
        attribute m3:
            "kita m3"
        attribute m4:
            "kita m4"
        attribute m5:
            "kita m5"
        attribute m6:
            "kita m6"
        attribute m7:
            "kita m7"
        attribute m8:
            "kita m8"
        attribute m9:
            "kita m9"
        attribute m10:
            "kita m10"
        attribute m11:
            "kita m11"
        attribute m12:
            "kita m12"
        attribute m13:
            "kita m13"
        attribute m14:
            "kita m14"
        attribute m15:
            "kita m15"
        attribute m16:
            "kita m16"

    group brow:
        attribute b1 default:
            "kita b1"
        attribute b2:
            "kita b2"
        attribute b3:
            "kita b3"
        attribute b4:
            "kita b4"
        attribute b5:
            "kita b5"
        attribute b6:
            "kita b6"
        attribute b7:
            "kita b7"
        attribute b8:
            "kita b8"
 
    group eyes:
        attribute e1 default:
            "kita e1"
        attribute e2:
            "kita e2"
        attribute e3:
            "kita e3"
        attribute e4:
            "kita e4"
        attribute e5:
            "kita e5"
        attribute e6:
            "kita e6"

image kita:
    "kita_test.png"
    zoom 1.3

image bocchi:
    "bocchi.png"
    zoom 0.67

image bg:
    "bg.png"
    zoom 2
    
image bg 2:
    "bg_2.png"
    zoom 2

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define bc = Character('后藤一里',color="#e47f90")
define bci = Character('', what_color= "#e47f90")
#define b_inner = Character('后藤一里', color="#FFC0CB",what_prefix="(",what_suffix=")")
define kt = Character('喜多郁代',color="#FF0000")
define 观众 = Character('观众',color="#000000")
define 其他同学 = Character('其他同学',color="#000000")
define 店长 = Character('店长',color="#d6ed46")
# 游戏在此开始。

label start:

    #电车上 正在准备上学 波奇
    scene bg with None
    show bocchi at center 
    bci "……"
    bci "今天是忧郁的周一"
    bci "……不想上学"
    bci "后藤一里。没有朋友，没有交际，学习也很一般。衣服上说不定还有壁橱的霉味，想装病骗前辈旷工结果真的病了两天搞得一塌糊涂的后藤一里，就是如此糟糕的我。"
    bci "要说为什么不趁机多请假还要上学的话……"
    bci "不去上学就会被全班忘记，然后好不容易积蓄的微薄存在感会全部毁于一旦，那样就非常糟糕。"
    bci "……当然还有一点原因……因为学校有一个很在意的孩子。一个前段时间不由注意到的孩子。"
    bci "第一次见到她是一个昏昏沉沉的午后。什么都很无聊，没有邀约没有朋友的无聊放学。"
    bci "然后她轻巧的跑到了班门口那里，似乎是被朋友叫住了。真的是肉眼可见的有活力……"
    bci "发鬓和衣领有点湿，眼睛很亮。红色的头发很好看"
    bci "熟练的和朋友打招呼，然后和她们约好了要去下次KTV。"
    bci "夕阳洒在她的脸上，很好看"
    bci "我从她朋友的称呼知道她叫喜多。不，应该说我经常会听到她们聊天的时候提到这个名字，只是我第一次知道"
    bci "这个名字对应的，是这么可爱的女孩子。又受欢迎运动有好又超级可爱！"
    bci "最重要的！她背着吉他！而且而且，从她们去KTV的对话来看，好像唱歌非常好听！会弹吉他，唱歌好听，说不定也是个乐队女孩！"
    bci "真好啊，如果我要也可以变得像喜多一样……"

    #幻想场景 演唱会
    scene bg 2 with fade
    show bocchi at center 
    bc "呀吼！各位！这里是大家最爱的小一里哦！"
    观众 "一里！一里！一里！"
    bc "跟着一里~一起度过快乐的演唱会吧~"
    观众 "哦！！！"
    #幻想场景 演出结束
    scene bg 2 with fade
    show bocchi at center 
    bc "老板，给我来一份卡基芬尔兰斯诺特的特调口味，要特调。"
    店长 "什么？那可是我们独家秘传的超级口味！不愧是后藤一里，果然神通广大！我知道了，这就去准备……"

    #回到现实 电车上 正在准备上学 波奇
    scene bg with None
    show bocchi at center
    bci "这，这简直太完美了！这是社恐梦寐以求的梦想啊！真的好羡慕，为什么会有这么完美的好孩子！"
    bci "如果可以成为朋友，我是不是也可以沾染这样的气息，然后变成这样耀眼的人？然后变成super star！"
    bci "……上学似乎没这么无趣了。"
    bci "说不定喜多还能和我一起加入结束乐队，虹夏好像说过差一个主唱，喜多同学绝对超级合适。然后天天和喜多排练，然后变得像那样的闪闪发光……"
    bci "不过仔细想想，喜多那么闪耀的人，一定有自己的乐队吧，说不定背地里还是个名歌手……这不是还没开始就结束了，我这种和螨虫一个段位的存在怎么可以去和这样的……"
    bc "等等！"
    bc "我前几天不是已经在繁星顺利打工了？！说不定我现在已经比螨虫厉害了！结束乐队差一个主唱，我可以！"
    bc "对！后藤一里！你现在是可以完成在酒吧打工这种高难度任务的人了！是成熟的乐队girl！没有问题的！"
    "播报声下一站，京急鹤见。本列车终点站为……"
    bc "好了！今天的学校生活，要充实起来了！"

    #学校秘密空间 午休 波奇 喜多 其他同学
    scene bg with None
    show bocchi at center 

    bc "今天也是在秘密空间吃便当的悠闲时光呢~"
    bc "像我这样只比螨虫高一段位的家伙去邀请喜多入乐队还是太难了对吧~"
    bc "而且喜多同学那么可爱又活跃，想必已经有乐队了吧，是哟，就这样吧，就这样悠闲的度过今天吧，啊哈哈哈，啊哈哈哈……"

    hide bocchi
    其他同学 "喜多桑~"
    
    show bocchi:
        xalign -0.2 #left =  0.0, right = 1.0 you can go higher than 1.0 to move it off screen or the right and a negeative number to move it off screen on the left
        yalign 1.2 #top 0.0, bottom 1.0 same for these
    bc "啊？！（惊慌）"
    show kita at center
    kt "呀吼~"

    #"（可以有一个波奇露小头的小图）"
    show bocchi:
        xalign -0.3 #left =  0.0, right = 1.0 you can go higher than 1.0 to move it off screen or the right and a negeative number to move it off screen on the left
        yalign 1.3 #top 0.0, bottom 1.0 same for these
    其他同学 "喜多桑今天去卡拉OK么~"
    kt "抱歉，今天想早点回去，毕竟保护嗓子也是很重要的哦~kita~"
    其他同学 "这样啊，喜多同学退出乐队了是真的吗，真可惜啊。"
    kt "嗯，出了点情况，没办法的事情啦！不过不用担心，你们很快就能看到我表演啦!~kita~"
    其他同学 "不愧是喜多同学！那明天记得来玩哦~拜拜~"
    kt "拜拜。"
    hide kita

    show bocchi at center 
    bci "好闪耀！太闪耀了！长得可爱运动又强又受欢迎，无论看多少次都会觉得多么完美的好孩子啊！"
    bci "而且现在她没有乐队！这是我此生仅有的机会！所以我现在要……"
    bci "直接上去你好有没有兴趣加入我的乐队？感觉这样会被当成图谋不轨的！还是装作偶遇然后不经意的那个我乐队差一个主唱？感觉也不对！《社交法则三百条》上面这里是怎么说的！为什么什么都想不起来了！"
    bci "为什么都不对啊！怎么做！要怎么做啊！脑子转起来！快转起来！！！"

    #教室内 波奇 喜多
    scene bg with None
    show kita at right
    show bocchi:
        xalign -0.3 #left =  0.0, right = 1.0 you can go higher than 1.0 to move it off screen or the right and a negeative number to move it off screen on the left
        yalign 1.3 #top 0.0, bottom 1.0 same for these
    #（这里游戏组和美工组讨论一下吧，是搞小CG还是怎么办，把波奇悄悄看喜多的名场面还原一下）
    bci "总……总之先观察一下吧，寻找机会，嗯，寻找机会。"
    bci "等一下，她是不是瞥到我了？"

    kt "后藤同学？"
    show bocchi at left 
    bc "啊！是……是……"
    bci "她居然知道我的名字！！！第一次有人主动知道我这种水藻的名字！为什么！这里应该要直接问\"欸为什么喜多同学知道我的名字啊\"这样的吧，说出口啊！说出口啊！"
    bc "为什……我……名……"
    bci "舌头打结了！！"
    kt "嗯……后藤同学是想问为什么知道名字么？"
    bci "她听懂了！不愧是喜多，果然连我这样的水藻的信息也能读懂……"
    "（疯狂点头）"
    kt "因为啊，那天放学的时候"
    kt "后藤同学那天穿着很厉害的衣服，桌子上摆着CD，还带着那~么大一把吉他，真的超级有趣嘛，像个摇滚怪咖似的，一眼就注意到了~"
    bci "啊咧？"
    bci "是说我很奇怪么？"
    bci "我给喜多同学留下的是怪人的映像么？"

    #幻想场景 波奇 喜多
    scene bg 2 with fade
    show bocchi at center
    其他同学 "后藤同学整这么怪来上学，还真以为自己是什么摇滚人啊？在我看来就是个怪咖，打扰了别人还不知道，真的是讨厌极了！"

    #回到现实 学校 午休 波奇 喜多
    scene bg with None
    show bocchi at left 
    show kita at right
    bci "喜多眼里我一定已经变成了这样吧，结束啦，全部结束啦，好难受，好伤心……"
    bc "我这样的怪人想打扰喜多同学真的是痴心妄想我终于意识到了我犯了多么严重的错误对不起我会立刻消失的！"
    hide bocchi
    show kita at center
    kt "啊后藤同学不是那个意……"
    "（波奇的起飞的脚步声）"

    #学校秘密空间 午休 波奇 喜多
    scene bg with None
    show bocchi at center 
    bc "被讨厌了啊……为什么我的心好痛，好奇怪啊……"
    bc "不能再见到喜多，还增添了新的黑历史，这样的屈辱，怎么偿还也是不够的吧。"
    bc "所以请欣赏这首新歌，《忘不掉的痛，孤独悲伤弹唱版》"
    #（这里看情况，写新曲还是用这里的原曲）
    bc "喜多……还是忘不掉……"

    show kita at right
    kt "好厉害！"
    show bocchi at left 
    bc "啊啊啊！喜多不是讨厌我为什么……"
    kt "怎么会！我是想说后藤同学打扮那么专业一看就很厉害啦啦!刚刚的吉他谈的也超级好！感动！后藤同学真的超级厉害！"
    bc "不！不愧是喜多！她说我超级厉害！果然是大好人！"
    kt "后藤同学这么厉害一定有乐队吧！这么棒的技术一定超级受欢迎！"
    bc "啊哈！"
    bci "如果让喜多知道我们第一次演出大失败现在还没有主唱为了下次演唱会还要打工那一定会拒绝我那一切都完蛋了！"
    bc "啊是的我们的乐队正在蒸蒸日上粉丝也再创新高是非常有潜力的乐队现在正好缺一个主唱喜多同学也刚好没加入乐队吧哎呀真是超级巧合啊喜多同学真是超级适合呢请加入我们吧真的超级拜托了。"
    bci "糟了说漏嘴了！"
    kt "原来是这样啊，难怪后藤同学看起来这么怪。"
    bci "难道是要同意……"
    kt "但真的非常抱歉，我现在没有办法加入乐团。"
    bci "欸？"
    bci "我是……被拒绝了么？"
    bci "也是啊，喜多这么棒的孩子，比起我，肯定会加入更完美的乐队吧。"
    bci "喜多之前也在自己的乐队，想必一定是粉丝众多，超级受欢迎，后援团排满整个东京巨蛋……"
    bci "虽然不知道喜多为什么离开了，但……现在确实是唯一的……"
    bci "唯一的机会就在眼前，我……我……"
    bci "不，我要在接近喜多一点，不能在这里放弃！"
    bci "喜多这么完美的女孩子，只要……只要可以一起在结束乐队！"
    bci "我的梦想一定可以实现，我不要失去喜多！我不要在这里结束！"
    bc "不，我！我！我可……可以改正！我不会再当乐队怪咖了！喜……喜多同学不喜欢的！我可以改！下课也可以给喜多买水！午饭也可以给喜多买豪华便当！喜多不喜欢我的地方我都可以改！喜多的要求我都可以做！"
    kt "不是那个原因啦，我没有不喜欢后藤同学，倒不如说后藤同学真的很有趣，所以请不要这样……"
    bc "那！我们乐团发展的非常好！演出不会缺观众的！一定可以让喜多变成最闪耀的主唱！"
    kt "我也高攀不起……"
    bc "那！乐队福利超级好！平时还有BBQ，半年举办一次排球大赛！表演后更有豪华轿车庆功宴！总之就是活动一级丰富"
    kt "这样排队咖一样的乐队还要排练也太辛苦了吧……"
    bc "那…………那…………"
    bci "糟了脑子转不过来了，喜多同学要错过了啊！"
    kt "还是和后藤同学实话实说吧。"
    kt "那个……其实我不会弹吉他……一点都不会的那种……"
    bc "欸？"
    kt "之前是奔着学姐才参加的乐队，为了加入才谎称自己会吉他，最后还是一窍不通所以逃跑了。"
    bc "一窍不通……"
    kt "嗯，比如吧（拿过吉他）"
    extend "我一开始还以为这个指板这些都是装饰呢。"
    bc "装饰……"

return
