class PostCode():
    def __init__(self, postcode: str):
        self.head = postcode[:2]
        self.tail = postcode[3:]
        self.fullcode = (int(self.head) * 1000) + int(self.tail)

    def __lt__(self, other):
        return self.fullcode < other.fullcode

    def __repr__(self):
        return f"{self.head}-{self.tail}"

    @classmethod
    def from_int(cls, postcode: int) -> 'PostCode':
        return cls(postcode=f"{str(postcode)[:2]}-{str(postcode)[2:]}")


def lower_first(first: PostCode, second: PostCode) -> tuple:
    if first < second:
        return first, second
    else:
        return second, first


def postcodes_generator(first: str, second: str) -> list:
    lower_code, higher_code = lower_first(PostCode(first), PostCode(second))
    postcodes = list()
    for pc in range(lower_code.fullcode, higher_code.fullcode + 1):
        postcode = PostCode.from_int(pc)
        postcodes.append(postcode)

    return postcodes


if __name__ == '__main__':
    first, second = "79-900", "80-155"
    pcg = postcodes_generator(first, second)
    print("\nLista następujących po sobie kodów pocztowych od ", end="")
    print(f"{first} do {second} to: ")
    for pc in pcg:
        print(f"{pc}", end=", ")
    print()
    print()
