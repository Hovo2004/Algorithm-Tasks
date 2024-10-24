class CustomDict:
    def __init__(self):
        self.keys = []
        self.values = []

    def set_item(self, key, value):
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get_item(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            raise KeyError(f"Key '{key}' not found.")

    def add_to_array(self, key, value):
        if key in self.keys:
            index = self.keys.index(key)
            if isinstance(self.values[index], list):
                self.values[index].append(value)
            else:
                raise ValueError(f"Value at key '{key}' is not a list.")
        else:
            self.keys.append(key)
            self.values.append([value])

    def merge_arrays(self, key1, key2):
        if key1 in self.keys and key2 in self.keys:
            index1 = self.keys.index(key1)
            index2 = self.keys.index(key2)

            if isinstance(self.values[index1], list) and isinstance(self.values[index2], list):
                return self.values[index1] + self.values[index2]
            else:
                raise ValueError("Both values must be lists to merge.")
        else:
            raise KeyError("One or both keys not found.")


my_dict = CustomDict()

my_dict.set_item('fruits', ['apple'])
my_dict.add_to_array('fruits', 'banana')

my_dict.set_item('vegetables', ['carrot'])
my_dict.add_to_array('vegetables', 'broccoli')

merged_list = my_dict.merge_arrays('fruits', 'vegetables')

print(merged_list)
