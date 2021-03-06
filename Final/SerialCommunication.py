导入相关模块
import serial

#定义SerialCommunication类
class SerialCommunication:
    def dataProcess(self, ser,a,b):
        #进行数据处理，将原始数据转换成16进制字符串，便于与stm32通信
        a1 = str(hex(a)) 
        b1 = str(hex(b))
        data1 = a1[2:4]
        data2 = b1[2:4]
        
        #由于17以下的数字无法转换成stm32可读取的字符串，进行分类讨论并对坐标限幅
        if (a < 17 and b >= 17):
            try:
                a = 17
                a1 = str(hex(a))
                data1 = a1[2:4]
                data2 = bytes.fromhex(str(data2))
                data1 = bytes.fromhex(str(data1))
                # data1 ='0'+ data1
                ser.write(data1 + data2)
                response = ser.readall()
                print(response)
            except:
                print('data transmission failed')


        elif (a >= 17 and b < 17):

            b = 17
            b1 = str(hex(b))
            data2 = b1[2:4]
            data1 = bytes.fromhex(str(data1))
            data2 = bytes.fromhex(str(data2))
            ser.write(data1 + data2)
            response = ser.readall()
            print(response)


        elif (a < 17 and b < 17):

            try:
                a = 17
                a1 = str(hex(a))
                data1 = a1[2:4]
                b = 17
                b1 = str(hex(b))
                data2 = b1[2:4]
                data1 = bytes.fromhex(str(data1))
                data2 = bytes.fromhex(str(data2))
                ser.write(data1 + data2)
                response = ser.readall()
                print(response)
            except:
                print('data transmission failed')
        else:
            d1 = bytes.fromhex(data1)
            d2 = bytes.fromhex(data2)
            ser.write(d1 + d2)
            response = ser.readall()
            print(response)
        
