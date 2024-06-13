def generate_carpet(n):
    if n % 2 == 0:
        return "لطفاً یک عدد فرد وارد کنید."
    else:
        carpet = ""
        for i in range(n):
            for j in range(n):
                if i == n // 2 or j == n // 2:
                    carpet += "X"
                else:
                    carpet += "O"
            carpet += "\n"
        return carpet

