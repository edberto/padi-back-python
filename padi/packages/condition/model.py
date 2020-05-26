from padi import padi_db
import collections

class Model:
    def find_by_label_id(label_id):
        col = padi_db['plant_conditions']
        result = {}     
        try:
            filter = {
                "label_id": label_id
            }
            result = col.find_one(filter=filter)
        except Exception as ex:
            print("Exception: {0}, Arguments: {1!r}".format(type(ex).__name__, ex.args))
            pass
        return result
        