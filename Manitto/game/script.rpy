# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen normal = "eileen_normal.png"

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
define jj = Character( "줴훈줴훈", who_color="999999", what_color="999999")
define jm = Character( "지민", who_color="999999", what_color="999999")
define sb = Character( "수빈", who_color="999999", what_color="999999")
define rv = Character( "김원식", who_color="999999", what_color="999999")
define dw = Character( "참치", who_color="999999", what_color="999999" )
define sm = Character( "김민석", who_color="999999", what_color="999999")
define sd = Character( "서자기", who_color="999999", what_color="999999")

#배경
image bg black = "#000000"
image bg red = "#AA0000"
image bg violet = "#6600cc"

image bg ky = "#de3163"
image bg ms = "#ff6f61"
image bg sy = "#ffc81e"
image bg yi = "#00ff7f"
image bg jh = "#00bfff"
image bg hj = "#ba55d3"

image bg main = "gui/main_menu.png"
image bg school = "gui/bg/school.jpeg"
image bg bg_class = "gui/bg/class.jpg"
image bg sulzip = "gui/bg/sulzip.png"
image bg sultop = "gui/bg/sultop.png"
image bg cherryblossom = "gui/bg/cherryblossom.jpeg"
#효과
define flashbulb = Fade(0.3, 0.0, 0.8, color='#fff')

#이미지
image manitto = im.Scale("gui/manitto.jpeg", 600,500)
image sultop = im.Scale("gui/sultop.jpg", 300,600)
# 이미지 set
image na_i = im.Scale("gui/img/na.png",400,550)
image jj_i = im.Scale("gui/img/jj/jj_native.png",380,600)
image jj_i nervous = im.Scale("gui/img/jj/jj_nervous.png",380,600)
image jj_i tears = im.Scale("gui/img/jj/jj_tears.png",350,300)

# image hb cool = im.Scale("gui/img/hb/hb_cool.png",380,500)

image sb_i = im.Scale("gui/img/sb/sb_normal.png",450,620)
image jm_i = im.Scale("gui/img/jm/jm_native.png",380,600)
image sm_i = im.Scale("gui/img/sm/sm.png",380,580)
image rv_i = im.Scale("gui/img/rv/rv.png",380,600)
image dw_i = im.Scale("gui/img/dw/dw.png",330,580)

#라이벌들
image ss_i = im.Scale('gui/img/ss/ss.png',380,500)
image sd_i = im.Scale('gui/img/sd/sd.png',380,500)


image sy normal = im.Scale("gui/img/sy/sy_normal.png",400,450)
image jh normal = im.Scale("gui/img/jh/jh_normal.png",330,450)
image ky normal = im.Scale("gui/img/ky/ky_normal.png",280,400)
image hj normal = im.Scale("gui/img/hj/hj_normal.png",250,420)
image ms normal = im.Scale("gui/img/ms/ms_normal.png",330,550)
image yi normal = im.Scale("gui/img/yi/yi_normal.png",400,450)

image ky surprise = im.Scale("gui/img/ky/ky_surprise.png",280,300)



style say_dialogue:
    line_spacing 10

# 마니또
init python in Manitto:

    loves = {"ky":0, "ms":0, "sy":0, "jh":0, "hj":0, "yi":0}
    chap = {"ky":[0],"ms":[0],"sy":[0],"jh":[0],"yi":[0],"hj":[0]}
    names = {"ky":"김가윤", "ms":"이미송", "sy":"이수연", "jh":"서정현", "hj":"정현지", "yi":"심예인"}


    stories = {
        "ky": ["김가윤, 마니또 중 가장 활발하고 엉뚱한 인물"],

        "ms": ["이미송, 마니또 중 가장 장난끼가 많은 인물"],

        "sy": ["이수연, 마니또 중 가장 조용하고 착한? 인물"],

        "jh": ["서정현, 마니또 중 가장 무서워 보이는 인상을 갖고 있는 인물"],

        "yi": ["심예인, 마니또 중 가장 말을 잘 받아주는 인물"],

        "hj": ["정현지, 마니또 중 가장 속을 알수 없는 인물"],
    }

    chinghos = []

    def getName(name):
        return names.get(name)

    #호감도
    def allChange(love):
        for k, v in loves.items():
            loves[k] += love

    def getLove(name):
        return loves.get(name)

    def lChange(lover, love):
        loves[lover] += love

    def test():
        return loves.items()

    #이야기
    def getStory(name, chap_num):

        if chap_num in chap.get(name):
            story = stories.get(name)[chap_num]
        else:
            story = "아직 열리지 않은 스토리 입니다."
        return story

    def addStory(name, chap_num):
        chap[name].append(chap_num)

    def addChingho(chingho):
        chinghos.append(chingho)


label state:
    menu :
        "마니또 살펴보기":
            call manitto_state
            jump state
        "내 상태 " :
            "아직 오픈되지 않은 기능입니다."
            jump state
        "이어서 진행하기":
            return

label manitto_state:
    scene bg black
    menu:
        "가윤":
            scene bg ky
            show ky normal :
                xalign 0.05
                yalign 0.5
            call manitto_ho("ky")
            hide ky normal
            jump manitto_state

        "미송":
            scene bg ms
            show ms normal:
                xalign 0.05
                yalign 0.5
            call manitto_ho("ms")
            hide ms normal
            jump manitto_state

        "수연":
            scene bg sy
            show sy normal:
                xalign 0.02
                yalign 0.5
            call manitto_ho("sy")
            hide sy normal
            jump manitto_state

        "예인":
            scene bg yi
            show yi normal:
                xalign 0.05
                yalign 0.5
            call manitto_ho("yi")
            hide yi normal
            jump manitto_state

        "정현":
            scene bg jh
            show jh normal:
                xalign 0.05
                yalign 0.5
            call manitto_ho("jh")
            hide jh normal
            jump manitto_state

        "현지":
            scene bg hj
            show hj normal:
                xalign 0.05
                yalign 0.5
            call manitto_ho("hj")
            hide hj normal
            jump manitto_state

        "되돌아가기":
            return

label manitto_ho(name):
    $ m_name = Manitto.getName(name)
    menu:
        "story 보기":
            menu:
                "기본 정보":
                    $ story = Manitto.getStory(name, 0)
                    "[story]"
                    return
                "Chapter1":
                    $ story = Manitto.getStory(name, 1)
                    "[story]"
                    return
            return

        "호감도 보기":
            $ ho =  Manitto.getLove(name)
            "[m_name]의 호감도 : [ho] "
            return

        "되돌아가기":
            return






############    Chap1   ###################
# 수연 루트
label chap1_sy:
    "술집을 나서려고 일어서자 마니또 수연도 갑자기 자리에서 일어났다."
    show sy normal :
        xalign 0.9
        yalign 0.4
    sy "[na] "
    extend "지금 갈꺼면 같이가자"
    na "어? 어? 응.."

    #벛꽃씬
    scene bg cherryblossom with Dissolve(1)
    n "{color=000000}{size=+10}밖으로 나오니 벚꽃이 한참 지고 있었다{/size}{/color}"

    show sy normal :
        xalign 0.9
        yalign 0.4
    sy "이렇게 둘이서 걷는것도 초등학교때 이후로 처음이네 ^-^"
    show na_i :
        xalign 0.1
        yalign 1.0
    na "아 .. 응 그렇네.."
    "수연과 나는 사실 어린시절 꽤나 친했었다."
    "물론 '그 사건' 이후로 멀어져서 비록 지금은 어색한 사이이긴 하지만.."
    "이렇게 오랫만에 함께 걸어가니 마치 옛날로 돌아간것만 같다"

    sy "[na]"
    na "응?"
    sy "조심히 들어가"
    na "아.. 응"
    na "저.. 수연아"
    na "대려다 줘서 고마워"
    sy "^-^"

    hide na_i
    sy "...."
    sy "넌 그대로구나 [na]..."
    return


##########################################
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
    show jj_i :
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

    show yi normal :
        xalign 0.95
        yalign 0.5

    yi "으아아악 늦었어 늦었어!"
    yi "o_0 앗;; 안녕하세요ㅎㅎ"

    "[yi].  "
    extend "내 밑에 집에 사는 과 후배다."
    "종종 방음이 되지 않아서 가끔 [yi]의 욕소리가 들리는데.."
    extend " 약간 마니또 같다."
    "무섭다."
    hide yi normal

    scene bg bg_class
    play music "vixx_parallel_piano.mp3"

    "(웅성웅성)"
    show na_i :
        xalign 0.1
        yalign 1.0
    "왜 다들 나를 쳐다보는 것 같지?;;"
    "자의식 과잉인가 ㅎㅎ;;"

    show jm_i :
        xalign 0.95
        yalign 1.0
    jm "야 너 진짜 마니또랑 사귀어?"
    na "엥? 그게 무슨소리야?"

    show sb_i :
        xalign 0.65
        yalign 1.0
    sb "아 됐고 그래서 그 중에 누구야?"
    na "으..응?"
    sb "마니또 여섯명중에 누구냐구"
    hide jm_i
    hide sb

    show jh normal :
        xalign 0.95
        yalign 0.4

    jh "아 ㅅㅂ 남친 사칭 누구야 -_-^ "

    show ms normal :
        xalign 0.7
        yalign 0.5

    ms "이름이 [na]..? 라고 했었나?"

    "나는 황급히 강의실 문쪽으로 몸을 돌렸다."

    hide jh normal
    hide ms normal

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


    show ms normal :
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
    hide ms normal

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
            show na_i :
                xalign 0.1
                yalign 1.0
            na "조용히 해. 나도 너희 때문에 HP와도 같은 커피를 못먹었으니까"
            "..."
            $ Manitto.lChange("ms", 3)
            $ Manitto.lChange("yi", 3)

        "헉..ㅠ_ㅠ 미안 내가 커피 사다줄까??" :
            show na_i :
                xalign 0.1
                yalign 1.0
            na "헉..ㅠ_ㅠ 미안 내가 커피 사다줄까??"
            $ Manitto.allChange(5)

        "쿸.. 이쁜의들 그럼 지금부터 옵하랑 coffee input하러 cafe 갈까?" :
            show na_i :
                xalign 0.1
                yalign 1.0
            na "쿸.. 이쁜의들 그럼 지금부터 옵하랑 coffee input하러 cafe 갈까?"
            "..."
            "역시 무리수였나.."
            $ Manitto.allChange(-5)

        "무시한다" :
            "(무시)"
            "...."
            show na_i :
                xalign 0.1
                yalign 1.0
            $ Manitto.lChange("sy", 3)



        "..(말없이 눈물 흘린다)" :
            show na_i :
                xalign 0.1
                yalign 1.0
            na "...(글썽)"
            $ Manitto.lChange("ky",3)

    show yi normal :
        xalign 0.95
        yalign 0.5

    yi "o_O 앗, 다들!! 뭐하는고야;;ㅎ\n"
    extend "[na] 선배 곤란하게 하지마~ ;;"

    show hj normal :
        xalign 0.65
        yalign 0.55

    hj "ㅋ "
    extend "진지하기는~\n"
    extend "재밌어~ "
    extend "[na]."

    na "어.. 그.. "
    extend "어째뜬 난 다음수업이 있어서"
    na "이만 가볼께!!!!"

    stop music fadeout 1.0
    scene bg black

    n "이걸로 6명의 마니또와의 악연은 끝이라고\n\n"
    extend "마니또라는 loop에서 break문을 만난거라고 \n\n"
    extend "그렇게 바보같이 믿고있었다.\n\n"
    extend "하지만 나는 exception이였고\n\n"
    extend "마니또들에게 catch 당할 운명이란 것을...\n\n"
    extend "그때의 난 아직 모르고 있었다."

    # 마니또 호감도 보여주기
    window hide dissolve
    call state

    #chap1

    scene bg violet
    n "{cps=3}{size=+30} Chapter1. 마니또,"
    extend " C2H5OH {/size}{/cps}"
    with flashbulb
    scene bg black with Dissolve(1)

    "휴우 "
    extend "드디어 마지막 수업이 끝이 났다."

    show sm_i:
        xalign 0.95
        yalign 1.0

    sm "[na] 오늘있는 신입생 환영회 갈꺼지?"

    show na_i :
        xalign 0.1
        yalign 1.0

    na "신입생 환영회?"
    na "음 나는 글쎄.."

    sm "에이 복학생이 빠져서 쓰나!"

    show jm_i :
        xalign 0.7
        yalign 1.0

    jm "그래 너 그러다 아싸되서 조별과제 독박쓴다?"

    na "조별과제 독박..!!"

    hide jm_i
    hide sm_i
    hide na

    # 술집 화면전환
    scene bg sulzip with Dissolve(1)

    "후- "
    extend "결국 와버렸다"

    show ky normal:
        xalign 0.6
        yalign 0.5
    ky "야 빨리 마셔마셔! 차 끊기전에 취해야 돼!"
    show jj_i :
        xalign 0.1
        yalign 1.0
    jj "역시 막차의 김가윤,\n"
    extend "막차 끊기기 전에 항상 취해야 된다고 브레이크가 고장난 에잇톤 트럭처럼 빨리달리지"
    "음 가까히 가지 말아야겠군"
    hide ky normal
    hide jj_i normal

    show sy normal :
        xalign 0.9
        yalign 0.5
    sy "현지 진영오빠 여자친구 생겼다는게 사실이야?"

    show hj normal:
        xalign 0.6
        yalign 0.5
    hj "아 그게 어떻게 된거냐면~"
    show jm_i :
        xalign 0.1
        yalign 1.0
    jm "역시 컴공과의 인싸 정현지,\n"
    extend "컴공과의 모든 소문은 현지라는 proxy를 거치지 "
    "역시 학생회, 나도 친구 많이사귀고 싶다"

    hide sy normal
    hide hj normal
    hide jm_i

    # image bg
    show sultop at truecenter with Dissolve(1)

    show rv_i :
        xalign 0.1
        yalign 1.0

    rv "퍼포먼스의 이미송,\n"
    extend "소주잔으로 탑을쌓았어"
    "세상에 저걸 다 누가 다마시는걸까.."
    "나는 마음속으로 저 술을 다 마시게될 사람들에게 애도를 표했다"
    hide rv_i
    hide sultop

    show sb_i :
        xalign 0.1
        yalign 1.0

    sb "역시 침착함의 이수연, \n"
    extend "이 난리통속에 얼굴색 하나 변하지 않고 마시는군"
    show sy normal :
        xalign 0.6
        yalign 0.5
    sy "ㅎㅎ.."
    "순간 아무도 모르는 수연의 주량이 무서워졌다"

    hide sb_i
    hide sy normal

    show sm_i :
        xalign 0.1
        yalign 1.0

    sm "술자리의 최종보스 심예인,\n"
    extend "아니 엘렌"

    show dw_i :
        xalign 0.3
        yalign 1.0
    dw "그리고 그 엘렌을 컨트롤하는 컨트롤러  서정현"

    show yi normal :
        xalign 0.6
        yalign 0.5
    yi "달리기 시합할싸람~~! @//@"

    show jh normal :
        xalign 0.85
        yalign 0.5
    jh "어허 엘렌, 술집에서 뛰는거 아냐"
    "혼란하다 혼란해..."

    scene bg black with Dissolve(1)

    n "{cps=11}정신없이 술을 먹다보니 어느새 분기가 무르익어갔다{/cps}"

    scene bg sulzip with Dissolve(1)

    show sd_i :
        xalign 0.9
        yalign 0.5

    sd "야 거기 너! -_-+"
    sd "니가 그 자칭 마니또 남친?ㅋ"

    show na_i :
        xalign 0.1
        yalign 1.0

    na "네?"

    sd "니가 진짜 마니또 남친이면 술 잘마시겠네"
    sd "자 마셔"

    $ sul = False
    # 술 먹는 선택지
    menu:
        "어;; 전 술 잘 못마셔서요..":
            sd "뭐야.. 누군 잘마셔서 마시나"
            sd "선배가 주면 그냥 마셔"
            na "..."
            "결국 어쩔수 없이 나는 술을 먹게 되었다."

            # 호감도 sy + 3, hj + 2


        "이미 취한 척 한다":
            na "삼성 개객기해봐~! \n"
            extend "이재용 개객기!"
            extend "개객기 해보라고~"
            sd "뭐야 ㅅㅂ;;;"
            # 호감도  ms+5 yi+5


        "남자답게 마신다":
            "나는 술잔을 깔끔히 비워냈다."
            sd "ㅋ 꼴에 다 마시네"
            # 호감도 all + 2
            $ sul = True


    jh "? 거기 뭐야? -_-"
    "마니또 정현이 다가오자 나머지 마니또들 역시 일제히 나와 서자기를 주목했다."

    sd "아니~ 나는 [na]가 준 술을 마셨는데 [na]는 자꾸 내가 준 술을 안먹는다고 해서~"
    sd "정말 서운하다 [na]야~"
    "?!?!!"

    # 변명 타임~
    menu :
        "에이 까짓것 남자답게 마신다":
            "술을 너무 많이 마셔서 그런지 조금 취기가 오르는 것 같다"
            #호감도 yi ms jh + 2
            if sul == True :
                $ Manitto.addChingho("너도.. 술.. 좋아해?")
                $ tmp = Manitto.chinghos[0]
                "[tmp] 칭호를 획득하셨습니다."

            hj "[na]."
            hj "...."
            hj "괜찮아?"



        "아.. 아냐..!! 전혀 그런 상황이 아니었어!":
            na "아.. 아냐..!! 전혀 그런 상황이 아니었어!"

            # 흑기사


        "토한다":
            na "우에에에엑"
            # 호감도 All -2


    hide sd_i

    "[na] 너 취했어?"

    menu :
        "응.. 좀 난 이제 집에 가봐야겠다":
            na "응.. 좀 난 이제 집에 가봐야겠다"

            #수연 루트
            call chap1_sy

        "아니? 나 하나도 안취했는데":
            "ㅅㅏ 실 취햇ㅆ다"
            #현지루트

        "아직 까진 괜찮은 것 같아":
            na " 아직까진 괜찮은 것 같아"
            #예인 루트



    window hide dissolve
    scene bg red with Dissolve(1)
    n "{cps=3}{size=+20} 마니또,"
    extend " OVERFLOW {/size}{/cps}"
    with flashbulb




    return

# # 예인 루트
# n "마니또들은 마치 ~마냥 술을 마셔댔고"
# extend "날이 가장 어두울때가 되어서야 비로소 환영회 자리는 끝을 맞이했다."
#
# ""







screen set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5
