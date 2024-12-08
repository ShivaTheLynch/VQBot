from Py4GWCoreLib import *


module_name = "FarmingBot"
outpost_coordinate_list = [
( -634.6568, 14939.2100),
( -415.9068, 14793.3770),
( -145.0734, 14678.7939),
(  125.7599, 14574.6270),
(  290.5596, 14562.8818),
(  413.2263, 14552.2152),
(  535.8929, 14530.8818),
(  738.5596, 14525.5485),
(  925.2263, 14482.8818),
(  989.2263, 14418.8818),
( 1079.8929, 14322.8818),
( 1138.5596, 14253.5485),
( 1293.2263, 14088.2152),
( 1463.8929, 13954.8818),
( 1698.5596, 13810.8818),
( 1991.8929, 13661.5485),
( 2226.5596, 13517.5485),
( 2519.8929, 13368.2152),
( 2679.8929, 13272.2152),
( 2850.5596, 13245.5485)
]

map_paths = { 
    105: [
(-4583.3984,  -968.7500),
(-4491.7319,  -835.4167),
(-4383.3984,  -718.7500),
(-4241.7319,  -560.4167),
(-4091.7317,  -418.7500),
(-3966.7317,  -302.0833),
(-3791.7317,  -177.0833),
(-3533.3984,   -10.4167),
(-3408.3984,    97.9167),
(-3208.3984,   297.9167),
(-3041.7317,   422.9167),
(-2883.3984,   581.2500),
(-2741.7317,   797.9167),
(-2600.0652,  1081.2500),
(-2558.3984,  1331.2500),
(-2616.7317,  1631.2500),
(-2725.0652,  1864.5833),
(-2833.3984,  2072.9167),
(-2925.0652,  2381.2500),
(-3000.0652,  2864.5833),
(-3141.7317,  3306.2500),
(-3158.3984,  3631.2500),
(-2983.3984,  3914.5833),
(-2758.3984,  4164.5835),
(-2591.7317,  4372.9165),
(-2458.3984,  4597.9165),
(-2341.7317,  4831.2500),
(-2275.0652,  4997.9165),
(-2233.3984,  5239.5835),
(-2125.0652,  5497.9165),
(-2083.3984,  5706.2500),
(-1983.3984,  6056.2500),
(-1925.0651,  6214.5835),
(-1741.7318,  6481.2500),
(-1491.7318,  6797.9165),
(-1291.7318,  7114.5835),
(-1133.3984,  7314.5835),
(-1025.0651,  7431.2500),
( -758.3984,  7689.5835),
( -508.3984,  7947.9165),
( -291.7318,  8181.2500),
(  -83.3984,  8231.2500),
(  183.2682,  8239.5830),
(  466.6016,  8106.2500),
(  699.9349,  7947.9165),
(  791.6016,  7614.5835),
(  883.2682,  7331.2500),
(  991.6016,  7056.2500),
( 1058.2682,  6914.5835),
( 1191.6016,  6497.9165),
( 1266.6016,  6214.5835),
( 1374.9349,  5997.9165),
( 1724.9349,  5597.9165),
( 1933.2682,  5439.5835),
( 2233.2683,  5097.9165),
( 2299.9348,  4997.9165),
( 2449.9348,  4797.9165),
( 2616.6016,  4647.9165),
( 3008.2683,  4139.5835),
( 3249.9348,  3856.2500),
( 3444.0398,  3751.5889),
( 3694.7063,  3618.2556),
( 3883.2683,  3506.2500),
( 4121.3730,  3506.2556),
( 4382.7065,  3506.2556),
( 4633.2681,  3472.9167),
( 4804.0400,  3490.2556),
( 5054.7065,  3500.9221),
( 5193.3730,  3506.2556),
( 5408.2681,  3514.5833),
( 5598.7065,  3532.9221),
( 5785.3730,  3527.5889),
( 5924.9351,  3531.2500),
( 6073.3730,  3527.5889),
( 6174.7065,  3527.5889),
( 6308.0400,  3522.2556),
( 6424.9351,  3514.5833),
( 6849.9351,  3489.5833),
( 7102.7065,  3479.5889),
( 7310.7065,  3447.5889),
( 7624.9351,  3397.9167),
( 7742.7065,  3287.5889),
( 7881.3730,  3196.9221),
( 8066.6016,  3081.2500),
( 8224.9346,  2889.5833),
( 8350.7061,  2823.5889),
( 8478.7061,  2700.9221),
( 8596.0400,  2588.9221),
( 8766.6016,  2447.9167),
( 8932.0400,  2338.2556),
( 9060.0400,  2258.2556),
( 9316.6016,  2064.5833),
( 9401.3730,  1959.5889),
( 9609.3730,  1847.5889),
( 9721.3730,  1762.2555),
( 9908.2686,  1647.9167),
(10025.3730,  1506.2555),
(10062.7061,  1340.9222),
(10124.9346,  1106.2500),
(10100.0400,  1010.2555),
(10020.0400,   812.9222),
( 9998.7061,   695.5889),
( 9924.9346,   472.9167),
( 9849.9346,   247.9167),
( 9799.9346,    97.9167),
( 9649.9346,   -52.0833),
( 9549.9346,  -218.7500),
( 9424.9346,  -477.0833),
( 9308.2686,  -618.7500),
( 9126.7061,  -648.4111),
( 8866.7061,  -748.4111),
( 8621.2891,  -835.9375),
( 8214.3877,  -917.3177),
( 8060.0400,  -935.0778),
( 7866.7065,  -968.4111),
( 7661.0024, -1014.9740),
( 7480.0400, -1041.7445),
( 7233.3730, -1135.0778),
( 7026.2368, -1259.1146),
( 6760.0400, -1348.4111),
( 6633.3730, -1455.0778),
( 6433.3730, -1528.4111),
( 6273.3730, -1615.0778),
( 6126.7065, -1735.0778),
( 5953.3730, -1855.0778),
( 5826.7065, -1968.4111),
( 5646.7065, -2135.0779),
( 5473.3730, -2261.7444),
( 5386.7065, -2368.4111),
( 5260.0400, -2501.7444),
( 5105.6641, -2642.5781),
( 4845.2476, -3065.7551),
( 4682.4868, -3375.0000),
( 4454.6226, -3879.5574),
( 4519.7266, -4367.8384),
( 4731.3149, -5116.5366),
( 4766.7065, -5293.7446),
( 4761.3730, -5443.0776),
( 4804.0400, -5640.4111),
( 4798.7065, -5848.4111),
( 4761.3730, -5992.4111),
( 4766.7065, -6147.0776),
( 4809.3730, -6371.0776),
( 4846.7065, -6520.4111),
( 4884.0400, -6744.4111),
( 4948.0400, -7069.7446),
( 4958.7065, -7325.7446),
( 4937.3730, -7448.4111),
( 5060.1501, -7746.2096),
( 5176.8167, -8062.8763),
( 5143.4834, -8437.8763),
( 5143.4834, -8704.5430),
( 5110.1501, -8987.8763),
( 5076.8167, -9254.5430),
( 5085.1501, -9562.8763),
( 5026.8167, -9937.8763),
( 5051.8167, -10271.2096),
( 4968.4834, -10537.8763),
( 4926.8167, -10896.2096),
( 4768.4834, -11221.2096),
( 4701.8167, -11654.5430),
( 5226.8167, -11862.8763),
( 5893.4834, -12004.5430),
( 6260.1501, -11996.2096),
( 6726.8167, -11929.5430),
( 7226.8167, -11879.5430),
( 7360.1501, -11829.5430),
( 7743.4834, -11746.2096),
( 7918.4834, -11696.2096),
( 8158.7065, -11677.7441),
( 8420.0400, -11661.7441),
( 8697.3730, -11597.7441),
( 8963.0859, -11447.9170),
( 9483.9189, -11350.2607),
( 9892.0400, -11469.7441),
(10151.2373, -11561.8486),
(10574.7061, -11645.7441),
(10916.2109, -11740.8857),
(11371.9404, -11757.1611),
(11974.1533, -11740.8857),
(12104.3623, -11561.8486),
(12608.9189, -11447.9170),
(13308.7891, -11382.8125),
(13492.0400, -11256.4111),
(13715.6904, -11089.8438),
(13945.3730, -10915.0781),
(14203.9717, -10748.0469),
(14398.7061, -10429.7441),
(14521.3730, -10216.4111),
(14643.4248, -9950.5205),
(14601.3730, -9656.4111),
(14594.5967, -9462.2393),
(14448.1123, -9185.5469),
(14329.3730, -9000.4111),
(14142.7061, -8787.0781),
(13881.3730, -8717.7441),
(13620.0400, -8627.0781),
(13321.3730, -8429.7441),
(13006.7061, -8339.0781),
(12692.0400, -8269.7441),
(12478.7061, -8227.0781),
(12217.3730, -8243.0781),
(11908.0400, -8344.4111),
(11550.7061, -8451.0781),
(11156.0400, -8568.4111),
(10473.3730, -8675.0781),
(10110.7061, -8813.7441),
( 9753.3730, -8957.7441),
( 9769.3730, -8515.0781),
(10076.8167, -8354.5430),
(10693.4834, -8262.8763),
(11093.4834, -8171.2096),
(11518.4834, -8029.5430),
(11876.8167, -7837.8763),
(12168.4834, -7704.5430),
(12660.1501, -7637.8763),
(13051.8167, -7387.8763),
(13243.6846, -7118.4897),
(13536.6533, -6760.4165),
(13731.9658, -6418.6196),
(13976.1064, -6044.2710),
(14155.1436, -5702.4741),
(14366.7314, -5279.2969),
(14529.4922, -4839.8438),
(14441.3730, -4541.7446),
(14383.0078, -4286.4585),
(14252.7998, -3895.8333),
(14228.0400, -3667.0779),
(14196.0400, -3448.4111),
(14187.6953, -3326.1719),
(14155.1436, -2935.5469),
(14171.4189, -2284.5051),
(14171.4189, -1991.5365),
(14297.3730, -1869.7445),
(14436.0400, -1741.7445),
(14594.5967, -1600.9115),
(14729.3730, -1549.7445),
(14916.0400, -1368.4111),
(15017.3730, -1267.0778),
(15172.0400, -1123.0778),
(15353.3730,  -925.7445),
(15513.3730,  -749.7445),
(15614.7061,  -568.4111),
(15806.7061,  -344.4111),
(16057.3730,   -99.0778),
(16137.3730,    23.5889),
(16292.0400,   183.5889),
(16420.0391,   295.5889),
(16745.3730,   567.5889),
(17149.9355,   921.8750),
(17638.2168,  1524.0885),
(17784.7012,  2142.5781),
(17556.8359,  2614.5833),
(17320.5667,  2885.0404),
(17122.6501,  2989.2070),
(16903.9001,  3301.7070),
(16633.0667,  3572.5404),
(16445.5667,  3853.7904),
(16372.6501,  4260.0404),
(16247.6501,  4645.4570),
(16018.4834,  4895.4570),
(15674.7334,  5114.2070),
(15351.8167,  5364.2070),
(15289.3167,  5687.1237),
(15351.8167,  6072.5404),
(15393.4834,  5624.6237),
(15549.7334,  5395.4570),
(16122.6501,  5197.5404),
(16528.9001,  5187.1237),
(16841.4001,  5291.2904),
(17205.9834,  5551.7070),
(17445.5667,  5957.9570),
(17476.8167,  6457.9570),
(17497.6501,  6937.1237),
(17549.7334,  7385.0404),
(17560.1501,  7801.7070),
(17591.4001,  8176.7070),
(17570.5667,  8582.9570),
(17476.8167,  9103.7904),
(17268.4834,  9416.2904),
(16976.8167,  9707.9570),

    ],
    13: [
        ( 2927.8432, 13157.9603),
        ( 3167.4266, 13116.2936),
        ( 3365.3432, 13376.7103),
        ( 3365.3432, 13647.5436),
        ( 3459.0932, 13918.3769),
        ( 3604.9266, 14126.7103),
        ( 3875.7599, 14512.1269),
        ( 4282.0099, 14887.1269),
        ( 4646.5932, 15074.6269),
        ( 5094.5099, 15449.6269),
        ( 5334.0932, 15616.2936),
        ( 5938.2599, 15741.2936),
        ( 6417.4266, 15657.9603),
        ( 6698.6766, 15376.7103),
        ( 7334.0932, 15376.7103),
        ( 7552.8432, 15428.7936),
        ( 8490.3432, 15595.4603),
        ( 8886.1766, 15689.2103),
        ( 9282.0099, 15793.3769),
        ( 9552.8432, 15824.6269),
        (10063.2599, 16043.3769),
        (10532.0099, 16241.2936),
        (10959.0932, 16449.6269),
        (11584.0932, 16512.1269),
        (12261.1766, 16553.7936),
        (12886.1766, 16553.7936),
        (13250.7599, 16532.9603),
        (13542.4266, 16355.8769),
        (13729.9266, 16137.1269),
        (14011.1766, 15897.5436),
        (14344.5099, 15605.8769),
        (14604.9266, 15293.3769),
        (14719.5099, 14991.2936),
        (14834.0932, 14564.2103),
        (14813.2599, 14105.8769),
        (14907.0099, 13741.2936),
        (15250.7599, 13595.4603),
        (15854.9266, 13741.2936),
        (16594.5099, 14105.8769),
        (17000.7599, 14376.7103),
        (17282.0099, 14574.6269),
        (17657.0099, 14720.4603),
        (17990.3432, 14793.3769),
        (18677.8432, 15032.9603),
        (18740.3432, 15126.7103),
        (18886.1766, 15387.1269),
        (19032.0099, 15553.7936),
        (19344.5099, 15647.5436),
        (19740.3432, 15720.4603),
        (19959.0932, 15689.2103),
        (20167.4266, 15491.2936),
        (20417.4266, 15324.6269),
        (20948.6766, 15282.9603),
        (21167.4266, 15543.3769),
        (21365.3432, 15928.7936),
        (21709.0932, 16616.2936),
        (21709.0932, 16741.2936),
        (21625.7599, 17022.5436),
        (21323.6766, 17397.5436),
        (21104.9266, 17845.4603),
        (21104.9266, 18303.7936),
        (21198.6766, 18647.5436),
        (21334.0932, 18939.2103),
        (21375.7599, 19470.4603),
        (21407.0099, 19751.7103),
        (21344.5099, 19939.2103),
        (21115.3432, 20199.6269),
        (20854.9266, 20480.8769),
        (20667.4266, 20772.5436),
        (20573.6766, 21116.2936),
        (20479.9266, 21366.2936),
        (20417.4266, 21480.8769)
    ],
    106: [
        (-17664.4395, -21434.5566),
        (-17747.7734, -21132.4727),
        (-17851.9395, -20830.3906),
        (-18008.1895, -20434.5566),
        (-18206.1055, -20257.4727),
        (-18295.7702, -20061.5270),
        (-18372.5702, -19882.3270),
        (-18419.5035, -19771.3937),
        (-18466.5234, -19705.3906),
        (-18470.7035, -19622.0604),
        (-18496.3035, -19519.6604),
        (-18517.6369, -19387.3937),
        (-18547.5035, -19263.6604),
        (-18568.8369, -19174.0604),
        (-18611.5035, -19041.7937),
        (-18628.5702, -18956.4604),
        (-18649.9035, -18871.1270),
        (-18696.8369, -18743.1270),
        (-18726.7035, -18640.7270),
        (-18726.7035, -18563.9270),
        (-18735.2369, -18491.3937),
        (-18747.7734, -18361.6406),
        (-18756.5702, -18307.9270),
        (-18756.5702, -18205.5270),
        (-18756.5702, -18120.1937),
        (-18747.7734, -18007.4727),
        (-18743.7702, -17906.8604),
        (-18743.7702, -17808.7270),
        (-18737.3555, -17694.9727),
        (-18720.7302, -17586.8604),
        (-18700.2502, -17484.4604),
        (-18690.0102, -17423.0204),
        (-18674.8555, -17309.5566),
        (-18655.8769, -17187.5004),
        (-18649.0502, -17071.4470),
        (-18649.0502, -17003.1804),
        (-18612.3555, -16872.0566),
        (-18597.8502, -16784.7270),
        (-18567.1302, -16699.3937),
        (-18550.0635, -16637.9537),
        (-18549.8555, -16569.9727),
        (-18543.2369, -16470.7004),
        (-18515.9302, -16388.7804),
        (-18502.2769, -16296.6204),
        (-18485.2102, -16207.8737),
        (-18478.3835, -16108.8870),
        (-18468.1435, -16050.8604),
        (-18457.9035, -15931.3937),
        (-18437.4235, -15869.9537),
        (-18414.4395, -15788.7236),
        (-18423.7702, -15706.1137),
        (-18440.8369, -15620.7804),
        (-18454.4902, -15562.7537),
        (-18476.9395, -15455.3906),
        (-18495.4502, -15357.9537),
        (-18522.7569, -15293.1004),
        (-18526.1702, -15235.0737),
        (-18560.2734, -15142.8906),
        (-18587.6102, -15071.2337),
        (-18580.7835, -14965.4204),
        (-18580.7835, -14866.4337),
        (-18580.7835, -14781.1004),
        (-18570.6895, -14663.7236),
        (-18556.8902, -14542.1670),
        (-18543.2369, -14446.5937),
        (-18532.9969, -14364.6737),
        (-18518.6055, -14299.1406),
        (-18512.5169, -14190.5937),
        (-18502.2769, -14095.0204),
        (-18502.2769, -14060.8870),
        (-18497.7734, -13965.8066),
        (-18488.6235, -13903.8737),
        (-18492.0369, -13791.2337),
        (-18498.8635, -13705.9004),
        (-18502.2769, -13603.5004),
        (-18509.1035, -13487.4470),
        (-18519.3435, -13405.5270),
        (-18532.9969, -13320.1937),
        (-18553.4769, -13238.2737),
        (-18577.3702, -13159.7670),
        (-18591.5234, -13059.5566),
        (-18611.5035, -12975.4470),
        (-18621.7435, -12866.2204),
        (-18635.3969, -12815.0204),
        (-18638.8102, -12767.2337),
        (-18643.6055, -12705.3906),
        (-18638.8102, -12634.1137),
        (-18649.0502, -12579.5004),
        (-18655.8769, -12473.6870),
        (-18655.8769, -12419.0737),
        (-18655.8769, -12340.5670),
        (-18652.4635, -12272.3004),
        (-18635.3969, -12197.2070),
        (-18635.3969, -12122.1137),
        (-18625.1569, -12002.6470),
        (-18621.7435, -11927.5537),
        (-18601.2635, -11866.1137),
        (-18594.4369, -11835.3937),
        (-18560.2734, -11757.4736),
        (-18556.8902, -11630.5937),
        (-18556.8902, -11541.8470),
        (-18553.4769, -11459.9270),
        (-18553.4769, -11343.8737),
        (-18581.1055, -11257.4736),
        (-18567.1302, -11050.3270),
        (-18587.6102, -10937.6870),
        (-18612.3555, -10840.8066),
        (-18652.4635, -10726.0604),
        (-18690.0102, -10647.5537),
        (-18716.5234, -10580.3906),
        (-18956.1055, -10226.2236),
        (-19133.1895, -10059.5566),
        (-19310.2734, -9799.1406),
        (-19338.5435, -9705.4737),
        (-19389.7435, -9592.8337),
        (-19430.7035, -9510.9137),
        (-19466.5234, -9403.3066),
        (-19485.3169, -9323.1804),
        (-19522.8635, -9183.2337),
        (-19533.1035, -9087.6604),
        (-19539.4395, -9028.3066),
        (-19546.7569, -8923.8204),
        (-19546.7569, -8845.3137),
        (-19546.7569, -8753.1537),
        (-19549.8555, -8642.8906),
        (-19539.9302, -8524.4604),
        (-19519.4502, -8418.6470),
        (-19492.1435, -8329.9004),
        (-19454.5969, -8271.8737),
        (-19393.1569, -8230.9137),
        (-19321.4769, -8176.3004),
        (-19206.1055, -8111.6401),
        (-19157.6369, -8022.7004),
        (-19099.6102, -7940.7804),
        (-19039.4395, -7872.0571),
        (-18980.1435, -7800.8337),
        (-18918.7035, -7722.3270),
        (-18829.9569, -7636.9937),
        (-18747.7734, -7528.3071),
        (-18497.7734, -7330.3901),
        (-18112.3555, -7194.9736),
        (-18018.2969, -7150.2170),
        (-17894.5635, -7103.2837),
        (-17749.4969, -7017.9504),
        (-17529.0234, -6913.7236),
        (-17344.1635, -6821.6837),
        (-17143.6302, -6783.2837),
        (-16943.0969, -6706.4837),
        (-16768.1635, -6693.6837),
        (-16657.2302, -6672.3504),
        (-16414.4395, -6684.5571),
        (-16324.4302, -6689.4170),
        (-16196.4302, -6715.0170),
        (-16072.6969, -6732.0837),
        (-15935.2725, -6788.7236),
        (-15768.6064, -6924.1401),
        (-15601.9395, -7101.2236),
        (-15320.6895, -7382.4736),
        (-15195.6895, -7476.2236),
        (-15060.2725, -7653.3071),
        (-14993.2302, -7768.8837),
        (-14942.0302, -7841.4170),
        (-14789.4395, -7997.0571),
        (-14698.8302, -8071.8170),
        (-14617.7635, -8127.2837),
        (-14523.8969, -8216.8837),
        (-14331.1064, -8361.6406),
        (-14212.4302, -8434.4837),
        (-14080.1635, -8489.9504),
        (-13914.4395, -8572.5781),
        (-13497.7725, -8650.7031),
        (-13354.8302, -8681.9504),
        (-13226.8302, -8652.0837),
        (-13081.7635, -8622.2170),
        (-12894.0302, -8536.8837),
        (-12851.3635, -8498.4837),
        (-12757.4969, -8400.3504),
        (-12702.0302, -8293.6837),
        (-12612.4302, -8204.0837),
        (-12561.2302, -8135.8170),
        (-12514.2969, -8041.9504),
        (-12456.1064, -7973.6196),
        (-12399.0969, -7593.9504),
        (-12394.8302, -7500.0837),
        (-12399.0969, -7397.6837),
        (-12369.2302, -7282.4837),
        (-12364.9600, -7140.2861),
        (-12360.6969, -7013.6837),
        (-12339.3635, -6855.8170),
        (-12322.2969, -6689.4170),
        (-12313.7635, -6604.0837),
        (-12312.8770, -6450.1821),
        (-12292.4302, -6296.8837),
        (-12288.1635, -6151.8170),
        (-12286.8350, -6033.5151),
        (-12288.1635, -5887.2837),
        (-12275.3635, -5746.4837),
        (-12286.8350, -5590.8071),
        (-12254.0302, -5473.4170),
        (-12262.5635, -5272.8837),
        (-12258.2969, -5132.0837),
        (-12234.7520, -4978.8276),
        (-12169.6475, -4718.4111),
        (-12168.6969, -4573.1504),
        (-12100.4302, -4406.7504),
        (-12023.6302, -4300.0837),
        (-11925.4969, -4206.2170),
        (-11766.0020, -4119.4526),
        (-11579.8969, -4108.0837),
        (-11400.6969, -4061.1504),
        (-11167.0439, -4041.3279),
        (-10999.3842, -4022.9333),
        (-10789.4395, -4002.2654),
        (-10524.7175, -3990.9333),
        (-10333.7100, -4002.2654),
        (-10163.3635, -3984.3504),
        (-10001.2302, -3945.9504),
        (-9890.2969, -3916.0837),
        (-9745.2302, -3907.5504),
        (-9595.8969, -3877.6837),
        (-9412.4302, -3775.2837),
        (-9314.2969, -3715.5504),
        (-9239.9600, -3702.7861),
        (-9147.8969, -3664.3504),
        (-9071.0969, -3621.6837),
        (-9019.8969, -3515.0170),
        (-8947.3635, -3455.2837),
        (-8857.7635, -3408.3504),
        (-8780.9635, -3327.2837),
        (-8721.2302, -3224.8837),
        (-8674.2969, -3139.5504),
        (-8635.8969, -2981.6837),
        (-8614.5635, -2815.2837),
        (-8567.6302, -2546.4837),
        (-8478.0302, -2427.0170),
        (-8379.8969, -2286.2170),
        (-8324.4302, -2188.0837),
        (-8251.8969, -2055.8170),
        (-8162.2969, -1979.0170),
        (-8047.0969, -1889.4170),
        (-7970.2969, -1812.6170),
        (-7880.6969, -1735.8170),
        (-7744.1635, -1577.9504),
        (-7586.2969, -1407.2837),
        (-7415.6302, -1270.7504),
        (-7308.9635, -1134.2170),
        (-7104.1635, -1031.8170),
        (-6805.4969, -1023.2837),
        (-6583.6302, -1010.4837),
        (-6468.4302, -1006.2170),
        (-6220.9635,  -976.3504),
        (-6092.9635, -1001.9504),
        (-5909.4969,  -993.4170),
        (-5738.8302,  -984.8837),
        (-5576.6969, -1001.9504),
        (-5478.5635, -1006.2170),
        (-5307.8969, -1027.5504),
        (-5201.2302, -1048.8837),
        (-5039.0969, -1044.6170),
        (-4795.8969, -1044.6170),
        (-4650.8302,  -955.0170),
        (-4522.8302,  -869.6837),
        (-4420.4302,  -780.0837)
    ]
}
FARM_MODEL_IDS = [] 
OUTPOST_ID = 36
FARM_END_ID = 105

class BotVars:
    def __init__(self, starting_outpost_id=0, farm_end_id=0):
        self.starting_map = starting_outpost_id
        self.farm_end_id = farm_end_id
        self.bot_started = False
        self.window_module = None
        self.variables = {}
        self.has_env_reset = False

        # Simple Farm Configurations
        self.resign_to_farm = True
        self.pick_up_chests = True
        self.load_skillbar = False

        
        # Simple Farm Tracking Metrics
        self.farm_timer = Py4GW.Timer()
        self.farm_count = 0
        self.chests_found = 0
        self.deaths = 0
        

bot_vars = BotVars(starting_outpost_id=OUTPOST_ID, farm_end_id=FARM_END_ID)
bot_vars.window_module = ImGui.WindowModule(module_name, window_name="Simple Farming", window_size=(300, 350))

class StateMachineVars:
        def __init__(self):
            # FSMs
            self.state_machine = FSM("Main")
            self.path_to_farm_machine = FSM("PathToFarm")
            self.farm_machine = FSM("Farm")
            self.loot_items = FSM("Loot")
            self.loot_chest = FSM("Chest")
            self.fight_enemies = FSM("Fight")

            # Movement
            self.outpost_pathing = Routines.Movement.PathHandler(outpost_coordinate_list)
            self.current_map_pathing = Routines.Movement.PathHandler([])
            self.chest_found_pathing = None
            self.current_map_id = 0
            self.movement_handler = Routines.Movement.FollowXY()

            # Other tools and variables
            self.ping_handler = Py4GW.PingHandler()
            self.timer = Py4GW.Timer()
            self.timer_check = 0
            self.has_resigned = False
            self.map_loaded = False
            self.explorable_loading = False
            self.finished_resigning = False
            self.collected_coords = []
            self.current_target = None
            self.current_loot_target = None
            self.current_chest_target = 0
            self.completed_chests = []
            

FSM_vars = StateMachineVars()

#Helper Functions
def StartBot():
    global bot_vars

    if not bot_vars.has_env_reset:
        ResetEnvironment()
        bot_vars.has_env_reset = True
        bot_vars.farm_timer.reset()

    bot_vars.bot_started = True

def StopBot():
    global bot_vars
    bot_vars.farm_timer.stop()
    bot_vars.bot_started = False

def IsBotStarted():
    global bot_vars
    return bot_vars.bot_started

def IfActionIsPending():
    if FSM_vars.timer_check != 0 and FSM_vars.timer.get_elapsed_time() > 0:
        if FSM_vars.timer.has_elapsed(FSM_vars.timer_check):
            FSM_vars.timer_check = 0
            FSM_vars.timer.stop()
            return False
    if FSM_vars.timer_check == 0 and FSM_vars.timer.get_elapsed_time() == 0:
        return False
    return True

def SetPendingAction(timer_check=1000):
    FSM_vars.timer_check = timer_check
    FSM_vars.timer.reset()

def DoesNeedInventoryHandling():
    return ( Inventory.GetFreeSlotCount() < 1 or Inventory.GetModelCount(22751) < 1)

def CheckMapLocation():
    global bot_vars, FSM_vars
    if IfActionIsPending():
        return

    if Routines.Transition.IsExplorableLoaded():
        if Map.GetMapID() not in map_paths:
            Routines.Transition.TravelToOutpost(bot_vars.starting_map) # travel to starting outpost if not in one of the zones
            SetPendingAction(2000)
            return
        
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"{Map.GetMapName(Map.GetMapID())} ({Map.GetMapID()}) already loaded. Switching to Farm step.", Py4GW.Console.MessageType.Info)
        FSM_vars.current_map_id = 0
        FSM_vars.current_map_pathing = Routines.Movement.PathHandler([])
        FSM_vars.state_machine.jump_to_state_by_name("Start Pathing for Farm")
        return
        
    if Routines.Transition.IsOutpostLoaded():
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Outpost loaded", Py4GW.Console.MessageType.Info)
        if Map.GetMapID() != bot_vars.starting_map:
            Routines.Transition.TravelToOutpost(bot_vars.starting_map)
            SetPendingAction(3000)
            return
        
        FSM_vars.timer.stop()
        FSM_vars.state_machine.jump_to_state_by_name("Leaving Outpost")
    
    SetPendingAction(int(FSM_vars.ping_handler.GetCurrentPing()) * 2) # to help prevent it from checking too frequently

def LoadSkillBar(): # TODO ould need to set skill templates for the farm
    global bot_vars
    if bot_vars.load_skillbar:
        primary_profession, secondary_profession = Agent.GetProfessionNames(Player.GetAgentID())

        if primary_profession == "Warrior":
            SkillBar.LoadSkillTemplate("OQcAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Ranger":
            SkillBar.LoadSkillTemplate("OgcAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Monk":
            SkillBar.LoadSkillTemplate("OwcAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Necromancer":
            SkillBar.LoadSkillTemplate("OAdAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Mesmer":
            SkillBar.LoadSkillTemplate("OQdAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Elementalist":
            SkillBar.LoadSkillTemplate("OgdAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Assassin":
            SkillBar.LoadSkillTemplate("OwBAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Ritualist":
            SkillBar.LoadSkillTemplate("OACiIukLdNVOxMtMVN5D6MNACA")
        elif primary_profession == "Paragon":
            SkillBar.LoadSkillTemplate("OQeAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Dervish":
            SkillBar.LoadSkillTemplate("OgCjwqpoKThX7XdftXWgOXQX0k")

def IsSkillBarLoaded():
    global bot_vars
    if bot_vars.load_skillbar:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"SkillBar Loaded.", Py4GW.Console.MessageType.Info)       
    return True

def HandleSkills():
    global FSM_vars
    if not Routines.Transition.IsExplorableLoaded():
        return
    
    if IfActionIsPending():
        return

    if not Agent.IsAlive(Player.GetAgentID()):
        return
    
    if Agent.IsCasting(Player.GetAgentID()):
        return

    if Agent.IsKnockedDown(Player.GetAgentID()):
        return

    for i in [1, 2, 3]:
        if Agent.GetEnergy(Player.GetAgentID()) * Agent.GetMaxEnergy(Player.GetAgentID()) >= Skill.Data.GetEnergyCost(SkillBar.GetSkillIDBySlot(i)) and SkillBar.GetSkillData(i).recharge == 0:
            delay = int(Skill.Data.GetActivation(SkillBar.GetSkillIDBySlot(i))) * 1000
            delay += int(Skill.Data.GetAftercast(SkillBar.GetSkillIDBySlot(i))) * 1000
            delay += int(FSM_vars.ping_handler.GetCurrentPing()) * 2
            SetPendingAction(delay)
            SkillBar.UseSkill(i)
            return

def Resign():
    global FSM_vars, bot_vars
    if IfActionIsPending():
        return

    if bot_vars.resign_to_farm == True and FSM_vars.has_resigned == False:
        Player.SendChatCommand("resign") # only resign once
        FSM_vars.has_resigned = True
        bot_vars.farm_count += 1
        SetPendingAction(2000)
    
    if Routines.Transition.IsOutpostLoaded() or Map.IsMapLoading():
        FSM_vars.state_machine.jump_to_state_by_name("Finished")
    
    SetPendingAction(1000) # make sure to wait before spamming IsLoaded

def UpdateTarget(max_distance=2500):
    if IfActionIsPending():
        return
    
    if not Agent.IsAlive(Player.GetAgentID()): # if not alive
        return
    
    # reset target once its dead
    if FSM_vars.current_target != None and Agent.IsDead(FSM_vars.current_target):
        FSM_vars.current_target = None
        return

    # only look for target if we don't have one
    if FSM_vars.current_target == None:
        enemy_array = AgentArray.GetEnemyArray()
        xy = Player.GetXY()
        filtered_enemy_array = Utils.Filters.FilterAgentArrayByAlive(xy, enemy_array, area=2500)
        filtered_enemy_array = AgentArray.Sort.ByDistance(filtered_enemy_array, xy)
        nearby_enemies = [
            agent for agent in filtered_enemy_array 
            if Utils.Distance(xy, Agent.GetXY(agent)) <= max_distance
        ]
        
        for agent in nearby_enemies:
            try:
                # player_number = Agent.GetPlayerNumber(agent) # if you need to check the model id of the enemy to only farm specific enemies

                FSM_vars.current_target = agent
                Py4GW.Console.Log(bot_vars.window_module.module_name, f"Target Farm found! {agent}", Py4GW.Console.MessageType.Info)
                return agent  # Return the target enemy if found
            except Exception as e:
                # Log any errors that occur during the player number retrieval
                Py4GW.Console.Log(bot_vars.window_module.module_name, f"Error retrieving player number: {str(e)}", Py4GW.Console.MessageType.Error)

    return None  # No valid target found


def EnemyFound():
    global FSM_vars
    UpdateTarget(max_distance=1150)
    return FSM_vars.current_target != None

def ChangeTargeting():
    global FSM_vars
    Player.ChangeTarget(FSM_vars.current_target)

def ResetPathing(pathing):
    global FSM_vars
    if not Routines.Movement.IsFollowPathFinished(pathing, FSM_vars.movement_handler):
        pathing.reset()
    else:
        FSM_vars.farm_machine.jump_to_state_by_name("Finished")

def UpdateLootTarget(max_distance=1250):
    global FSM_vars
    if IfActionIsPending():
        return

    # Reset loot target once it's no longer valid or has been picked up
    if FSM_vars.current_loot_target is not None and not Agent.IsItem(FSM_vars.current_loot_target):
        FSM_vars.current_loot_target = None
        return

    # Only look for a new loot target if we don't have one
    if FSM_vars.current_loot_target is None:
        # Retrieve all items within the area
        item_array = AgentArray.GetItemArray()
        xy = Player.GetXY()
        filtered_item_array = AgentArray.Sort.ByDistance(item_array, xy)
        
        # Filter items within the maximum distance
        nearby_items = [
            item for item in filtered_item_array
            if Utils.Distance(xy, Agent.GetXY(item)) <= max_distance
        ]
        
        # Set the current loot target to the nearest valid item
        for item in nearby_items:
            FSM_vars.current_loot_target = item
            Py4GW.Console.Log(bot_vars.window_module.module_name, f"Loot Item found! {item}", Py4GW.Console.MessageType.Info)
            return item  # Return the loot item if found

    return None  # No valid loot item found

def LootFound():
    UpdateLootTarget(max_distance=1250)
    return FSM_vars.current_loot_target is not None

def IsChestFound(max_distance=2500):
    return Routines.Targeting.GetNearestChest(max_distance) != 0

def ResetFollowPathToChest():
    global FSM_vars
    FSM_vars.movement_handler.reset()
    ResetPathing(FSM_vars.current_map_pathing)
    if FSM_vars.current_chest_target != 0:
        chest_x, chest_y = Agent.GetXY(FSM_vars.current_chest_target)
        found_chest_coord_list = [(chest_x, chest_y)]
    
    if found_chest_coord_list != None:
        FSM_vars.chest_found_pathing = Routines.Movement.PathHandler(found_chest_coord_list)
        FSM_vars.loot_chest.jump_to_state_by_name("MoveToChest")
    else:
        FSM_vars.loot_chest.jump_to_state_by_name("Finished")

def CheckForChest():   
    global FSM_vars, bot_vars
    if bot_vars.pick_up_chests != False and FSM_vars.current_chest_target != 0 and FSM_vars.current_chest_target not in FSM_vars.completed_chests:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Chest {FSM_vars.current_chest_target} found and not in completed_chests {FSM_vars.completed_chests}", Py4GW.Console.MessageType.Info)
        FSM_vars.loot_chest.jump_to_state_by_name("Reset Follow Path To Chest")
    else:
        FSM_vars.loot_chest.jump_to_state_by_name("Finished")

def ChestFound(max_distance=1250):
    global FSM_vars
    if IfActionIsPending():
        return False
    
    chest = Routines.Targeting.GetNearestChest(max_distance)
    if chest != 0 and chest not in FSM_vars.completed_chests:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Chest {chest} found!", Py4GW.Console.MessageType.Info)
        FSM_vars.current_chest_target = chest
        return True
    
    FSM_vars.current_chest_target = 0
    return False

def TrackChest():
    global FSM_vars, bot_vars
    
    if FSM_vars.current_chest_target != 0:
        FSM_vars.completed_chests.append(FSM_vars.current_chest_target)
        FSM_vars.current_chest_target = 0
        bot_vars.chests_found += 1

    return True

def PlayerDied():
    global bot_vars
    if not Agent.IsAlive(Player.GetAgentID()):
        FSM_vars.current_target = None # reset target so that it can restart the sub machine
        bot_vars.deaths += 1
        return True
    return False

def CheckForMap():
    global FSM_vars
    if IfActionIsPending():
        return False
    
    current_map = Map.GetMapID()
    if Routines.Transition.IsExplorableLoaded():
        if current_map in map_paths:
            Py4GW.Console.Log(bot_vars.window_module.module_name, f"Setting current map and path to {current_map}", Py4GW.Console.MessageType.Info)
            FSM_vars.current_map_pathing = Routines.Movement.PathHandler(map_paths[current_map])
            FSM_vars.current_map_id = current_map
            return
    
    # not sure if I need to handle the case where this map path doesn't get loaded correctly
    Py4GW.Console.Log(bot_vars.window_module.module_name, f"CheckForMap() when Explorable not loaded.", Py4GW.Console.MessageType.Info)
    SetPendingAction(2000)

def IsCurrentPathFinished():
    return (Routines.Movement.IsFollowPathFinished(FSM_vars.current_map_pathing, FSM_vars.movement_handler) and not EnemyFound())

def format_elapsed_time(milliseconds):
    """
    Converts elapsed time in milliseconds to a human-readable format.
    Displays seconds if under 60 seconds, otherwise displays minutes and seconds.
    """
    total_seconds = milliseconds / 1000
    if total_seconds < 60:
        return f"{total_seconds:.2f} seconds"
    else:
        minutes = int(total_seconds // 60)
        seconds = total_seconds % 60
        return f"{minutes}m {seconds:.2f}s"
    
def WaitForLoot():
    if IfActionIsPending():
        return False
    
    if not LootFound():
        return True
    else:
        SetPendingAction(2000)
        return True


FSM_vars.loot_items.AddState(name="Select Item",
                    execute_fn=lambda: FSM_vars.current_loot_target != None and Player.ChangeTarget(FSM_vars.current_loot_target),
                    transition_delay_ms=1000)
FSM_vars.loot_items.AddState(name="PickUpItem",
                    execute_fn=lambda: FSM_vars.current_loot_target != None and Routines.Targeting.InteractTarget(),
                    transition_delay_ms=1000)
FSM_vars.loot_items.AddState(name="Wait for Loot to Finish",
                    exit_condition=lambda: WaitForLoot(),
                    run_once=False)

# FSM Routine for looting chests only
FSM_vars.loot_chest.AddState(name="CheckForChest",
                    execute_fn=lambda: CheckForChest())
FSM_vars.loot_chest.AddState(name="Reset Follow Path To Chest",
                    execute_fn=lambda: ResetFollowPathToChest())
FSM_vars.loot_chest.AddState(name="MoveToChest",
                    execute_fn=lambda: Routines.Movement.FollowPath(FSM_vars.chest_found_pathing, FSM_vars.movement_handler),
                    exit_condition=lambda: Routines.Movement.IsFollowPathFinished(FSM_vars.chest_found_pathing, FSM_vars.movement_handler),
                    run_once=False)
FSM_vars.loot_chest.AddState(name="Select Chest",
                    execute_fn=lambda: Player.ChangeTarget(FSM_vars.current_chest_target),
                    transition_delay_ms=1000)
FSM_vars.loot_chest.AddState(name="Track Chest",
                    exit_condition=lambda: TrackChest(),
                    transition_delay_ms=1000)
FSM_vars.loot_chest.AddState(name="Interact with Chest",
                    execute_fn=lambda: Routines.Targeting.InteractTarget(),
                    transition_delay_ms=1000)
FSM_vars.loot_chest.AddState(name="Open With Lockpick",
                    execute_fn=lambda: Player.SendDialog(2),
                    transition_delay_ms=1000)
FSM_vars.loot_chest.AddState(name="Finished")


FSM_vars.fight_enemies.AddState(name="Target Enemy",
                    execute_fn=lambda: Player.ChangeTarget(FSM_vars.current_target),
                    transition_delay_ms=500)
FSM_vars.fight_enemies.AddState(name="Engage Enemy",
                    execute_fn=lambda: Routines.Targeting.InteractTarget(),
                    transition_delay_ms=500)
FSM_vars.fight_enemies.AddState(name="Wait for Combat to Finish",
                    exit_condition=lambda: not Agent.IsAlive(FSM_vars.current_target) or PlayerDied(),
                    run_once=True)
FSM_vars.fight_enemies.AddState(name="Check for Next Enemy",
                    exit_condition=lambda: not EnemyFound() or not Agent.IsAlive(Player.GetAgentID()), # if no enemies found or if Player died, then we are finished
                    run_once=True)

# Farming Map Routine
FSM_vars.farm_machine.AddState(name="Check if Alive",
                       exit_condition=lambda: Agent.IsAlive(Player.GetAgentID()),
                       run_once=False)
FSM_vars.farm_machine.AddState(name="Seek for Farm",
                       execute_fn=lambda: Routines.Movement.FollowPath(FSM_vars.current_map_pathing, FSM_vars.movement_handler),
                       exit_condition=lambda: Routines.Movement.IsFollowPathFinished(FSM_vars.current_map_pathing, FSM_vars.movement_handler) or EnemyFound() or ChestFound() or Map.GetMapID() != FSM_vars.current_map_id,
                       run_once=False)
FSM_vars.farm_machine.AddSubroutine(name="Engage Farm",
                       sub_fsm = FSM_vars.fight_enemies,
                       condition_fn=lambda: not EnemyFound() or not Agent.IsAlive(Player.GetAgentID()))
FSM_vars.farm_machine.AddSubroutine(name="Loot Chest",
                       sub_fsm=FSM_vars.loot_chest,
                       condition_fn=lambda: not ChestFound() or not Agent.IsAlive(Player.GetAgentID()))
FSM_vars.farm_machine.AddSubroutine(name="Loot Items",
                       sub_fsm=FSM_vars.loot_items,
                       condition_fn=lambda: not LootFound() or not Agent.IsAlive(Player.GetAgentID()))
FSM_vars.farm_machine.AddState(name="Reset pather to find nearest point",
                       execute_fn=lambda: ResetPathing(FSM_vars.current_map_pathing) if not Routines.Movement.IsFollowPathFinished(FSM_vars.current_map_pathing, FSM_vars.movement_handler) else None,
                       run_once=True)
FSM_vars.farm_machine.AddState(name="Finished")

# Pathing to Farm Routine
FSM_vars.path_to_farm_machine.AddState(name="Check For Pathing Map",
                        execute_fn=lambda: CheckForMap(),
                        run_once=False)
FSM_vars.path_to_farm_machine.AddState(name="Reset Movement", # after mapping into new zone, need to prevent previous coord from trying to finish
                       execute_fn=lambda: FSM_vars.movement_handler.reset(), 
                       transition_delay_ms=1200)
FSM_vars.path_to_farm_machine.AddSubroutine(name="Handle Map Pathing",
                       sub_fsm = FSM_vars.farm_machine,
                       condition_fn=lambda: IsCurrentPathFinished() or Map.GetMapID() != FSM_vars.current_map_id) # if path finished or not in same map, then move on

#MAIN STATE MACHINE CONFIGURATION
FSM_vars.state_machine.AddState(name="Map Check for Farm", 
                       execute_fn=lambda: CheckMapLocation(),
                       transition_delay_ms=1000,
                       run_once=False)
FSM_vars.state_machine.AddState(name="Load SkillBar",
                       execute_fn=lambda: LoadSkillBar(),
                       transition_delay_ms=1000,
                       exit_condition=lambda: IsSkillBarLoaded())
FSM_vars.state_machine.AddState(name="Leaving Outpost",
                       execute_fn=lambda: Routines.Movement.FollowPath(FSM_vars.outpost_pathing, FSM_vars.movement_handler),
                       exit_condition=lambda: Routines.Movement.IsFollowPathFinished(FSM_vars.outpost_pathing, FSM_vars.movement_handler) or Map.IsMapLoading(),
                       run_once=False) # run once is false because we want to keep updating the pathing objects
FSM_vars.state_machine.AddState(name="Waiting for Explorable Map Load",
                       exit_condition=lambda: Routines.Transition.IsExplorableLoaded(log_actions=True),
                       transition_delay_ms=1200)
FSM_vars.state_machine.AddState(name="Reset Movement", # after mapping into new zone, need to prevent previous coord from trying to finish
                       execute_fn=lambda: FSM_vars.movement_handler.reset(), 
                       transition_delay_ms=1200)
FSM_vars.state_machine.AddSubroutine(name="Start Pathing for Farm",
                       sub_fsm = FSM_vars.path_to_farm_machine, # use farm_machine for the farm map, path_to_farm_machine to path to the farm zone
                       condition_fn=lambda: Map.GetMapID() == bot_vars.farm_end_id and IsCurrentPathFinished())
FSM_vars.state_machine.AddState(name="Resign",
                       execute_fn=lambda: Resign(),
                       run_once=False,
                       transition_delay_ms=1000)
FSM_vars.state_machine.AddState(name="Wait if no resign",
                       exit_condition=bot_vars.resign_to_farm, # this will hold unless it gets check (prevents unintentional resign after incomplete vanquish)
                       run_once=False)
FSM_vars.state_machine.AddState(name="Finished")

def DrawWindow():
    global bot_vars, FSM_vars

    try:
        if bot_vars.window_module.first_run:
            PyImGui.set_next_window_size(bot_vars.window_module.window_size[0], bot_vars.window_module.window_size[1])     
            PyImGui.set_next_window_pos(bot_vars.window_module.window_pos[0], bot_vars.window_module.window_pos[1])
            bot_vars.window_module.first_run = False

        if PyImGui.begin(bot_vars.window_module.window_name, bot_vars.window_module.window_flags):
            if PyImGui.begin_tab_bar("Simple Farming Options"):
                if PyImGui.begin_tab_item("Farm"):
                    if IsBotStarted():
                        if PyImGui.button("Pause Bot"):
                            StopBot()
                        if PyImGui.button("Stop Bot"):
                            ResetEnvironment()
                            bot_vars.has_env_reset = False
                            StopBot()
                    else:
                        if PyImGui.button("Start Bot"):
                            StartBot()
                        if PyImGui.button("Reset Env"):
                            ResetEnvironment()
                            bot_vars.has_env_reset = False

                    bot_vars.resign_to_farm = PyImGui.checkbox("Resign At End?", bot_vars.resign_to_farm)
                    bot_vars.pick_up_chests = PyImGui.checkbox("Loot Chests?", bot_vars.pick_up_chests)
                    bot_vars.load_skillbar = PyImGui.checkbox("Load SkillBar?", bot_vars.load_skillbar)


                    headers = ["Farm Stats","Data"]
                    data = [
                        ("Farm Count:", f"{bot_vars.farm_count}"),
                        ("Tracked Deaths:", f"{bot_vars.deaths}"),
                        ("Chests Found:", f"{bot_vars.chests_found}"),
                        ("Is Path Finished:", f"{IsCurrentPathFinished()}"),
                        ("Farm Timer:", f"{format_elapsed_time(bot_vars.farm_timer.get_elapsed_time())}")
                    ]

                    ImGui.table("State Machine Info", headers, data)

                    if PyImGui.button("Resign"):
                        if FSM_vars.state_machine != None:
                            FSM_vars.state_machine.jump_to_state_by_name("Resign")

                    PyImGui.end_tab_item() # end Farm Options
            
                # State Machine Debugger
                if PyImGui.begin_tab_item("State Machine Debugging"):
                    PyImGui.separator()

                    if FSM_vars.state_machine != None:
                        fsm_previous_step = FSM_vars.state_machine.get_previous_step_name()
                        fsm_current_step = FSM_vars.state_machine.get_current_step_name()
                        fsm_next_step = FSM_vars.state_machine.get_next_step_name()

                        headers = ["Main State Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.state_machine.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.state_machine.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("State Machine Info", headers, data)

                    if FSM_vars.path_to_farm_machine != None:
                        fsm_previous_step = FSM_vars.path_to_farm_machine.get_previous_step_name()
                        fsm_current_step = FSM_vars.path_to_farm_machine.get_current_step_name()
                        fsm_next_step = FSM_vars.path_to_farm_machine.get_next_step_name()

                        headers = ["Path To Farm Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.path_to_farm_machine.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.path_to_farm_machine.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Path To Farm Machine Info", headers, data)

                    if FSM_vars.farm_machine != None:
                        fsm_previous_step = FSM_vars.farm_machine.get_previous_step_name()
                        fsm_current_step = FSM_vars.farm_machine.get_current_step_name()
                        fsm_next_step = FSM_vars.farm_machine.get_next_step_name()

                        headers = ["Farm Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.farm_machine.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.farm_machine.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Farm Machine State Machine Info", headers, data)

                    if FSM_vars.fight_enemies != None:
                        fsm_previous_step = FSM_vars.fight_enemies.get_previous_step_name()
                        fsm_current_step = FSM_vars.fight_enemies.get_current_step_name()
                        fsm_next_step = FSM_vars.fight_enemies.get_next_step_name()

                        headers = ["Fight Enemies Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.fight_enemies.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.fight_enemies.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Fight Enemies State Machine Info", headers, data)

                    if FSM_vars.loot_chest != None:
                        fsm_previous_step = FSM_vars.loot_chest.get_previous_step_name()
                        fsm_current_step = FSM_vars.loot_chest.get_current_step_name()
                        fsm_next_step = FSM_vars.loot_chest.get_next_step_name()

                        headers = ["Loot Chest Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.loot_chest.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.loot_chest.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Loot Items Machine Info", headers, data)

                    if FSM_vars.loot_items != None:
                        fsm_previous_step = FSM_vars.loot_items.get_previous_step_name()
                        fsm_current_step = FSM_vars.loot_items.get_current_step_name()
                        fsm_next_step = FSM_vars.loot_items.get_next_step_name()

                        headers = ["Loot Chest Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.loot_items.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.loot_items.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Loot Items Machine Info", headers, data)
                    PyImGui.separator()

                    PyImGui.end_tab_item() # end State Machine Debugging

                PyImGui.end_tab_bar() # end Skelefarm Options

            PyImGui.end()

    except Exception as e:
        current_function = inspect.currentframe().f_code.co_name
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Error in {current_function}: {str(e)}", Py4GW.Console.MessageType.Error)
        raise

def ResetEnvironment():
    global FSM_vars
    FSM_vars.outpost_pathing.reset()
    FSM_vars.movement_handler.reset()
    FSM_vars.state_machine.reset()
    FSM_vars.path_to_farm_machine.reset()
    FSM_vars.loot_items.reset()
    FSM_vars.farm_machine.reset()
    FSM_vars.fight_enemies.reset()
    FSM_vars.timer.stop()
    FSM_vars.timer_check = 0
    FSM_vars.finished_resigning = False
    FSM_vars.has_resigned = False
    FSM_vars.map_loaded = False
    FSM_vars.explorable_loading = False
    FSM_vars.state_machine.log_actions = False
    FSM_vars.current_map_pathing = Routines.Movement.PathHandler([])
    FSM_vars.current_target = None
    FSM_vars.current_loot_target = None
    FSM_vars.current_chest_target = 0
    FSM_vars.completed_chests = []

def main():
    global bot_vars,FSM_vars
    try:
        DrawWindow()

        if IsBotStarted():
            if FSM_vars.state_machine.is_finished():
                ResetEnvironment()
            else:
                FSM_vars.state_machine.update()

    except ImportError as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"ImportError encountered: {str(e)}", Py4GW.Console.MessageType.Error)
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Stack trace: {traceback.format_exc()}", Py4GW.Console.MessageType.Error)
    except ValueError as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"ValueError encountered: {str(e)}", Py4GW.Console.MessageType.Error)
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Stack trace: {traceback.format_exc()}", Py4GW.Console.MessageType.Error)
    except TypeError as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"TypeError encountered: {str(e)}", Py4GW.Console.MessageType.Error)
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Stack trace: {traceback.format_exc()}", Py4GW.Console.MessageType.Error)
    except Exception as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Unexpected error encountered: {str(e)}", Py4GW.Console.MessageType.Error)
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Stack trace: {traceback.format_exc()}", Py4GW.Console.MessageType.Error)
    finally:
        pass

if __name__ == "__main__":
    main()
