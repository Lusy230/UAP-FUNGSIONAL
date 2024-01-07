# soal nomor 12
def halo_decorator(fungsi):
    def halo(*first, **last):
        print('Eyyo')
        fungsi(*first, **last)
        print('Whassup')
@halo_decorator
def whoami(firstName, lastName):
    print(firstName, lastName)

whoami("Lusy", "Rohmadhoni")