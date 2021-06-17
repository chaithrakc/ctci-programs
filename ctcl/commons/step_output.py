class StepOutput:
    output_map = None

    def set_output_map(self, output_map: dict):
        self.output_map = output_map

    def get_output_map(self) -> dict:
        return self.output_map

    def get_output(self, key: str):
        return self.output_map.get(key)

    def set_output(self, key: str, output_val):
        if self.output_map is None:
            self.output_map = dict()
        self.output_map[key] = output_val
