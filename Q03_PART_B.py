import pandas as pd
dfOrbit = pd.DataFrame({
    "Name":    ["Muhammad Talal Tariq", "Ali Raza", "Sara Khan",
                "Hamza Malik", "Ayesha Noor", "Usman Ahmed"],
    "Section": ["A", "A", "B", "B", "A", "B"],
    "City":    ["Kamra", "Attock", "Rawalpindi", "Attock", "Kamra", "Islamabad"],
    "Marks":   [82, 67, 91, 58, 74, 65]
})
print("===== Original DataFrame (dfOrbit) =====")
print(dfOrbit)
# (i) students with marks greater than 70
print("\n===== (i) Students with Marks > 70 =====")
print(dfOrbit[dfOrbit["Marks"] > 70])
# (ii) average marks of each section
print("\n===== (ii) Average Marks of each Section (groupby) =====")
print(dfOrbit.groupby("Section")["Marks"].mean())
# (iii) Grade column: A if >= 80, B if >= 60, otherwise C
def give_grade(m):
    if m >= 80:
        return "A"
    elif m >= 60:
        return "B"
    else:
        return "C"

dfOrbit["Grade"] = dfOrbit["Marks"].apply(give_grade)
print("\n===== (iii) DataFrame with new Grade column =====")
print(dfOrbit)
# (iv) sort by marks, highest first
dfOrbit = dfOrbit.sort_values("Marks", ascending=False)
print("\n===== (iv) Sorted by Marks (descending) =====")
print(dfOrbit)
