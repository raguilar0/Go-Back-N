import threading
def worker(count):
    if count == 1:
    	print "Este es el %s trabajo que hago hoy para Genbeta Dev" % count
    return
threads = list()
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()