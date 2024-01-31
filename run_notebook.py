import time
from subprocess import run

notebook_path = "DownloadingBuoyImages.ipynb"

while True:
    # Run the Jupyter Notebook using nbconvert in execute mode
    run(["jupyter", "nbconvert", "--to", "notebook", "--execute", notebook_path])

    print("running!")
    # Wait for 5 minutes before the next execution
    time.sleep(60)  # 300 seconds = 5 minutes