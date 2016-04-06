from attackerWrapper import  AttackerWrapper
from monitorWrapper import MonitorWrapper
from resultCheckerWrapper import ResultCheckerWraper
from actionType import ActionType
from operationWrapper import  OperationWrapper
class ActionHandler:

    # def __init__(self,actionType):
    #     if actionType == '':
    #         pass
    #     elif actionType == '':
    #         pass
    #     elif actionType == '':
    #         pass
    #     else:
    #         pass

    def createAction(self,actionType):
         if actionType == ActionType.ATTACKER:
            return AttackerWrapper()
         elif actionType == ActionType.MONITOR:
            return MonitorWrapper()
         elif actionType == ActionType.RESULTCHECKER:
            return ResultCheckerWraper()
         elif actionType == ActionType.OPERATION:
             return OperationWrapper()
         else:
            pass
