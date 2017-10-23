# python系统库
import os
import platform
import sys
# 第三方库
from PyQt5.QtGui import QImage, QIcon, QKeySequence, QImageReader, QPixmap, QImageWriter, QPainter
from PyQt5.QtCore import Qt, QSettings, QT_VERSION_STR, PYQT_VERSION_STR
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import *

# 自己写的库


__version__ = "1.0.0"


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizonlly = False

        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setCentralWidget(self.imageLabel)

        # 停靠窗体
        # 停靠窗体不能放在布局中，所以在创建的时候除了需要提供窗体标题外，还要对其给定父对象
        # 通过父对象的设置可以保证停靠窗体不会超出作用域
        logDockWidget = QDockWidget('log', self)
        # 每一个Pyqt对象都有一个对象名，对象名称在调试的时候非常有用
        logDockWidget.setObjectName('LogDockWidget')
        # 默认情况下停靠窗体可以移动，停靠，浮动，关闭，并且可以拖拽的任何区域
        # 由于这里的停靠窗体打算保留一个列表，使用setAllowedAreas来限制停靠区域
        # 还有一个setFeatures() 可以控制窗口是否可以移动，浮动，关闭等特性。
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        # 停靠窗体创建好了之后就可以创建窗体需要包含的部件了
        # 创建列表窗口部件
        self.listWidget = QListWidget()
        logDockWidget.setWidget(self.listWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)

        # 打印图片，首先创建一个printer（打印机实例变量）
        self.printer = None

        self.sizeLable = QLabel()
        self.sizeLable.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        # 创建状态栏，调用showMessage方法显示内容
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLable)
        status.showMessage("Ready", 5000)

        # 新建action
        # 显示名称，槽，快捷键，图标名称，显示status内容
        fileNewAction = self.createAction("&New...", self.fileNew,
                                          QKeySequence.New, "filenew", "Create an image file")
        # 打开文件action
        # 显示名称，槽，快捷键，图标名称，显示status内容
        fileOpenAction = self.createAction("&Open...", self.fileOpen,
                                           QKeySequence.Open, "fileopen", "Open an existing image file")
        # 保存action
        # 显示名称，槽，快捷键，图标显示，显示status内容
        fileSaveAction = self.createAction("&Save", self.fileSave,
                                           QKeySequence.Save, "filesave", "Save the image")
        # 另存为action
        # 显示名称，槽，快捷键，图标显示，显示satus内容
        fileSaveAsAction = self.createAction("&Save as", self.fileSaveAs,
                                             QKeySequence.SaveAs, "filesaveas", "Save the image using a new name")

        # 打印action
        # 显示名称，槽，快捷键，图标显示，显示status内容
        filePrintAction = self.createAction("&Print", self.filePrint,
                                            QKeySequence.Print, "fileprint", "print the image")

        fileQuitAction = self.createAction("&Quit", self.close, "Ctrl+Q", "filequit", "Close the application")

        #
        editInvertAction = self.createAction("&Invert", self.editInvert, "Ctrl+I", "editinvert",
                                             "Invert the Image's colors",
                                             True, True)

        editSwapRedAndBlueAction = self.createAction("&Sw&ap Ren and Blue", self.editSwapRedAndBlue, "Ctrl+A", "editswap",
                                                     "Swap the image's red and blue color components",
                                                     True,True)


        editZoomAction = self.createAction("&Zoom...", self.editZoom, "Alt+Z", "editzoom", "Zoom the image")


        mirrorGroup = QActionGroup(self)
        editUnMirrorAction = self.createAction("&Unmirror", self.edidUnMirror, "Ctrl+U", "editunmirror",
                                               "Unmirror the image", True, True)
        mirrorGroup.addAction(editUnMirrorAction)

        editMirrorHorizontalAction = self.createAction("Mirror &Horizontally", self.editMirrorHorizontal,
                                                       "Ctrl+H", "editmirrorhoriz",
                                                       "Horizontally mirror the image", True, True)
        mirrorGroup.addAction(editMirrorHorizontalAction)

        editMIrrorVerticalAction = self.createAction("Mirror &Vertically", self.editMirrorVertical,
                                                     "Ctrl+V", "editmirrorvert",
                                                     "Vertically mirror the image", True, True)
        mirrorGroup.addAction(editMIrrorVerticalAction)

        helpAboutAction = self.createAction("&About", self.about)
        helpHelpAction = self.createAction("&Help", self.help)


        menuBar = self.menuBar()
        newfile = menuBar.addMenu("&File")
        self.addActions(newfile, (fileNewAction, fileOpenAction, fileSaveAction,
                                  fileSaveAsAction, filePrintAction, fileQuitAction))

        editMenu = menuBar.addMenu("&Edit")
        self.addActions(editMenu, (editInvertAction, editSwapRedAndBlueAction,editZoomAction))

        mirrMenu = menuBar.addMenu(QIcon("images/editmirror.png"), "&mirror")
        self.addActions(mirrMenu, (editUnMirrorAction, editMirrorHorizontalAction, editMIrrorVerticalAction))

        helpMenu = menuBar.addMenu("&Help")
        self.addActions(helpMenu, (helpAboutAction, helpHelpAction))


        fileToolBar = self.addToolBar("File")
        fileToolBar.setObjectName("FileToolBar")
        self.addActions(fileToolBar,(fileNewAction, fileOpenAction, fileSaveAction,
                                  fileSaveAsAction, filePrintAction))

        editToolBar = self.addToolBar("Edit")
        editToolBar.setObjectName("EditToolBar")
        self.addActions(editToolBar,  (editInvertAction, editSwapRedAndBlueAction,editZoomAction,
                                       editUnMirrorAction, editMirrorHorizontalAction, editMIrrorVerticalAction))

        self.zoomSpinBox = QSpinBox()
        self.zoomSpinBox.setRange(1, 400)
        self.zoomSpinBox.setValue(100)
        self.zoomSpinBox.setSuffix(" %")
        self.zoomSpinBox.setStatusTip(self.zoomSpinBox.toolTip())
        self.zoomSpinBox.setFocusPolicy(Qt.NoFocus)
        self.zoomSpinBox.valueChanged.connect(self.showImage)
        editToolBar.addSeparator()
        editToolBar.addWidget(self.zoomSpinBox)

        settings = QSettings()
        # self.recentFiles = settings.value("RecentFiles").toStringList()

    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=None,togglesigle = False):
        """
        text:显示内容
        """

        action = QAction(text, self)

        if icon is not None:
            action.setIcon(QIcon("images/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            if togglesigle:
                action.toggled[bool].connect(slot)
            else:action.triggered.connect(slot)
        if checkable is not None:
            action.setCheckable(True)

        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def updateStatus(self, message):
        statusBar = self.statusBar()
        statusBar.showMessage(message, 5000)
        self.listWidget.addItem(message)
        if self.filename is not None:
            self.setWindowTitle("Image Changer - {0}".format(os.path.basename(self.filename)))
        elif not self.image.isNull():
            self.setWindowTitle("Image Changer - Unnamed")
        else:
            self.setWindowTitle("Image Changer[*]")
        self.setWindowModality(self.dirty)

    def okToContiune(self):
        """
        判断图片是否修改没有保存
        """
        if self.dirty:
            replay = QMessageBox.question(self,
                                          "ImageChanger - Unsaved Changed",
                                          "Save unsaved changes",
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        # 取消操作
        if replay == QMessageBox.Cancel:
            return
        # 确定保存
        elif replay == QMessageBox.Yes:
            self.fileSave()
        return True

    def fileNew(self):
        pass

    def fileOpen(self):
        dir = os.path.dirname(self.filename) if self.filename is not None else "."
        # 构建所有QImageReader支持的图片类型列表
        formats = ['*.{0}'.format(format.data().decode("ascii").lower()) for format in QImageReader.supportedImageFormats()]
        # getOpenFileName返回
        fname, type = QFileDialog.getOpenFileName(self,
                                            "Image Changer - Choose Image", dir,
                                            "Image files (%s)" % " ".join(formats))
        # 如果选中了图片，加载图片
        if fname:
            self.loadFile(fname)

    def loadFile(self, fname=None):
        if fname is None:
            action = self.render()
            if isinstance(action, QAction):
                fname = str(action.data())
        if fname:
            self.filename = None
            try:
                image = QImage(fname)
            except Exception as e:
                print(e)
            if image.isNull():
                message = "Failed to read {0}".format(fname)

            else:
                # self.addRecentFile(fname)
                self.image = QImage()
                # for action, check in self.resetableActions:
                #     action.setChecked(check)
                self.image = image
                self.filename = fname
                self.showImage()
                self.dirty = False

    def addRecentFile(self, fname):
        if fname is None:
            return
        if not self.recentFiles.contains(fname):
            self.recentFiles.prepend(fname)
            while self.recentFiles.count() > 9:
                self.recentFiles.takeLast()

    def fileSave(self):
        """
        保存文件
        :return:
        """
        if self.image.isNull():
            return
        if self.filename is None:
            self.fileSaveAs()
        else:
            if self.image.save(self.filename, None):
                self.dirty = False
                self.updateStatus("Save as {0}".format(self.filename))
            else:
                self.updateStatus("Failed to save {0}".format(self.filename))

    def fileSaveAs(self):
        if self.image.isNull():
            return
        fname = self.filename if self.filename is not None else "."
        formats = ["*.{0}".format(format.data().decode("ascii").lower()) for format in QImageWriter.supportedImageFormats()]

        fname, type = QFileDialog.getSaveFileName(self, "Image Changer - Save Image", fname, "Image files ({0})".format(" ".join(formats)))

        if fname:
            if "." not in fname:
                fname += ".png"
            self.filename = fname
            self.fileSave()

    def filePrint(self):
        if self.image.isNull():
            return
        if self.printer is None:
            self.printer = QPrinter(QPrinter.HighResolution)
            self.printer.setPageSize(QPrinter.Letter)

        form = QPrintDialog(self.printer, self)
        if form.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.drawImage(0, 0, self.image)

    def editInvert(self, on):
        if self.image.isNull():
            return
        self.image.invertPixels()
        self.showImage()
        self.dirty = True

    def editSwapRedAndBlue(self):
        if self.image.isNull():
            return
        self.image = self.image.rgbSwapped()
        self.showImage()
        self.dirty = True

    def editZoom(self):
        if self.image.isNull():
            return
        percent, ok = QInputDialog.getInt(self, "Image Changer - Zoom", "Percent:", self.zoomSpinBox.value(), 1, 400)

        if ok:
            self.zoomSpinBox.setValue(percent)

    def edidUnMirror(self):
        if self.image.isNull():
            return
        if self.mirroredhorizonlly:
            self.editMirrorHorizontal(False)
        if self.mirroredvertically:
            self.editMirrorVertical(False)

    def editMirrorHorizontal(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(False, True)
        self.showImage()
        self.mirroredhorizonlly = not self.mirroredhorizonlly
        self.dirty = True

    def editMirrorVertical(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(True, False)
        self.showImage()
        self.mirroredvertically = not self.mirroredvertically
        self.dirty = True

    def showImage(self, parcent=None):
        if self.image.isNull():
            return
        if parcent is None:
            parcent = self.zoomSpinBox.value()

        factor = parcent / 100.0
        width = self.image.width() * factor
        height = self.image.height() * factor

        image = self.image.scaled(width, height, Qt.KeepAspectRatio)

        self.imageLabel.setPixmap(QPixmap.fromImage(image))

    def about(self):
        QMessageBox.about(self,"about image changer",
                          """<b>Image Changer</b> v {0}
                          <p>Copyright &copy; 2007 Qtrac Ltd. 
                          All rights reserved.
                          <p>This application can be used to perform
                          simple image manipulations.
                          <p>Python {1} - Qt {2} - PyQt {3} on {4}""".format(
                              __version__, platform.python_version(),
                              QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))

    def help(self):
        print("跳转到网页界面！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setOrganizationName("Qtrac Ltd.")
    app.setOrganizationDomain("qtrac.eu")
    app.setApplicationName("Image Changer")
    app.setWindowIcon(QIcon("images/icon.png"))
    form = MainWindow()
    form.show()
    app.exec_()
