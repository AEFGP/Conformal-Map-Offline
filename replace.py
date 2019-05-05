import shutil


filenames = [
    'earth/tx_2_0.jpg',
    'earth/tx_2_1.jpg',
    'earth/tx_3_0.jpg',
    'earth/tx_3_1.jpg',
    'earth/tx_0_0.jpg',
    'earth/tx_0_1.jpg',
    'earth/tx_1_0.jpg',
    'earth/tx_1_1.jpg'
    ]
file = input('<<<').replace("\"",'')
for name in filenames:
    shutil.copy(file,name)
    #shutil.rename(file, file)
