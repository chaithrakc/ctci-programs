class StepInput:
    input_map = None

    def get_input_map(self) -> dict:
        return self.input_map

    def set_input_map(self, input_map: dict):
        self.input_map = input_map

    def get_input(self, key: str):
        return self.input_map.get(key)

    def set_input(self, key:str, input_val):
        if self.input_map is None:
            self.input_map = dict()
        self.input_map[key] = input_val
