from socket import MSG_ERRQUEUE
from ppadb.client import Client as AdbClient
import time
# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = client.device("9b2ad4a67cf5")
l = ['+917633965554', '+917857913775', '+916372710610', '+919668581157', '+917978095194', '+917008054194', '+919832767172', '+919439922695', '+919937095804', '+916370106634', '+918101583670', '+919475692263', '+917654723818', '+917873199271', '+918260553201', '+916370910655', '+918480942125', '+919937757600', '+917846811737', '+919849728541', '+919348748476', '+918009909227', '+919334704730', '+916371461816', '+919827616883', '+917978702229', '+917856937855', '+918280192630', '+919319233575', '+917488024423', '+919556352783', '+919905190117', '+919117713730', '+918658868846', '+919833107226', '+918249369985', '+918144500826', '+919348309664', '+918018835259', '+919439939927', '+916370736852', '+917205574086', '+918249359823', '+917723896752', '+919827082001', '+918102745117', '+918249222076', '+916370400521', '+917873207115', '+919178664444', '+919692287887', '+919337164351', '+916372675751', '+918114977028', '+917978663108', 
'+917979001717', '+917978265588', '+917001776853', '+916371850876', '+917008833724', '+917209825889', '+919040950756', '+916204093813', '+919113761531', '+916370102221', '+918768932443', '+918144430527', '+918018110905', '+916206985871', '+917357705503', '+916204677277', '+917978750144', '+918763323161', '+919820073015', '+918658274828', '+916370726445', '+917903828662', '+919938095804', '+917077587513', '+917894080263', '+919439423367', '+917008189975', '+918260675585', '+918456971739', '+916203034490', '+919096608234', '+917479844459', '+919776555820', '+917978479391', '+918260333427', '+916207075872', '+918271917157', '+918114733653', '+916296865597', '+916201328231', '+917894419859', '+917977157721', '+917003214833', '+918260557169', '+919491047168', '+917735296566', '+917008297605', '+918118071603', '+917846918789', '+918260742373', '+919330416962', '+917873700103', '+918658000185', '+919437584964', '+919348167920', '+917848946600', '+916200213521', '+919337736490', '+917684919783', '+919124005707', '+916371792098', '+919348639018', '+917008190943', '+917978095194', '+918456990218', '+917004358296', '+919861707903', '+919406298457', '+919938445295', '+919771139430', '+916204402519', '+919937977258', '+918210121421', '+918249937597', '+918210875970', '+918840397507', '+918984463695', '+919078445800', '+917004925157', '+919365457610', '+917327833606', '+918260010263', '+916370662019', '+917033369235', '+919438625192', '+919608271300', '+917008494644', '+919348338135', '+919534857947', '+917205261611', '+919437404401', '+919861254497', '+917846916267', '+919040492516', '+918260775874', '+918249955434', '+917857083208', '+916370153681', '+919937138502', '+918448820239', '+917848886490', '+918260570225', '+917873207115', '+917250401416', '+919438634534', '+919938481655', '+916372654636', '+917205450915', '+919078776736', '+919348198311', '+916372961626', '+917205968655', '+919142998113', '+918658112251', '+917008189959', '+919304547289', '+917978830898', 
'+919337003147', '+918873497904', '+918260932278', '+917855819779', '+917205291407', '+918249079328', '+919338213386', '+918340165652', '+917327870868', '+918457907211', '+919348873304', '+917978094138', '+919382538007', '+917903750269', '+917655926717', '+917326921248', '+918249417550', '+917854828856', '+919304645988', '+919439503251', '+917759998588', '+919783451290', '+919438030030', '+918249220318', '+917205881321', '+917978262528', '+918249006524', '+918144933345', '+918763276952', '+917979974480', '+918599071065', '+918328952956', '+918340702948', '+917847088166', '+919835618082', '+919771041326', '+917751834802', '+918292782800', '+917978399767', '+919583432233', '+918984936091', '+919142858058', '+918917577586', '+918117069202', '+918529737898', '+918294934356', '+918596097916', '+916299972365', '+919333638554', '+919556592892', '+919832501873', '+918144784701', '+916203343457', '+918249824767', '+918076886229', '+918114306351', '+919113381072', '+919431312789', '+919556829010', '+919090925090', '+919570215125', '+919525800780', '+919006959994', '+917978163454', '+917327068167', '+917657076205', '+918093737253', '+916372969123', '+919798044375', '+917735683302', '+917205783051', '+919658526319', '+919692401166', '+918617455218', '+918100346352', '+919777484187', '+916371639599', '+919771652530', '+917846994971', '+919693643413', '+918260018701', '+919439498100', '+919178822844', '+919861526955', '+917908111565', '+916287832792', '+918169770640', '+918235939539', '+919142015648', '+917008003734', '+919470983868', '+918249598400', '+919801180742', '+918340375704', '+917008398843', '+917205782426', '+919852716284', '+916372064893', '+919861646700', '+917061983022', '+917749902726', '+919508081743', '+916201959248', '+917008080063', '+918144170465', '+917894579689', '+919142750165', '+917627017141', '+918249397297', '+916204377668', '+917979772280', '+919777547585', '+918917352698', '+919777257759', '+917008223103', '+919437334283', '+919337284062', 
'+917004821983', '+919938628422', '+917377964173', '+918984759382', '+917978647008', '+916370590858', '+919348801114', '+917008011232', '+917978195500', '+918789599216', '+918987838854', '+918521900395', '+918260926707', '+917004814123', '+919508849311', '+919166916219', '+917667220314', '+919337722959', '+919439791134', '+919149567259', '+918864084387', '+919348093747', '+919304816134', '+918252196772', '+918114952962', '+917735897151', '+918114657726', '+919337693600', '+916370045860', '+917894746355', '+919348161030', '+917735206791', '+918895200706', '+918144969954', '+919432168906', '+919439155076', '+918451082228', '+916370887350', '+917735474429', '+919556093994', '+919437915725', '+918260499958', '+918002361904', '+917764836684', '+917606076643', '+917063832214', '+919337451296', '+918260630250', '+919337788308', '+916295919288', '+919078880078', '+917033553993', '+917008209254', '+917978856756', '+916371132875', '+917008308971', '+918984050933', '+916371388939', '+917605902777', '+919692649430', '+917847021427', '+919861430910', '+917008169924', '+918249017822', '+919938817936', '+917978961020', '+917846876031', '+917077415735', '+918249595166', '+919938761940', '+916006547567', '+919937984071', '+917295901186', '+917008756015', '+918984714116', '+919178030456', '+918653088750', '+916371846795', '+918917544852', '+919583627504', '+918763357190', '+919827418767', '+917978975343', '+917991005515']
l = ["+919348309664","+919937391708","+917857913775","+917001776853","+919332631181"]
#l = ["+919348309664"]

b = "am start -a android.intent.action.VIEW -d "

f = open("msg.txt","r")
msg = f.readlines()
f.close()

print(msg)

#device.shell(b + "https://wa.me/" + "+919937391708")

#time.sleep(2)
"""
for i in msg:
        device.shell("input text " + '"'+i+'"')
"""






for i in l:
    device.shell(b + "https://wa.me/" + i)
    time.sleep(2)
    #device.shell("input text " + "Hello")
    """
    for i in msg:
        device.shell("input text " + '"'+i+'"')
    """
    device.shell("input keyevent 279")
    device.shell("input keyevent 66")
    #device.shell("input swipe 100 500 100 500 250")
    #device.shell(f'input tap {search_bar}')

"""
    for i in k:
        device.shell("input text " + '"'+i+'"')
        if i == '':
            continue
        device.shell("input keyevent 66")
        """
    #device.shell("input text " + msg)
    #device.shell("input text "+msg)
    #device.shell("input keyevent 66")


#pks = device.list_packages()

#print(apks)