class Cart():
    def __init__(self):
        self.cart = {"data":[]}

    def tambahProduk(self, kodeProduk, kuantitas):
        list_all = [i["kodeProduk"] for i in self.cart.get("data")]
        
        if kodeProduk not in list_all:
            self.cart.get("data").append({"kodeProduk": kodeProduk, "kuantitas": kuantitas})
        else:
            for i, value in enumerate(self.cart.get("data")):
                if kodeProduk == value.get("kodeProduk"):
                    self.cart.get("data")[i].update({"kuantitas": kuantitas + value.get("kuantitas")})

    def hapusProduk(self, kodeProduk):
        for i in range(len(self.cart.get("data"))):
            if self.cart.get("data")[i].get("kodeProduk") == kodeProduk:
                del self.cart.get("data")[i]
                break

    def tampilkanCart(self):
        for i in self.cart.get("data"):
            print(f'{i.get("kodeProduk")} ({i.get("kuantitas")})')

keranjang = Cart()

keranjang.tambahProduk("Pisang Hijau", 2)
keranjang.tambahProduk("Semangka Kuning", 3)
keranjang.tambahProduk("Apel Merah", 1)
keranjang.tambahProduk("Apel Merah", 4)
keranjang.tambahProduk("Apel Merah", 2)
keranjang.hapusProduk("Semangka Kuning")
keranjang.hapusProduk("Semangka Merah")
keranjang.tampilkanCart()