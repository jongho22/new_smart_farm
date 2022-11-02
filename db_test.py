from pymongo import MongoClient
from time import sleep
import paho.mqtt.client as mqtt

my_client = MongoClient("mongodb://localhost:27017/")
db = my_client['Measurement']
#print(my_client.list_database_names())

db_col = db.data

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("클라이언트와 연결 되었습니다.")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("연결이 해제 되었습니다.")

def on_subscribe(client, userdata, mid, granted_qos):
    print("연결 상태 : " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))
    data = str(msg.payload.decode("utf-8"))

    post = {'data':data}
    db_col.insert_one(post)
    #return str(msg.payload.decode("utf-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect('broker.hivemq.com', 1883)
client.subscribe('test/send_data', 1)
client.loop_forever()
