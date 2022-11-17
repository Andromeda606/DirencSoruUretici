import random

formule = {
    "Siyah":        [0, 1, None],
    "Kahverengi":   [1, pow(10, 1), 1],
    "Kırmızı":      [2, pow(10, 2), 2],
    "Turuncu":      [3, pow(10, 3), 3],
    "Sarı":         [4, pow(10, 4), 4],
    "Yeşil":        [5, pow(10, 5), 0.5],
    "Mavi":         [6, pow(10, 6), 0.25],
    "Mor":          [7, pow(10, 7), 0.1],
    "Gri":          [8, pow(10, 8), 0.05],
    "Beyaz":        [9, pow(10, 9), 1],
    "Altın":        [None, None, 5],
    "Gümüş":        [None, None, 10],
}
formule_keys = list(formule.keys())


def get_var(item: int, should: bool = False):
    while True:
        var = random.choice(formule_keys + [None])
        if var is None:
            if not should:
                return None, None
        else:
            if formule[var][item] is not None:
                return var, str(formule[var][item])


bands = [get_var(0, True), get_var(0), get_var(0)]
increment = get_var(1, True)
tolerance = get_var(2, True)
builder = ""
answer_str = ""
for i, band in enumerate(bands):
    if band[0] is not None and band[1] is not None:
        name, value = band
        builder += "Bir şeriti " + name + ",\n"
        answer_str += value
builder += "Bir şeriti " + increment[0] + ",\n"
builder += "Bir şeriti " + tolerance[0] + ",\n"
increment = increment[1]
tolerance = tolerance[1]
answer_str = int(str(answer_str) + str(increment)[1:])
if answer_str >= 1000:
    answer_float = float(answer_str)
    value = 0
    while answer_float >= 1000 and "000" in str(answer_float):
        answer_float = answer_float / 1000
        value += 1
    answer_str = str(int(answer_float))
    if value == 0:
        answer_str += "W"
    elif value == 1:
        answer_str += "KW"
    elif value == 2:
        answer_str += "MW"
    elif value == 3:
        answer_str += "GW"
else:
    answer_str = str(answer_str)
    answer_str += "W"
answer_str += " " + tolerance + "%"
builder = builder[:len(builder) - 2] + "\nOlan direncin ohm değeri nedir?\n\n"
print(builder)
for x in range(5):
    print("Yüzdeden önceki şeritlerin değerini giriniz: ")
    prompt = input()
    print("Yüzdeyi giriniz: ")
    prompt += " " + input() + "%"
    print("Yazdığınız cevap:", prompt)
    if answer_str == prompt:
        print("Cevabınız Doğru!")
        exit()
    else:
        print("Cevabınız Yanlış!", 4 - x + 1, "Deneme hakkınız kaldı")
print("Doğru Cevap: ", answer_str)
