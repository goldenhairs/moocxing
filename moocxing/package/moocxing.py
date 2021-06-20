from moocxing.robot import Constants
from moocxing.robot import Config   
from moocxing.robot.utils import serialUtils
import os
import logging

log = logging.getLogger(__name__)

version = "v0.8.0"

class MOOCXING:
    def __init__(self,config = None):
        logging.basicConfig(level=Config.get("loglevel"), format='[%(levelname).4s - %(filename)s]: %(message)s')
    
    def getAllSkill(self):
        SKILL = {}
        SKILL["media"] = self.initMedia()
        SKILL["speech"] = self.initSpeech()
        SKILL["nlp"] = self.initNLP()
        SKILL["pinyin"] = self.initPinyin()
        SKILL["mqtt"] = self.initMqtt()
        SKILL["serial"] = self.initSerial()
        SKILL["mc"] = self.initMinecraft()

        log.info("——"*25)
        log.info("初始化完成\n\n")

        return SKILL

    def initMqtt(self):
        from .MXMqtt import MXMqtt
        try:
            log.info("——"*25)
            log.info(">>> 初始化 MQTT模块")
            log.info(f">>> 服务器IP: {Config.get('mqtt/host')} 端口号: {Config.get('mqtt/post')}")
            return MXMqtt()
        except:
            log.warning("xxx 初始化 MQTT模块 失败")

    def initMinecraft(self):
        from mcpi.minecraft import Minecraft
        try:
            log.info("——"*25)
            log.info(">>> 初始化 Minecraft模块")
            log.info(f">>> 服务器IP: {Config.get('minecraft/host')} 端口号: {Config.get('minecraft/post')}")
            return Minecraft.create(Config.get('minecraft/host'), Config.get('minecraft/post'))
        except:
            log.warning("xxx 未检测到Minecraft服务器")

    def initNLP(self):
        from .MXNLP import MXNLP
        try:
            log.info("——"*25)
            log.info(">>> 初始化 自然语言分析模块")
            return MXNLP()
        except:
            log.warning("xxx 初始化 自然语言分析模块 失败")

    def initSpeech(self):
        from .MXSpeech import MXSpeech
        try:
            log.info("——"*25)
            log.info(">>> 初始化 语音识别/合成模块")
            return MXSpeech()
        except:
            log.warning("xxx 初始化 语音识别/合成模块 失败")

    def initPinyin(self):
        from .MXPinyin import MXPinyin
        try:
            log.info("——"*25)
            log.info(">>> 初始化 拼音模块")
            return MXPinyin()
        except:
            log.warning("xxx 初始化 拼音模块 失败")

    def initMedia(self):
        from .MXMedia import MXMedia
        try:
            log.info("——"*25)
            log.info(">>> 初始化 播放器模块")
            return MXMedia()
        except:
            log.warning("xxx 初始化 播放器模块 失败")

    def initSerial(self):
        from .MXSerial import MXSerial
        try:
            log.info("——"*25)
            log.info(">>> 初始化 串口通信模块")

            if Config.get('serial/com'):
                log.info(f">>> 串口号: {Config.get('serial/com')} 波特率: {Config.get('serial/bps')}")
                return MXSerial(Config.get('serial/com'), Config.get('serial/bps'))
            else:
                log.info(f">>> 串口号: {serialUtils.getCom(-1)} 波特率: {Config.get('serial/bps')}")
                return MXSerial(serialUtils.getCom(-1), Config.get('serial/bps'))
        except:
            log.warning("xxx 未检测到串口")
