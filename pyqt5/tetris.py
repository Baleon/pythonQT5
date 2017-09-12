# -*- coding: utf-8 -*-
import random
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QBasicTimer, Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QFrame, QApplication


class Tetrominoe(object):
    """
    方块的种类
    """
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredShape = 7

    corrdesTable =(
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )

class Shape(object):
    def __init__(self):
        # 初始化方块的四个点
        self.corrds = [[0,0] for i in range(4)]
        self._pieceShape = Tetrominoe.NoShape
        self.corrdesDict = {}
        self.corrdesDict[Tetrominoe.NoShape] = Tetrominoe.corrdesTable[Tetrominoe.NoShape]
        self.corrdesDict[Tetrominoe.ZShape] = Tetrominoe.corrdesTable[Tetrominoe.ZShape]
        self.corrdesDict[Tetrominoe.SShape] = Tetrominoe.corrdesTable[Tetrominoe.SShape]
        self.corrdesDict[Tetrominoe.LineShape] = Tetrominoe.corrdesTable[Tetrominoe.LineShape]
        self.corrdesDict[Tetrominoe.TShape] = Tetrominoe.corrdesTable[Tetrominoe.TShape]
        self.corrdesDict[Tetrominoe.SquareShape] = Tetrominoe.corrdesTable[Tetrominoe.SquareShape]
        self.corrdesDict[Tetrominoe.LShape] = Tetrominoe.corrdesTable[Tetrominoe.LShape]
        self.corrdesDict[Tetrominoe.MirroredShape] = Tetrominoe.corrdesTable[Tetrominoe.MirroredShape]

    @property
    def Shape(self):
        return self._pieceShape

    @Shape.setter
    def Shape(self, shape:Tetrominoe):
        """
        设置方块类型
        """
        for i in range(4):
            for j in range(2):
                self.corrds[i][j] = self.corrdesDict[shape][i][j]
        self._pieceShape = shape

    def setRandomShape(self):
        self.Shape = random.randint(1,7)

    def x(self, index):
        return self.corrds[index][0]

    def y(self,index):
        return self.corrds[index][1]

    def setX(self, index, x):
        self.corrds[index][0] = x

    def setY(self, index, y):
        self.corrds[index][1] = y

    def minX(self):
        m = self.corrds[0][0]

        for i in range(4):
            m = min(m, self.corrds[i][0])

        return m

    def maxX(self):
        m = self.corrds[0][0]

        for i in range(4):
            m = max(m, self.corrds[i][0])

        return m

    def minY(self):
        m = self.corrds[0][0]

        for i in range(4):
            m = min(m, self.corrds[i][1])

        return m

    def maxY(self):
        m = self.corrds[0][0]

        for i in range(4):
            m = max(m, self.corrds[i][1])

        return m

    def rotateLeft(self):
        """
        逆时针旋转方框
        :return:Shape
        """
        if self.Shape == Tetrominoe.SquareShape:
            return self
        result = Shape()
        result.Shape = self.Shape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))
        print("up key down:")
        print("before: %s : " % self.corrds)
        print("After:  %s : " % result.corrds)
        return result

    def rotateRight(self):
        if self.Shape == Tetrominoe.SquareShape:
            return self
        result = Shape()
        result.Shape = self.Shape

        return result

class Board(QFrame):
    # 网格的宽度
    BoardWidth = 10
    # 网格的高度
    BoardHeight = 22
    Speed = 300

    def __init__(self):
        super(Board, self).__init__()
        self.initBoard()

    def initBoard(self):
        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False
        self.removedLines = 0
        self.boards = {}

        self.curX,self.curY = 0,0

        self.hasBeginGame = False
        self.isPause = False
        self.curPiece = None

    @property
    def SquareWidth(self):
        return self.contentsRect().width() // Board.BoardWidth

    @property
    def SquareHeight(self):
        return self.contentsRect().height() // Board.BoardHeight

    def shapeAt(self, x, y):
        if (y * Board.BoardWidth) + 1 in self.boards.keys():
            print('in')
        return self.boards.get((y * Board.BoardWidth) + x, 0)

    def setShapeAt(self, x, y, shape):
        self.boards[(y * Board.BoardWidth) + x] = shape

    def start(self):
        """
        开始游戏，程序在更启动的情况下没有方框产生，当调用这个方法的时候会产生新的方框
        :return:None
        """
        # 如果系统在启动之后是不能够重新开始游戏的
        if self.hasBeginGame:
            return
        # 将游戏是否开启反置
        self.hasBeginGame = not self.hasBeginGame

        # 此时没有需要清除的完成的行
        self.isWaitingAfterLine = False
        # 完成的行数为0
        self.removedLines = 0

        # 创建新的方框，时钟开启
        self.newPiece()
        self.timer.start(Board.Speed, self)

    def pause(self):
        """
        暂停游戏
        """
        # 如果游戏没有开启，那么暂停是没有意义的
        if not self.hasBeginGame:
            return
        # 将游戏是否暂停状态反置
        self.isPause = not self.isPause

        if self.isPause:
            self.timer.start(Board.Speed, self)
        else:
            self.timer.stop()

        self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QPainter(self)

        # 获取QFrame的矩形范围
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.SquareHeight
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                #shape = self.shapeAt(j,Board.BoardHeight - i -1)
                shape = self.shapeAt(j, Board.BoardHeight - i -1)
                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,rect.left() + j * self.SquareWidth,boardTop + i*self.SquareHeight,shape)



        if self.curPiece != None and self.curPiece.Shape != Tetrominoe.NoShape:
            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY + self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.SquareWidth, boardTop + (Board.BoardHeight - y -1) * self.SquareHeight,
                                self.curPiece.Shape)

    def timerEvent(self, event: 'QTimerEvent'):
        if event.timerId() == self.timer.timerId():
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
        else:
            super(Board, self).timerEvent(event)

    def oneLineDown(self):
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self):
        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY + self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.Shape)

        self.removeFullLines()
        if not self.isWaitingAfterLine:
            self.newPiece()

    def removeFullLines(self):
        self.isWaitingAfterLine = True
        rowsToRemove = []
        numFullLines = 0

        #循环行
        for col in range(Board.BoardHeight):
            num = 0
            # 循环列
            for row in range(Board.BoardWidth):
                if not self.shapeAt(row, col) == Tetrominoe.NoShape:
                    num = num + 1
            if num == 10:
                rowsToRemove.append(col)

        # 将列表进行翻转，目的是从最下面开始移除
        rowsToRemove.reverse()

        for line in rowsToRemove:
            for col in range(Board.BoardHeight):
                for row in range(Board.BoardWidth):
                    self.setShapeAt(row, col, self.shapeAt(row, col + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.removedLines = self.removedLines + numFullLines
            self.curPiece.Shape = Tetrominoe.NoShape
            self.update()

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        key = event.key()

        if key == Qt.Key_1:
            self.start()

        elif key == Qt.Key_2:
            self.pause()

        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

    def newPiece(self):
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
        if not self.tryMove(self.curPiece, self.curX, self.curY):
            return

    def tryMove(self, newPiece, newX, newY):
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY + newPiece.y(i)

            # 判断在移动或者下落的过程中是否到达范围的边界
            if x < 0 or x > Board.BoardWidth or y < 0 or y > Board.BoardHeight:
                return False

            # 判断在下落的过程中每一个方框的下面是否已经存在方框
            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True

    def drawSquare(self, painter:QPainter, x, y, shape:Shape):
        colorTable =  [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x+1,y+1,self.SquareWidth - 2, self.SquareHeight - 2, color)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Board()
    s.show()
    sys.exit(app.exec_())
