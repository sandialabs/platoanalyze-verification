import verification_utils
import math

data = [[0, 0], \
[0.0100000000000000000, 0.0000308258157783895394], \
[0.0200000000000000000, 0.0000611078514165321084], \
[0.0300000000000000000, 0.0000908422643548797379], \
[0.0400000000000000000, 0.000120025242897582829], \
[0.0500000000000000000, 0.000148653007432439675], \
[0.0600000000000000000, 0.000176721811672216002], \
[0.0700000000000000000, 0.000204227943917252922], \
[0.0800000000000000000, 0.000231167728339254093], \
[0.0900000000000000000, 0.000257537526286118971], \
[0.100000000000000000, 0.000283333737607659067], \
[0.110000000000000000, 0.000308552802002004056], \
[0.120000000000000000, 0.000333191200382477906], \
[0.130000000000000000, 0.000357245456264686473], \
[0.140000000000000000, 0.000380712137173536483], \
[0.150000000000000000, 0.000403587856069859705], \
[0.160000000000000000, 0.000425869272796288215], \
[0.170000000000000000, 0.000447553095541994078], \
[0.180000000000000000, 0.000468636082325851896], \
[0.190000000000000000, 0.000489115042497578300], \
[0.200000000000000000, 0.000508986838256318100], \
[0.210000000000000000, 0.000528248386186145604], \
[0.220000000000000000, 0.000546896658807893279], \
[0.230000000000000000, 0.000564928686146662948], \
[0.240000000000000000, 0.000582341557314363279], \
[0.250000000000000000, 0.000599132422106546814], \
[0.260000000000000000, 0.000615298492612779686], \
[0.270000000000000000, 0.000630837044839743549], \
[0.280000000000000000, 0.000645745420346213435], \
[0.290000000000000000, 0.000660021027889001223], \
[0.300000000000000000, 0.000673661345078931236], \
[0.310000000000000000, 0.000686663920045832822], \
[0.320000000000000000, 0.000699026373111516454], \
[0.330000000000000000, 0.000710746398469641128], \
[0.340000000000000000, 0.000721821765871320667], \
[0.350000000000000000, 0.000732250322315285184], \
[0.360000000000000000, 0.000742029993741359336], \
[0.370000000000000000, 0.000751158786725967826], \
[0.380000000000000000, 0.000759634790178330670], \
[0.390000000000000000, 0.000767456177035972381], \
[0.400000000000000000, 0.000774621205958108284], \
[0.410000000000000000, 0.000781128223015445161], \
[0.420000000000000000, 0.000786975663374855786], \
[0.430000000000000000, 0.000792162052977390171], \
[0.440000000000000000, 0.000796686010208003505], \
[0.450000000000000000, 0.000800546247555343699], \
[0.460000000000000000, 0.000803741573259937744], \
[0.470000000000000000, 0.000806270892949038703], \
[0.480000000000000000, 0.000808133211256376700], \
[0.490000000000000000, 0.000809327633425012188], \
[0.500000000000000000, 0.000809853366891498871], \
[0.510000000000000000, 0.000809709722849461314], \
[0.520000000000000000, 0.000808896117790753417], \
[0.530000000000000000, 0.000807412075022267235], \
[0.540000000000000000, 0.000805257226156489347], \
[0.550000000000000000, 0.000802431312573856272], \
[0.560000000000000000, 0.000798934186854977947], \
[0.570000000000000000, 0.000794765814180754294], \
[0.580000000000000000, 0.000789926273698426159], \
[0.590000000000000000, 0.000784415759851598421], \
[0.600000000000000000, 0.000778234583672262475], \
[0.610000000000000000, 0.000771383174032889279], \
[0.620000000000000000, 0.000763862078856591097], \
[0.630000000000000000, 0.000755671966283477572], \
[0.640000000000000000, 0.000746813625791268015], \
[0.650000000000000000, 0.000737287969268272080], \
[0.660000000000000000, 0.000727096032036873147], \
[0.670000000000000000, 0.000716238973825722002], \
[0.680000000000000000, 0.000704718079688807213], \
[0.690000000000000000, 0.000692534760869690895], \
[0.700000000000000000, 0.000679690555609212439], \
[0.710000000000000000, 0.000666187129894987937], \
[0.720000000000000000, 0.000652026278151156616], \
[0.730000000000000000, 0.000637209923866829085], \
[0.740000000000000000, 0.000621740120161772426], \
[0.750000000000000000, 0.000605619050287968617], \
[0.760000000000000000, 0.000588849028065710576], \
[0.770000000000000000, 0.000571432498253027134], \
[0.780000000000000000, 0.000553372036847270352], \
[0.790000000000000000, 0.000534670351317803084], \
[0.800000000000000000, 0.000515330280768860460], \
[0.810000000000000000, 0.000495354796031635073], \
[0.820000000000000000, 0.000474746999684895910], \
[0.830000000000000000, 0.000453510126003405477], \
[0.840000000000000000, 0.000431647540833596938], \
[0.850000000000000000, 0.000409162741396042889], \
[0.860000000000000000, 0.000386059356014352775], \
[0.870000000000000000, 0.000362341143770279935], \
[0.880000000000000000, 0.000338011994084889099], \
[0.890000000000000000, 0.000313075926225780000], \
[0.900000000000000000, 0.000287537088740450354], \
[0.910000000000000000, 0.000261399758816056697], \
[0.920000000000000000, 0.000234668341565845429], \
[0.930000000000000000, 0.000207347369242751912], \
[0.940000000000000000, 0.000179441500380709759], \
[0.950000000000000000, 0.000150955518864337272], \
[0.960000000000000000, 0.000121894332927815520], \
[0.970000000000000000, 0.0000922629740838462088], \
[0.980000000000000000, 0.0000620665959837093766], \
[0.990000000000000000, 0.0000313104732095324280], \
[1.00000000000000000, 0]]

def displacement(x):

  pointIndex = -1
  numData = len(data)-1
  for iPt in range(numData):
    if data[iPt][0] <= x and data[iPt+1][0] >= x:
      pointIndex = iPt
      break

  if pointIndex == -1:
    return 0.0

  return data[iPt][1] + (data[iPt+1][1]-data[iPt][1])*(x - data[iPt][0])/(data[iPt+1][0]-data[iPt][0])

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
verification_utils.printErrorTolerance(tol=1e-2)

variable = {'name': 'displacement X'}

# get x, y data from results
x_data, y_data = verification_utils.getLineData('./output_data.exo', variable, 'plot')

# sample analytical displacement solution
a_data = [displacement(x_data[i]) for i in range(len(x_data))]

# compute error norm
verification_utils.computeAndPrintErrorNorm(y_data, a_data)
verification_utils.printLineSolution(x_data, y_data, a_data)
