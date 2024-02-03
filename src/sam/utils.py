import time


class ConstructParams:
    def __init__(self) -> None:
        pass

    def sort(self, key):
        key = str(key).lower()

        if key == "relevance":
            return "-relevance"
        elif key == "AtoZ" or key == "1":
            return "title"
        elif key == "ZtoA" or key == "-1":
            return "-title"
        else:
            return "relevance"

    def status(self, key):
        key = str(key).lower()

        if key == "active":
            return "true"
        elif key == "inactive":
            return "false"
        else:
            return "null"

    def limit(self, key):
        if not isinstance(key, int):
            if isinstance(key, str) and key.isdigit():
                key = int(key)
            else:
                key = 9999999999
        else:
            if key < 0:
                key = 9999999999

        return key

    def time(self):
        return str(int(time.time() * 1000))
