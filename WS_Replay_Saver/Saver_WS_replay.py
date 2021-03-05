import os
from datetime import datetime
if __name__ == '__main__':
    replayRepPath = r'C:\Program Files (x86)\Steam\steamapps\common\War Selection\gen\replay.rep'
    replayStatPath = r'C:\Program Files (x86)\Steam\steamapps\common\War Selection\gen\replay.stat'
    folderName = str(datetime.fromtimestamp(int(os.path.getmtime(replayRepPath)))).replace(' ', '_').replace(':','-')
    os.system("mkdir E:\WS_Replay\\{}".format(folderName))
    os.system(r'copy "{}" E:\WS_Replay\{}\replay.rep'.format(replayRepPath, folderName))
    os.system(r'copy "{}" E:\WS_Replay\{}\replay.stat'.format(replayStatPath, folderName))
