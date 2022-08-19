#с богом

M_IN_KM = 1000

class Training:
    def __init__(self, action: int, duration: float, weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight  

    LEN_STEP = 0.65

    def get_mean_speed(self) -> float:
        speed = self.distance / self.time
        return round(speed, 3)

    def get_distance(self) -> float:  
        distance = self.action * self.LEN_STEP / M_IN_KM 
        return round(distance, 3)

    def get_spent_calories(self) -> float:
        round(self.calories, 3)
        
    def show_training_info(self) -> 'InfoMessage':
        return self.InfoMessage(self.training_type, self.duration, self.distance, self.speed, self.calories)


class Running(Training): 
    def __init__(self) -> None:
        super().__init__('Running')

    coeff_calorie_1 = 18
    coeff_calorie_2 = 20  

    def get_spent_calories(self) -> float:
        calories = (self.coeff_calorie_1 * self.speed - self.coeff_calorie_2) * self.weight / M_IN_KM * self.duration
        return round(calories, 3)
    
        
class SportsWalking(Training): 
    coeff_hight_1 = 0.035
    coeff_hight_2 = 2
    coeff_hight_3 = 0.029

    def __init__(self) -> None:
        super().__init__('SportsWalking')

    def hight(self) -> float:
        hight = (self.coeff_hight_1 * self.weight + (self.speed * self.coeff_hight_2 / self.height) * self.coeff_hight_3 * self.weight) * self.duration
        return round(hight, 3)


class Swimming(Training):  
    coeff_swimming_1 = 1.1
    coeff_swimming_2 = 2

    def __init__(self, length_pool: float, count_pool: float) -> None:  
        self.length_pool = length_pool
        self.count_pool = count_pool 
        super().__init__('Swimming')
    
    LEN_STEP = 1.38

    coeff_swimming_1 = 1.1
    coeff_swimming_2 = 2

    def get_spent_calories(self) -> float:
        calories = (self.speed + self.coeff_swimming_1) * self.coeff_swimming_2 * self.weight
        return round(calories, 3)

    def get_mean_speed(self) -> float:
        speed = self.length_pool * self.count_pool / M_IN_KM / self.duration
        return round(speed, 3)
        
        
class InfoMessage:
    def __init__(self, training_type: str, duration: float, distance: float, speed: float, calories: float ) -> None:
        self.training_type = training_type
        self.duration = duration 
        self.distance = distance
        self.speed = speed 
        self.calories = calories 

    def get_message(self):
        return f'Тип тренировки: {self.training_type}; Длительность: {round(self.duration, 3)} ч.; Дистанция: {round(self.distance, 3)} км; Ср.скорость: {round(self.speed, 3)} км/ч; Потрачено ккал: {round(self.calories, 3)}.'



