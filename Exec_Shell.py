import threading
import sys
import time

class ExecuteShell(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        self.running = True
        while self.running:
            try:
                i = input(">>> ")
                if self.running:
                    exec(i)
            except KeyboardInterrupt:
                self.running = False
                time.sleep(0.1)
            except:
                print(sys.exc_info()[1])
                
    def stop(self):
        self.running = False


if __name__ == "__main__":
    ExecShell = ExecuteShell()
    ExecShell.start()

    while ExecShell.running:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            ExecShell.running = False
            time.sleep(0.1)
