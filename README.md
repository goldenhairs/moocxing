# MOOCXING v0.7.6 使用文档


### 描述

当前最新版本0.7.6  [github链接](https://github.com/Aanzhi/moocxing )  [最新文档](http://sliot.top:7505/)

[python](https://www.python.org/)版本需>=3.8，不兼容<=3.7

**(推荐) [moocxing工具包](http://sliot.top:7505/tools.html)，收集了所需的python安装包，pyaudio离线版，moocxing离线版，wget，ffmpeg。**



### 1. 安装与配置

因为python>=3.8，会出现pyaudio安装失败的提示，所以需要手动下载与**python版本对应的pyaudio的函数库**进行安装。

[pyaudio下载链接](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

**安装pyaudio离线版**

```shell
$ pip3 install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl
```

**安装moocxing**

```shell
# 安装在线版本
$ pip3 install moocxing
# 安装离线版本
$ pip3 install moocxing-0.7.6-py3-none-any.whl
```



**配置wget和ffmpeg到环境变量**

window 需手动下载[wget](https://eternallybored.org/misc/wget/)和[ffmpeg](https://www.gyan.dev/ffmpeg/builds/)，并配置环境变量。

macOS  只需安装wget。

```shell
$ brew install wget
```



**测试代码**

```python
from moocxing.package import MOOCXING
```

**运行成功**

```python
*************************************************
*    M O O C X I N G 人 工 智 能 学 习 专 用 库    *
*             (c) 2020 anzhi v0.7.6             *
*       https://github.com/Aanzhi/moocxing      *
*************************************************
```



###  2. 初始化模块

**配置文件**

配置文件分为`default.yaml`(默认配置)和`config.yaml`(用户配置)，`config.yaml`文件会在主程序根目录下自动生成。

配置文件读取顺序 **`config.yaml` > `default.yaml`**， `config.yaml`中的参数将会覆盖`default.yaml`。

**当前可配置的全部参数如下：**

`default.yaml`以下内容为自动生成的默认配置。

```python
# 日志等级
loglevel: 20

# 我的世界服务器
minecraft:
  host: localhost
  post: 4711

# mqtt服务器
mqtt:
  host: mqtt.16302.com
  post: 1883
```

`config.yaml`以下内容为用户自定义，可覆盖默认配置。

其中`loglevel`参数将覆盖`default.yaml`中的`loglevel`参数。

```python
# 日志等级
loglevel: 30

# 百度api
baidu:
  APP_ID: 'xxxx'
  API_KEY: 'xxxxxxxxxxxx'
  SECRET_KEY: 'xxxxxxxxxxxx'

# 和风天气api
heweather:
  city: "上海"
  key: "xxxxxxxxxxxx"

# 网易云api
netease:
  baseUrl: "http://xxx.xxx.xxx"
```



**初始化全部模块。**所有参数通过配置文件来配置，无需在初始化时设置参数。

```python
from moocxing.package import MOOCXING

mx = MOOCXING()

media = mx.initMedia()
speech = mx.initSpeech()
nlp = mx.initNLP()
mqtt = mx.initMqtt()
serial = mx.initSerial()
pinyin = mx.initPinyin()
mc = mx.initMinecraft()
```

**初始化成功**

```python
[INFO][moocxing.py]: ===================================
[INFO][moocxing.py]: >>> 正在初始化 Minecraft模块
```

**初始化失败**

```python
[INFO][moocxing.py]: ===================================
[INFO][moocxing.py]: >>> 正在初始化 Minecraft模块
[WARNING][moocxing.py]: xxx 未检测到Minecraft服务器
```



### 3. 模块介绍<span id = "model"> </span>

moocxing目前有七个功能模块。[Media](#media)  [Speech](#speech)  [NLP](#nlp)  [Mqtt](#mqtt)  [Serial](#serial)  [Pinyin](#pinyin)  [Minecraft](#minecraft)

<span id = "media">**Media -- 媒体模块**</span>  [返回](#model)

```python
# 录音
# RS: 录音时长(int), 默认: 4
# path: 录音文件保存路径(str), 默认: "back.wav"
record(RS=4,path="back.wav")

# 播放
# path: 播放文件路径(str), 默认: "back.wav"
play(path="back.wav")

# 多线程播放
# path: 播放文件路径(str), 默认: "back.wav"
playThread(path="back.wav")

# 暂停
stop()

# 停止
pause()

# 继续
unpause()
```



<span id = "speech">**Speech -- 语音识别+语音合成模块**</span>  [返回](#model)

```python
# 语音转文本
# fname: 识别文件的路径(str), 默认: "back.wav"
# _print: 是否打印识别出的文本(bool), 默认: False
# 返回值: 识别出的文本(str)
STT(fname="back.wav", _print=False)

# 文本转语音
# text: 需要转换的文本(str)
TTS(text)
```



<span id = "nlp">**NLP -- NLP模块**</span>  [返回](#model)

```python
# 获取词法分析的结果
# text: 需要分析的文本(str)
# 返回值: 词法分析的结果(list)
getInfo(text)

# 获取城市名称
# text: 需要分析的文本(str)
# 返回值: 城市名称(str)
getCity(text)

# 获取歌曲名称
# text: 需要分析的文本(str)
# 返回值: 歌曲名称(str)
getMusicName(text)
```



<span id = "mqtt">**Mqtt -- MQTT模块**</span>  [返回](#model)

```python
# 发送消息
# topic: 发送的频道(str)
# payload: 发送的内容(str)
# qos: 服务质量(0:只发一次, 1:最少收到一次, 2:只收到一次), 默认: 1
PUB(topic, payload, qos=1)

# 订阅频道
# topic: 订阅的频道(str)
# qos: 服务质量(0:只发一次, 1:最少收到一次, 2:只收到一次), 默认: 1
SUB(topic, qos=1)

# 获取返回的消息
# 返回值: 接收到的消息(tuple) 
returnMsg()
```



<span id = "serial">**Serial -- 串口模块**</span>  [返回](#model)

```python
# 获取串口列表(无需实例化)
# num: 	 None, 默认: None
#        下标(int)
# 返回值: 串口列表, 默认: 返回列表(list)
#				 单独串口(str)
getCom(num=None)

# 发送
# data: 需要发送的数据(str)
send(data)  

# 读取一行
# 返回值: 读取到的数据(str)
readline()

# 读取数据
# 返回值: 读取单个字符(str)
read()

# 关闭串口
close()
```



<span id = "pinyin">**Pinyin -- 拼音模块**</span>  [返回](#model)

```python
# 获取文本的拼音
# text: 需要转换的文本(str)
# cut: 分割符(str), 默认: ""
# 返回值: 文本的拼音(str)
getPinyin(text, cut="")
```



<span id = "minecraft">**Minecraft -- 我的世界模块**</span>  [返回](#model)

所有函数用法与mcpi函数库***用法一致***，且***无需再调用***mcpi中`create`函数来进行初始化我的世界模块。



### 4. 技能插件

技能插件当前集成了查日期、时间、星期，查天气，听音乐，传话，闲聊功能。

**触发关键词** 

```
	时间插件 -- 日期、时间、星期、几号、日子
​	天气插件 -- 天气
​	音乐插件 -- 播放、听、首、歌
​	播放插件 -- 暂停、继续、停止
​	传话插件 -- 传话
​	闲聊插件 -- <开启后自动匹配>
```

**(推荐使用) -- moocxing提供了`getAllSkill()`方法用于获取全部模块初始化的字典，避免了每个模块都需要单独初始化的麻烦。**需要调用技能时请使用此方法初始化实例。

```python
from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain

###===================================###
SKILL = MOOCXING().getAllSkill()
brain = Brain(SKILL)
###===================================###

order = input("请输入关键词")
brain.query(order)
```

**(不推荐使用)** -- 单个模块初始化方法

```python
from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain

###===================================###
mx = MOOCXING()

media = mx.initMedia()
speech = mx.initSpeech()
nlp = mx.initNLP()
mqtt = mx.initMqtt()
serial = mx.initSerial()
pinyin = mx.initPinyin()
mc = mx.initMinecraft()

SKILL = {
  "media": media, "speech": speech, "nlp": nlp, "mqtt": mqtt, "serial": serial, "pinyin": pinyin, "mc": mc
}
brain = Brain(SKILL)
###===================================###

order = input("请输入关键词")
brain.query(order)
```



### 5. 示例代码

**语音对话** -- [Media](#media)  [Speech](#speech)

```python
from moocxing.package import MOOCXING

mx = MOOCXING()

media = mx.initMedia()
speech = mx.initSpeech()

def recordSTT():
    media.record()
    return speech.STT(_print=True)

def TTSPlay(text):
    speech.TTS(text)
    media.play()
    
result = recordSTT()
if "你好" in result:
    TTSPlay("你好呀，很高兴认识你。")
```

**语音调用技能** -- [Media](#media)  [Speech](#speech)

```python
from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain

SKILL = MOOCXING().getAllSkill()
brain = Brain(SKILL)

def recordSTT():
    SKILL["media"].record()
    return SKILL["speech"].STT(_print=True)

result = recordSTT()
brain.query(result)
```

**mqtt发布消息** -- [Mqtt](#mqtt) 

```python
from moocxing.package import MOOCXING
import time

mx = MOOCXING()
mqtt = mx.initMqtt()

while True:
    time.sleep(1)
    mqtt.PUB("mooc_test", "hello world!")
```

**mqtt订阅消息** -- [Mqtt](#mqtt)

```python
from moocxing.package import MOOCXING

mx = MOOCXING()
mqtt = mx.initMqtt()

mqtt.SUB("mooc_test")
while True:
    if (msg := mqtt.returnMsg()) != ("",""):
        print(msg)
```

**NLP词法分析** -- [NLP](#nlp)

```python
from moocxing.package import MOOCXING
import time

mx = MOOCXING()
nlp = mx.initNLP()

# 并发数量为2，注意请求间隔
print(nlp.getCity("我在上海"))
time.sleep(0.5)
print(nlp.getMusicName("播放海阔天空"))
time.sleep(0.5)
print(nlp.getInfo("上海慕客信信息科技有限公司"))
```

**获取拼音** -- [Pinyin](#pinyin)

```python
from moocxing.package import MOOCXING

mx = MOOCXING()
pinyin = mx.initPinyin()

p1 = pinyin.getPinyin("上海慕客信信息科技有限公司")
p2 = pinyin.getPinyin("上海慕客信信息科技有限公司", cut="-")
print(p1)
print(p2)
```

**串口查看** -- [Serial](#serial)

```python
from moocxing.package import MOOCXING

mx = MOOCXING()
# 默认选择最后一个串口
serial = mx.initSerial()

print(serial.getCom())
serial.close()
```

**串口发送** -- [Serial](#serial)

```python
from moocxing.package import MOOCXING

mx = MOOCXING()
# 默认选择最后一个串口
serial = mx.initSerial()

serial.send("moocxing")
serial.close()
```

**串口接收** -- [Serial](#serial)

```python
from moocxing.package import MOOCXING

mx = MOOCXING()
# 默认选择最后一个串口
serial = mx.initSerial()

print(serial.readline())
serial.close()
```



## 常见问题

1. pyaudio

   因为python>=3.8，会出现pyaudio安装失败的提示，所以需要手动下载与**python版本对应的pyaudio的函数库**进行安装。

   [pyaudio下载链接](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

   ```shell
   $ pip3 install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl
   ```

2. python版本需>=3.8，使用了3.8的语法，不兼容<=3.7





