import yaml
from actionHandler import ActionHandler
from actionType import ActionType

class Scenario:

    def setup(self):
        pass

    def run(self):
        file = open('senario.yaml','r')
        s = yaml.load(file)
        scenarios = s['scenarios']
        the_first_case = scenarios[0]
        steps = the_first_case['options']['steps']
        orderedSteps = sorted(steps,key = lambda x:x['index'])
        for step in orderedSteps:
          action = ActionHandler().createAction(step['actionType'])
          action.do()


    def teardown(self):
        pass
