# BuildingAnAQSensorNetwork
Code files for Undergraduate Research Program: Building an Air Quality Sensor Network under Dr. Aditya Vaishya.

## Instructions

Clone repository and run `$ source setup.sh` to setup development environment.


## Results

### SPS30
{'sample_nr': 1, 'timestamp': 4062576, 'raw_temperature': 29.807947158813477, 'raw_pressure': 993.4461059570312, 'raw_humidity': 37.93738555908203, 'raw_gas': 2397.1376953125, 'status': 160}
{'sample_nr': 2, 'timestamp': 4063781, 'raw_temperature': 29.808574676513672, 'raw_pressure': 993.4453125, 'raw_humidity': 37.896331787109375, 'raw_gas': 46.52265930175781, 'status': 176}
{'sample_nr': 3, 'timestamp': 4064986, 'raw_temperature': 29.80951499938965, 'raw_pressure': 993.4452514648438, 'raw_humidity': 37.83770751953125, 'raw_gas': 55.124794006347656, 'status': 176}
{'sample_nr': 4, 'timestamp': 4066191, 'raw_temperature': 29.810771942138672, 'raw_pressure': 993.4454956054688, 'raw_humidity': 37.749786376953125, 'raw_gas': 78.25055694580078, 'status': 176}
{'sample_nr': 5, 'timestamp': 4067395, 'raw_temperature': 29.812026977539062, 'raw_pressure': 993.4456176757812, 'raw_humidity': 37.63846206665039, 'raw_gas': 102.32131958007812, 'status': 176}
{'sample_nr': 6, 'timestamp': 4068606, 'raw_temperature': 29.8135986328125, 'raw_pressure': 993.4463500976562, 'raw_humidity': 37.55068588256836, 'raw_gas': 125.28048706054688, 'status': 176}
{'sample_nr': 7, 'timestamp': 4069811, 'raw_temperature': 29.815481185913086, 'raw_pressure': 993.4459228515625, 'raw_humidity': 37.47471618652344, 'raw_gas': 145.27320861816406, 'status': 176}

### BME680

Polling data: 
{'pm1p0': 9.40277099609375, 'pm2p5': 12.014436721801758, 'pm4p0': 13.747060775756836, 'pm10p0': 14.659709930419922, 'nc0p5': 58.250694274902344, 'nc1p0': 71.34091186523438, 'nc2p5': 73.86448669433594, 'nc4p0': 74.30712890625, 'nc10p0': 74.41680145263672, 'typical': 0.6754058599472046}
{'pm1p0': 5.255046367645264, 'pm2p5': 10.539371490478516, 'pm4p0': 14.584619522094727, 'pm10p0': 16.71546173095703, 'nc0p5': 22.73638153076172, 'nc1p0': 35.775390625, 'nc2p5': 41.28406524658203, 'nc4p0': 42.282203674316406, 'nc10p0': 42.509342193603516, 'typical': 0.7761850357055664}
{'pm1p0': 5.253097057342529, 'pm2p5': 10.306899070739746, 'pm4p0': 14.166770935058594, 'pm10p0': 16.199966430664062, 'nc0p5': 23.314720153808594, 'nc1p0': 36.00688552856445, 'nc2p5': 41.26860046386719, 'nc4p0': 42.22150802612305, 'nc10p0': 42.43864822387695, 'typical': 0.9621853232383728}
{'pm1p0': 5.131501197814941, 'pm2p5': 9.08420181274414, 'pm4p0': 12.063019752502441, 'pm10p0': 13.63211727142334, 'nc0p5': 25.301509857177734, 'nc1p0': 36.227291107177734, 'nc2p5': 40.31270217895508, 'nc4p0': 41.050376892089844, 'nc10p0': 41.21982192993164, 'typical': 0.9150159955024719}
{'pm1p0': 5.085080623626709, 'pm2p5': 8.416245460510254, 'pm4p0': 10.896869659423828, 'pm10p0': 12.203539848327637, 'nc0p5': 26.576454162597656, 'nc1p0': 36.52687072753906, 'nc2p5': 39.94764709472656, 'nc4p0': 40.563663482666016, 'nc10p0': 40.7061767578125, 'typical': 0.8210545182228088}
{'pm1p0': 5.116040229797363, 'pm2p5': 8.497868537902832, 'pm4p0': 11.018037796020508, 'pm10p0': 12.345536231994629, 'nc0p5': 26.660263061523438, 'nc1p0': 36.71672439575195, 'nc2p5': 40.190879821777344, 'nc4p0': 40.816612243652344, 'nc10p0': 40.961307525634766, 'typical': 0.8315474987030029}
{'pm1p0': 5.140224933624268, 'pm2p5': 8.457456588745117, 'pm4p0': 10.924710273742676, 'pm10p0': 12.224336624145508, 'nc0p5': 26.993175506591797, 'nc1p0': 36.97658920288086, 'nc2p5': 40.38081741333008, 'nc4p0': 40.993690490722656, 'nc10p0': 41.13557815551758, 'typical': 0.8297363519668579}
{'pm1p0': 5.130147457122803, 'pm2p5': 7.9226484298706055, 'pm4p0': 9.96816349029541, 'pm10p0': 11.045638084411621, 'nc0p5': 28.270658493041992, 'nc1p0': 37.45905303955078, 'nc2p5': 40.30131530761719, 'nc4p0': 40.81126403808594, 'nc10p0': 40.93040466308594, 'typical': 0.758557915687561}
{'pm1p0': 5.166430473327637, 'pm2p5': 7.815093040466309, 'pm4p0': 9.743467330932617, 'pm10p0': 10.759238243103027, 'nc0p5': 28.890575408935547, 'nc1p0': 37.899169921875, 'nc2p5': 40.586238861083984, 'nc4p0': 41.067684173583984, 'nc10p0': 41.180572509765625, 'typical': 0.7561582326889038}
{'pm1p0': 5.193805694580078, 'pm2p5': 7.514959812164307, 'pm4p0': 9.178790092468262, 'pm10p0': 10.055209159851074, 'nc0p5': 29.92047119140625, 'nc1p0': 38.465736389160156, 'nc2p5': 40.80107116699219, 'nc4p0': 41.21802520751953, 'nc10p0': 41.31670379638672, 'typical': 0.7038206458091736}
{'pm1p0': 5.253849983215332, 'pm2p5': 7.552952289581299, 'pm4p0': 9.19668960571289, 'pm10p0': 10.062524795532227, 'nc0p5': 30.391878128051758, 'nc1p0': 38.9627799987793, 'nc2p5': 41.27273178100586, 'nc4p0': 41.68490982055664, 'nc10p0': 41.78260803222656, 'typical': 0.7152426242828369}
{'pm1p0': 5.35544490814209, 'pm2p5': 7.722230911254883, 'pm4p0': 9.416434288024902, 'pm10p0': 10.308857917785645, 'nc0p5': 30.919950485229492, 'nc1p0': 39.69133758544922, 'nc2p5': 42.07084655761719, 'nc4p0': 42.49555206298828, 'nc10p0': 42.59614562988281, 'typical': 0.704315185546875}
{'pm1p0': 5.422866344451904, 'pm2p5': 7.828138828277588, 'pm4p0': 9.550665855407715, 'pm10p0': 10.458003044128418, 'nc0p5': 31.286901473999023, 'nc1p0': 40.18171691894531, 'nc2p5': 42.600494384765625, 'nc4p0': 43.03225326538086, 'nc10p0': 43.134490966796875, 'typical': 0.7112828493118286}
{'pm1p0': 5.478117942810059, 'pm2p5': 7.851759433746338, 'pm4p0': 9.546673774719238, 'pm10p0': 10.439462661743164, 'nc0p5': 31.749794006347656, 'nc1p0': 40.65123748779297, 'nc2p5': 43.03450393676758, 'nc4p0': 43.45964050292969, 'nc10p0': 43.56048583984375, 'typical': 0.7084083557128906}
{'pm1p0': 5.553150653839111, 'pm2p5': 8.001490592956543, 'pm4p0': 9.753559112548828, 'pm10p0': 10.676458358764648, 'nc0p5': 32.076351165771484, 'nc1p0': 41.162845611572266, 'nc2p5': 43.62396240234375, 'nc4p0': 44.06320571899414, 'nc10p0': 44.16726303100586, 'typical': 0.7153928279876709}
{'pm1p0': 5.651459693908691, 'pm2p5': 8.263278007507324, 'pm4p0': 10.143011093139648, 'pm10p0': 11.133157730102539, 'nc0p5': 32.33579635620117, 'nc1p0': 41.762916564941406, 'nc2p5': 44.39632797241211, 'nc4p0': 44.86692810058594, 'nc10p0': 44.97803497314453, 'typical': 0.7112472653388977}
{'pm1p0': 5.745640754699707, 'pm2p5': 8.541389465332031, 'pm4p0': 10.565403938293457, 'pm10p0': 11.631547927856445, 'nc0p5': 32.514217376708984, 'nc1p0': 42.308536529541016, 'nc2p5': 45.13628387451172, 'nc4p0': 45.64228439331055, 'nc10p0': 45.76133346557617, 'typical': 0.7138231992721558}
{'pm1p0': 5.8255696296691895, 'pm2p5': 8.640093803405762, 'pm4p0': 10.67607593536377, 'pm10p0': 11.748526573181152, 'nc0p5': 33.0181770324707, 'nc1p0': 42.918636322021484, 'nc2p5': 45.76416778564453, 'nc4p0': 46.273258209228516, 'nc10p0': 46.393089294433594, 'typical': 0.7086270451545715}
{'pm1p0': 5.897562026977539, 'pm2p5': 8.736835479736328, 'pm4p0': 10.789905548095703, 'pm10p0': 11.87136459350586, 'nc0p5': 33.45198059082031, 'nc1p0': 43.45977783203125, 'nc2p5': 46.32971954345703, 'nc4p0': 46.843135833740234, 'nc10p0': 46.96400833129883, 'typical': 0.7069190144538879}
{'pm1p0': 5.935412406921387, 'pm2p5': 8.664170265197754, 'pm4p0': 10.626851081848145, 'pm10p0': 11.660688400268555, 'nc0p5': 33.997169494628906, 'nc1p0': 43.87656021118164, 'nc2p5': 46.626976013183594, 'nc4p0': 47.1184196472168, 'nc10p0': 47.2344856262207, 'typical': 0.6940212845802307}
{'pm1p0': 5.982722759246826, 'pm2p5': 8.707806587219238, 'pm4p0': 10.665678024291992, 'pm10p0': 11.696985244750977, 'nc0p5': 34.33342742919922, 'nc1p0': 44.25352096557617, 'nc2p5': 46.99861526489258, 'nc4p0': 47.488983154296875, 'nc10p0': 47.60487747192383, 'typical': 0.6972951889038086}
{'pm1p0': 5.989965438842773, 'pm2p5': 8.566629409790039, 'pm4p0': 10.404818534851074, 'pm10p0': 11.373083114624023, 'nc0p5': 34.76448440551758, 'nc1p0': 44.46957015991211, 'nc2p5': 47.05541229248047, 'nc4p0': 47.51659393310547, 'nc10p0': 47.62604904174805, 'typical': 0.682867705821991}
{'pm1p0': 6.025304794311523, 'pm2p5': 8.502777099609375, 'pm4p0': 10.259781837463379, 'pm10p0': 11.185280799865723, 'nc0p5': 35.26326370239258, 'nc1p0': 44.85443115234375, 'nc2p5': 47.33295822143555, 'nc4p0': 47.77440643310547, 'nc10p0': 47.87954330444336, 'typical': 0.6885342597961426}