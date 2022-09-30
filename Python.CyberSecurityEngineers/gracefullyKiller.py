import signal
import time

class GracefulKillerProcess:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    self.kill_now = True

if __name__ == '__main__':
  killer = GracefulKillerProcess()
  while not killer.kill_now:
    time.sleep(1)
    print("I am still executing ...")
    print("Precc Ctrl+C to stop me")
   
  print("End of the program. I was killed")