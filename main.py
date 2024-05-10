from Grades import *

#get to git hub
def main():
    application = QApplication([])
    window = Grades()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
