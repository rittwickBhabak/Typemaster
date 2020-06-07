# models.py
from myproject import db, login_manager
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    avgSpeed = db.Column(db.Integer)
    level = db.Column(db.Integer)
    weakKeys = db.Column(db.String)
    def __init__(self,name,email,username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password_hash = gph(password)
        self.level = 0
        self.weakKeys = str({"97": 0, "98": 0, "99": 0, "100": 0, "101": 0, "102": 0, "103": 0, "104": 0, "105": 0, "106": 0, "107": 0, "108": 0, "109": 0, "110": 0, "111": 0, "112": 0, "113": 0, "114": 0, "115": 0, "116": 0, "117": 0, "118": 0, "119": 0, "120": 0, "121": 0, "122": 0, "65": 0, "66": 0, "67": 0, "68": 0, "69": 0, "70": 0, "71": 0, "72": 0, "73": 0, "74": 0, "75": 0, "76": 0, "77": 0, "78": 0, "79": 0, "80": 0, "81": 0, "82": 0, "83": 0, "84": 0, "85": 0, "86": 0, "87": 0, "88": 0, "89": 0, "90": 0, "96": 0, "49": 0, "50": 0, "51": 0, "52": 0, "53": 0, "54": 0, "55": 0, "56": 0, "57": 0, "48": 0, "45": 0, "61": 0, "126": 0, "33": 0, "64": 0, "35": 0, "36": 0, "37": 0, "94": 0, "38": 0, "42": 0, "40": 0, "41": 0, "95": 0, "43": 0, "91": 0, "93": 0, "123": 0, "125": 0, "124": 0, "59": 0, "39": 0, "58": 0, "34": 0, "44": 0, "46": 0, "47": 0, "60": 0, "62": 0, "63": 0})
    def check_password(self,password):
        return cph(self.password_hash,password)

# class PracticeLine(db.Model):
#     __tablename__ = 'practicelines'
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(64))
#     def __init__(self,text):
#         self.text = text 

class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    line_id = db.Column(db.Integer)
    speed = db.Column(db.Float)
    error = db.Column(db.Integer)

    def __init__(self,user_id,line_id,speed,error):
        self.user_id = user_id
        self.line_id = line_id
        self.speed = speed
        self.error = error

class TestResults(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    speed = db.Column(db.Float)
    accuracy = db.Column(db.Float)
    def __init__(self,user_id,speed,accuracy):
        self.user_id = user_id
        self.speed = speed
        self.accuracy = accuracy

PracticeLine = [
    "jkkjk kjkkj jkjjk kkjkj jjkjk jkjkk kjkjj jkjkj kkjkj jjkjk",
    "dffdf fdffd dfddf ffdfd ddfdf dfdff fdfdd dfdfd ffdfd ddfdf",
    "dkfdj jdfkf kjdkf fkjdk fkdkj fkfdj kjdkf dfkfj kfkdj fjkjd",
    "djk kjd dfk kfdf jdfk jkjdj",
    "l;;l; ;l;;l l;ll; ;;l;l ll;l; l;l;; ;l;ll l;l;l ;;l;l ll;l;",
    "lfk ;fk djlf kflf ;fkj kj;f dj;;f ;f;lf ;lfkf dljdf ;f;lfkf",
    "assas sassa asaas ssasa aasas asass sasaa asasa ssasa aasas",
    "all add; as ask; sad; fas lad dak; dad fad fall; lass dall;",
    "alas dald fall; dad flak; lass sad; fass; all fall lad; ask",
    "ghhgh hghhg ghggh hhghg gghgh ghghh hghgg ghghg hhghg gghgh",
    "gad has aha; had flag gas; sag ash; gag dash glag half;",
    "gaff; hall hald saga hash; sash gall flag; has dash half",
    "rttrt trttr rtrrt ttrtr rrtrt rtrtt trtrr rtrtr ttrtr rrtrt",
    "art tad gar at sat rag tag; far jar tar rah hat rat rag tat",
    "daft dart jars task; hard tart start grad data talk; shaft rash",
    "hart; haft karat halt salt dark; raft draft shark; fart grass",
    "graft fast raja shark gard shard start lard; flat",
    "yuuyu uyuuy yuyyu uuyuy yyuyu yuyuu uyuyy yuyuy uuyuy yyuyu",
    "day fly dug lay jay sky lug fur fry try hut; say lady yard",
    "lush gay shut fray surd lurk usual surf flay just lust dust",
    "vbbvb bvbbv vbvvb bbvbv vvbvb vbvbb bvbvv vbvbv bbvbv vvbvb",
    "bad vag bug bar vug vas vat bav bay bat bag bah vast bur",
    "baby vagary burst vary ruby valuta buy vast vault vulgar by",
    "nmmnm mnmmn nmnnm mmnmn nnmnm nmnmm mnmnn nmnmn mmnmn",
    "ham gun jam ran gum man fun mat nab arm sun may nut tun mud",
    "hang damm harm darn farm hung lamb rang sand tang tank many",
    "must bank gang busy hand thank bury junk human marry funny",
    "numb bush ray baulk flask bald stuff bask shark navy hurry",
    "iooio oiooi ioiio ooioi iioio ioioo oioii ioioi ooioi iioio",
    "hid ill oil for hit out rid dog hot old too sit oat fin aim",
    "weewe eweew wewwe eewew wwewe wewee eweww wewew eewew wwewe",
    "red tea way leg tie let see owe wet set lie few how sir who",
    ",..,. .,.., ,.,,. ..,., ,,.,. ,.,.. .,.,, ,.,., ..,., ,,.,.",
    "why, yes. low, two, was, den. led. ebb, ten, you. new, met.",
    "xccxc cxccx xcxxc ccxcx xxcxc xcxcc cxcxx xcxcx ccxcx xxcxc",
    "act, six icy cub fix cab car. wax cry arc axe, can cat cod",
    "also take, wake late ease, joke sort food obey under beyond",
    "exercise hair rare. gold xenon warry; worm shirt luxury soul",
    "after death known; early first jewel large offer raise order",
    "hotel later ready. agree dirty earth, floor weight water soil",
    "night knife; house lunch naught yield; world story where habit",
    "zqqzq qzqqz zqzzq qqzqz zzqzq zqzqq qzqzz zqzqz qqzqz zzqzq",
    "zoo quit zit quite zoom quick zest zing quake zeal zany",
    "p[[p[ [p[[p p[pp[ [[p[p pp[p[ p[p[[ [p[pp p[p[p [[p[p pp[p[",
    "put opaque [pup puzzle [proposal [prompt plan [pomp lamp",
    "']]'/ ]'/]' ']'/] /]']' '/]'] ']'/] ]']/' /]']' ]/']' '']/]",
    "plus/minus; acropolis' [appall] miles/hour [cm/sec] per' pair",
    "zombie square; poetic /marquee/ question prize [quiz] proper",
    "poster. price queen [plate] zippy, reply zero km/h quality;",
    "zigzag' porosity, quantity peace/poker camp zodiac damp plan",
    "zone quarter. prosperity zirconium' /pound/ power; [press]",
    "zipper [zoological] quack, piece proud; pearl. penetrate/",
    "mean mean mean mean mean mean mean mean mean mean mean mean",
    "jeans jeans jeans jeans jeans jeans jeans jeans jeans jeans",
    "echo echo echo echo echo echo echo echo echo echo echo echo",
    "thin thin thin thin thin thin thin thin thin thin thin thin",
    "disk disk disk disk disk disk disk disk disk disk disk disk",
    "dish dish dish dish dish dish dish dish dish dish dish dish",
    "dale dale dale dale dale dale dale dale dale dale dale dale",
    "oils oils oils oils oils oils oils oils oils oils oils oils",
    "path path path path path path path path path path path path",
    "last last last last last last last last last last last last",
    "land land land land land land land land land land land land",
    "pets pets pets pets pets pets pets pets pets pets pets pets",
    "mean jeans echo thin disk dish dale oils path last land pets",
    "mean jeans echo thin disk dish dale oils path last land pets",
    "mean jeans echo thin disk dish dale oils path last land pets",
    "mean jeans echo thin disk dish dale oils path last land pets",
    "mean jeans echo thin disk dish dale oils path last land pets",
    "pound pound pound pound pound pound pound pound pound pound",
    "pits pits pits pits pits pits pits pits pits pits pits pits",
    "ryas ryas ryas ryas ryas ryas ryas ryas ryas ryas ryas ryas",
    "ebbed ebbed ebbed ebbed ebbed ebbed ebbed ebbed ebbed ebbed",
    "risk risk risk risk risk risk risk risk risk risk risk risk",
    "reeks reeks reeks reeks reeks reeks reeks reeks reeks reeks",
    "leak leak leak leak leak leak leak leak leak leak leak leak",
    "lens lens lens lens lens lens lens lens lens lens lens lens",
    "flux flux flux flux flux flux flux flux flux flux flux flux",
    "leave leave leave leave leave leave leave leave leave leave leave leave",
    "leis leis leis leis leis leis leis leis leis leis leis leis",
    "leaf leaf leaf leaf leaf leaf leaf leaf leaf leaf leaf leaf",
    "pound pits ryas ebbed risk reeks leak lens flux leave leis leaf",
    "pound pits ryas ebbed risk reeks leak lens flux leave leis leaf",
    "pound pits ryas ebbed risk reeks leak lens flux leave leis leaf",
    "pound pits ryas ebbed risk reeks leak lens flux leave leis leaf",
    "pound pits ryas ebbed risk reeks leak lens flux leave leis leaf",
    "lief lief lief lief lief lief lief lief lief lief lief lief",
    "lazy lazy lazy lazy lazy lazy lazy lazy lazy lazy lazy lazy",
    "keno keno keno keno keno keno keno keno keno keno keno keno",
    "quack quack quack quack quack quack quack quack quack quack",
    "knife knife knife knife knife knife knife knife knife knife",
    "jack jack jack jack jack jack jack jack jack jack jack jack",
    "chap chap chap chap chap chap chap chap chap chap chap chap",
    "sock sock sock sock sock sock sock sock sock sock sock sock",
    "keys keys keys keys keys keys keys keys keys keys keys keys",
    "obey obey obey obey obey obey obey obey obey obey obey obey",
    "men's men's men's men's men's men's men's men's men's men's",
    "caps caps caps caps caps caps caps caps caps caps caps caps",
    "lief lazy keno quack knife jack chap sock keys obey men's caps",
    "lief lazy keno quack knife jack chap sock keys obey men's caps",
    "lief lazy keno quack knife jack chap sock keys obey men's caps",
    "lief lazy keno quack knife jack chap sock keys obey men's caps",
    "lief lazy keno quack knife jack chap sock keys obey men's caps",
    "vile vile vile vile vile vile vile vile vile vile vile vile",
    "fine fine fine fine fine fine fine fine fine fine fine fine",
    "vent vent vent vent vent vent vent vent vent vent vent vent",
    "vale vale vale vale vale vale vale vale vale vale vale vale",
    "back back back back back back back back back back back back",
    "bans bans bans bans bans bans bans bans bans bans bans bans",
    "bags bags bags bags bags bags bags bags bags bags bags bags",
    "tins tins tins tins tins tins tins tins tins tins tins tins",
    "gift gift gift gift gift gift gift gift gift gift gift gift",
    "grit grit grit grit grit grit grit grit grit grit grit grit",
    "herb herb herb herb herb herb herb herb herb herb herb herb",
    "hand hand hand hand hand hand hand hand hand hand hand hand",
    "vile fine vent vale back bans bags tins gift grit herb hand",
    "vile fine vent vale back bans bags tins gift grit herb hand",
    "vile fine vent vale back bans bags tins gift grit herb hand",
    "vile fine vent vale back bans bags tins gift grit herb hand",
    "vile fine vent vale back bans bags tins gift grit herb hand",
    "ouoie uaueo iyaei yoeia eyaie uaoyi oyaey iyoeo iouya eaiyu",
    "ieyoi auyei oeaui eyaey oyuae eyoei uyieo aeoyi yioae oiyeu",
    "aeoua ieyoa uaeoe iaeoa ueaya aeyoi uaeoy eioae uaeya ioeia",
    "oeiau yoeie ieaua ieyei auaeo yoieu aeyoi auioy eaiae uoaie",
    "oyeao ieauy ioeya aueai oaeya iueie yoeau eioei aeyei iyuoa",
    "gowof hrocj ayxle rfkqk dugpw cjxln dma]e xjnup skxnz rmokl",
    "aixle rlnlb dmywg tvprh lumtk ajrmw heomc zlnuk pfpex ndlyv",
    "nsptn bwitk zopsw vkstg mdibw auvle quvkn smrkx nithd krihx",
    "odmyl dlekh xutnv cmdiw lwubr hcken amrug ltnxp kwoby cysna",
    "kruxm aodnw ylq]s kpayc xuspg nzkej iehxf krmxl hsitb dmysk",
    "ing ing ing ing ing ing ing ing ing ing ing ing ing",
    "tion tion tion tion tion tion tion tion tion tion tion",
    "ment ment ment ment ment ment ment ment ment ment ment",
    "ure ure ure ure ure ure ure ure ure ure ure ure ure ure",
    "sion sion sion sion sion sion sion sion sion sion sion",
    "ous ous ous ous ous ous ous ous ous ous ous ous ous ous",
    "our our our our our our our our our our our our our our",
    "er or er or er or er or er or er or er or er or er or",
    "tch tch tch tch tch tch tch tch tch tch tch tch tch tch",
    "ck ch ck ch ck ch ck ch ck ch ck ch ck ch ck ch ck ch ck",
    "ea ea ea ea ea ea ea ea ea ea ea ea ea ea ea ea ea ea ea",
    "er er er er er er er er er er er er er er er er er er er",
    "the ht the ht the ht the ht the ht the ht the ht the ht the",
    "ght ght ght ght ght ght ght ght ght ght ght ght ght ght ght",
    "es ly es ly es ly es ly es ly es ly es ly es ly es ly es ly",
    "ed ed ed ed ed ed ed ed ed ed ed ed ed ed ed ed ed ed ed",
    "and and and and and and and and and and and and and and",
    "78878 87887 78778 88787 77878 78788 87877 78787 88787 77878",
    "mean7 jeans8 echo7 thin8 disk7 dish8 dale7 oils8 path7 last8",
    "56656 65665 56556 66565 55656 56566 65655 56565 66565 55656",
    "land5 pets6 pound8 pits7 ryas5 ebbed6 risk5 reeks7 leak8 lens6",
    "90090 09009 90990 00909 99090 90900 09099 90909 00909 99090",
    "flux9 lave0 leis7 leaf0 lief6 lazy9 keno5 quack9 knife8 jack0",
    "34434 43443 34334 44343 33434 34344 43433 34343 44343 33434",
    "chap3 sock4 keys3 obey0 men's7 caps4 vile3 fine4 vent6 vale4",
    "-==-= =-==- -=--= ==-=- --=-= -=-== =-=-- -=-=- ==-=- --=-=",
    "back= bans- bags3 tins- gift4 grit= herb5 hand= pink7 chin=",
    "12212 21221 12112 22121 11212 12122 21211 12121 22121 11212",
    "cash2 come1 earn= evil2 form- join3 vote1 deck6 fern2 zeal1",
    "only6 pain3 sale3 rank0===king7 5bait5 3 5deny5 3 4find42-10",
    "17-5=12 8-3=5 10-3=7 6-4=2 13-2=11 19-4=15 8-5=3 5-1=4 19-12=7",
    "49-1=48 12-3=9 15-9=6 12-8=4 11-4=7 19-13=6 12-3=9 10-6=4 9-4=5",
    "GHDJY GYDUC Z:CCH HGXCD V:JPR JGKXG JDJEG YLG<N JENGT CJGCY",
    "GTY<D FGYDH KYNUN RDA:G F<DUJ LPDUY RLCPF GCGGD YAFCJ YGEXR",
    "RPVDC D<DV BVXCN TWYPY DNBTG AGLYV RFKBD HYPVL YRPJC G<H:X",
    "MAGIC RIVER MONEY NOISE PAPER WOMAN EVENT ANGRY COVER METAL",
    "COMPANY HORSES HAPPY SPECIAL VENTURE CHANGE RETURN KNIGHT",
    "MagiC RiveR MoneY NoisE PapeR WomaN EvenT AngrY CoveR MetaL",
    "ComPanY HorSeS HappY SpeCiaL VenTurE ChaNgE RetUrN KniGhT",
    "! @! @ !@! @ ! @!! ! @! @@ !@@ @ ! !@ @ !!@ !@ ! @! @ @! !@@",
    "@song ! song @! song @ song !@ song ! song @@! song @ song !!",
    "# $# #$$ $# $#$ # $ $ ##$ # $# $ #$# # $#$ #$ $ # $$# $ #$$",
    "rain $ rain #$ rain ##$ rain # rain $# rain $ rain $# rain $",
    "%^ ^ %%^ % ^% ^ %^% ^^ % ^%^ ^ %^ % ^%% ^% ^ %^^ % ^^% % ^%^",
    "pale %^ pale ^ pale ^%^ pale % pale %^ pale ^% pale ^ pale %",
    "& *& * &*& * *&& & *& ** &** & * &* * &&* &* & *& * *& &* **",
    "calf & calf *& calf * calf &*& calf & calf **& calf * calf &",
    "() ) ( ))( ( )( ()( ) () ))( ( ) ))( )( ) (() )( ( )() () ((",
    "mask ( mask )( mask) mask ( mask )() mask ) mask () mask )(",
    "+ _ _+_ _+ _ __+ +_+ _ ++ _+ + _ ++_ _ + +_+ _ +_ + _+ + _+_",
    "mine _ mine +_ mine _+_ mine + mine _+ mine + mine _ mine _+",
    "coal (@ coal ?# coal ) coal $^ coal #_ coal )% coal & coal ^",
    "face $ face #( face $% face * face ^_ face @ face ) face %&@",
    "deal *$ deal )# deal ( deal &? deal %^ deal &_ deal $ deal @",
    "view & view @# view (_) view $ view * view % view ^_ view &$",
    "maid ^ maid &# maid * maid (% maid )$ maid ?_ maid & maid %#",
    "task * task $( task )@^ task % task *_ task # task ) task &$",
    "part % part #? part &( part ) part $ part &_ part ?#* part ^",
    "1. Mean, 2. Jeans, 3. Echo? 4. Thin, 5. Disk? 6. Dish, 7. Last? 8. Oils, 9. Path",
    "1. A bad workman quarrels with his tools.",
    "2. Better a glorious death than a shameful life.",
    "3. Calamity is man's true touchstone.",
    "4. Eat at pleasure, drink with measure.",
    "5. He who pleased everybody died before he was born.",
    "6. Jack of all trades and master of none.",
    "7. Keep a thing seven years and you will find a use for it.",
    "8. Make hay while the sun shine.",
    "9. Between two stools one falls to the ground.",
    "10. Roll my log and I will roll yours.",
    "11. Scornful dogs will eat dirty puddings.",
    "12. We never know the value of water till the well is dry.",
    "13. Old birds are not to be caught with chaff.",
    "14. Zeal without knowledge is a runaway horse.",
    "15. Better die standing than live kneeling.",
    "Looks like I'm typing a bit faster now. Now it's a good time to take a certification test."

]
TestLines = ['this is text line 1', 'this is text line 2']
# TestLines = [
#     '''In parts of Alaska, it's illegal to feed alcohol to a moose. You're subject to fines and/or imprisonment for making "ugly faces" at dogs in Oklahoma. In Utah, birds have the right of way on all highways. Christmas was once illegal in England. In Turkey, in the sixteenth and seventeenth centuries, anyone caught drinking coffee was put to death. It is illegal to hunt camels in the state of Arizona.''',
#     '''The first telephone exchange opened on January 28, 1878, in New Haven, Connecticut. In the late 30's, a man named Abe Pickens of Cleveland, Ohio, attempted to promote world peace by placing personal calls to various country leaders. He managed to contact Mussolini, Hirohito, Franco and Hitler (Hitler, who didn't understand English, transferred him to an aide). He spent $10,000 to "give peace a chance."''',
#     '''It's impossible to sneeze with your eyes open. The expression "to get fired" comes from long, long ago. When clans wanted to get rid of their unwanted people without killing them used to burn their houses down. The word 'corr' actually means 'odd' in Irish. Los Angeles' full name is "El Pueblo de Nuestra Senora la Reina de los Angeles de Porciuncula". In English this means 'The City of Angels'.''',
#     '''Abe Silverstein, who headed NASA's Space Flight Development Program, proposed the name Apollo for the space exploration programs in the 1960's. He chose that legendary Greek name because the virile Apollo was a god who rode through the skies in a magnificent golden dent of naming manned spacecraft for mythological gods had been set earlier with Project Mercury, also named by Silverstein.''',
#     '''Human skulls had been used as drinking cups for hundreds of years. The muscles and flesh were scraped away, the bottom was hacked off and then they were suitable to hold any beverage. The first Bowie knife was forged at Washington, Arkansas. All the dirt from the foundation to build the World Trade Center in NYC was dumped into the Hudson River to form the community now known as Battery City Park.''',
#     '''In 1845 Boston had an ordinance banning bathing unless you had a doctor's prescription. Hypnotism is banned by public schools in San Diego. Texas is the only state that permits residents to cast absentee ballots from space. The first to exercise this right to vote while in orbit was astronaut David Wolf, who cast his vote for Houston mayor via e-mail from the Russian space station Mir in November 1997.''',
#     '''When Thomas Jefferson became U.S. President in 1801, 20 percent of all people in the young nation were slaves. Early Egyptians wore sandals made from woven papyrus leaves. The Marquis de Lafayette, America's Revolutionary War ally, named his only son George Washington Lafayette. Karl Marx and Friedrich Engels, the fathers of communism, wrote 500 articles for the "New York Tribune" from 1851 to 1862.''',
#     '''Ancient Greeks wove marjoram into funeral wreaths and put them on the graves of loved ones. The wreaths served as prayers for the happiness of the deceased in a future life. Breaking of a glass is traditional in some wedding ceremonies. This custom symbolizes different things. To some it is the destruction of the temple in Jerusalem, and for some it is the represents the fragility of a relationship.''',
#     '''Marco Polo was born on the Croatian island of Korcula (pronounced Kor-Chu-La). Karl Marx was targeted for assassination when he met with two Prussian officers in his house in Cologne in 1848. Marx had friends among the German labor unions, and he was considered a threat to the autocrats. Dressed in his bathrobe, he forced the officers out at the point of a revolver, which, it turned out, was not loaded.''',
#     '''In 1974 there were 90 tornadoes in the U.S. in one day. Satirist Jonathan Swift suggested in his essay "A Modest Proposal" that the children of the poor be sold as food to feed the rich. This shocking essay is one of the best examples of satire you'll find. Akhbar the Great Mughal routed the Hindus under Hemu by turning their elephants against them at the battle of Panipat in the Hindu revolt.''',
#     '''The human heart creates enough pressure when it pumps out to the body to squirt blood 30 feet. Bats always turn left when exiting a cave. Our eyes are always the same size from birth, but our nose and ears never stop growing. All polar bears are left-handed. A snail can sleep for three years. Elephants are the only animals that can't jump. Only one person in two billion will live to be 116 or older.''',
#     '''The minimum age set in the U.S. Constitution for the President of the United States is 35. In Athens, Greece, a driver's license can be taken away by law if the driver is deemed either "unbathed" or "poorly dressed". Impotence is grounds for divorce in 24 U.S. states. The murder rate in the United States is 200 times greater than in Japan. In Japan no private citizen can buy a handgun legally.''',
#     '''The steel industry, in 1943, introduced the 5-day, 40 hour work week. Henry Ford adopted it in 1926. 1892 by Presidential Proclamation 1.8 million acres of Crow Indian reservation in Montana were opened to White settlers. The U.S. government had induced the Crow to give up a sizable portion of their land in the mountainous western area of Montana. The Crow received 50 cents per acre for their land.''',
#     '''Americans on the average eat 18 acres of pizza every day. Banging your head against a wall uses 150 calories an hour. Contrary to popular belief, the British flag is not called "The Union Jack" it is actually called "The Union Flag". It's only called the Union Jack when out at sea on navy ships. You are most likely to get murdered at Christmas time due to more alcohol being drunk. Merry Christmas.''',
#     '''The mythical Scottish town of Brigadoon appears for one day every 100 years. January named after the Roman god Janus. Influenza got its name from the fact that people believed the disease was because of the evil "influence" of stars. During the middle ages, it was widely believed that men had one less rib than women. This is because of the story in the Bible that Eve had been created out of Adam's rib.''',
#     '''Traffic engineering was not developed in London, New York or Paris, but rather in ancient Rome. The Romans, of course, were noted road builders. The Appian Way, for example, stretched 350 miles from the Eternal City to Brundisium. In Rome itself there were actually stop signs and even alternate-side-of-the-street parking. Until the 19th century, solid blocks of tea were used as money in Siberia.''',
#     '''In some smaller towns in the state of Arizona, it is illegal to wear suspenders. In South America, it would be rude not to ask a man about his wife and children. In most Arab countries, it would be rude to do so. Being rude to a telephone operator in Prussia was once a crime. In 1908, a respected citizen was reprimanded by the government after becoming exasperated with an operator and saying "My dear girl!"''',
#     '''American Airlines saved $40,000 in 1987 by eliminating one olive from each salad served in first-class. Sticking your two middle fingers up dates back from the middle ages. When archers were caught they had their two middle fingers cut off so that they couldn't shoot any more arrows. So when an archer was shooting people he would stick his fingers up to say "look I still have them, hahaha".''',
#     '''In the Middle Ages, the highest court in France ordered the execution of a cow for injuring a human. A girl, in the Vacococha tribe of Peru, to prepare her for marriage at the age of 12, is placed in a basket in the hut of her prospective in-laws and must remain suspended over an open fire night and day for 3 months. The Spanish Inquisition once condemned the entire Netherlands to death for heresy.''',
#     '''Virginia O'Hanlon Douglas was the eight-year-old girl who, in 1897, asked the staff of The New York Sun whether Santa Claus existed. In the now-famous editorial, Francis Church assured Virginia that yes, indeed, "there is a Santa Claus." The first dictionary of American English was published on April 14th, 1828, by - who else? - Noah Webster. No automobile made after 1924 should be designated as antique.''',
#     '''The Eisenhower interstate system requires that one-mile in every five must be straight. These straight sections are usable as airstrips and in times of war or other emergencies. The water of Angel Falls (the World's highest) in Venezuela drops 3,212 feet (979 meters). They are 15 times higher than Niagara Falls. Theatres in Glendale, California can show horror films only on Monday, Tuesday, or Wednesday.''',
#     '''John Hancock was the only one of fifty signers of the Declaration of Independence who actually signed it on July 4. The first United States coast to coast airplane flight occurred in 1911 and took 49 days. Escape maps, compasses, and files were inserted into Monopoly game boards and smuggled into POW camps inside Germany during W.W.II; real money for escapees was slipped into the packs of Monopoly money.''',
#     '''In most American states, a wedding ring is exempt by law from inclusion among the assets in a bankruptcy estate. This means that a wedding ring cannot be seized by creditors, no matter how much the bankrupt person owes. In New York State, it is still illegal to shoot a rabbit from a moving trolley car. Vermont, Alaska, Hawaii, and Maine are the four states in the U.S. that do not allow billboards.''',
#     '''Babies are born without knee caps. They don't appear until the child reaches 2-6 years of age. Modern records do not compare with that of St Simeon the younger called stylites a monk who spent the final 45 years of his life living at the top of a stone pillar on the hill of wonders near Antioch in Syria! 14% of all facts and statistics are made up and 27% of people know that fact.''',
#     '''23% of all photocopier faults worldwide are caused by people sitting on them and photocopying their butts. In every episode of Seinfeld there is a Superman somewhere. If the government has no knowledge of aliens, then why does Title 14, Section 1211 of the Code of Federal Regulations, implemented on July 16, 1969, make it illegal for U.S. citizens to have any contact with extraterrestrials or their vehicles?''',
#     '''Houses were first numbered in Paris in 1463. In Britain, numbering did not appear until 1708, on a street in London's Whitechapel area. In ancient Greece, courtesans wore sandals with nails studded into the sole so that their footprints would leave the message "Follow me". In 1937 the emergency 999 telephone service was established in London. More than 13,000 genuine calls were made in the first month.''',
#     '''Virginia O'Hanlon Douglas was the eight-year-old girl who, in 1897, asked the staff of The New York Sun whether Santa Claus existed. In the now-famous editorial, Francis Church assured Virginia that yes, indeed, "there is a Santa Claus." The first dictionary of American English was published on April 14th, 1828, by - who else? - Noah Webster. No automobile made after 1924 should be designated as antique.''',
#     '''A girl, in the Vacococha tribe of Peru, to prepare her for marriage at the age of 12, is placed in a basket in the hut of her prospective in-laws and must remain suspended over an open fire night and day for 3 months. The Spanish Inquisition once condemned the entire Netherlands to death for heresy. During the eighteenth century, books that were considered offensive were sometimes punished by being whipped.''',
#     '''In 1893, Chicago hired its first police woman. Her name was Marie Owens. While the city was progressive in its hiring practices, Chicago's female police officers were not allowed to wear uniforms until 1956. In ancient times, any Japanese who tried to leave his homeland was summarily put to death. In the 1630's, a decree in Japan forbade the building of any large ocean-worthy ships to deter defection.''',
#     '''DaVinci made detailed drawings of human anatomy, which are still highly regarded today. DaVinci wrote notebook entries in mirror (backwards) script, a trick that kept many of his observations from being widely known until decades after his death. It is believed that he was hiding his scientific ideas from the powerful Roman Catholic Church, whose teachings sometimes disagreed with what Leonardo observed.''',
#     '''It was only after 440 A.D. that December 25 was celebrated as the birth date of Jesus Christ. The first aerial photograph was taken from a balloon during the U.S. civil war. Olive oil was used for washing the body in the ancient Mediterranean world. In 1801, 20 percent of the people in the U.S. were slaves. Slaves under the last emperors of China wore pigtails so they could be picked out quickly.''',
#     '''During the Renaissance blond hair became so much de rigueur in Venice that a brunette was not to be seen except among the working classes. Venetian women spent hours dyeing and burnishing their hair until they achieved the harsh metallic glitter that was considered a necessity. During the Renaissance, fashionable aristocratic Italian women shaved their hair several inches back from their natural hairlines.''',
#     '''In Lehigh, Nebraska it's against the law to sell donut holes. Under the law of Mississippi, there's no such thing as a female Peeping Tom. Anti-modem laws restrict Internet access in the country of Burma. Illegal possession of a modem can lead to a prison term. Lawn darts are illegal in Canada. In Idaho a citizen is forbidden by law to give another citizen a box of candy that weighs more than 50 pounds.''',
#     '''The Guinness Book of Records holds the record for being the book most often stolen from public libraries. If you removed the stomach, the spleen, 75% of the liver, 80% of the intestines, one kidney, one lung, and virtually every organ from the pelvic and groin area, the human body would still be able to survive. In 10 minutes, a hurricane releases more energy than all of the world's nuclear weapons combined.''',
#     '''A B-25 bomber airplane crashed into the 79th floor of the Empire State Building on July 28, 1945. India tested its first nuclear bomb in 1974. After the great fire of Rome in A.D. 64, the emperor Nero ostensibly decided to lay the blame on Christians residing in the city of Rome. These he gathered together, crucified, covered in pitch (tar), and burnt alive. He walked around his gardens admiring the view.''',
#     '''Dentists have recommended that a toothbrush be kept at least 6 feet away from a toilet to avoid airborne particles resulting from the flush. The plastic things on the end of shoelaces are called aglets. Rixon was the first US president whose name contains all the letters from the word 'criminal'. The second was William Jefferson Clinton. A crocodile can't stick its tongue out.''',
#     '''Marco Polo was born on the Croatian island of Korcula (pronounced Kor-Chu-La). Karl Marx was targeted for assassination when he met with two Prussian officers in his house in Cologne in 1848. Marx had friends among the German labor unions, and he was considered a threat to the autocrats. Dressed in his bathrobe, he forced the officers out at the point of a revolver, which, it turned out, was not loaded.''',
#     '''China was the first country to introduce paper money (in 812), but it wasn't until 1661 that a bank (Banco-Sedlar of Sweden) issued banknotes. If the arm of King Henry I of England had been 42 inches long, the unit of measure of a "foot" today would be fourteen inches. But his arm happened to be 36 inches long and he decreed that the "standard" foot should be one-third that length: 12 inches.''',
#     '''Abe Silverstein, who headed NASA's Space Flight Development Program, proposed the name Apollo for the space exploration programs in the 1960's. He chose that legendary Greek name because the virile Apollo was a god who rode through the skies in a magnificent golden dent of naming manned spacecraft for mythological gods had been set earlier with Project Mercury, also named by Silverstein.''',
#     '''In 1878 Wanamaker's of Philadelphia was the first U.S. department store to install electric lighting. Playing cards were issued to British pilots in WWII. If captured, they could be soaked in water and unfolded to reveal a map for escape. The first telephone book ever issued contained only fifty names. It was published in New Haven, Connecticut, by the New Haven District Telephone Company in February, 1878.''',
#     '''In England, the Speaker of the House is not allowed to speak. If a statue in the park of a person on a horse has both front legs in the air, the person died in battle; if the horse has one front leg in the air, the person died as a result of wounds received in battle; if the horse has all four legs on the ground, the person died of natural causes. Peanuts are one of the ingredients of dynamite.''',
#     '''Mailing an entire building has been illegal in the U.S. since 1916 when a man mailed a 40,000-ton brick house across Utah to avoid high freight rates. Snoring is prohibited in Massachusetts unless all bedroom windows are closed and securely locked. It is also illegal to go to bed without first having a full bath. Women in Florida may be fined for falling asleep under a hair dryer, as can the salon owner.''',
#     '''King Tut's tomb contained four coffins. The third coffin was made from 2,500 pounds of gold. And in today's market is worth approximately $13,000,000. The very first enclosed shopping mall was and is Valley Faire in Appleton, Wisconsin. Not in Minnesota as most people believe. Appleton is also famous for being the birth place of Harry Houdini and the first city in America to use Hydro-electric power in homes.''',
#     '''In 1974 there were 90 tornadoes in the U.S. in one day. Satirist Jonathan Swift suggested in his essay "A Modest Proposal" that the children of the poor be sold as food to feed the rich. This shocking essay is one of the best examples of satire you'll find. Akhbar the Great Mughal routed the Hindus under Hemu by turning their elephants against them at the battle of Panipat in the Hindu revolt.''',
#     '''The human heart creates enough pressure when it pumps out to the body to squirt blood 30 feet. Bats always turn left when exiting a cave. Our eyes are always the same size from birth, but our nose and ears never stop growing. All polar bears are left-handed. A snail can sleep for three years. Elephants are the only animals that can't jump. Only one person in two billion will live to be 116 or older.''',
#     '''Found on a box of Kellogg's Pop-Tarts: "Warning: Pastry Filling May Be Hot When Heated" Found on the instruction sheet of a Conair Pro Style 1600 hair dryer: "WARNING: Do not use in shower. Never use while sleeping." Found on Bat Man The Animated Series Armor Set Halloween costume box: "PARENT: Please exercise caution, mask and chest plate are not protective; cape does not enable wearer to fly."''',
#     '''The British once went to war over a sailor's ear. It happened in 1739, when Britain launched hostilities against Spain because a Spanish officer had supposedly sliced off the ear of a ship's captain named Robert Jenkins. Alexander Hamilton and his son, Philip, both died on the same spot, and both during duels. Philip went first, 3 years before his father would be killed in that same field by Aaron Burr.''',
#     '''It is legal in North Dakota to shoot an Indian on horseback, provided you are in a covered wagon. The mummified hand of a notary public, chopped off for falsely certifying a document, has been on display in the city hall of Munster, Germany, as a warning to other notaries for 400 years. The curtain or veil used by some Hindus and Moslems to seclude or hide their women from strangers is called a "purdah."''',
#     '''The first aerial photograph was taken from a balloon during the U.S. civil war. Olive oil was used for washing the body in the ancient Mediterranean world. In 1801, 20 percent of the people in the U.S. were slaves. Slaves under the last emperors of China wore pigtails so they could be picked out quickly. Dinner guests during the medieval times in England were expected to bring their own knives to the table.''',
#     '''A girl, in the Vacococha tribe of Peru, to prepare her for marriage at the age of 12, is placed in a basket in the hut of her prospective in-laws and must remain suspended over an open fire night and day for 3 months. The Spanish Inquisition once condemned the entire Netherlands to death for heresy. During the eighteenth century, books that were considered offensive were sometimes punished by being whipped.''',
#     '''In Italy, it is illegal to make coffins out of anything except nutshells or wood. "To prevent violence" it was at one time customary at certain phases of the moon to chain and flog inmates of England's notorious Bedlam Hospital. In Milan, Italy, when an operator dialled a wrong number, the phone company fined the operator. In Hartford Connecticut, it is illegal for a husband to kiss his wife on Sundays.''',
#     '''Almonds are a member of the peach family. Dentists have recommended that a toothbrush be kept at least 6 feet away from a toilet to avoid airborne particles resulting from the flush. The plastic things on the end of shoelaces are called aglets. Rixon was the first US president whose name contains all the letters from the word 'criminal'. The second was William Jefferson Clinton.''',
#     '''The famous Citgo sign near Fenway Park in Boston is maintained not by Citgo, but by Boston's historical society. In the 1700's you could purchase insurance against going to hell, in London England. The Aztec Indians of Mexico believed turquoise would protect them from physical harm, and so warriors used these green and blue stones to decorate their battle shields. Black cats are considered lucky in England.''',
#     '''The Eisenhower interstate system requires that one-mile in every five must be straight. These straight sections are usable as airstrips and in times of war or other emergencies. The water of Angel Falls (the World's highest) in Venezuela drops 3,212 feet (979 meters). They are 15 times higher than Niagara Falls. Theatres in Glendale, California can show horror films only on Monday, Tuesday, or Wednesday.'''
# ]
