# class Solution:
#     def get_the_int_prifix_between_two_intigers(self, num1, num2):
#         if num1 >= 1 and num2 >= 1:
#             smaller_num_len = num1 if num1 < num2 else num2 # get the smalles length of these numbers 

#             num1 = str(num1)
#             num2 = str(num2)
#             smaller_num_len = str(smaller_num_len)

#             prifix = ''
#             for i in range(len(smaller_num_len)):
#                 if num1[i] == num2[i]:
#                     prifix += num1[i] # no matter which one
#                     continue
#                 break

#             return int(prifix) if prifix else None 

#     def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
#         all_prifixes = []
#         for i in arr1:
#             for j in arr2:
#                 prifix = self.get_the_int_prifix_between_two_intigers(i, j)
#                 if prifix:
#                     all_prifixes.append(prifix)
        
#         if len(all_prifixes) >= 1:
#             max_prif = all_prifixes[0]
#             for prif in all_prifixes:
#                 if prif > max_prif:
#                     max_prif = prif
            
#             return len(str(max_prif))
                    
#         return 0


        
# if __name__ == "__main__":
#     solu = Solution()
#     print(solu.longestCommonPrefix([13,27,45], [21,27,48]))


# shorter version
class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        all_prifixes = []
        for i in arr1:
            for j in arr2:

                smaller_num_len = len(str(i)) if i < j else len(str(j))

                prifix = []
                
                for x in range(smaller_num_len):
                    item1 = str(i)[x]
                    item2 = str(j)[x]
                    if item1 == item2:
                        prifix.append(item2) # no matter which one
                        continue
                    break

                if len(prifix):
                    all_prifixes.append(len(prifix))
        
        if all_prifixes:
            max_prif = all_prifixes[0]
            for prif in all_prifixes:
                if prif > max_prif:
                    max_prif = prif
            
            return max_prif
                    
        return 0

        






first = [73520658,50489637,93394597,43389305,39737040,53620666,71150760,43991343,54623856,28506707,7631333,57117611,77181556,91933655,94196336,50313666,49029806,28111632,62996497,67124163,80102084,37783871,38614885,1994346,66301619,97938482,32806714,68865733,16813679,92919443,52833199,82225940,63176698,24110492,16299679,29375085,28001197,4564727,2154225,90560317,38419714,30325254,73283345,2160554,89055921,7909630,1623803,6825206,42505684,66816499,7721400,77360021,81518835,24354646,30458303,27092657,60045940,20975453,91629801,90852562,88552993,30781694,26129999,84964101,90092453,68028045,3932918,65339170,30383879,18185254,12651635,81740949,41508309,10763133,78469374,22737096,73248730,32927719,22034292,82020240,11380206,1552625,85235343,60940952,83101362,41570522,84975638,28480755,59787311,14167948,1531384,99092681,23669100,96942140,11673532,43414531,76737431,94919669,3694562,15680268,89599526,96102941,43238992,64001258,29566635,13331535,14407562,59897160,46647325,36153452,88816452,54884056,37026596,54836820,74495165,66033989,56584566,60801451,17839705,26011170,78843200,84727920,30912616,809351,23160428,38533528,86468529,16230383,28862014,19990466,53244464,82743643,41294087,48886567,69111464,79967401,16508061,3708135,95650471,86028364,48169467,11503033,29645072,34163284,88751638,19232686,89506417,61847632,12570564,25018881,36490629,13059071,56793858,81998731,47065473,21391623,41389328,83944750,12631867,6774679,50304037,50814558,74305966,89686113,88973873,97105810,68067820,92316501,41147671,42239402,74094647,70193126,36421048,54094299,76225500,17548271,51542980,31895874,22033321,28662285,13244028,94468098,76056417,38601796,94524440,55567340,25668546,41379338,50651444,27521529,14858783,39163546,32867960,34843182,65004563,73881019,94343973,26683110,96995327,41370214,72950360,65006108,12950327,6981629,97203515,82722825,82166976,10841279,85310668,71891778,53333830,67219879,56404464,38778014,85555402,92904335,53254156,81907956,81019460,40307478,59068712,49916854,98211909,53049015,37797429,18312102,80745767,65632224,56092786,85649518,27357504,25548304,89242383,44187829,57542103,77238890,69946068,51585147,63684161,84145062,23382558,58105880,44853173,29873019,44880275,66681376,37332056,69303411,48479600,80950411,62719122,74452670,44096330,9662118,52723395,11157296,94307243,56473324,59565173,88865551,50314429,28434692,7220206,67445192,23005284,40169382,74648529,13298023,72830368,55859278,14136106,28579085,20744343,53504093,5296261,13650433,83943338,85346578,36462734,18001094,1579159,98435551,63728004,58929571,61475731,5981120,21576277,21570241,96113900,71497677,7207157,63061081,57339960,24079595,39051788,17260161,72440332,90365548,3540606,56668091,18503785,96142870,57148757,96547949,84349716,24573337,60777539,99709319,7860197,31192025,82963482,21608723,93534809,62229625,72985103,93151953,780286,10306536,94245170,15184071,74782332,22049540,90558372,27541674,54217389,79993408,70013197,9497395,50349081,73912528,94799245,37688965,80479045,12461777,44792767,77322162,67631302,89814076,34848209,60515094,77101277,3097471,35711675,58797943,68525748,99979796,5871,50879917,17479428,96073370,63834970,83947680,94972819,23650948,40390510,23624275,96167055,28642262,84309844,75669867,81356695,68727387,18313111,2202131,26295901,8720548,68850929,72167580,53864911,83303431,11122626,4529060,1277081,95381675,24295654,47897921,479442,64966176,50690253,72120922,30615661,45690593,37701292,94068096,78988556,65800228,41774467,84915774,83302792,68634803,11384406,56330032,26768680,13085930,86588246,5570419,22026002,92504723,10350393,22670571,29886158,65916515,95760241,86284872,21884055,71492619,15471674,70696332,25449613,77506971,20221670,14972181,52930749,79273252,86135292,25433088,22625249,70539658,79294981,83852121,53902258,17245563,47075186,82263826,8178323,69977014,49853865,13680619,86857880,6435811,40880127,93895597,85994935,27680225,26376396,6574293,51054369,90817957,79440373,15117848,20759221,42167874,74756238,70517679,49425586,28591232,44949276,96839523,87954505,34638756,35665509,14167965,18918203,83837026,76978285,40206848,81446503,21454642,28654565,78454287,2172544,29583309,21288012,33943682,88800399,9636005,2508948,21378796,9219871,8046801,72288826,75139653,64307410,63345246,79848700,76256738,68565210,90121804,9135557,21759355,38605395,33546581,94655797,16892919,46408284,96084346,52455051,74315021,38201533,46393200,48983971,36309366,27050145,23378713,59615947,82488788,42927082,69931545,56227767,85498778,23577931,85049466,84537649,74797635,93397902,86283396,65472433,21133669,77200089,16634298,61971727,26090575,6662167,79326738,64264836,20461427,75788394,96649708,40184902,17194985,6771461,65071034,27685694,24563121,14753897,8306485,56444648,62252726,77988089,50886367,29318713,26362585,62913469,50019735,98598953,5011032,661403,11606716,2261771,43162329,70968007,72636475,9660172,36924425,99388873,34953119,51805698,67619218,54285295,8523534,29698286,59818128,56573166,20566251,35624253,55243871,79006039,76994980,80588072,17678433,35257054,51405934,91082559,95815579,51255544,77720104,53212947,19150834,52664020,61976758,23728772,85247001,34228580,19604429,36755336,4483370,523125,61217957,44436012,20177871,1333310,33807793,13073054,38099408,80011429,9495082,97085488,67473400,51890707,66254859,16760989,26606789,7263076,38788397,78158253,81892881,47785323,13243383,53567413,64095098,91903197,25955287,64428584,41104367,18648324,70719835,45748193,67565021,47560812,29796226,69863465,32124382,36354351,10693622,29110803,89507874,10367542,11277855,90482103,22807275,22632885,2986138,35887811,90837041,78519754,24820407,28204176,85841365,33962988,74999036,74058263,18713079,22228513,12088573,44725520,55042526,6155777,15060101,76419418,43872979,59880786,29381825,81000285,61630756,29362431,64010564,53579250,97518185,62277651,28792860,3197424,89488635,71309111,82353832,64039290,28358095,62535787,71009557,48927341,47677809,31574136,45053268,53090029,29777545,81596258,69501614,41848829,21995259,1519409,93008505,13069356,37510083,10360030,53464909,85481244,37033697,3960506,72589133,72585933,14324938,1210156,22354459,412880,31169538,87629171,25937350,30023146,51287183,97085855,14593215,65055567,69410969,47850933,68385296,17337231,33777814,74469218,78531963,35213674,16199696,60139804,12626047,87279323,96179733,55459416,46829040,52698775,44679075,33333272,65854856,75573907,4907143,50170690,33358099,21276530,79040864,39549108,73544865,77323463,30347608,4513539,28286704,42514954,6064835,20682476,35350421,15680547,24370282,14588311,91128610,26208542,66886749,51293436,37770888,51215167,99102534,13006287,91313059,2040058,29956076,63937391,43519380,87894365,97132907,43027372,93417714,65025032,62301067,91710841,25045292,26924493,77726650,82505725,25028595,76552303,9484401,85136859,53493351,69357631,52597261,244889,95679604,12322493,10686859,76680768,13208198,95386481,69347926,53871393,53909430,64366099,96926444,52849254,58762984,73946075,62995012,88590992,25104292,33567900,52172474,39675258,64589618,60098515,61341100,54657792,15513316,720425,49168183,3134067,9186012,64509705,31332964,93006345,50594347,68912137,17117335,98694346,21949231,70866340,23907838,19848902,13288976,46898675,50071324,18495563,26252313,86694456,1803711,49813263,96285051,53823783,60719524,58199515,51178552,13929630,92551815,39317262,53619798,74286413,99032403,30949278,53899700,95007107,87532694,64941650,77950451,73634773,14360728,55729264,57076412,29994525,48003940,79166884,339688,84382694,66527867,40573971,55996682,47126253,9406752,3410006,26454743,2452557,58036965,4527121,25017527,41391560,79086309,46370278,35285324,26185193,91497912,75365406,56245968,66570437,77321637,33723508,55100689,13246485,70715799,92190732,8818605,47554148,11213138,36510485,99016619,11178851,24641560,34098164,73839330,50847300,62069471,4089139,69454845,29277464,56902678,64372808,87814067,86700209,26561937,56169419,84998048,75578963,91535723,49399558,83476358,86287344,76021815,59904093,57570726,26580582,73830042,71167035,63902746,13374932,39332048,37588708,59681031,97954224,69874710,2345377,59064532,77160560,70762536,33076942,96299735,93514980,58043668,28670956,14281130,47281025,62221986,20508794,81607104,30159606,78481668,17606204,91594360,77993650,90201452,86362387,35818440,78624658,8954819,45430803,51227733,66038917,89529300,34196729,3661167,30681533,20298535,21732657,86718933,87126296,18901234,89162316,70777859,55532257,96744061,98783615,30896564,46831221,41749417,49753814,22784800,5098161,74081955,45734824,76858439,8941554,14481629,2588858,53278231,22420343,6551465,75501233,48332858,86955359,9209998,49128479,99139457,58531389,64520082,57578285,55534766,32235045,42723202,84396600,42608091,47469091,52947271,43543489,69244325,54183944,62046710,39376186,34844505,80225125,97206230,70731875,87740220,48489343,94917696,50700115,84710666,33111919,29064875,41258259,27670989,2202358,52981935,99754225,61434783,69328272,51615644,98046124,17131930,53361730,60164580]
second = [29118956,23548543,52369884,84042903,41241110,82985239,75052347,25825704,97283390,74428103,88184303,56502382,70920399,57660523,12213054,82229697,75410065,85779749,30266720,30802533,50551608,85663447,35576554,73523999,91210248,50596251,24568350,98146445,38189122,59255036,20118030,19784049,92450863,36554667,98744055,78136594,51428755,23295087,18790265,57854061,31182436,15633290,3868497,68892251,7817054,96098381,77325687,27722880,86241729,62386855,85268306,46207496,51510799,92690468,26578609,80051443,36582560,37607859,13756858,40348930,2846065,44740306,92184189,18706797,32591747,9205696,45937713,66611346,50324447,93504994,54738429,29526430,1237936,392399,35900599,31511066,28912334,89755258,95853857,90186368,3448627,77972741,46054094,44040347,49513165,62927323,21566721,87073884,82112540,45288857,99612141,73797826,52182269,3928731,59111899,58066501,14047426,14980919,60250480,40077755,38214435,71901272,90605948,64057330,41873897,39463238,39223560,34114497,407178,35211452,37093489,92391341,25128749,82558294,21456342,75524067,86913243,47887437,34167798,23710890,13764035,92809782,32786677,51969621,98342328,4414362,63478258,51631667,21231013,65571977,81382475,8111612,6741695,89839785,80544633,73791193,64684258,10811041,89095196,28348395,7305956,64065045,75214375,42855935,14589694,46825040,14359580,17068312,9305092,82918545,95978804,478960,22794160,17046813,11067572,9608996,24032364,64707130,1370150,81026058,31672203,88956734,7150224,94335788,66696549,92551576,61348936,62284475,71930745,74128929,51740623,42687570,30250435,80356502,92319345,73008254,27511544,52809405,67850488,98289882,12332892,65085073,74326488,98129194,1532835,22862073,96152962,45438466,1187923,38246147,26072620,47724608,66272507,97438929,78413621,37677898,16618871,62497961,7553499,99706533,23567848,56148564,3003038,7943631,52120105,37007281,58782057,93007782,75203028,97870278,26643382,85096276,28988830,88230055,49062947,88046384,37513955,82503300,31430188,62740808,89329045,9607756,61664174,80742926,93517299,17764701,53699699,71988181,54862136,44582144,41873603,21544595,50866679,80157415,93230087,49928613,21799760,73950675,7715229,11864954,78928564,53353427,89451783,6520532,63915306,45210185,60299968,63371917,19545557,67611073,39468277,12574061,82875861,58891666,501702,43034910,80060305,91793906,50413422,33560891,44022207,50393220,93347531,60611346,41624437,76257783,86895755,39087861,98403152,32045597,15731611,37046003,26050007,51880256,62369477,43279747,32700074,46933940,91766249,33964152,25357226,48205541,86444351,4951390,72983497,48550916,8207827,94129639,59560432,62548065,42732529,83431031,22702827,49345881,45372550,11172597,19393382,74356234,59505975,55947728,94074009,68971700,30806800,28297581,62102394,60496725,79347647,82896292,50351895,56259632,39177053,59115318,80568432,38361756,88859345,22780431,56127331,83445330,43548787,49184023,83935406,88764968,45557799,76136394,6822160,55587622,73688092,29686354,12015055,71088714,81662850,52817459,37785550,2047341,31804505,63736077,35207306,6189997,30416501,59395702,68002394,54006100,89956283,95061261,24955537,53507600,52371418,73040881,48849357,69317879,71072548,42323754,19754292,7141786,46177561,83638345,85363125,24712941,76226766,42215813,77423988,78013212,48404823,15346388,98799794,33330397,81482762,13781922,20901355,65258077,21209291,16248877,63616209,56108581,43932145,1132193,65493426,30282749,88028986,75208517,66883839,65564921,43185679,45022488,73286448,49108884,36914557,86756257,51164574,12053599,25191101,6837884,63290183,5016291,84616218,44765043,38421578,61604989,76789641,11200806,2142696,20122545,5462024,68498116,47153378,31757264,73722717,84839524,19423210,42503959,69156465,7697281,52195291,95919773,66254414,14302911,27157592,65574886,95115095,67580363,63330590,15445327,50595044,41169931,28424287,9190385,60660281,48431996,93003462,53911760,50632682,54676444,18492832,82543093,75586289,90766455,70188413,10482531,34402869,20500934,28590489,97152251,88564720,39403885,12750896,93276458,9085098,38587087,16607799,1020637,5256571,78579337,89072225,8490329,13662429,47657674,44840672,5638212,34806859,27108484,99228909,50135009,34827886,97073879,63519632,6556302,24665290,29167096,30760320,60065361,96131608,31429427,8059149,68995276,92873942,70657301,14869077,28493382,37080076,61040788,30144867,69127747,43317306,29859540,23569054,95996227,19085151,32855765,73686022,22047555,69428757,37184449,15763238,71684661,36922906,41532910,87820018,10261605,81375830,88246334,41984571,56857239,10529082,74254065,25746532,87115826,70360548,16865480,30244943,20801697,45822877,34697078,6317371,84502845,94050950,51069357,57280090,67775984,89335555,48120039,91202416,76506588,90418823,25576933,29410403,66271537,68767530,27289629,69550767,37907495,28146808,3023060,36543449,74463757,52644507,18412691,41163914,68723854,93639768,57884688,16610556,30117596,31082089,39908623,58880672,86984415,30185285,80157826,76542507,6195597,30379224,91639537,44167800,75833436,70170328,84649780,1482023,34116844,24309455,75787684,51989711,85912830,38144729,51414696,83360418,43430247,70195577,84218611,57855209,11042460,59019509,15309562,9073097,40669391,12875132,73549419,62071690,83250573,50882077,78372926,51369936,20258052,66147908,27827032,66393745,28081860,30881994,53349316,70655682,31870044,25826016,26719566,81436619,79020450,69233220,65121245,94517880,84084709,82183203,16936458,69792248,48449797,77153254,25052447,91060539,78182378,27368214,24366889,75251752,70883777,98367890,13595632,53842317,33640865,63331104,51999694,82220918,40742060,17917531,36615870,9328493,58073933,89763251,40023308,45357353,8919956,20267415,23453650,21653872,72660833,22576414,37175447,63534079,70904228,32937666,12172198,35415266,60516658,10853615,32273212,3063113,6399485,83046546,64874201,56331214,13622163,65653743,92334731,4403270,67669617,31599109,661450,99912030,29479038,86274056,96084804,39503524,62256843,59062183,4898026,91895364,44843725,13212945,7940207,41557766,5755684,94890809,87847917,80757976,12973085,35686145,84126539,58116476,68866721,63106757,73229212,53998655,81673148,7072132,32593870,96117633,39434498,22403756,26597450,25493861,60389311,13064716,50088611,68054764,38397414,80953806,271178,18411337,74290097,58971159,93434427,88552622,79088052,14659369,43354620,94292774,77833372,8588894,35820633,43202029,93234454,43768607,703512,34420655,64260191,10586113,6976733,24056215,66259901,61927310,40812477,16577580,12314636,90690347,3468045,31465028,14641972,33807989,75510628,20562978,67536036,19133976,88847790,48552066,61907902,16974943,80373698,9375932,19758603,24515944,99591037,53605186,85677829,17647484,84386937,37417455,73923748,83855610,80161641,1867049,77765296,57335899,80425114,3554764,11753331,80873004,25418226,76912432,29850403,9041825,84721992,35058115,44465534,62450215,16492309,3120781,30107762,22863808,27058394,10667884,34719903,87093454,18660079,72165016,46914115,57398857,16341438,82237692,23165211,6270171,86684189,80466030,7402167,20030573,73492519,99016984,89554376,47381028,5417094,78929598,68960596,8130091,40085606,86479546,12198023,74776250,59622346,73302200,40352067,14177722,35514702,85767056,71681200,13795077,16315929,64519880,6782519,93646320,17525124,22965300,81539636,3362920,55837785,2672173,26382663,95548438,82175575,14501878,23537107,6076910,35179488,2759857,58810078,96992062,24242341,33070374,98854653,88140066,44396688,1037244,54629384,84733448,64410632,87394203,99714122,20844769,66832653,40288036,29596328,85174335,63256051,768308,92173226,26924565,55078612,13695223,43070788,98326806,5700787,280055,2581576,10256154,94062075,61553580,31567153,49453619,58969453,83859903,90752611,59132798,63671499,33316759,37030192,77095995,32464205,94082776,83879121,63851619,33643095,41401291,76168314,62480360,31361039,88312831,81129692,42472285,83870942,44208607,95991415,80080088,57219322,31678648,65575250,93925042,59133258,36005143,59673709,48080582,44710418,63992663,31284976,26943006,86889238,333409,23742292,93506341,52698332,62966912,90944955,98961504,68344135,45813908,77767036,80593524,58135905,52026678,88048165,76538567,48484476,26463552,41373360,82376408,27529459,99934325,56304439,39919077,30301123,36145958,73573778,76813595,52974303,84504010,59701464,82909276,91759274,91442604,2562216,53412691,68943774,83900458,98384292,64381536,60357249,6893958,36475305,50713948,43828213,64884630,26150326,49858897,95186330,85485436,88605819,22646565,50141500,46789730,78610962,58667634,53573459,5891871,36834501,78386782,90722248,22836654,60791909,40370703,84545877,14376018,53340216,71711418,22236454,2867287,36844790,16317267,51834489,61953201,57305699,1105772,78458179,19427440,75622149,46686334,43755949,16059025,85890422,81687475,86909880,40307217,75503643,96864354,43064147,34344613,49255947,89402759,87065276,6729942,67591549,73659628,509535,10863184,62889744,30266223,30894891,78097300,99236148,78271095,8260688,9414774,94443038,85525509,64156413,19966713,65596892,87695149,92489332]      
solu = Solution()
print(solu.longestCommonPrefix(first, second))
