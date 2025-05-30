
class GeneratedResponse:

    @property
    def Value(self) -> str:
        return self.__value

    @Value.setter
    def Value(self, reponse: str) -> None:
        self.__value = reponse

    def __init__(self, reponse: str):
        self.__value = reponse
