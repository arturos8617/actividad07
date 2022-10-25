import imp
import re
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulasact.particula import Particula
from particulasact.index import Nodo, Lista_ligada


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.lista_ligada = Lista_ligada()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarFinal_pushButton.clicked.connect(
            self.click_agregarFinal)
        self.ui.agregarInicio_pushButton.clicked.connect(
            self.click_agregarInicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    def creadorDeParticulas(self):
        destinoX = self.ui.destinoX_spinBox.value()
        origenX = self.ui.origenX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        return Particula(self.lista_ligada.no_elements+1, origenX, origenY,
                         destinoX, destinoY, velocidad, red, green, blue)

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.lista_ligada.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(self, "Error", "El archivo no pudo crearse")

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.lista_ligada.guardar(ubicacion):
            QMessageBox.information(
                self, "Exito", "Se pudo crear el archivo"+ubicacion)
        else:
            QMessageBox.critical(
                self,
                "Error",
                "El archivo no se pudo crear"
            )

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.lista_ligada))

    @Slot()
    def click_agregarFinal(self):
        particula = self.creadorDeParticulas()
        nodo = Nodo(particula)
        self.lista_ligada.agregar_final(nodo)
        self.ui.salida.clear()
        self.ui.salida.insertPlainText("Agregado al Final")

    @Slot()
    def click_agregarInicio(self):
        particula = self.creadorDeParticulas()
        nodo = Nodo(particula)
        self.lista_ligada.agregar_inicio(nodo)
        self.ui.salida.clear()
        self.ui.salida.insertPlainText("Agregado al Inicio")
