import sys
import uuid
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem, QMessageBox
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtMultimedia import QSound

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("form.ui", self)

        self.oncelik = "Düşük"
        self.pushButton_dusuk.clicked.connect(lambda: self.oncelik_sec("Düşük"))
        self.pushButton_orta.clicked.connect(lambda: self.oncelik_sec("Orta"))
        self.pushButton_yuksek.clicked.connect(lambda: self.oncelik_sec("Yüksek"))
        self.oncelik_butonlarini_guncelle()

        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1440)
        self.spinBox.setSuffix(" dk")
        self.spinBox.setValue(5)

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Başlık", "Açıklama", "Süre", "Öncelik", "Tamamlandı"]
        )
        self.tableWidget.setSelectionBehavior(self.tableWidget.SelectRows)
        self.tableWidget.setEditTriggers(self.tableWidget.NoEditTriggers)
        self.tableWidget.cellDoubleClicked.connect(self.tablo_duzenle)

        self.pushButton.clicked.connect(self.gorev_ekle)
        self.pushButton_2.clicked.connect(self.gorev_sil)
        self.pushButton_4.clicked.connect(self.gorev_tamamla)
        if hasattr(self, 'pushButton_sirala'):
            self.pushButton_sirala.clicked.connect(self.oncelik_ve_sureye_gore_sirala)
        self.tableWidget.selectionModel().selectionChanged.connect(self.satir_secildi)

        self.editing_row = None
        self.timers = {}
        self.kalan_saniyeler = {}
        self.ilk_sureler = {}
        self.row_ids = []

    def oncelik_sec(self, secim):
        self.oncelik = secim
        self.oncelik_butonlarini_guncelle()

    def oncelik_butonlarini_guncelle(self):
        for buton, isim in [
            (self.pushButton_dusuk, "Düşük"),
            (self.pushButton_orta, "Orta"),
            (self.pushButton_yuksek, "Yüksek")
        ]:
            if self.oncelik == isim:
                buton.setStyleSheet("background-color: #aaffaa; font-weight: bold;")
            else:
                buton.setStyleSheet("")

    def gorev_ekle(self):
        baslik = self.lineEdit.text().strip()
        aciklama = self.textEdit.toPlainText().strip()
        sure = self.spinBox.value()
        oncelik = self.oncelik
        tamamlandi = "Hayır"

        if not baslik:
            QMessageBox.warning(self, "Uyarı", "Başlık boş olamaz!")
            return

        gorev_id = str(uuid.uuid4())
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(baslik))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(aciklama))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{sure} dk"))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(oncelik))
        self.tableWidget.setItem(row, 4, QTableWidgetItem(tamamlandi))

        self.satir_renklendir(row)

        kalan_saniye = sure * 60
        self.kalan_saniyeler[gorev_id] = kalan_saniye
        self.ilk_sureler[gorev_id] = kalan_saniye
        self.row_ids.insert(row, gorev_id)

        timer = QTimer(self)
        timer.timeout.connect(lambda gid=gorev_id: self.geri_sayim(gid))
        timer.start(1000)
        self.timers[gorev_id] = timer

        self.alanlari_temizle()
        self.oncelik_ve_sureye_gore_sirala()

    def geri_sayim(self, gorev_id):
        if gorev_id not in self.kalan_saniyeler:
            return
        self.kalan_saniyeler[gorev_id] -= 1
        kalan = self.kalan_saniyeler[gorev_id]
        row = self.get_row_by_id(gorev_id)
        if row is None:
            return
        if kalan >= 0:
            item = self.tableWidget.item(row, 2)
            if item is None:
                item = QTableWidgetItem(self.sure_formatla(kalan))
                self.tableWidget.setItem(row, 2, item)
            else:
                item.setText(self.sure_formatla(kalan))
            item.setBackground(QColor(255, 128, 0))
        else:
            self.timers[gorev_id].stop()
            item = self.tableWidget.item(row, 2)
            if item is None:
                item = QTableWidgetItem("Süre doldu!")
                self.tableWidget.setItem(row, 2, item)
            else:
                item.setText("Süre doldu!")
            item.setBackground(QColor(255, 0, 0))
            QSound.play("ding.wav")
            cevap = QMessageBox.question(
                self, "Süre Doldu!",
                "Ekstra süre eklemek ister misiniz?",
                QMessageBox.Yes | QMessageBox.No
            )
            if cevap == QMessageBox.Yes:
                ekstra = self.ilk_sureler[gorev_id]
                self.kalan_saniyeler[gorev_id] = ekstra
                self.timers[gorev_id].start(1000)
                self.tableWidget.setItem(row, 2, QTableWidgetItem(self.sure_formatla(ekstra)))
                self.tableWidget.item(row, 2).setBackground(QColor(255, 128, 0))
            else:
                QMessageBox.warning(self, "Görev Başarısız", "Görev başarısız oldu ve silindi!")
                self.gorev_sil_by_id(gorev_id)

    def get_row_by_id(self, gorev_id):
        try:
            return self.row_ids.index(gorev_id)
        except ValueError:
            return None

    def gorev_sil(self):
        selected = self.tableWidget.currentRow()
        if selected >= 0:
            gorev_id = self.row_ids[selected]
            self.gorev_sil_by_id(gorev_id)
        else:
            QMessageBox.warning(self, "Uyarı", "Silmek için bir görev seçin.")

    def gorev_sil_by_id(self, gorev_id):
        row = self.get_row_by_id(gorev_id)
        if row is not None:
            self.tableWidget.removeRow(row)
            self.alanlari_temizle()
            for d in [self.timers, self.kalan_saniyeler, self.ilk_sureler]:
                if gorev_id in d:
                    del d[gorev_id]
            del self.row_ids[row]
            self.oncelik_ve_sureye_gore_sirala()

    def gorev_tamamla(self):
        selected = self.tableWidget.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Uyarı", "Bir görev seçin.")
            return
        QMessageBox.information(self, "Tamamlandı", "Görev tamamlandı olarak işaretlendi ve silindi!")
        gorev_id = self.row_ids[selected]
        self.gorev_sil_by_id(gorev_id)

    def tablo_duzenle(self, row, column):
        if column in [0, 1]:
            item = self.tableWidget.item(row, column)
            if item is None:
                item = QTableWidgetItem("")
                self.tableWidget.setItem(row, column, item)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.tableWidget.editItem(item)
            self.tableWidget.itemChanged.connect(self.duzenlemeyi_kilitle)
        else:
            QMessageBox.information(self, "Bilgi", "Sadece başlık ve açıklama hücreleri düzenlenebilir.")

    def duzenlemeyi_kilitle(self, item):
        if item.column() in [0, 1]:
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.tableWidget.itemChanged.disconnect(self.duzenlemeyi_kilitle)

    def satir_secildi(self):
        selected = self.tableWidget.currentRow()
        if selected >= 0:
            self.lineEdit.setText(self.tableWidget.item(selected, 0).text())
            self.textEdit.setPlainText(self.tableWidget.item(selected, 1).text())
            sure_text = self.tableWidget.item(selected, 2).text()
            sure = int(sure_text.split()[0]) if sure_text.split()[0].isdigit() else 5
            self.spinBox.setValue(sure)
            self.oncelik = self.tableWidget.item(selected, 3).text()
            self.oncelik_butonlarini_guncelle()
            self.editing_row = selected

    def alanlari_temizle(self):
        self.lineEdit.clear()
        self.textEdit.clear()
        self.spinBox.setValue(5)
        self.oncelik = "Düşük"
        self.oncelik_butonlarini_guncelle()
        self.editing_row = None

    def sure_formatla(self, saniye):
        dakika = saniye // 60
        sn = saniye % 60
        return f"{dakika:02d}:{sn:02d}"

    def satir_renklendir(self, row):
        oncelik = self.tableWidget.item(row, 3)
        if oncelik is None:
            oncelik_text = "Düşük"
        else:
            oncelik_text = oncelik.text()
        renk = QColor("white")
        if oncelik_text == "Yüksek":
            renk = QColor(255, 102, 102)
        elif oncelik_text == "Orta":
            renk = QColor(102, 178, 255)
        elif oncelik_text == "Düşük":
            renk = QColor(102, 255, 178)
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            if item is None:
                item = QTableWidgetItem("")
                self.tableWidget.setItem(row, col, item)
            item.setBackground(renk)
        item = self.tableWidget.item(row, 2)
        if item is None:
            item = QTableWidgetItem("")
            self.tableWidget.setItem(row, 2, item)
        item.setBackground(QColor(255, 128, 0))

    def oncelik_ve_sureye_gore_sirala(self):
        oncelik_sirasi = {"Yüksek": 0, "Orta": 1, "Düşük": 2}
        rows = []
        for idx, gorev_id in enumerate(self.row_ids):
            row_data = [self.tableWidget.item(idx, col).text() if self.tableWidget.item(idx, col) else "" for col in range(self.tableWidget.columnCount())]
            sure_text = row_data[2]
            if "dk" in sure_text:
                try:
                    sure_saniye = int(sure_text.split()[0]) * 60
                except:
                    sure_saniye = 99999
            elif ":" in sure_text:
                dakika, saniye = sure_text.split(":")
                sure_saniye = int(dakika) * 60 + int(saniye)
            elif sure_text == "Süre doldu!":
                sure_saniye = 99999
            else:
                sure_saniye = 99999
            rows.append((oncelik_sirasi.get(row_data[3], 3), sure_saniye, row_data, gorev_id))
        rows.sort(key=lambda x: (x[0], x[1]))
        self.tableWidget.setRowCount(0)
        self.row_ids = []
        for _, _, row_data, gorev_id in rows:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, value in enumerate(row_data):
                self.tableWidget.setItem(row, col, QTableWidgetItem(value))
            self.satir_renklendir(row)
            self.row_ids.append(gorev_id)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
