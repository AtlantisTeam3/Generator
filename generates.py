from faker import Faker
import random

fake = Faker()



for _ in range(10):
# while True:
    # print(fake.name())


    #mac generation
    Gmac = [0x00, 0x8c, 0xfa,
            random.randint (0x00, 0xff),
            random.randint (0x00, 0xff),
            random.randint (0x00, 0xff)
            ]

    mac = ':'.join(map(lambda x:"%02x" %x,Gmac))

    # date generation

    metricDate = fake.past_datetime()

    deviceType = fake.randomize_nb_elements(number=10)

    if deviceType==7:
        metricValue = "N;45;45;51.4;E;4;50;37.2"
    else:
        metricValue = fake.random_number()




    if deviceType<=10:
        print ("----------------------------------------")
        print(mac)
        print (metricDate)
        print (deviceType)
        print (metricValue)
