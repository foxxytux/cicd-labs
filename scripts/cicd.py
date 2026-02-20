from subprocess import run
import subprocess
from os import listdir
from os.path import isfile, join
import os
import time
import shutil
import filecmp
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)

change = True
base_path = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(base_path, "../src/")
prod_dir = os.path.join(base_path, "../production/")

while True:
    print(f"[{time.strftime('%H:%M:%S')}] Monitoring for changes...", end="\r")
    onlyfiles = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
    logging.info("Checking for changes...")
    for f in onlyfiles:
        if run(["flake8", (src_dir+f)], capture_output=True, text=True).returncode != 0:
            print("Errors found in Python file:" + f + "!")
            logging.error(f"CI Failed for {f}!")
        else:
            if os.path.exists(prod_dir+f):
                if not filecmp.cmp(src_dir+f,prod_dir+f, shallow=False):
                    shutil.copyfile(src_dir+f,prod_dir+f)
                    change = True
            else:
                shutil.copyfile(src_dir+f,prod_dir+f)
                change = True
    if change:
        try:
            process.kill()
        except Exception as e:
            logging.error(f"CD Failed because of: {e}!")
            print("Program is starting or an error occured!: ",e)
        process = subprocess.Popen(["bash","run.sh"])
        print("Changes are integrated.")
        logging.info("Changes are integrated...")
        change = False
    time.sleep(5)
