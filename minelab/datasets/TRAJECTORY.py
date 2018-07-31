# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 14:12
# @Author  : buf
# @Email   : niuxinzan@cennavi.com.cn
# @File    : TRAJECTORY.py
# @Software: PyCharm
class Trajectory:
    def __init__(self,line):
        lineArr=str(line).split(",")
        self.__rowkey = lineArr[0]
        self.__datasource = lineArr[1]
        self.__carID = lineArr[2]
        self.__carType = int(lineArr[3])
        self.__linkSequence = lineArr[4]
        self.__gridSequence = lineArr[5]
        self.__meshSequence = lineArr[6]
        self.__citySequence = lineArr[7]
        self.__enterTimeSequence = lineArr[8]
        self.__speedSequence = lineArr[9]
        self.__travelLengthSequence = lineArr[10]
        self.__linkNo = int(lineArr[11])
        self.__status = int(lineArr[12])
        self.__event = int(lineArr[13])
        self.__travelDistance = int(lineArr[14])
        self.__travelTime = int(lineArr[15])
        self.__averageSpeed = int(lineArr[16])
        self.__oLinkID = int(lineArr[17])
        self.__dLinkID = int(lineArr[18])
        self.__splitConfidence = float(lineArr[19])
        self.__integrityConfidence = float(lineArr[20])
        self.__confidence = float(lineArr[21])
        self.__oLongitude = float(lineArr[22])
        self.__oLatitude =float(lineArr[23])
        self.__dLongitude = float(lineArr[24])
        self.__dLatitude = float(lineArr[25])
        self.__oTime = int(lineArr[26])
        self.__dTime = int(lineArr[27])
        self.__orgGPSSequence = lineArr[28]
        self.__prejSequence = lineArr[29]

    @property
    def rowkey(self):
        return self.__rowkey
    @rowkey.setter
    def rowkey(self, rowkey):
        self.__rowkey = rowkey
    @property
    def datasource(self):
        return self.__datasource
    @datasource.setter
    def datasource(self, datasource):
        self.__datasource = datasource
    @property
    def carID(self):
        return self.__carID
    @carID.setter
    def carID(self, carID):
        self.__carID = carID
    @property
    def carType(self):
        return self.__carType
    @carType.setter
    def carType(self, carType):
        self.__carType = carType
    @property
    def linkSequence(self):
        return self.__linkSequence
    @linkSequence.setter
    def linkSequence(self, linkSequence):
        self.__linkSequence = linkSequence
    @property
    def gridSequence(self):
        return self.__gridSequence
    @gridSequence.setter
    def gridSequence(self, gridSequence):
        self.__gridSequence = gridSequence
    @property
    def meshSequence(self):
        return self.__meshSequence
    @meshSequence.setter
    def meshSequence(self, meshSequence):
        self.__meshSequence = meshSequence
    @property
    def citySequence(self):
        return self.__citySequence
    @citySequence.setter
    def citySequence(self, citySequence):
        self.__citySequence = citySequence
    @property
    def enterTimeSequence(self):
        return self.__enterTimeSequence
    @enterTimeSequence.setter
    def enterTimeSequence(self, enterTimeSequence):
        self.__enterTimeSequence = enterTimeSequence
    @property
    def speedSequence(self):
        return self.__speedSequence
    @speedSequence.setter
    def speedSequence(self, speedSequence):
        self.__speedSequence = speedSequence
    @property
    def travelLengthSequence(self):
        return self.__travelLengthSequence
    @travelLengthSequence.setter
    def travelLengthSequence(self, travelLengthSequence):
        self.__travelLengthSequence = travelLengthSequence
    @property
    def linkNo(self):
        return self.__linkNo
    @linkNo.setter
    def linkNo(self, linkNo):
        self.__linkNo = linkNo
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status
    @property
    def event(self):
        return self.__event
    @event.setter
    def event(self, event):
        self.__event = event
    @property
    def travelDistance(self):
        return self.__travelDistance
    @travelDistance.setter
    def travelDistance(self, travelDistance):
        self.__travelDistance = travelDistance
    @property
    def travelTime(self):
        return self.__travelTime
    @travelTime.setter
    def travelTime(self, travelTime):
        self.__travelTime = travelTime
    @property
    def averageSpeed(self):
        return self.__averageSpeed
    @averageSpeed.setter
    def averageSpeed(self, averageSpeed):
        self.__averageSpeed = averageSpeed
    @property
    def oLinkID(self):
        return self.__oLinkID
    @oLinkID.setter
    def oLinkID(self, oLinkID):
        self.__oLinkID = oLinkID
    @property
    def dLinkID(self):
        return self.__dLinkID
    @dLinkID.setter
    def dLinkID(self, dLinkID):
        self.__dLinkID = dLinkID
    @property
    def splitConfidence(self):
        return self.__splitConfidence
    @splitConfidence.setter
    def splitConfidence(self, splitConfidence):
        self.__splitConfidence = splitConfidence
    @property
    def integrityConfidence(self):
        return self.__integrityConfidence
    @integrityConfidence.setter
    def integrityConfidence(self, integrityConfidence):
        self.__integrityConfidence = integrityConfidence
    @property
    def confidence(self):
        return self.__confidence
    @confidence.setter
    def confidence(self, confidence):
        self.__confidence = confidence
    @property
    def oLongitude(self):
        return self.__oLongitude
    @oLongitude.setter
    def oLongitude(self, oLongitude):
        self.__oLongitude = oLongitude
    @property
    def oLatitude(self):
        return self.__oLatitude
    @oLatitude.setter
    def oLatitude(self, oLatitude):
        self.__oLatitude = oLatitude
    @property
    def dLongitude(self):
        return self.__dLongitude
    @dLongitude.setter
    def dLongitude(self, dLongitude):
        self.__dLongitude = dLongitude
    @property
    def dLatitude(self):
        return self.__dLatitude
    @dLatitude.setter
    def dLatitude(self, dLatitude):
        self.__dLatitude = dLatitude
    @property
    def oTime(self):
        return self.__oTime
    @oTime.setter
    def oTime(self, oTime):
        self.__oTime = oTime
    @property
    def dTime(self):
        return self.__dTime
    @dTime.setter
    def dTime(self, dTime):
        self.__dTime = dTime
    @property
    def orgGPSSequence(self):
        return self.__orgGPSSequence
    @orgGPSSequence.setter
    def orgGPSSequence(self, orgGPSSequence):
        self.__orgGPSSequence = orgGPSSequence
    @property
    def prejSequence(self):
        return self.__prejSequence
    @prejSequence.setter
    def prejSequence(self, prejSequence):
        self.__prejSequence = prejSequence
    def __str__(self):
        return str(self.carID)+","+str(self.travelDistance)+","+str(self.averageSpeed)

