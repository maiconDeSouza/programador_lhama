class Alarme:
    def __init__(self, status=False) -> None:
        self.__status = status

    @property
    def now_status(self):
        return f'Seu alarme está {self.__status}'

    def change_status(self):
        self.__status = not self.__status


casa_1 = Alarme()

print(casa_1.now_status)
casa_1.change_status()
print(casa_1.now_status)
