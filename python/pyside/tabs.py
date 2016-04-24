from PySide import QtCore, QtGui
from PySide.QtCore import QObject, Signal, Slot

import gui
from gui import PunchingBag

class setting_callbacks():
    @Slot()
    def testSlot(self):
        print "OK pressed"
        exit()

    @Slot()
    def say_punched():
        ''' Give evidence that a bag was punched. '''
        print('Bag was punched.')

if __name__ == '__main__':


    import sys

    app = QtGui.QApplication(sys.argv)

    if len(sys.argv) >= 2:
        fileName = sys.argv[1]
    else:
        fileName = "."

    tabdialog = gui.TabDialog(fileName, callbacks=setting_callbacks())
    sys.exit(tabdialog.exec_())
