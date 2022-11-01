from django.shortcuts import render
from subeana.models import Song
from rest_framework import viewsets
from .serializer import SongSerializer
from config.settings import BASE_DIR as BASE_DIRpath
import hashlib
import requests
from time import sleep
from config.settings import BASE_DIR as BASE_DIRpath


# パスワード関連
SHA256a = "5802ea2ddcf64db0efef04a2fa4b3a5b256d1b0f3d657031bd6a330ec54abefd"


#初期化関連
SUBEANA_LIST = [
    {
        "title" : ".",
        "lyrics" : "携帯ゲームの裏\nフタを開けてみて\n空っぽだったはずなのに\n淡い光が漏れていたので\nいたずらに覗いたら\nデンチが腐っていた\n掌から滑り落ち\n叩きつけられて\nやむ終えず覗いたら\n画面が割れていました\nたわむれに書いた傘の中\nひとりでに骨が折れ\n心地よい音　頭蓋の中\n湿って砕けました\n湧き出た光る水を\n飲んでみたくなり\n空っぽだったはずなのに\n器から溢れてしまいそうで\nひとくち含んでみたら\n甘すぎて吐き出したよ\n漏れ出た黒い液が\n怖くてたまらないのに\n指先が触れてしまい\n血液と混ざりました\n心地よい音　頭蓋の中\nひとりでに骨が折れ\nたわむれに書いた傘の中\n全てあなたの所為です\n心地よい音　頭蓋の中\nひとりでに骨が折れ\nたわむれに書いた傘の中\n全て■■の所為です\n沢山の目が光り\n見つめていたのか",
        "imitate" : "原曲"
    },
    {
        "title" : "..",
        "lyrics" : "蛍光灯の明かりの下\n艶やかな足跡がある\nシアン化物の甘い匂いで\n手足が痺れはじめ\nからだ中に差し込まれてく\nいかにもな理由を添えて\nどうして針はこちらを向いて\n繰り言を吐くの？\n砂を噛み\n鏤骨を齧り\nナメクジが死んでました\nそれは万有引力の\n様なモノであり\n抗えば抗うほど\n青く燃え上がるのです\nそれはテレメトリ信号が\n指し示す通り\nもがく腕や足はもう\n意味をなさないのです\n後は野となれ山となれと\n何も成し遂げられず居る\n偶像崇拝妄信者が\n溜飲を下げる\n四辺形に収容された\n路傍の人の慰みが\n植えつける様にこちらを向いて\n咎めるのでしょう\n砂を噛み\n鏤骨を齧り\nナメクジが溶けてました\nそれは万有引力の\n様なモノであり\n抗えば抗う程\n青く燃え上がるのです\nそれはテレメトリ信号が\n指し示す通り\nもがく腕や足はもう\n意味をなさないのです\n這いずり方が\n思い出せなくなりました\n全てあなたの所為です\nそれは万有引力の\n様なモノであり\n抗えば抗う程\n青く燃え上がるのです\nそれはテレメトリ信号が\n指し示す通り\nもがく腕や足はもう\n意味をなさないのです\n柔らかい場所を\n沢山の指先で\n触れようとしていたのか。",
        "imitate" : "原曲"
    },
    {
        "title" : "教育",
        "lyrics" : "誰もそこにいない事\n誰にも教えたくなくて\n誰もそこにいないなら\n見つめているのはだあれ？\nあなたがここにいない事\nあなたにも教えたくなくて\nあなたもここにいないなら\nなにを見つめているの？\nそれは土を捏ねて作ったヒトの様だった。\n脊髄という名の神経の\n片方の端が膨らんで\n自ら意思を持ち始め\n我々を操り始めたのです。\nいつもそこにいない事\nいつもあなたに教えたくて\nいつもそこにいないなら\nなにを追いかけているの？\nあなたがここにいない事\nあなたにも教えたくなくて\nあなたもここにいないなら\nなにを見つめているの？\nそれは型だけを模したミメシスの様だった。\n脊髄という名の神経の\n片方の端が膨らんで\n自ら意思を持ち始め\n我々を操り始めたのです。",
        "imitate" : "原曲"
    },
    {
        "title" : "アブジェ",
        "lyrics" : "水平線の遥か上を\n飛んで征く\n裏返った蜻蛉の羽が\n世を分かつ、\n考えた事はありますか\nおぞましさとは？\n美しさとは？\n初めから其処に在るが儘\n誰が為に花は咲くのでしょう\n羨望の囚われ人が\n飛んで征く\n心骨処は乖離し\n捻じれ落ちる、\n感じた事はありますか\nおぞましさとか、\n美しさとか、\n初めから其処に在るが儘\n誰が為に花は散るのでしょう\n継ぎ接ぎだらけの筏が\nとろけて川と混ざり\n独りよがりの退廃に\n首まで浸かったまま\nつぎはぎだらけの筏が\nとろけて川と混ざり\n独りよがりの退廃に\n首まで浸かったまま",
        "imitate" : "原曲"
    },
    {
        "title" : "...",
        "lyrics" : "穴の空いた両の手で\n喉の渇きは潤せず\n甘いはずの水は\n掬っても零れてゆく\n穴の空いた両の手で\n目を遮ることは出来ず\n柔らかな熱源が\n視神経を焼き切りました\n腕の無い三重の\n振り子が描き出す背骨を\n短慮な烏が\n啄ばむのでした\n不快な音を鳴らして\n無い爪を立てる\n形骸化した心地よさには\n遅効性の毒があるのです\n見たいモノだけを見て\n信じたいモノを信じ\n目が覚めたときは既に遅し\n死に至るでしょう\n全てあなたの所為です\n穴の空いた両の目で\n逃げ水を追いかけて行く\n気がつけば遠くまで\n歩いてしまいました\n穴の空いた両の目で\n硝子の向こうをそっと見る\n意味のない言葉は\n此の世に存在しないのです\n陰になり日向になり\n顰蹙の密売商人が\n土足で踏み込んで\n来るのでした\nただ緩やかに黄昏て行く\n誰も止め方がわからずに\n心臓の位置を避けるようにと\n横から杭が打ち込まれました\n不快な音を鳴らして\n無い爪を立てる\n形骸化した心地よさには\n遅効性の毒があるのです\n見たいモノだけを見て\n信じたいモノを信じ\n沢山の足の音が\n近づいていたのか。",
        "imitate" : "原曲"
    },
    {
        "title" : "表/裏",
        "lyrics" : "絡まった電線が解けなくて\n屋上に夜明けの晩のチャイムが響く\n帰り道ジリリと左のほうで\nベルの音が聞いて欲しそうに鳴った\n小さな窓があり\n真っ赤な屋根の\n電話ボックスが手を招き\nでたらめな抑揚で声をかけてきたのです\nぬめりとした呻き穏やかな不協和音\nガチャリと折れる腕\n箱の中の鵺の無く声に\n耳を澄ましてはいけません\n枝の無い電子が流し込まれて\n侵された合目的的ヘモフォビア\n手回しの自我意識が腐り落ち\n底なしの静寂に骨身を浸す\n三なる兆候に\n気づかないまま\n光ソリトンの赤い灯が\nでまかせの衝動を\n仄めかしてきたのです\n不明瞭な愁い\n歯と歯が重なった音\nガチャリとしまる喉\n三寸五分の煙突の方\n目を合わせてはいけません\n小さな窓があり\n真っ赤な屋根の\n電話ボックスが手を招き\nでたらめな抑揚で\n声をかけてきたのです\nぬめりとした呻き穏やかな不協和音\nガチャリと折れる腕\n箱の中の鵺のなく声に\n不明瞭な愁い\n歯と歯が重なった音\nガチャリと絞まる喉\n三寸五分の煙突の方\n二度と聞こえはしないのです",
        "imitate" : "原曲"
    },
    {
        "title" : "名の無い星が空に堕ちたら模倣",
        "lyrics" : "歌声が聞こえた\n空をたゆたうあなたの声\nこの日は強い風の日で\n見上げたらもう居なくなってた\nゆうやけこやけのチャイムは\n早くお帰りよと\nそっと教えてくれたけど\n目を開けたら日が暮れていた\n帰りの空はとても赤くて\n急いだのを覚えています\n名の無い星が空に堕ちたら\n鯨の歌が聞こました\n天の川の方へ\nどんどん伸びる彼方の影\n呼ぶ声が聞こえないほど\n遠くの空へ飛んでいった\nむつまじく\nあやとりをして\nわらうのに\nむちゅうで\nめをつむり\nかぞえおろして\nたのしそうに\nてをふっていた\n帰りの空はとても赤くて\n見るや否や走っていった\n名の無い星が空に堕ちたら\n鯨の歌が聞こえるでしょう\nわらべ歌の意味は\n二度と思い出せず\n緩やかに忘れられて\n瑠璃色の石になるでしょう\n帰りの空はとても赤くて\n見るや否や走っていった\n名の無い星が空に堕ちたら\n鯨の歌が聞こえるでしょう\n帰りの空はとても赤くて\n見るや否や走っていった\n名の無い星が空に堕ちたら\n鯨の歌が聞こえるでしょう\n歌声が聞こえた\n空をたゆたうあなたの声",
        "imitate" : "原曲"
    },
    {
        "title" : "エヌ",
        "lyrics" : "国道沿いの海で、可視光線が笑い。\n斜め後ろの熱病は、推敲を重ねると言う。\n天狗の面を被った、懐かしい栄養が。\nゴミ捨て場から飛び降りて、\n明日が転がった。\n放射状の四季と、\nそれを食べる怖さ。\nつま先立ちでも、足りないのです。\n因数分解とオタマジャクシは、\n刃物で日記を混ぜました。\n私は細胞ですが、\n肉はエヌですか？\nギザ十が泣いていました、\n井戸は見えますか？\nお地蔵様は緩み、アナクロの曇り雨。\n夢見心地のビーカーは、妙な感じがすると言う。\n無痛の地下室では、白夜とは呼べないが。\nぬいぐるみが覚えていた。\n待ち合わせの音。\n紙粘土が暮らす、\n除草剤のままで。\n檻の曜日より、葦が行う。\nデジタルデータは今でも達磨で、\n８×８＝６４の名残です。\n私は細胞ですが、\n肉はエヌですか？\nギザ十が泣いていました、\n井戸は見えますか？\n新しい解剖は、有り得べき。\nそれに気がついても、おびやかされ。\n確証バイアス達は、\n斯く語りき。\n私は細胞ですが、\n肉はエヌですか？\nギザ十が泣いていました、\n井戸は見えますか？\n私は細胞ですが、\n肉はエヌですか？\nギザ十が泣いていました、\n井戸は見えますか？\n何が見えますか？",
        "imitate" : "原曲"
    }
]


def get_API(url) :
    try :
        get = requests.get(url)
    except :        # プロキシエラー等のエラーが発生したら
        print("5xx Error")
        return ""

    if (get.status_code == 200) :
        try :
            get_dict = get.json()
        except :        # JSON形式ではなかったら（メンテナンス等）
            print("Not JSON Error", get.status_code)
            return ""

        if "error" in get_dict :     # dictのキーにerrorがあったら
            print("Invalid path Error", get.status_code)
            return ""
        
        if "message" in get_dict :     # dictのキーにerrorがあったら
            print("404 on json API", get.status_code)
            
        else :      # 正常に取得できたら
            print("OK", get.status_code)
            return get_dict

    else :      # エラーステータスコードを受け取ったら（HEROKU error等）
        print("not 2xx", get.status_code)
        return ""


def top(request):
    return render(request, 'subeana/top.html')


def new(request) :
    dir = {}

    if request.method == "POST":
        inp_title = request.POST.get("title")
        inp_channel = request.POST.get("channel")
        inp_url = request.POST.get("url")
        inp_lyrics = request.POST.get("lyrics")
        inp_imitatenums = request.POST.get("imitatenums")

        if ("" in [inp_title, inp_channel, inp_imitatenums]) :
            return render(request, "subeana/error.html")

        ins_song, _ = Song.objects.get_or_create(title = inp_title, defaults = {"title" : inp_title})
        ins_song.title = inp_title
        ins_song.channel = inp_channel
        if inp_url :
            if inp_url in "https://www.youtube.com/watch?v=" :
                url = "https://youtu.be/" + inp_url[32:44]
                ins_song.url = url
            else :
                ins_song.url = inp_url
        if inp_lyrics :
            ins_song.lyrics = inp_lyrics

        imitates = set()
        for i in range(int(inp_imitatenums)) :
            imitate = request.POST.get(f"imitate{i + 1}")
            if imitate == "模倣曲模倣" :
                imitate = request.POST.get(f"imitateimitate{i + 1}")
                if imitate :
                    imitates.add(imitate)
            else :
                imitates.add(imitate)

        imitates.discard("模倣曲模倣")
        ins_song.imitate = str(list(imitates))
        ins_song.save()

    BASE_DIR = str(BASE_DIRpath)
    if "C:" in BASE_DIR :
        dir["basedir"] = "http://127.0.0.1:8000"
    elif "heroku" in BASE_DIR :
        BASE_DIR = ""
        
    return render(request, 'subeana/new.html', dir)


def song(request, song_title) :
    dir = {"title" : song_title}
    return render(request, "subeana/song.html", dir)

def error(request) :
    return render(request, "subeana/error.html")


def dev(request) :
    dir = {"locked" : True}
    if request.method == "POST":
        password = request.POST.get("password")
        
        BASE_DIR = str(BASE_DIRpath)
        if "C:" in BASE_DIR :
            BASE_DIR = "http://127.0.0.1:8000"
        elif "heroku" in BASE_DIR :
            BASE_DIR = ""
        dir["BASE_DIR"] = BASE_DIR

        if password :
            if hashlib.sha256(password.encode()).hexdigest() == SHA256a :
                dir["locked"] = False
        else :
            Song.objects.all().delete()

            for song in SUBEANA_LIST :
                requests.post(url = BASE_DIR + "/subeana/api/song/?format=json" ,data = song)
            
    return render(request, "subeana/dev.html", dir)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer