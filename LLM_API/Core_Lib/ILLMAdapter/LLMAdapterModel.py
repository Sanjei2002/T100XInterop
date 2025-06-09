
class GeneratedResponse:

    @property
    def Value(self) -> str:
        return self.__value

    @Value.setter
    def Value(self, reponse: str) -> None:
        self.__value = reponse

    def __init__(self, response: str):
        self.__value = response
