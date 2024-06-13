import subprocess
from update_lottery import update_lottery
from update_predict import PredictGame, update_predict
import os
import datetime as dt
import time

base_path = os.path.dirname(os.path.realpath(__file__))

def commit():
  subprocess.call(['sh', f'{base_path}/update-git.sh'])

delay = 600
if __name__ == "__main__":
  # update(config=testnet, update_all=False)
  while True:
    print("Updating PS_MAINNET...")
    update_predict(game=PredictGame.PS_MAINNET, update_all=False)
    print("Updating PRDT_MAINNET...")
    update_predict(game=PredictGame.PRDT_MAINNET, update_all=False)
    print("Updating lottery...")
    update_lottery(update_all=False)
    print("Updating commit...")
    commit()
    print(f"Finished updates, waiting {delay} seconds...")
    time.sleep(delay)
    
