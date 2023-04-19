# while True:
#     with open("files/tanga.txt", 'r') as file:
#         sides = file.readlines()
#
#     side = input("Tanga tomonini kiriting, gerb yoki raqam?") + "\n"
#
#     sides.append(side)
#
#     with open("files/tanga.txt", 'w') as file:
#         file.writelines(sides)
#
#     nr_heads = sides.count("head\n")
#     percentage = nr_heads / len(sides) * 100
#
#     print(f"Heads: {percentage}%")

gerb = 0
son = 0
def calc(a, b):
    gerb_ulushi = a*100/(a+b)
    son_ulushi = b*100/(a+b)
    print(f"Gerb ulushi: {gerb_ulushi}\nSon ulushi esa: {son_ulushi}")
while True:
    option = (input("Tanga tomonini tanlang: gerb yoki son:  ").lower()).strip()
    if option == "gerb":
        gerb += 1
    elif option == "son":
        son += 1
    else:
        print("Sin noto'g'ri birlik kiritdingiz")
        continue
    calc(gerb, son)

