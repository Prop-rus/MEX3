import time
from background_task import background
import shutil




@background()
def deletefile(dir_pat):
    '''deletes uploaded and result files after 2 min delay. Operates in background'''

    time.sleep(120)
    shutil.rmtree(dir_pat)

