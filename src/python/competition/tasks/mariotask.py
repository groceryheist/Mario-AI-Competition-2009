__author__="Sergey Karakovskiy, sergey at idsia fullstop ch"
__date__ ="$May 7, 2009 12:47:18 PM$"

from client.marioenvironment import MarioEnvironment
from episodictask import EpisodicTask

if __name__ != "__main__":
    print "Loading %s ..." % __name__;

class MarioTask(EpisodicTask):
#    def __init__(self):
#        """Encapsulates Mario specific options and transfers them to EpisodicTask"""
#        EpisodicTask(MarioEnvironment())
#        EpisodicTask.reset(self)
#        pass
#
    finished = False
    reward = 0
    status = 0

    def isFinished(self):
        return self.finished

    def getObservation(self):
        """Documentation"""
        obs = EpisodicTask.getObservation(self)
        if len(obs) == 2:
            self.reward = obs[1]
            self.status = obs[0]
            self.finished = True
        return obs

    def startNew(self):
        self.finished = False
        
    def getReward(self):
        """ compute and return the current reward (i.e. corresponding to the last action performed) """
        return self.reward
    def getStatus(self):
        return self.status
