import json

class Domain:

    @classmethod
    def from_json(cls, json_str):
        return json.loads(json_str, object_hook=lambda o: cls(**o))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)