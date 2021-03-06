class Animals:
    def __init__(self, name: str = '', weight: float = 0.0):
        self.animal = ""
        self.name = name
        self.weight = weight
        self.voice = ""

    def korm(self):
        """
        Кормежка животного
        """
        return "%s %s получил(а) корм." % (self.animal, self.name)

    def printer(self):
        print(self.animal, self.name, 'весом ' + str(self.weight) + ' кг.', 'говорит ' + str(self.voice))

    def action(self):
        pass


class Cow(Animals):
    def __init__(self, name: str = '', weight: float = 0.0):
        super().__init__(name, weight)
        self.animal = "Корова"
        self.voice = "му-му"

    def doika(self):
        """
        Процесс дойки
        """
        return "%s %s подоена." % (self.animal, self.name)

    def action(self):
        print(self.doika())


class Goose(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Гусь"
        self.voice = "га-га"

    def eggs(self):
        """
        Процесс сборки яиц
        """
        return "%s %s дал яйца." % (self.animal, self.name)

    def action(self):
        print(self.eggs())


class Chicken(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Курица"
        self.voice = "ко-ко"

    def eggs(self):
        """
        Процесс сборки яиц
        """
        return "%s %s дала яйца." % (self.animal, self.name)

    def action(self):
        print(self.eggs())


class Sheep(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Овца"
        self.voice = "бе-бе"

    def postrich(self):
        """
        Процесс пострижки овец
        """
        return "%s %s была пострижена." % (self.animal, self.name)

    def action(self):
        print(self.postrich())


class Goat(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Коза"
        self.voice = "ме-е-е"

    def doika(self):
        """
        Процесс дойки
        """
        return "%s %s подоена." % (self.animal, self.name)

    def action(self):
        print(self.doika())


class Duck(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Утка"
        self.voice = "кря-кря"

    def eggs(self):
        """
        Процесс сборки яиц
        """
        return "%s %s дала яйца." % (self.animal, self.name)

    def action(self):
        print(self.eggs())


# initialization
animals = []
goose1 = Goose("Джон", 3)
animals.append(goose1)
goose2 = Goose("Степа", 2)
animals.append(goose2)
cow = Cow("Зорька", 450)
animals.append(cow)
sheep1 = Sheep("Ной", 75)
animals.append(sheep1)
sheep2 = Sheep("Юлик", 85)
animals.append(sheep2)
chick1 = Chicken("Рыжик", 1.2)
animals.append(chick1)
chick2 = Chicken("Бела", 1)
animals.append(chick2)
goat1 = Goat("Галка", 50)
animals.append(goat1)
goat2 = Goat("Тихоня", 54)
animals.append(goat2)
duck = Duck("Даги", 3)
animals.append(duck)
summa = 0
maximum = 0
name = ''

for animal in animals:
    animal.printer()
    print(animal.korm())
    animal.action()
    summa += animal.weight
    if animal.weight >= maximum:
        maximum = animal.weight
        name = animal.animal + ' ' + animal.name

print("Общий вес всех животных:", summa)
print("Самое тяжелое животное:", name, 'весом', maximum, 'кг.')
