class InvalidSeatNumberError(Exception):
    pass


class Ticket:
    def __init__(self, movie_title, seat_number, price):
        if not (1 <= seat_number <= 40):
            raise InvalidSeatNumberError("Номер місця повинен бути в межах від 1 до 40.")
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

    def display_info(self):
        return f"Фільм: {self.movie_title}, Місце: {self.seat_number}, Ціна: {self.price} грн"


class StandardTicket(Ticket):
    def __init__(self, movie_title, seat_number, price, discount=0):
        super().__init__(movie_title, seat_number, price)
        self.discount = discount

    def display_info(self):
        info = super().display_info()
        if self.discount > 0:
            info += f", Знижка: {self.discount}%"
        return info


class VIPTicket(Ticket):
    def __init__(self, movie_title, seat_number, price, lounge_access=True, complimentary_drinks=1):
        super().__init__(movie_title, seat_number, price)
        self.lounge_access = lounge_access
        self.complimentary_drinks = complimentary_drinks

    def display_info(self):
        info = super().display_info()
        info += f", Доступ до VIP-зони: {'Так' if self.lounge_access else 'Ні'}, Безкоштовні напої: {self.complimentary_drinks}"
        return info


class Cinema:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        try:
            self.tickets.append(ticket)
        except Exception as e:
            print(f"Сталася помилка при створенні квитка: {e}")

    def display_all_tickets(self):
        if not self.tickets:
            print("Не видано жодного квитка.")
        for ticket in self.tickets:
            print(ticket.display_info())


cinema = Cinema()

try:
    standard_ticket = StandardTicket("Фільм 1", 10, 100, discount=15)
    vip_ticket = VIPTicket("Фільм 2", 5, 200, complimentary_drinks=2)

    cinema.add_ticket(standard_ticket)
    cinema.add_ticket(vip_ticket)

    cinema.display_all_tickets()
except InvalidSeatNumberError as e:
    print(f"Помилка при створенні квитка: {e}")
except Exception as e:
    print(f"Сталася загальна помилка: {e}")
