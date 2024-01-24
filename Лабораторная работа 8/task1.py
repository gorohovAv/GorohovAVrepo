class SunkKey:
    """
       Класс описывающий шпонку
       :param lenght: длина шпонки
       :param width: ширина шпонки
       :param shaft: диаметр вала на котором устанавливается шпонка
       :param lug: высота выступа шпонки для зацепления
       :param max_shear_stress: Максимальное напряжение среза, обычно берется 130 МПа
       :param max_bearing_stress: максимальное напряжение смятия, обычно берется 80 МПа
    """
    def __init__(self, lenght: float, width: float, shaft: int, lug: float, max_shear_stress = 130, max_bearing_stress = 80):
        """
            Инициализация класса
        """
        if not isinstance(lenght, float):
            raise TypeError("Длина шпонки должна быть числом")
        if lenght < 0:
            raise ValueError("Необходимо положительное значение")
        self.lenght = lenght
        if not isinstance(width, float):
            raise TypeError("Ширина шпонки должна быть числом")
        if lenght < 0:
            raise ValueError("Необходимо положительное значение")
        self.width = width
        if not isinstance(shaft, int):
            raise TypeError("Диаметр вала должна быть натуральным числом")
        if lenght < 0:
            raise ValueError("Необходимо положительное значение")
        self.shaft = shaft
        if not isinstance(lug, float):
            raise TypeError("Выступ шпонки должен быть числом")
        if lenght < 0:
            raise ValueError("Необходимо положительное значение")
        self.lug = lug
        if not isinstance(lug, float):
            raise TypeError("Максимальное напряжение среза определяется материалом должно быть числом")
        if lenght < 0:
            raise ValueError("Необходимо положительное значение")
        self.max_shear_stress = max_shear_stress
        if not isinstance(lug, float):
            raise TypeError("Максимальное напряжение смятия определяется материалом должно быть числом")
        if lenght < 0:
            raise ValueError("Необходимо положительное значение")
        self.max_bearing_stress = max_bearing_stress

    def get_max_torque(self):
        """
        Возвращает максимальный момент в кН/м
        """
        bearing_torque = 0.5 * self.shaft * self.lug * self.lenght * self.max_shear_stress / 1000
        shear_torque = 0.5 * (self.shaft + self.lug) * self.width * self.lenght * self.max_bearing_stress / 1000
        if bearing_torque < shear_torque:
            return bearing_torque
        else:
            return shear_torque

    def optimize_shaft(self, delta_diam):
        """
        Метод оптимизирует машину путем уменьшения диаметра вала, после чего вызывает get_max_torque()
        :param delta_diam: разница диаметров оптимизированного и не оптимизированного валов
        Для увеличения вала можно задать отрицательный параметр
        """
        if not isinstance(delta_diam, int):
            raise TypeError("Разница должна быть натуральным числом")
        self.shaft -= delta_diam
        return self.get_max_torque()


    def __str__(self):
        """
                Метод возвращает строку с параметрами объекта
        """
        return f'''Шпонка длинной {self.lenght} мм, шириной {self.width} мм, выступом {self.lug}
        на валу диаметром {self.shaft}. Максимальные напряжение среза и смятия соответственно: {self.max_shear_stress}, {self.max_bearing_stress}'''

    def __repr__(self):
        """
                Метод возвращает строку с кодом созданием объекта
        """
        return f"{self.__class__.__name__}(lenght={self.lenght}, width={self.width}, shaft={self.shaft}, lug={self.lug}, max_shear_stress={self.max_shear_stress}, max_bearing_stress={self.max_bearing_stress})"

class CillindricalKey(SunkKey):
    """
       Класс описывающий циллиндрическую шпонку

       :param lenght: длина шпонки
       :param width: ширина шпонки
       :param shaft: диаметр вала на котором устанавливается шпонка
       :param key_diam: диаметр циллиндрической шпонки
       :param max_shear_stress: Максимальное напряжение среза, обычно берется 130 МПа
       :param max_bearing_stress: максимальное напряжение смятия, обычно берется 80 МПа

    """
    def __init__(self, lenght: float, width: float, shaft: float, key_diam: float, max_shear_stress = 130, max_bearing_stress = 80):
        """
            Инициализация класса CillindricalKey. При вызове __init__ родительского класса в параметр lug
            подается key_diam чтобы не срабатывала проверка, на работу не влияет.
        """
        super().__init__(lenght, width, shaft, lug = key_diam, max_shear_stress = max_shear_stress, max_bearing_stress = max_bearing_stress)
        self.key_diam = key_diam

    def get_max_torque(self):
        """
        Возвращает максимальный момент
        """
        bearing_torque = 0.5 * self.shaft * self.key_diam * self.lenght * self.max_shear_stress / 1000
        shear_torque = 0.2 * (self.shaft + self.key_diam) * self.width * self.lenght * self.max_bearing_stress / 1000
        if bearing_torque < shear_torque:
            return round(bearing_torque, 2)
        else:
            return round(shear_torque, 2)

    def __str__(self):
        """
            Метод возвращает строку с параметрами объекта
        """
        return f'''Циллиндрическая шпонка длинной {self.lenght} мм, шириной паза {self.width} мм, диаметром {self.key_diam}
        на валу диаметром {self.shaft}. Максимальные напряжение среза и смятия соответственно: {self.max_shear_stress}, {self.max_bearing_stress}.'''

    def __repr__(self):
        """
            Метод возвращает строку с кодом созданием объекта
        """
        return f"{self.__class__.__name__}(lenght={self.lenght}, width={self.width}, shaft={self.shaft}, key_diam={self.key_diam}, max_shear_stress={self.max_shear_stress}, max_bearing_stress={self.max_bearing_stress})"


if __name__ == "__main__":
    sunk_key = SunkKey(lenght = 10.0, width = 2.3, shaft = 40, lug = 0.8)
    cillindrical_key = CillindricalKey(lenght = 10.0, width = 2.3, shaft = 40, key_diam = 2.8)
    print(cillindrical_key.get_max_torque())
    print(sunk_key.get_max_torque())
    print(cillindrical_key.optimize_shaft(5))
    print(sunk_key.optimize_shaft(5))
    print(sunk_key.__str__())
    print(cillindrical_key.__repr__())
