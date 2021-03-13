class Art:
    def __init__(self, artist, title, year, medium, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return '{a}. "{t}". {y}, {m}. {o}, {c}.'.format(a=self.artist, t=self.title, y=self.year, m=self.medium, o=self.owner.name, c=self.owner.location)


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, listing):
        self.listings.append(listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        print('Available listings:')
        for listing in self.listings:
            print(listing)


class Client:
    def __init__(self, name, location='Private Collection', is_museum=False):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def sell_artwork(self, work, price):
        if work.owner.name == self.name:
            new_listing = Listing(work, price, self.name)
            veneer.add_listing(new_listing)

    def buy_artwork(self, work):
        if work.owner.name != self.name:
            for listing in veneer.listings:
                if work == listing.art:
                    work.owner = self
                    veneer.remove_listing(listing)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return '{name}: {price}'.format(name=self.art.title, price=self.price)


veneer = Marketplace()
edytta = Client('Edytta Halpirt')
moma = Client('The MOMA', 'New York', True)
girl_w_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', '1910', 'oil on canvas', edytta)

edytta.sell_artwork(girl_w_mandolin, '$6M (USD)')
veneer.show_listings()
moma.buy_artwork(girl_w_mandolin)
print(girl_w_mandolin)
veneer.show_listings()

# print(girl_w_mandolin)
