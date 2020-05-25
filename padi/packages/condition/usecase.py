from .model import Model

class Usecase:
    def find_plant_condition(label_id):
        model_result = {}
        try:
            model_result = Model.find_by_label_id(label_id)
        except Exception as ex:
            print("Exception: {0}, Arguments: {1!r}".format(type(ex).__name__, ex.args))
        
        label, description, effect, solution = '', '' ,'', ''
        try:
            label = model_result['label_name']
            description = model_result['description']
            effect = model_result['effect']
            solution = model_result['solution']
        except Exception as ex:
            print("Exception: {0}, Arguments: {1!r}".format(type(ex).__name__, ex.args))

        result = {
            "label": label,
            "description": description,
            "effect": effect,
            "solution": solution
        }
        return result