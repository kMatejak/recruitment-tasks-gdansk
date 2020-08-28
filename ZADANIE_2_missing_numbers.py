def missing_numbers(m: list, n: int) -> list:
    data = {number: None for number in range(1, n + 1)}
    missing_numbers = list()
    for x in m:
        data.update({x: 1})
    for number in data:
        if data[number]:
            continue
        else:
            missing_numbers.append(number)

    return missing_numbers


if __name__ == '__main__':
    m = [2, 3, 7, 4, 9]
    n = 10
    mn = missing_numbers(m, n)
    print(f"\nDla danego zbioru m = {m}")
    print(f"brakujące liczby w tym zbiorze z ciągu liczb 1..{n} to:")
    for x in mn:
        print(f"{x}", end=", ")
    print()
    print()
