from random import randint

DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA = 80
SPECIAL_SKILL: str = 'Удача'
SPECIAL_BUFF: int = 15


class Character:
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (1, 5)
    # Объявляем конструктор класса.

    def __init__(self, name):
        self.name = name

    # Объявляем метод атаки
    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный '
                f'{5 + value_attack}')

    # Объявляем метод защиты.
    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    # Объявляем метод специального умения.
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(self, char_name: str) -> Character:
    '''Возвращает строку с выбранным классом персонажа'''
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice = None
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: '
                               'Воитель - warrior, '
                               'Маг - mage, Лекарь - healer')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми "Y", чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(self, character):
    commands = {'skip': 'Тренировка окончена',
                'attack': character.attack(),
                'defence': character.defence(),
                'special': character.special()}
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    user_comand = input('Введи команду: ')
    if user_comand != 'skip':
        print(commands[user_comand])
    print('Тренировка окончена.')
