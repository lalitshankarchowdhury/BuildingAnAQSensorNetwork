import sqlite3

conn = sqlite3.connect('db-rp1') 
c = conn.cursor()
                   
c.execute('''
          INSERT INTO bme680 (sample_nr, time, raw_temperature, raw_pressure, raw_humidity, raw_gas, status)

                VALUES
                (1,'12:58 PM',29.807947158813477,993.4461059570312,37.93738555908203,2397.1376953125,160),
                (2,'2:55 AM',50.807947158813477,80.4461059570312,32.93738555908203,2346.1376953125,180)
                
          ''')
conn.commit()


conn = sqlite3.connect('db-rp1') 
c = conn.cursor()
                   
for row in c.execute('''
          SELECT * FROM bme680
          '''):
    print(row)

conn.close()