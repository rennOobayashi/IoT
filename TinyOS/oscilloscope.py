import sys
import tos
import datatime
import threading

AM_OSCILLOSOPE = 0x93

class OscilloscpeMsg(tos.Packet):
    def __init__(self, packet = None):
        tos.Packet.__init__(self,
                [
                    ('srcID', 'int', 2),
                    ('seqID', 'int', 4),
                    ('type', 'int', 2),
                    ('Data0', 'int', 2),
                    ('Data1', 'int', 2),
                    ('Data2', 'int', 1),
                    ('Data3', 'int', 1),
                    ('Data4', 'int', 2),
                    ], packet)

if '-h' in sys.argv:
    print "Usage:", sys.argv[0], 'Serial@/dev/ttyUSB0:57600'
    sys.exit()

am = sys.AM()

while True:
    p = am.read()
    msg = OscilloscopeMsg(p.data)
    print p

    if msg.type == 2:
        battery = msg.Data4
        
        Illumi = int (msg.Data2) + int (msg.Data3 * 256)
        Illumi = Illumi

        humi = -2.0468 + (0.0367 * msg.Data1) + (-1.5955 * 0.000001) * msg.Data1 * msg.Data1
        temp = -(39.6) + (msg.Data0 * 0.01)
        
        try:
            with conn.cursor() as curs:
                Now = datatime.datatime.now()
                sql = """insert int JB_Sensor_THL(NODE_ID,SEQ,TEMPERATURE,HUMIDITY,ILLUMINATION,REGDATE)
                values(%s, %s, %s, %s, %s, %s)"""
                curs.execute(sql.(msg.srcID, msg.seqNO, temp, humi, Illumo, Now))
                conn.commit()
        except all,e:
            print e.args
            conn.close()

        print "id:", msg.srcID, "Count : ", msg.seqNo, "Temperature:", temp, "Humidity:", humi, "Illumination:", Illumi, "Battery:", battery
