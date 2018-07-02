from faker import Faker
import random

fake = Faker ()

options = {1: "presenceSensor",
           2: "temperatureSensor",
           3: "brightnessSensor",
           4: "atmosphericPressureSensor",
           5: "humiditySensor",
           6: "soundLevelSensor",
           7: "gpsSensor",
           8: "co2Sensor",
           9: "ledDevice",
           10: "beeperDevice",
           }

print ("{")
print ("\"devices\" : [")

for _ in range(50):
    # while True:
    # print(fake.name())

    # mac generation
    Gmac = [0x00, 0x8c, 0xfa,
            random.randint (0x00, 0xff),
            random.randint (0x00, 0xff),
            random.randint (0x00, 0xff)
            ]

    mac = ':'.join (map (lambda x: "%02x" % x, Gmac))

    # date generation
    devicefirstcoDate = fake.past_datetime ()

    deviceType = fake.randomize_nb_elements (number=10)

    if deviceType <= 10:
        print ("     {")
        print("     \"id_device\": \""+mac+"\",")
        print("     \"id_user\": \"\",")
        print ("     \"date_device\": \""+str(devicefirstcoDate)+"\",")
        print ("     \"name_device\": \""+options[deviceType]+"\",")
        print ("     \"type_device\": \""+options[deviceType]+"\",")
        print ("     \"values\" : [")
        for _ in range(random.randint(1,5)):

            if deviceType == 7:
                metricValue = "\"N;46;45;51.4;E;4;50;37.2\""

            else:
                metricValue = fake.random_int(min=0, max=100)

            metricDate = fake.past_datetime ()

            print ("        {")
            print ("            \"metrics\": "+str(metricValue)+",")
            print ("            \"date_metrics\": \""+str(metricDate)+"\",")
            print ("        },")
        print ("        ]")
        print ("     },")

print ("    ]")
print ("}")