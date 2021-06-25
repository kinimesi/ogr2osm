from simplekml import Kml, Color
kml = Kml(open=1)

# generate geometries
multipoint = kml.newmultigeometry(name="TestMultiPoint")
multipoint.newpoint(coords=[(-23.0967,33.4843)])
multipoint.newpoint(coords=[(-23.1061,33.4821)])
multipoint.newpoint(coords=[(-23.0975,33.4817)])

multilinestring = kml.newmultigeometry(name="TestMultiLinestring")
multilinestring.newlinestring(coords=[(-23.1393528,33.4886545),(-23.1372929,33.4908736),(-23.1354046,33.4923052),(-23.1326580,33.4933073),(-23.1289673,33.4938799),(-23.1253624,33.4945957),(-23.1232166,33.4956693),(-23.1216717,33.4970293),(-23.1198692,33.4986755),(-23.1191826,33.5002501)])
multilinestring.newlinestring(coords=[(-23.1383228,33.4876524),(-23.1366062,33.4888693),(-23.1350613,33.4897998),(-23.1324005,33.4913030),(-23.1293964,33.4920904),(-23.1259632,33.4924483),(-23.1233883,33.4932357),(-23.1211567,33.4943809),(-23.1192684,33.4950967),(-23.1157494,33.4956693),(-23.1130886,33.4952399),(-23.1100845,33.4943809),(-23.1072521,33.4945241),(-23.1044197,33.4956693),(-23.1022739,33.4966714),(-23.1011581,33.4981029),(-23.0999565,33.4993912)])
multilinestring.newlinestring(coords=[(-23.1362629,33.4940946),(-23.1372070,33.4928778),(-23.1397820,33.4918041),(-23.1425285,33.4906588),(-23.1438160,33.4887977),(-23.1434727,33.4865070),(-23.1419277,33.4847890),(-23.1367779,33.4840731),(-23.1336021,33.4856480),(-23.1317139,33.4877240),(-23.1293106,33.4897283),(-23.1266499,33.4902293),(-23.1219292,33.4916609),(-23.1195259,33.4907304),(-23.1154060,33.4896567),(-23.1114578,33.4907304),(-23.1070805,33.4923052),(-23.1033897,33.4936652),(-23.0994415,33.4965998),(-23.0986691,33.4986039),(-23.0986691,33.5011805),(-23.1011581,33.5029698)])

multipolygon = kml.newmultigeometry(name="TestMultiPolygon")
polygon1 = multipolygon.newpolygon(name="TestPolygonOnlyOuter")
polygon1.outerboundaryis = [(-23.0895710,33.4706855),(-23.0868244,33.4729050),(-23.0818462,33.4744085),(-23.0760098,33.4738357),(-23.0727482,33.4737641),(-23.0702591,33.4745517),(-23.0689716,33.4755540),(-23.0683708,33.4769142),(-23.0689716,33.4778449),(-23.0709457,33.4772722),(-23.0737782,33.4761267),(-23.0778122,33.4772006),(-23.0790138,33.4786324),(-23.0786705,33.4804938),(-23.0774689,33.4819255),(-23.0756664,33.4823551),(-23.0742931,33.4837868),(-23.0740356,33.4856480),(-23.0724049,33.4870797),(-23.0697441,33.4884398),(-23.0687141,33.4880103),(-23.0688000,33.4871513),(-23.0714607,33.4854333),(-23.0706882,33.4832857),(-23.0691433,33.4851469),(-23.0657101,33.4849322),(-23.0639076,33.4828562),(-23.0632210,33.4807085),(-23.0631351,33.4784892),(-23.0640793,33.4761983),(-23.0651093,33.4744085),(-23.0671692,33.4720458),(-23.0712032,33.4707571),(-23.0739498,33.4701843),(-23.0764389,33.4683228),(-23.0767822,33.4663180),(-23.0761814,33.4645995),(-23.0739498,33.4629526),(-23.0709457,33.4612341),(-23.0704308,33.4593008),(-23.0710316,33.4572958),(-23.0728340,33.4566513),(-23.0755806,33.4560068),(-23.0778122,33.4557920),(-23.0811596,33.4557920),(-23.0843353,33.4557920),(-23.0881119,33.4538585),(-23.0901718,33.4522831),(-23.0922318,33.4504211),(-23.0954933,33.4503495),(-23.0985832,33.4521398),(-23.1007290,33.4550043),(-23.1036472,33.4558636),(-23.1075096,33.4570810),(-23.1108570,33.4576538),(-23.1130028,33.4590144),(-23.1141186,33.4615922),(-23.1143761,33.4643131),(-23.1085396,33.4653871),(-23.1037331,33.4678216),(-23.1018448,33.4711151),(-23.1021881,33.4731198),(-23.1040764,33.4762699),(-23.1037545,33.4773975),(-23.1026173,33.4777196),(-23.1014800,33.4775765),(-23.1007719,33.4771111),(-23.0985403,33.4760014),(-23.0971670,33.4756614),(-23.0961800,33.4753392),(-23.0914593,33.4720458),(-23.0895710,33.4706855)]

polygon2 = multipolygon.newpolygon(name="TestPolygonWithInner")
# outer
polygon2.outerboundaryis = [(-23.1465626,33.4720458),(-23.1454468,33.4739073),(-23.1457901,33.4752676),(-23.1480217,33.4779881),(-23.1473351,33.4812096),(-23.1423569,33.4823551),(-23.1374645,33.4820687),(-23.1346321,33.4826414),(-23.1316280,33.4851469),(-23.1281948,33.4873660),(-23.1245041,33.4866502),(-23.1205559,33.4845742),(-23.1206417,33.4812812),(-23.1218433,33.4776301),(-23.1249332,33.4771290),(-23.1258774,33.4756972),(-23.1254482,33.4739073),(-23.1239033,33.4731198),(-23.1209850,33.4714015),(-23.1181526,33.4716163),(-23.1160069,33.4726902),(-23.1136036,33.4758403),(-23.1112862,33.4777017),(-23.1087971,33.4777733),(-23.1060505,33.4766995),(-23.1045914,33.4750528),(-23.1034756,33.4726186),(-23.1031322,33.4710435),(-23.1037331,33.4693967),(-23.1070805,33.4675352),(-23.1100845,33.4663896),(-23.1137753,33.4657451),(-23.1207275,33.4653871),(-23.1247616,33.4640983),(-23.1266499,33.4624514),(-23.1287098,33.4604465),(-23.1337738,33.4598020),(-23.1372070,33.4599452),(-23.1396961,33.4611625),(-23.1433868,33.4640983),(-23.1451893,33.4664612),(-23.1485367,33.4683228),(-23.1465626,33.4720458)]
# inner
polygon2.innerboundaryis = [(-23.1359196,33.4741937),(-23.1382370,33.4729050),(-23.1374645,33.4711151),(-23.1354904,33.4698263),(-23.1334305,33.4704707),(-23.1333447,33.4723322),(-23.1342888,33.4739789),(-23.1359196,33.4741937)]

kml.save("multi_geometries.kml")

# generate duplicate geometries
multipointdup = kml.newmultigeometry(name="TestMultiPoint")
multipointdup.newpoint(coords=[(-23.0967,33.4843)])
multipointdup.newpoint(coords=[(-23.1061,33.4821)])
multipointdup.newpoint(coords=[(-23.0975,33.4817)])

multilinestringdup = kml.newmultigeometry(name="TestMultiLinestring")
multilinestringdup.newlinestring(coords=[(-23.1393528,33.4886545),(-23.1372929,33.4908736),(-23.1354046,33.4923052),(-23.1326580,33.4933073),(-23.1289673,33.4938799),(-23.1253624,33.4945957),(-23.1232166,33.4956693),(-23.1216717,33.4970293),(-23.1198692,33.4986755),(-23.1191826,33.5002501)])
multilinestringdup.newlinestring(coords=[(-23.1383228,33.4876524),(-23.1366062,33.4888693),(-23.1350613,33.4897998),(-23.1324005,33.4913030),(-23.1293964,33.4920904),(-23.1259632,33.4924483),(-23.1233883,33.4932357),(-23.1211567,33.4943809),(-23.1192684,33.4950967),(-23.1157494,33.4956693),(-23.1130886,33.4952399),(-23.1100845,33.4943809),(-23.1072521,33.4945241),(-23.1044197,33.4956693),(-23.1022739,33.4966714),(-23.1011581,33.4981029),(-23.0999565,33.4993912)])
multilinestringdup.newlinestring(coords=[(-23.1362629,33.4940946),(-23.1372070,33.4928778),(-23.1397820,33.4918041),(-23.1425285,33.4906588),(-23.1438160,33.4887977),(-23.1434727,33.4865070),(-23.1419277,33.4847890),(-23.1367779,33.4840731),(-23.1336021,33.4856480),(-23.1317139,33.4877240),(-23.1293106,33.4897283),(-23.1266499,33.4902293),(-23.1219292,33.4916609),(-23.1195259,33.4907304),(-23.1154060,33.4896567),(-23.1114578,33.4907304),(-23.1070805,33.4923052),(-23.1033897,33.4936652),(-23.0994415,33.4965998),(-23.0986691,33.4986039),(-23.0986691,33.5011805),(-23.1011581,33.5029698)])

multipolygondup = kml.newmultigeometry(name="TestMultiPolygon")
polygon1dup = multipolygondup.newpolygon(name="TestPolygonOnlyOuter")
polygon1dup.outerboundaryis = [(-23.0895710,33.4706855),(-23.0868244,33.4729050),(-23.0818462,33.4744085),(-23.0760098,33.4738357),(-23.0727482,33.4737641),(-23.0702591,33.4745517),(-23.0689716,33.4755540),(-23.0683708,33.4769142),(-23.0689716,33.4778449),(-23.0709457,33.4772722),(-23.0737782,33.4761267),(-23.0778122,33.4772006),(-23.0790138,33.4786324),(-23.0786705,33.4804938),(-23.0774689,33.4819255),(-23.0756664,33.4823551),(-23.0742931,33.4837868),(-23.0740356,33.4856480),(-23.0724049,33.4870797),(-23.0697441,33.4884398),(-23.0687141,33.4880103),(-23.0688000,33.4871513),(-23.0714607,33.4854333),(-23.0706882,33.4832857),(-23.0691433,33.4851469),(-23.0657101,33.4849322),(-23.0639076,33.4828562),(-23.0632210,33.4807085),(-23.0631351,33.4784892),(-23.0640793,33.4761983),(-23.0651093,33.4744085),(-23.0671692,33.4720458),(-23.0712032,33.4707571),(-23.0739498,33.4701843),(-23.0764389,33.4683228),(-23.0767822,33.4663180),(-23.0761814,33.4645995),(-23.0739498,33.4629526),(-23.0709457,33.4612341),(-23.0704308,33.4593008),(-23.0710316,33.4572958),(-23.0728340,33.4566513),(-23.0755806,33.4560068),(-23.0778122,33.4557920),(-23.0811596,33.4557920),(-23.0843353,33.4557920),(-23.0881119,33.4538585),(-23.0901718,33.4522831),(-23.0922318,33.4504211),(-23.0954933,33.4503495),(-23.0985832,33.4521398),(-23.1007290,33.4550043),(-23.1036472,33.4558636),(-23.1075096,33.4570810),(-23.1108570,33.4576538),(-23.1130028,33.4590144),(-23.1141186,33.4615922),(-23.1143761,33.4643131),(-23.1085396,33.4653871),(-23.1037331,33.4678216),(-23.1018448,33.4711151),(-23.1021881,33.4731198),(-23.1040764,33.4762699),(-23.1037545,33.4773975),(-23.1026173,33.4777196),(-23.1014800,33.4775765),(-23.1007719,33.4771111),(-23.0985403,33.4760014),(-23.0971670,33.4756614),(-23.0961800,33.4753392),(-23.0914593,33.4720458),(-23.0895710,33.4706855)]

polygon2dup = multipolygondup.newpolygon(name="TestPolygonWithInner")
# outer
polygon2dup.outerboundaryis = [(-23.1465626,33.4720458),(-23.1454468,33.4739073),(-23.1457901,33.4752676),(-23.1480217,33.4779881),(-23.1473351,33.4812096),(-23.1423569,33.4823551),(-23.1374645,33.4820687),(-23.1346321,33.4826414),(-23.1316280,33.4851469),(-23.1281948,33.4873660),(-23.1245041,33.4866502),(-23.1205559,33.4845742),(-23.1206417,33.4812812),(-23.1218433,33.4776301),(-23.1249332,33.4771290),(-23.1258774,33.4756972),(-23.1254482,33.4739073),(-23.1239033,33.4731198),(-23.1209850,33.4714015),(-23.1181526,33.4716163),(-23.1160069,33.4726902),(-23.1136036,33.4758403),(-23.1112862,33.4777017),(-23.1087971,33.4777733),(-23.1060505,33.4766995),(-23.1045914,33.4750528),(-23.1034756,33.4726186),(-23.1031322,33.4710435),(-23.1037331,33.4693967),(-23.1070805,33.4675352),(-23.1100845,33.4663896),(-23.1137753,33.4657451),(-23.1207275,33.4653871),(-23.1247616,33.4640983),(-23.1266499,33.4624514),(-23.1287098,33.4604465),(-23.1337738,33.4598020),(-23.1372070,33.4599452),(-23.1396961,33.4611625),(-23.1433868,33.4640983),(-23.1451893,33.4664612),(-23.1485367,33.4683228),(-23.1465626,33.4720458)]
# inner
polygon2dup.innerboundaryis = [(-23.1359196,33.4741937),(-23.1382370,33.4729050),(-23.1374645,33.4711151),(-23.1354904,33.4698263),(-23.1334305,33.4704707),(-23.1333447,33.4723322),(-23.1342888,33.4739789),(-23.1359196,33.4741937)]

kml.save("multi_geometries_duplicate.kml")

