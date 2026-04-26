class Player:
    def __init__(self, name, start_pos):
        self.name = name
        self.position = start_pos
        self.cards = []
        self.is_active = True

    def move_to(self, pos):
        self.position = pos

    def add_card(self, card):
        self.cards.append(card)

    def has_card(self, card):
        return card in self.cards
    
    def show_cards(self):
        print(f"{self.name}'s cards: {self.cards}")
    
