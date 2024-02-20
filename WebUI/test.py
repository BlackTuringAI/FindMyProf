import shutil
from pathlib import Path

s = Path(__file__).parent / 'testtttt'
d = Path(__file__).parent / 'testt2' / 'testtttt'
# d.rmdir()
# for i in s.iterdir():
shutil.rmtree(str(d))
# print(i)




