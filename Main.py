print("Hello")
input("> ")

name = input()

int(1,2,3,4,)
float(0.3, 9.5)
str("string")
bool(True, False)

st = ["Yasha", "Sasha"]
st.append("Dima")
st.remove("Dima")

st ={"Yasha":
	 ["0506666666", "0687777777"]
	"Sasha":
	 ["0908888888", "0659999999"]
	}

if name == "Den":
	print("Hallo Den")
elif name != "Yasha":
	print("Yshel")
else:
	print("Hto ti voin")
##########################################
st = ["Yasha", "Sasha"]

if "Dima" not in st or "Grisha" in st:
	print("True")
else:
	print("Error")


mar = 0

while mar <=5:
	mar = mar + 1
	print(mar)

for i in range(1,6):
	print(i)