from operator import itemgetter


class Browser:
    def __init__(self, id, name, memory, comp_id):
        self.id = id
        self.name = name
        self.memory = memory
        self.comp_id = comp_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BrowserComputer:
    def __init__(self, comp_id, browser_id):
        self.comp_id = comp_id
        self.browser_id = browser_id


computers = [
    Computer(1, 'Альфа-ПК'),
    Computer(2, 'Игровой ПК'),
    Computer(3, 'Офисный ПК'),
    Computer(4, 'Архивный ПК'),
]


browsers = [
    Browser(1, 'Google Chrome', 450, 1),
    Browser(2, 'Microsoft Edge', 300, 1),
    Browser(3, 'Mozilla Firefox', 350, 2),
    Browser(4, 'Brave', 250, 2),
    Browser(5, 'Opera', 200, 3),
]


browsers_computers = [
    BrowserComputer(1, 1),
    BrowserComputer(1, 2),
    BrowserComputer(1, 3),
    BrowserComputer(2, 1),
    BrowserComputer(2, 3),
    BrowserComputer(2, 4),
    BrowserComputer(3, 5),
    BrowserComputer(4, 1),
    BrowserComputer(4, 2),
    BrowserComputer(4, 4),
]


def main():

    one_to_many = [
        (b.name, b.memory, c.name)
        for c in computers
        for b in browsers
        if b.comp_id == c.id
    ]

    many_to_many_temp = [
        (c.name, bc.comp_id, bc.browser_id)
        for c in computers
        for bc in browsers_computers
        if c.id == bc.comp_id
    ]

    many_to_many = [
        (b.name, b.memory, comp_name)
        for comp_name, comp_id, browser_id in many_to_many_temp
        for b in browsers
        if b.id == browser_id
    ]

    print('Задание Д1')

    res_11 = [
        (name, comp_name)
        for name, memory, comp_name in one_to_many
        if name.endswith('e')
    ]

    print(res_11)

    print('\nЗадание Д2')

    res_12_unsorted = []

    for c in computers:

        c_browsers = list(
            filter(lambda i: i[2] == c.name, one_to_many)
        )

        if len(c_browsers) > 0:

            c_memory = [memory for _, memory, _ in c_browsers]

            c_memory_sum = sum(c_memory)

            c_memory_avg = c_memory_sum / len(c_memory)

            res_12_unsorted.append((c.name, c_memory_avg))

    res_12 = sorted(
        res_12_unsorted,
        key=itemgetter(1),
        reverse=True
    )

    print(res_12)

    print('\nЗадание Д3')

    res_13 = {}

    for c in computers:

        if c.name.startswith('А'):

            c_browsers = list(
                filter(lambda i: i[2] == c.name, many_to_many)
            )

            c_browsers_names = [x for x, _, _ in c_browsers]

            res_13[c.name] = c_browsers_names

    print(res_13)


if __name__ == '__main__':
    main()
