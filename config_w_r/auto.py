# encoding=utf-8
"""
@File    :   auto.py    
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Description
------------          --------   --------    -----------
2023/5/14 0014 18:14  FuGui      1.0         python自动化运维
"""
import configparser

def read_config():
    config = configparser.ConfigParser()  # 实例化ConfigParser类
    config.read(r"TestPipConf.txt", encoding='utf-8')  # 读取配置文件

    for section in config.sections():  # 首先读取sections[部分]
        print(f"section is [{section}]")
        for key in config[section]:  # 讲到每个section的键和值
            print(f"key is [{key}], value is [{config[section][key]}]")  # 打印键和值


def write_config():
    config = configparser.ConfigParser()  # 实例化configparser类
    # 写操作时 待写入信息暂存在
    # 方法一 直接通过字典赋值写入配置文件
    config["DEFAULT"] = {
        "ServerAliveInterval": "45",
        "Compression": "yes",
        "CompressionLevel": "9",
    }
    config["Test"] = {
        "test_num": 6,  # 测试是否可以接收整型数值[可以，与正常的字典赋值无差别]
        "test_boolean": "False"
    }
    # 方法二 先对sections赋初值 初值为空字典，使用section[key]=value赋值
    config["bitbucket.org"] = {}
    config["bitbucket.org"]["User"] = "hg"
    config["bitbucket.org"]["test"] = "test_value"
    config["DEFAULT"]["ForwardX11"] = "yes"
    config["topsecret.server.com"] = {}
    config["test_blank"] = {}# 如果未写入值，只有sections
    # 方法三 使用变量接收sections指针，对变量使用 变量[key]=value
    topsecret = config["topsecret.server.com"]  # 对sections分开进行key赋值时，只能对已存在的sec赋key，不会自动创建
    topsecret["Port"] = "50022"  # mutates the parser
    topsecret["ForwardX11"] = "no"  # same here

    print(type(config["DEFAULT"].getboolean('Compression')))  # getboolean函数可以判断参数值的布尔值
    print(config["bitbucket.org"]["ServerAliveInterval"])

    with open("TestPipConf.txt", "w") as configfile:  # 将上述配置信息config写入文件example.ini
        config.write(configfile)

    with open("TestPipConf.txt", "r") as f:  # 读取example.ini 验证上述写入是否正确
        print(f.read())


if __name__ == '__main__':
    read_config()
    # write_config()

'''
configparser:配置文件解析库对配置文件的操作就是对嵌套字典的读写操作
处理形如：
[key1]
key = value
把每一个[]部分当作一个section，当作一个部分
每个部分都以类似字典格式的key：value处理，取值
[key2]
(key = value)==(value)
'''