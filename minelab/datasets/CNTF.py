# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 14:11
# @Author  : buf
# @Email   : niuxinzan@cennavi.com.cn
# @File    : CNTF.py
# @Software: PyCharm
class Cntf(object):
    def __init__(self,line):
        lineArr = str(line).split(",")
        self.__UNIQUEID=lineArr[0]
        self.__trafficIDType = lineArr[1]
        self.__directionFlag = lineArr[2]
        self.__regionType = lineArr[3]
        self.__objectID_type = lineArr[4]
        self.__regionID = lineArr[5]
        self.__objectID = lineArr[6]
        self.__roadLength = lineArr[7]
        self.__roadClass = lineArr[8]
        self.__linkType = lineArr[9]
        self.__timeStamp = lineArr[10]
        self.__locationFlag = lineArr[11]
        self.__flowFlag = lineArr[12]
        self.__trafficFlag = lineArr[13]
        self.__incidentFlag = lineArr[14]
        self.__fillFlag = lineArr[15]
        self.__hfillFlag = lineArr[16]
        self.__tfillFlag = lineArr[17]
        self.__lfillFlag = lineArr[18]
        self.__dfillFlag = lineArr[19]
        self.__precidentFlag = lineArr[20]
        self.__sprecidentFlag = lineArr[21]
        self.__mprecidentFlag = lineArr[22]
        self.__lprecidentFlag = lineArr[23]
        self.__status = lineArr[24]
        self.__travelTime = lineArr[25]
        self.__watingTime = lineArr[26]
        self.__linkCarCnt = lineArr[27]
        self.__linkSeqID = lineArr[28]
    @property
    def UNIQUEID(self):
        return  self.__UNIQUEID
    @UNIQUEID.setter
    def UNIQUEID(self,UNIQUEID):
        self.__UNIQUEID=UNIQUEID
    @property
    def trafficIDType(self):
        return  self.__trafficIDType
    @trafficIDType.setter
    def trafficIDType(self,trafficIDType):
        self.__trafficIDType=trafficIDType
    @property
    def directionFlag(self):
        return  self.__directionFlag
    @directionFlag.setter
    def directionFlag(self,directionFlag):
        self.__directionFlag=directionFlag
    @property
    def regionType(self):
        return  self.__regionType
    @regionType.setter
    def regionType(self,regionType):
        self.__regionType=regionType
    @property
    def objectID_type(self):
        return  self.__objectID_type
    @objectID_type.setter
    def objectID_type(self,objectID_type):
        self.__objectID_type=objectID_type
    @property
    def regionID(self):
        return  self.__regionID
    @regionID.setter
    def regionID(self,regionID):
        self.__regionID=regionID
    @property
    def objectID(self):
        return  self.__objectID
    @objectID.setter
    def objectID(self,objectID):
        self.__objectID=objectID
    @property
    def roadLength(self):
        return  self.__roadLength
    @roadLength.setter
    def roadLength(self,roadLength):
        self.__roadLength=roadLength
    @property
    def roadClass(self):
        return  self.__roadClass
    @roadClass.setter
    def roadClass(self,roadClass):
        self.__roadClass=roadClass
    @property
    def linkType(self):
        return  self.__linkType
    @linkType.setter
    def linkType(self,linkType):
        self.__linkType=linkType
    @property
    def timeStamp(self):
        return  self.__timeStamp
    @timeStamp.setter
    def timeStamp(self,timeStamp):
        self.__timeStamp=timeStamp
    @property
    def locationFlag(self):
        return  self.__locationFlag
    @locationFlag.setter
    def locationFlag(self,locationFlag):
        self.__locationFlag=locationFlag
    @property
    def flowFlag(self):
        return  self.__flowFlag
    @flowFlag.setter
    def flowFlag(self,flowFlag):
        self.__flowFlag=flowFlag
    @property
    def trafficFlag(self):
        return  self.__trafficFlag
    @trafficFlag.setter
    def trafficFlag(self,trafficFlag):
        self.__trafficFlag=trafficFlag
    @property
    def incidentFlag(self):
        return  self.__incidentFlag
    @incidentFlag.setter
    def incidentFlag(self,incidentFlag):
        self.__incidentFlag=incidentFlag
    @property
    def fillFlag(self):
        return  self.__fillFlag
    @fillFlag.setter
    def fillFlag(self,fillFlag):
        self.__fillFlag=fillFlag
    @property
    def hfillFlag(self):
        return  self.__hfillFlag
    @hfillFlag.setter
    def hfillFlag(self,hfillFlag):
        self.__hfillFlag=hfillFlag
    @property
    def tfillFlag(self):
        return  self.__tfillFlag
    @tfillFlag.setter
    def tfillFlag(self,tfillFlag):
        self.__tfillFlag=tfillFlag
    @property
    def lfillFlag(self):
        return  self.__lfillFlag
    @lfillFlag.setter
    def lfillFlag(self,lfillFlag):
        self.__lfillFlag=lfillFlag
    @property
    def dfillFlag(self):
        return  self.__dfillFlag
    @dfillFlag.setter
    def dfillFlag(self,dfillFlag):
        self.__dfillFlag=dfillFlag
    @property
    def precidentFlag(self):
        return  self.__precidentFlag
    @precidentFlag.setter
    def precidentFlag(self,precidentFlag):
        self.__precidentFlag=precidentFlag
    @property
    def sprecidentFlag(self):
        return  self.__sprecidentFlag
    @sprecidentFlag.setter
    def sprecidentFlag(self,sprecidentFlag):
        self.__sprecidentFlag=sprecidentFlag
    @property
    def mprecidentFlag(self):
        return  self.__mprecidentFlag
    @mprecidentFlag.setter
    def mprecidentFlag(self,mprecidentFlag):
        self.__mprecidentFlag=mprecidentFlag
    @property
    def lprecidentFlag(self):
        return  self.__lprecidentFlag
    @lprecidentFlag.setter
    def lprecidentFlag(self,lprecidentFlag):
        self.__lprecidentFlag=lprecidentFlag
    @property
    def status(self):
        return  self.__status
    @status.setter
    def status(self,status):
        self.__status=status
    @property
    def travelTime(self):
        return  self.__travelTime
    @travelTime.setter
    def travelTime(self,travelTime):
        self.__travelTime=travelTime
    @property
    def watingTime(self):
        return  self.__watingTime
    @watingTime.setter
    def watingTime(self,watingTime):
        self.__watingTime=watingTime
    @property
    def linkCarCnt(self):
        return  self.__linkCarCnt
    @linkCarCnt.setter
    def linkCarCnt(self,linkCarCnt):
        self.__linkCarCnt=linkCarCnt
    @property
    def linkSeqID(self):
        return  self.__linkSeqID
    @linkSeqID.setter
    def linkSeqID(self,linkSeqID):
        self.__linkSeqID=linkSeqID

    def __str__(self) -> str:
        return self.objectID+","+self.status+","+self.travelTime

