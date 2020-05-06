# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define gui.language = "korean-with-spaces"

#주연
define ky = Character( "가윤", who_color="de3163", what_color="de3163" ) # >_<
define ms = Character( "미송", who_color="ff6f61", what_color="ff6f61" ) # ^0^
define sy = Character( "수연", who_color="ffc81e", what_color="ffc81e") # ^-^
define yi = Character( "예인", who_color="00ff7f", what_color="00ff7f") # 0_0
define jh = Character( "정현", who_color="00bfff", what_color="00bfff") # -_-^
define hj = Character( "현지", who_color="ba55d3", what_color="ba55d3") # - -
define n = Character( None, centered, what_size=30)


# 조연
define jj = Character( "줴훈줴훈", color="ffffff")
define jm = Character( "지민", color="ffffff")
define sb = Character( "남 수빈", color="ffffff")
#배경
image bg black = "#000"
image bg main = "gui/main_menu.png"
image bg school = "gui/bg/school.jpeg"
image bg bg_class = "gui/bg/class.jpg"

#이미지
image manitto = im.Scale("gui/manitto.jpeg", 600,500)
image ms = "gui/img/ms_img.png"

# 이미지 set
image na_i = im.Scale("gui/img/na.png",400,550)
image jj_i native = im.Scale("gui/img/jj/jj_native.png",380,600)
image jj_i nervous = im.Scale("gui/img/jj/jj_nervous.png",380,600)
image jj_i tears = im.Scale("gui/img/jj/jj_tears.png",350,300)
image jm_i native = im.Scale("gui/img/jm/jm_native.png",380,600)

image hb cool = im.Scale("gui/img/hb/hb_cool.png",380,500)

image sb normal = im.Scale("gui/img/sb/sb_normal.png",450,620)

image sy normal = im.Scale("gui/img/sy/sy_normal.png",400,450)
image ms happy = im.Scale("gui/img/ms/ms_happy.png",330,550)
image jh normal = im.Scale("gui/img/jh/jh_normal.png",330,450)
image ky normal = im.Scale("gui/img/ky/ky_normal.png",280,400)
image ky surprise = im.Scale("gui/img/ky/ky_surprise.png",280,300)

image yi lovely = im.Scale("gui/img/yi/yi_lovely.png",400,450)
image hj normal = im.Scale("gui/img/hj/hj_normal.png",280,450)


style say_dialogue:
    line_spacing 10

init python in Mlove:



    loves = {"ky_l":0, "ms_l":0, "sy_l":0, "jh_l":0, "hj_l":0}

    def allChange(love):
        for k, v in loves.items():
            loves[k] += love

    def getLove(name):
        return loves.get(name)

    def lChange(lover, love):
        loves[lover] += love

    def test():
        return loves.items()

# 여기에서부터 게임이 시작합니다.
label start:
    image ctc_icon = Image("gui/flower_icon.png")

    #캐릭터 이름 입력받을꺼야
    $ name = renpy.call_screen("set_name",title="마니또 에게 이렇게 불리고 싶어!! ♥ ", init_name="이름 입력해주세용")
    $ na = Character( name , color="#ffffff", ctc="gui/flower_icon.png",ctc_position="nestled-close", what_suffix=" ")

    play music "vixx_whisper_piano.mp3"

    n "학교에는 4가지 분류의 아이들이 있다."

    n "범생이,\n\n"
    extend "평범이,\n\n"
    extend "찌질이,\n\n"
    extend "그리고.."

    n "{b}{cps=5}{size=+10}마니또..!!{/size}{/cps}{b}"

    n "나는 마니또도 아니고, 범생이도 아닌,\n\n"
    extend "그저 그런 평범이 정도..?"

    n "계속 평범하게 살고싶었다\n\n"
    extend "흘러가는 강물처럼,\n\n"
    extend "에러있는 프로그램처럼,\n\n"
    extend "평범하고도.. 평범하게..\n\n"
    extend "그런데...!\n\n"

    play music "vixx_gr8u.mp3"

    n "어느날 갑자기"
    n "{cps=7}{size=+10}{color=cd426b}6명{/color}의 {color=cd426b}마니또{/color}가 내 삶에 들어왔다.{/size}{/cps}"

    scene bg main
    with Dissolve(1)
    pause .8
    scene bg school with Dissolve(1)

    ####### 1.prologe #######
    show jj_i native :
        xalign 0.9
        yalign 1.0

    jj "[name]! 여기있었어?"

    "어..? 저 선배는 매번 보는 사람마다 술 먹자고 진상 개 진상을 부리는 선배잖아?"

    jj "아 진짜~ 너 서샘숭 알지? 서샘숭이 글쎄 요새 여친이 생겨서 술을 같이 안마시는거 있지?\n"
    jj "내가 진짜 너무 서운하다 정말.. \n"

    jj "그래도 [na], 너라도 있어서 다행이다."

    show na_i :
        xalign 0.1
        yalign 1.0

    na "네?"

    jj "앞으로 우리 둘이 소주메이트 인거다?"

    "내 직감이 외친다.\n"
    extend "이 선배에게서 벗어나야 한다고"

    na "저 선배.."

    jj "응?"

    na "저도 여친이 술먹는걸 싫어해서요ㅎㅎ.."

    jj "뭐 여친?? 누군데????"

    "나는 대충 대숲에 올라왔던 사진을 [jj]에게 보여주었다."
    scene bg black with Dissolve(1)
    show manitto at truecenter
    pause

    scene bg school
    show jj_i nervous :
        xalign 0.9
        yalign 1.0

    jj "?!!"

    "뭐지? 왜 저렇게 놀라는 거지?"

    jj "하..하하.. 그래 이제 여자친구있어서 이제 술 자주 못마시겠네..!!\n"
    extend "되게 아쉽다야!ㅎㅎ..\n"

    jj "어.. 저 그럼 난 수업이 있어서 이만!!"

    hide jj_i nervous

    "? 아까 까지만해도 술먹자고 그런거 아니었나?\n"
    "어째뜬 무사히 잘 넘어가서 다행이야.."

    stop music fadeout 1.0
    scene bg black

    n "그때까지만 해도 나는 전혀 모르고 있었다.\n\n"
    extend "앞으로 어떤일이 벌어질지..."

    ####### 2.첫 만남? #######
    show na_i :
        xalign 0.1
        yalign 1.0

    show yi lovely :
        xalign 0.95
        yalign 0.5

    yi "으아아악 늦었어 늦었어!"
    yi "o_0 앗;; 안녕하세요ㅎㅎ"

    "[yi].  "
    extend "내 밑에 집에 사는 과 후배다."
    "종종 방음이 되지 않아서 가끔 [yi]의 욕소리가 들리는데.."
    extend " 약간 마니또 같다."
    "무섭다."
    hide yi lovely

    scene bg bg_class
    play music "vixx_parallel_piano.mp3"

    "(웅성웅성)"
    show na_i :
        xalign 0.1
        yalign 1.0
    "왜 다들 나를 쳐다보는 것 같지?;;"
    "자의식 과잉인가 ㅎㅎ;;"

    show jm_i native :
        xalign 0.95
        yalign 1.0
    jm "야 너 진짜 마니또랑 사귀어?"
    na "엥? 그게 무슨소리야?"

    show sb normal :
        xalign 0.65
        yalign 1.0
    sb "아 됐고 그래서 그 중에 누구야?"
    na "으..응?"
    sb "마니또 여섯명중에 누구냐구"
    hide jm_i native
    hide sb normal

    show jh normal :
        xalign 0.95
        yalign 0.4

    jh "아 ㅅㅂ 남친 사칭 누구야 -_-^ "

    show ms happy :
        xalign 0.7
        yalign 0.5

    ms "이름이 [na]..? 라고 했었나?"

    "나는 황급히 강의실 문쪽으로 몸을 돌렸다."

    hide jh normal
    hide ms happy

    show hj normal :
        xalign 0.95
        yalign 0.4

    hj "ㅎ.. 저기 출튀하시네~"
    hj "우리들 {cps=3}남.친.님.{/cps}"

    show ky normal :
        xalign 0.7
        yalign 0.5

    ky "뭐? 어디 어디? 저기 저 거북이 말하는거야? ㅇ_ㅇ"

    hide hj normal

    show sy normal :
        xalign 0.95
        yalign 0.4
    sy "아무리 그래도 그렇지 사람한테 거북이가 뭐냐ㅋㅋ"

    ky "아니 백팩이 거북이 등딱지 같자노~ -0-"

    hide ky normal
    hide sy normal


    show ms happy :
        xalign 0.95
        yalign 0.5
    ms "됐고 잠깐, 그쪽이 저희들 남친? ^-^"
    "나는 마니또 [ms]에게 가방을 붙잡히고 말았다."
    ms "뭐야 왜이렇게 무거워 사양 풀로 채운 노트북이라도 들고다니나ㅋㅋ"
    na "...."

    show jh normal :
        xalign 0.7
        yalign 0.4
    jh "대답 -_-^"

    #구깃
    jh "하 좋은말로 해선 안돼겠네.. -_-^^^"
    hide ms happy

    show sy normal :
        xalign 0.95
        yalign 0.4
    sy "잠깐, 조금 있으면 교수님 오셔서 출석부를 것 같은데 ^_^"
    "헉 그래도 그나마 비교적 덜 마니또 같은 [sy]이가 날 구해주려고..!"
    jh "지금 수업이 중요해? -_-+"
    # 생긋
    sy "그러니까 출튀하고 장소를 옮겨서 이야기 하자 ^_^"
    hide sy normal
    hide jh normal
    hide na_i

    "망했다"


    "설마 그게 우리학교 마니또 사진이었다니.."
    "하지만 교수님은 끄끝내 출석을 부르지 않으셨고,"
    extend " 그대로 쉬는시간이 되었다."

    show ky normal :
        xalign 0.95
        yalign 0.5

    ky "아 배고파~ 거기다 엄청 졸리네 ㅜ_-"

    show jh normal :
        xalign 0.8
        yalign 0.4
    jh "그러니까.. 누구 때문에 아침에 커피도 못사고 -_-+"
    na "헉..!"

    hide jh normal
    hide ky normal

    menu:
        #선택지
        "조용히 해. 나도 너희 때문에 HP와도 같은 커피를 못먹었으니까":
            show hb cool:
                xalign 0.8
                yalign 0.6
            na "조용히 해. 나도 너희 때문에 HP와도 같은 커피를 못먹었으니까"

        "헉..ㅠ_ㅠ 미안 내가 커피 사다줄까??" :
            na "헉..ㅠ_ㅠ 미안 내가 커피 사다줄까??"


        "쿸.. 이쁜의들 그럼 지금부터 옵하랑 coffee input하러 cafe 갈까?" :
            na "쿸.. 이쁜의들 그럼 지금부터 옵하랑 coffee input하러 cafe 갈까?"
            "..."
            "ㅁㅊㄴ"

            $ Mlove.allChange(-5)

            na "역시 무리수였나.."



        "무시한다" :
            "(무시)"
            "...."
            show ms:
                xalign 0.5
                yalign 0.5


        "..(말없이 눈물 흘린다)" :
            show jj_i tears:
                xalign 0.1
                yalign 0.6
            na "..."




    #chap2



    #window hide dissolve
    #window show dissolve

    return

screen set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5
