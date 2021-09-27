import sys,time,threading
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        #rc:0.成功 1.错误的协议版本 2.无效的 client ID  3.服务器不可用  4.错误的用户名或密码  5.无法验证
        print("Failed to connect, return code %d\n", rc)

class myClient:
    def __init__(self):
        self.broker = '47.103.208.137'
        self.port = 1883
        self.topic = "Debug"
        self.client_id = f'myPython'
        self.client = mqtt.Client(self.client_id)



    def connect_mqtt(self):
        self.client.on_connect = on_connect
        self.client.connect(self.broker,self.port)

        return self.client

    def publish(self,inputTopic,inputMsg):
        msg_count = 0
        while True:
            time.sleep(1)
            msg = f"message:{msg_count}"
            result = self.client.publish(inputTopic,inputMsg)
            # result : [ 0 , 1 ]
            status = result[0]
            if status == 0:
                print(f"Send '{inputMsg}' to topic '{inputTopic}'")
            else:
                print(f"Failed to send message to topic '{inputTopic}'")
            msg_count+=1

    def subscribe(self):
