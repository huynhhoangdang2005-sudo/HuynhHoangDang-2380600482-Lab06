import sys
from PyQt5 import QtWidgets, uic
def rail_fence_encrypt(text,key):
    if key <= 1:return text
    rail = [[ '\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row,col = 0,0
    for char in text :
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row = row + 1 if dir_down else row -1
    return "".join([rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != '\n'])

def rail_fence_decrypt(cipher,key):
    result = []
    if key <= 1:return cipher
    rail = [[ '\n' for _ in range(len(cipher))]for _ in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0: dir_down = True
        if row == key - 1: dir_down = False
        rail[row][col] = '*'
        col += 1
        row = row +1 if dir_down else row -1
        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if rail[i][j] == '*'and index < len(cipher):
                    rail[i][j] = cipher[index]
                    index += 1
        for i in range(len(cipher)):
            if row == 0: dir_down = True
            if row == key - 1: dir_down = False
            result.append(rail[row][col])
            col += 1
            row = row + 1 if dir_down else row - 1
        
        return "".join(result)
    
class RailFenceApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('railfence.ui',self)
        
        self.btnEncrypt.clicked.connect(self.handle_encrypt)
        self.btnDecrypt.clicked.connect(self.handle_decrypt)

    def handle_encrypt(self):
        text = self.txtPlainText.text
        try:
            key = int(self.txtKey.text())
            res = rail_fence_encrypt(text,key)
            self.txtCipherText.setText(res)
        except:
            self.txtCipherText.setText("Lỗi: Key phải là số!")
            
    def handle_decrypt(self):
            cipher = self.txtCipherText.text()
            try:
                key = int(self.txtKey.text())
                res = rail_fence_decrypt(cipher,key)
                self.txtPlainText.setText("res")
            except:
                self.txtPlainText.setText("Lỗi: Key phải là số!")
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = RailFenceApp()
    win.show()
    sys.exit(app.exec_())
    