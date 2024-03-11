# import shutil
# from pathlib import Path

# s = Path(__file__).parent / 'testtttt'
# d = Path(__file__).parent / 'testt2' / 'testtttt'
# # d.rmdir()
# # for i in s.iterdir():
# shutil.rmtree(str(d))
# # print(i)


# num_16 = '0x1234abcd'
num_16 = '0x1234b000'
num_10 = int(num_16, 16)
num_2 = bin(num_10)

print(num_2, num_10, num_16)






