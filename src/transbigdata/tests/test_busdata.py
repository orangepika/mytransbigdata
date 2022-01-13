
import transbigdata as tbd
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon


class TestBikedata:
    def setup_method(self):
        self.data = pd.DataFrame([['沪D-R7103', '2019-01-16 23:59:59', 121.3308582912764,
                                  31.175129076427655],
                                 ['沪D-R7103', '2019-01-17 12:40:20', 121.33049311941906,
                                  31.175065802450753],
                                 ['沪D-R7103', '2019-01-17 13:05:32', 121.33049311941906,
                                  31.175065802450753],
                                 ['沪D-R7103', '2019-01-17 13:05:52', 121.33036738445367,
                                  31.175279932303557],
                                 ['沪D-R7103', '2019-01-17 13:06:07', 121.32967297800323,
                                  31.17497940724048],
                                 ['沪D-R7103', '2019-01-17 13:06:22', 121.33008305045536,
                                  31.174995618170627],
                                 ['沪D-R7103', '2019-01-17 13:06:42', 121.33029256851628,
                                  31.17510216522793],
                                 ['沪D-R7103', '2019-01-17 16:24:05', 121.33029256851628,
                                  31.17510216522793],
                                 ['沪D-R7103', '2019-01-17 16:24:30', 121.33093714049436,
                                  31.174819084849073],
                                 ['沪D-R7103', '2019-01-17 16:25:00', 121.33119656323854,
                                  31.174744630573823],
                                 ['沪D-R7103', '2019-01-17 16:25:35', 121.3313133039642,
                                  31.17470742816974],
                                 ['沪D-R7103', '2019-01-17 16:34:29', 121.3313133039642,
                                  31.17470742816974],
                                 ['沪D-R7103', '2019-01-17 16:34:54', 121.33121258219445,
                                  31.17410692572959],
                                 ['沪D-R7103', '2019-01-17 16:35:20', 121.32927503207796,
                                  31.173189080128747],
                                 ['沪D-R7103', '2019-01-17 16:35:45', 121.32774259804339,
                                  31.17211555668083],
                                 ['沪D-R7103', '2019-01-17 16:36:05', 121.32828742144076,
                                  31.171421870458047],
                                 ['沪D-R7103', '2019-01-17 16:36:35', 121.32889308056538,
                                  31.171053902452424],
                                 ['沪D-R7103', '2019-01-17 16:37:00', 121.33147515535293,
                                  31.172212396845183],
                                 ['沪D-R7103', '2019-01-17 16:37:25', 121.33256465354401,
                                  31.17289898466245],
                                 ['沪D-R7103', '2019-01-17 16:38:35', 121.33256465354401,
                                  31.17289898466245],
                                 ['沪D-R7103', '2019-01-17 16:39:01', 121.33345761253085,
                                  31.17344502270766],
                                 ['沪D-R7103', '2019-01-17 16:39:21', 121.33442839412734,
                                  31.17413784648959],
                                 ['沪D-R7103', '2019-01-17 16:39:46', 121.33490830097844,
                                  31.17448277252849],
                                 ['沪D-R7103', '2019-01-17 16:40:12', 121.33624028223001,
                                  31.175424811168998],
                                 ['沪D-R7103', '2019-01-17 16:40:42', 121.33855210267679,
                                  31.176992750548038],
                                 ['沪D-R7103', '2019-01-17 16:41:07', 121.33912682562804,
                                  31.177395495654412],
                                 ['沪D-R7103', '2019-01-17 16:41:12', 121.33912682562804,
                                  31.177395495654412],
                                 ['沪D-R7103', '2019-01-17 16:41:32', 121.33984722140025,
                                  31.178022866403307],
                                 ['沪D-R7103', '2019-01-17 16:41:57', 121.34230283289175,
                                  31.17997546117461],
                                 ['沪D-R7103', '2019-01-17 16:42:17', 121.34406503104313,
                                  31.18139063132967],
                                 ['沪D-R7103', '2019-01-17 16:42:37', 121.34565267426674,
                                  31.182475320933605],
                                 ['沪D-R7103', '2019-01-17 16:43:03', 121.34695897571785,
                                  31.183092769036772],
                                 ['沪D-R7103', '2019-01-17 16:44:13', 121.34695897571785,
                                  31.183092769036772],
                                 ['沪D-R7103', '2019-01-17 16:44:38', 121.34771044680997,
                                  31.183373352784702],
                                 ['沪D-R7103', '2019-01-17 16:44:58', 121.34986914233515,
                                  31.18401142963308],
                                 ['沪D-R7103', '2019-01-17 16:45:24', 121.35271164978475,
                                  31.184866403422394],
                                 ['沪D-R7103', '2019-01-17 16:45:44', 121.35296916183509,
                                  31.18495395177752],
                                 ['沪D-R7103', '2019-01-17 16:46:50', 121.35296916183509,
                                  31.18495395177752],
                                 ['沪D-R7103', '2019-01-17 16:47:10', 121.35310590274719,
                                  31.185008708410415],
                                 ['沪D-R7103', '2019-01-17 16:47:35', 121.35506825574805,
                                  31.185636343326177],
                                 ['沪D-R7103', '2019-01-17 16:47:55', 121.35622514959864,
                                  31.186098356723118],
                                 ['沪D-R7103', '2019-01-17 16:48:16', 121.35660148846878,
                                  31.1860708068457],
                                 ['沪D-R7103', '2019-01-17 16:48:46', 121.3605496684798,
                                  31.18750939452662],
                                 ['沪D-R7103', '2019-01-17 16:49:06', 121.36308454783347,
                                  31.188574433939618],
                                 ['沪D-R7103', '2019-01-17 16:49:27', 121.36374253432413,
                                  31.18862454957953],
                                 ['沪D-R7103', '2019-01-17 16:49:47', 121.36475999015713,
                                  31.188787165079752],
                                 ['沪D-R7103', '2019-01-17 16:50:12', 121.36528119368472,
                                  31.189100353278842],
                                 ['沪D-R7103', '2019-01-17 16:50:32', 121.36799531701536,
                                  31.189494880357508],
                                 ['沪D-R7103', '2019-01-17 16:51:03', 121.37051893150148,
                                  31.19027066127662],
                                 ['沪D-R7103', '2019-01-17 16:51:43', 121.37233468156712,
                                  31.190505638967373]], columns=['VehicleId', 'GPSDateTime', 'lon', 'lat'])
        self.line = gpd.read_file('{"type": "FeatureCollection", "features": [{"id": "0", "type": "Feature", "properties": {"Id": 0, "name": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)"}, "geometry": {"type": "LineString", "coordinates": [[121.48680833406775, 31.23479712221373, 0.0], [121.48654212047136, 31.234694676029786, 0.0], [121.48640321578763, 31.2344335165597, 0.0], [121.48620424418269, 31.234332091432126, 0.0], [121.48570963449876, 31.23407338399259, 0.0], [121.48520746843946, 31.233845822266794, 0.0], [121.48473939391056, 31.23371324838625, 0.0], [121.48435071992188, 31.233602809110284, 0.0], [121.48382747488549, 31.233252131305267, 0.0], [121.48358667235713, 31.23313436404436, 0.0], [121.4830110244368, 31.233081954943895, 0.0], [121.48159212474732, 31.233197283736708, 0.0], [121.48081840120713, 31.233175997627082, 0.0], [121.48046555948812, 31.233141592052398, 0.0], [121.4792684569557, 31.23294431959499, 0.0], [121.47728773381367, 31.23219022228969, 0.0], [121.47650938696911, 31.23182638081955, 0.0], [121.47615549794644, 31.231646740130707, 0.0], [121.47467923815317, 31.230790112644126, 0.0], [121.47396374247927, 31.23041805989505, 0.0], [121.4723546525761, 31.22946394254198, 0.0], [121.4718447208883, 31.22916120530873, 0.0], [121.47162507708418, 31.229063043002803, 0.0], [121.46971148882133, 31.228210311091555, 0.0], [121.46934522194101, 31.22804592028437, 0.0], [121.46895218140925, 31.22786892438538, 0.0], [121.46659610091696, 31.226897254621516, 0.0], [121.4649631794914, 31.226282609517412, 0.0], [121.46414113119387, 31.226039232240876, 0.0], [121.46346858001557, 31.225907738094904, 0.0], [121.4632085414404, 31.22585738171055, 0.0], [121.46201595667192, 31.22581602366564, 0.0], [121.46012337207506, 31.22589498094655, 0.0], [121.45964966243406, 31.225915179689988, 0.0], [121.45916931421996, 31.225933771603817, 0.0], [121.4584299334602, 31.225930994026747, 0.0], [121.45670394588448, 31.225917687177848, 0.0], [121.4562159201628, 31.225940340782877, 0.0], [121.45501414547563, 31.225896830409198, 0.0], [121.45313994909115, 31.225877546623256, 0.0], [121.45198747372488, 31.22586577680014, 0.0], [121.45067409831796, 31.225764124081973, 0.0], [121.45013850323112, 31.225696215249084, 0.0], [121.44963708616434, 31.22557417609614, 0.0], [121.44901469032412, 31.225393738760786, 0.0], [121.44838360085095, 31.22514849979612, 0.0], [121.44733265578334, 31.224768283214516, 0.0], [121.44611255033824, 31.22427423667348, 0.0], [121.44522256893964, 31.22391460749898, 0.0], [121.44452308747704, 31.22366370977997, 0.0], [121.44330864322482, 31.223290418495207, 0.0], [121.44112481042458, 31.22284394379711, 0.0], [121.43995086003079, 31.22265595116455, 0.0], [121.43965682754218, 31.22253773889234, 0.0], [121.43945583227031, 31.22246385732158, 0.0], [121.4377312910728, 31.22154875294891, 0.0], [121.43731636796971, 31.221405388725636, 0.0], [121.43603949285581, 31.221201287427256, 0.0], [121.43544581995262, 31.221071991941535, 0.0], [121.4348990684986, 31.22088608524194, 0.0], [121.43467425490213, 31.22071853108778, 0.0], [121.43383491280504, 31.219963604435318, 0.0], [121.43326810046672, 31.21956834228496, 0.0], [121.43271638663167, 31.21918489418819, 0.0], [121.4316242046651, 31.218552154482637, 0.0], [121.4308966230824, 31.21807088028686, 0.0], [121.42957690517412, 31.216984930602006, 0.0], [121.4287944923989, 31.2164177309201, 0.0], [121.42754314953099, 31.21585282823901, 0.0], [121.42734229008948, 31.21574291740339, 0.0], [121.42697681035582, 31.21554354789749, 0.0], [121.4262466534029, 31.214981151520842, 0.0], [121.42558822887514, 31.214198238106412, 0.0], [121.42498521028006, 31.213265073587262, 0.0], [121.42483922435368, 31.21309406726119, 0.0], [121.42458790302874, 31.212812951144944, 0.0], [121.42418302050427, 31.21257030804461, 0.0], [121.42380162839086, 31.212413702711984, 0.0], [121.42260278406569, 31.212177678103608, 0.0], [121.42175472319029, 31.21201013082237, 0.0], [121.41921253702968, 31.211508499065935, 0.0], [121.4187520573609, 31.21141803206741, 0.0], [121.4177502886381, 31.211121267547774, 0.0], [121.41536255685529, 31.210488005340114, 0.0], [121.41055823761425, 31.209352239123884, 0.0], [121.41006286819932, 31.209240779911678, 0.0], [121.408752749836, 31.208764570795754, 0.0], [121.40792185625311, 31.208235633945765, 0.0], [121.40689238792147, 31.207375895820764, 0.0], [121.40644113863621, 31.207040030048116, 0.0], [121.40335924078863, 31.204750029737966, 0.0], [121.4031127555595, 31.20460193270769, 0.0], [121.40268724211523, 31.20434458544406, 0.0], [121.40242295664385, 31.204185568754575, 0.0], [121.40191716595808, 31.203915584462763, 0.0], [121.40060518142528, 31.20337304738282, 0.0], [121.39968316268123, 31.20311153188489, 0.0], [121.39933123295673, 31.203012464510756, 0.0], [121.39873589558302, 31.202852168932246, 0.0], [121.39577650199107, 31.20205852958135, 0.0], [121.39509665023105, 31.201877658368137, 0.0], [121.39441015274966, 31.201649190619534, 0.0], [121.3940099837958, 31.201595740961917, 0.0], [121.3937718338187, 31.201482267093606, 0.0], [121.39298554970689, 31.200972737710618, 0.0], [121.3921855673392, 31.200597019045237, 0.0], [121.39026247388, 31.199540859206092, 0.0], [121.38996352795702, 31.199361005226017, 0.0], [121.38973187287756, 31.19922188072922, 0.0], [121.3882033554104, 31.198303687682014, 0.0], [121.3873974991391, 31.19781975360552, 0.0], [121.3868071526136, 31.197468809667487, 0.0], [121.38530162233323, 31.19657311156674, 0.0], [121.38431896985206, 31.195989530430772, 0.0], [121.38370690194671, 31.195624736822428, 0.0], [121.38335723534193, 31.195416964809528, 0.0], [121.38282183665989, 31.195098846977537, 0.0], [121.38238950410006, 31.194841400301573, 0.0], [121.38116048667693, 31.194107916831754, 0.0], [121.37956513571578, 31.19315746376731, 0.0], [121.37895990223895, 31.19287560196964, 0.0], [121.3772327786018, 31.192109490422816, 0.0], [121.37638770701506, 31.19173548103986, 0.0], [121.37596314767956, 31.191593924088796, 0.0], [121.37533303364798, 31.19138224863976, 0.0], [121.37441403604866, 31.191075411329503, 0.0], [121.37390440707601, 31.19090497257139, 0.0], [121.37350823172538, 31.190772731116017, 0.0], [121.37289122488428, 31.19056616016392, 0.0], [121.37263384980437, 31.19048039724518, 0.0], [121.37177233442036, 31.190207377985715, 0.0], [121.37015676569357, 31.189696531392993, 0.0], [121.36866289419575, 31.189225060507134, 0.0], [121.36805301851211, 31.18903196337387, 0.0], [121.36741267528593, 31.18882949729654, 0.0], [121.36713568710604, 31.18874130190273, 0.0], [121.36545918023688, 31.188211731534693, 0.0], [121.36427592822677, 31.187837451059956, 0.0], [121.36348112963613, 31.187594245160383, 0.0], [121.35960127617719, 31.186410680311965, 0.0], [121.35810148825273, 31.185993102692862, 0.0], [121.35784282994241, 31.18592152968835, 0.0], [121.35756087542264, 31.18581898477854, 0.0], [121.35565082386277, 31.185124726907542, 0.0], [121.35530640152558, 31.1849626468292, 0.0], [121.35428047015459, 31.184510732410818, 0.0], [121.35317311540628, 31.1840935443074, 0.0], [121.3527491330305, 31.183934015897815, 0.0], [121.35172236895487, 31.18362994201332, 0.0], [121.35142551117141, 31.183542155343932, 0.0], [121.34892765280848, 31.182803307385363, 0.0], [121.3484304605845, 31.182656931034103, 0.0], [121.34803300048519, 31.182538890449415, 0.0], [121.34749112698373, 31.182378726523886, 0.0], [121.34687421145703, 31.182194224406967, 0.0], [121.34614413837573, 31.181922018971626, 0.0], [121.34534688607388, 31.181573091491334, 0.0], [121.34494250164147, 31.181346816658316, 0.0], [121.34415808853373, 31.18090773418931, 0.0], [121.34366146976991, 31.180529650875503, 0.0], [121.34296025184004, 31.17999571895842, 0.0], [121.34219840514724, 31.179416525263225, 0.0], [121.34192201654791, 31.179206100416227, 0.0], [121.34143955204493, 31.17883883921868, 0.0], [121.33937970212246, 31.177271930382528, 0.0], [121.3390253936204, 31.176999658284107, 0.0], [121.33873935903235, 31.17678044295161, 0.0], [121.33831308857619, 31.17648439328463, 0.0], [121.33753628037235, 31.17594366146003, 0.0], [121.33604789800422, 31.17497203682833, 0.0], [121.33495675278324, 31.174259650219373, 0.0], [121.33462195194231, 31.174037199940333, 0.0], [121.33270025695657, 31.172760813025707, 0.0], [121.33118423301782, 31.171754317896283, 0.0], [121.32987961299621, 31.171128931445935, 0.0], [121.32936757297823, 31.170915817469155, 0.0], [121.32871072365552, 31.170641854595385, 0.0], [121.32808295962585, 31.170381012393694, 0.0], [121.32694229666748, 31.171535181527215, 0.0], [121.32949486297333, 31.1727777609417, 0.0]]}}]}')
        self.stop = gpd.read_file('{"type": "FeatureCollection", "features": [{"id": "0", "type": "Feature", "properties": {"lat": 31.232760281, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.483251722, "stopname": "\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9"}, "geometry": {"type": "Point", "coordinates": [121.48688469316784, 31.23484102475723]}}, {"id": "1", "type": "Feature", "properties": {"lat": 31.228843235, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.471204173, "stopname": "\\u897f\\u85cf\\u4e2d\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.47468505225578, 31.230783624070586]}}, {"id": "2", "type": "Feature", "properties": {"lat": 31.2262890815, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.46620721, "stopname": "\\u9ec4\\u9642\\u5317\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.46970615320824, 31.22822013538774]}}, {"id": "3", "type": "Feature", "properties": {"lat": 31.2241692712, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.460679191, "stopname": "\\u6210\\u90fd\\u5317\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.46413649158545, 31.226052872297608]}}, {"id": "4", "type": "Feature", "properties": {"lat": 31.2242450755, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.453549153, "stopname": "\\u8302\\u540d\\u5317\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.45670741736707, 31.225919681700777]}}, {"id": "5", "type": "Feature", "properties": {"lat": 31.2236712033, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.445507471, "stopname": "\\u4e0a\\u6d77\\u5c55\\u89c8\\u4e2d\\u5fc3"}, "geometry": {"type": "Point", "coordinates": [121.44838602968272, 31.2251447687407]}}, {"id": "6", "type": "Feature", "properties": {"lat": 31.2218815305, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.440473777, "stopname": "\\u5e38\\u5fb7\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.44330213951724, 31.22330447998906]}}, {"id": "7", "type": "Feature", "properties": {"lat": 31.221176291, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.436915266, "stopname": "\\u534e\\u5c71\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.4396592559502, 31.222534008422322]}}, {"id": "8", "type": "Feature", "properties": {"lat": 31.2182418106, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.430528141, "stopname": "\\u9547\\u5b81\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.43326636585115, 31.219570192858782]}}, {"id": "9", "type": "Feature", "properties": {"lat": 31.2141768618, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.424153694, "stopname": "\\u6c5f\\u82cf\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.4269853525943, 31.21553571707035]}}, {"id": "10", "type": "Feature", "properties": {"lat": 31.2116776284, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.421873542, "stopname": "\\u756a\\u79ba\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.42482985887163, 31.213102348709608]}}, {"id": "11", "type": "Feature", "properties": {"lat": 31.2098105223, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.414911763, "stopname": "\\u5b9a\\u897f\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.41774554724684, 31.21113323304618]}}, {"id": "12", "type": "Feature", "properties": {"lat": 31.208161334, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.40784817, "stopname": "\\u51ef\\u65cb\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.41053622161131, 31.209367641295568]}}, {"id": "13", "type": "Feature", "properties": {"lat": 31.2017646283, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.396563628, "stopname": "\\u5a04\\u5c71\\u5173\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.39934723279329, 31.202982794937725]}}, {"id": "14", "type": "Feature", "properties": {"lat": 31.1966784182, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.384656058, "stopname": "\\u6c34\\u57ce\\u5357\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.38739524533014, 31.197821587877485]}}, {"id": "15", "type": "Feature", "properties": {"lat": 31.1939698263, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.380070188, "stopname": "\\u8679\\u8bb8\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.38285770202909, 31.19512353567959]}}, {"id": "16", "type": "Feature", "properties": {"lat": 31.1917115341, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.376140027, "stopname": "\\u8679\\u6885\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.37896345371097, 31.192870959745306]}}, {"id": "17", "type": "Feature", "properties": {"lat": 31.189365838, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.369870201, "stopname": "\\u5251\\u6cb3\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.37264120880835, 31.1904682766765]}}, {"id": "18", "type": "Feature", "properties": {"lat": 31.1868269216, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.361545646, "stopname": "\\u8679\\u4e95\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.36419682256896, 31.18782342514133]}}, {"id": "19", "type": "Feature", "properties": {"lat": 31.1840846357, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.352767681, "stopname": "\\u5916\\u73af\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.35529817330725, 31.184972846336553]}}, {"id": "20", "type": "Feature", "properties": {"lat": 31.181572874, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.345073283, "stopname": "\\u822a\\u4e1c\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.347507406901, 31.182371829399024]}}, {"id": "21", "type": "Feature", "properties": {"lat": 31.1764410431, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.336834516, "stopname": "\\u822a\\u65b0\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.33937857556569, 31.177272847089057]}}, {"id": "22", "type": "Feature", "properties": {"lat": 31.1733903453, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.332337755, "stopname": "\\u5434\\u5b9d\\u8def"}, "geometry": {"type": "Point", "coordinates": [121.33496359737327, 31.174253204731254]}}, {"id": "23", "type": "Feature", "properties": {"lat": 31.1723921945, "linename": "71\\u8def(\\u5ef6\\u5b89\\u4e1c\\u8def\\u5916\\u6ee9-\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9)", "lon": 121.326950253, "stopname": "\\u7533\\u6606\\u8def\\u67a2\\u7ebd\\u7ad9"}, "geometry": {"type": "Point", "coordinates": [121.32944223863883, 31.17315254936537]}}]}')

    def test_busgps_arriveinfo(self):
        arriveinfo = tbd.busgps_arriveinfo(self.data, self.line, self.stop)
        assert len(arriveinfo) == 9
        assert len(tbd.busgps_arriveinfo(self.data, self.line, self.stop,method='dislimit'))==7
        onewaytime = tbd.busgps_onewaytime(arriveinfo,
                                           start='剑河路',
                                           end='航新路', col=['VehicleId', 'stopname','arrivetime','leavetime'])
        assert onewaytime['duration'].iloc[0] == 562.0
