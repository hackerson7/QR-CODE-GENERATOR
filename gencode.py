from rich import print
import qrcode
data=input("данные:")
qrcode.make(data).save('qrcode.png')
print("[red] сохранено как qrcode.png")