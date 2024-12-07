import random


class EcosystemEntity:
    def __init__(self, name, energy, position, survival_rate):
        self.name = name
        self.energy = energy
        self.position = position
        self.survival_rate = survival_rate

    def act(self):
        pass


class Plant(EcosystemEntity):
    def __init__(self, name, energy, position, survival_rate, growth_rate):
        super().__init__(name, energy, position, survival_rate)
        self.growth_rate = growth_rate

    def act(self):
        self.energy += self.growth_rate

    def reproduce(self):
        if random.random() < self.survival_rate:
            new_position = (self.position[0] + random.randint(-1, 1),
                            self.position[1] + random.randint(-1, 1))
            return Plant(self.name, 10, new_position, self.survival_rate, self.growth_rate)
        return None


class Animal(EcosystemEntity):
    def __init__(self, name, energy, position, survival_rate, speed, diet_type):
        super().__init__(name, energy, position, survival_rate)
        self.speed = speed
        self.diet_type = diet_type

    def move(self):
        self.position = (self.position[0] + random.randint(-self.speed, self.speed),
                         self.position[1] + random.randint(-self.speed, self.speed))

    def act(self):
        self.move()
        self.energy -= 1

    def reproduce(self):
        if random.random() < self.survival_rate:
            new_position = (self.position[0] + random.randint(-1, 1),
                            self.position[1] + random.randint(-1, 1))
            return self.__class__(self.name, 20, new_position, self.survival_rate, self.speed, self.diet_type)
        return None


class Herbivore(Animal):
    def eat(self, plant):
        self.energy += plant.energy
        return True


class Carnivore(Animal):
    def eat(self, prey):
        self.energy += prey.energy
        return True


class Omnivore(Animal):
    def eat(self, entity):
        self.energy += entity.energy
        return True


class Ecosystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def simulate_step(self):
        for entity in self.entities:
            entity.act()
            if isinstance(entity, Plant):
                new_plant = entity.reproduce()
                if new_plant:
                    self.add_entity(new_plant)
            if isinstance(entity, Animal):
                if entity.energy <= 0:
                    self.remove_entity(entity)
                new_animal = entity.reproduce()
                if new_animal:
                    self.add_entity(new_animal)

    def display(self):
        for entity in self.entities:
            print(f"{entity.name} at {entity.position} with energy {entity.energy}")


if __name__ == "__main__":
    ecosystem = Ecosystem(10, 10)

    ecosystem.add_entity(Plant("Grass", 10, (2, 3), 0.5, 2))
    ecosystem.add_entity(Herbivore("Rabbit", 20, (5, 5), 0.4, 2, "Herbivore"))
    ecosystem.add_entity(Carnivore("Wolf", 30, (7, 7), 0.3, 3, "Carnivore"))

    for _ in range(10):
        ecosystem.simulate_step()
        ecosystem.display()
