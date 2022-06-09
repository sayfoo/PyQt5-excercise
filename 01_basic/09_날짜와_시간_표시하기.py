from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()
print(f"{now = }")
print(now.toString())

now = QDate.currentDate()
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
print()
print(f"{now.toString(Qt.ISODate) = }")
print(f"{now.toString(Qt.ISODateWithMs) = }")

print(f"{now.toString(Qt.DefaultLocaleLongDate) = }")

time = QTime.currentTime()
print(f"{time.toString()}")

time = QTime.currentTime()
print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))

print(f"{time.toString('hh.mm.ss.zzz')}")
print(f"{time.toString('HH.mm.ss.zzz')}")


datetime = QDateTime.currentDateTime()
print(datetime.toString('d.M.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))
