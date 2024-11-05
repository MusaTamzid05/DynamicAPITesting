import json
import random

class Processor:
    def __init__(self, data_format_path, words_path):
        with open(data_format_path, "r") as f:
            self.data_format = json.load(f)

        with open(words_path, "r") as f:
            self.words = f.read().split()




    def process(self, route):
        current_route = self.data_format[route]
        count = current_route["count"]

        if count == 1:
            return self._process(data_schema=current_route["data"])
        else:
            response = []

            for _ in range(count):
                response.append(self._process(data_schema=current_route["data"]))
            return response

    def _get_random_word(self):
        return self.words[random.randrange(0, len(self.words) - 1)]


    def _process(self, data_schema):
        data = {}

        for data_name, data_type in data_schema.items():
            value = ""

            if data_type == "word":
                value = self._get_random_word()

            elif data_type == "number":
                value = random.randrange(1, 100)

            elif data_type == "date":
                value = "6th Nov, 2024"

            elif data_type == "text":
                for _ in range(10):
                    value += self._get_random_word() + " "

            elif data_type == "image":
                value = "https://picsum.photos/200"

            elif data_type == "copy":
                src =  data_schema["src"]
                return self.process(route=src)

            data[data_name] = value

        return data








if __name__ == "__main__":
    processor = Processor(
            data_format_path="../data_format.json",
            words_path="../random.txt"
            )
    print(processor.process(route="person"))
    print("====")

    for row in processor.process(route="persons"):
        print(row)


