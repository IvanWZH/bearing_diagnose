import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np
import sys
import csv
import os


dirs_test = os.listdir(r'D:\py-program\phm_zhoucheng\test_set_2\test')
dirs_test.sort(key=lambda x: int(x.split('T')[2][:-4]))
print(dirs_test)
['TEST1.csv', 'TEST2.csv', 'TEST3.csv', 'TEST4.csv', 'TEST5.csv', 'TEST6.csv', 'TEST7.csv', 'TEST8.csv', 'TEST9.csv', 'TEST10.csv', 'TEST11.csv', 'TEST12.csv', 'TEST13.csv', 'TEST14.csv', 'TEST15.csv', 'TEST16.csv', 'TEST17.csv', 'TEST18.csv', 'TEST19.csv', 'TEST20.csv', 'TEST21.csv', 'TEST22.csv', 'TEST23.csv', 'TEST24.csv', 'TEST25.csv', 'TEST26.csv', 'TEST27.csv', 'TEST28.csv', 'TEST29.csv', 'TEST30.csv', 'TEST31.csv', 'TEST32.csv', 'TEST33.csv', 'TEST34.csv', 'TEST35.csv', 'TEST36.csv', 'TEST37.csv', 'TEST38.csv', 'TEST39.csv', 'TEST40.csv', 'TEST41.csv', 'TEST42.csv', 'TEST43.csv', 'TEST44.csv', 'TEST45.csv', 'TEST46.csv', 'TEST47.csv', 'TEST48.csv', 'TEST49.csv', 'TEST50.csv', 'TEST51.csv', 'TEST52.csv', 'TEST53.csv', 'TEST54.csv', 'TEST55.csv', 'TEST56.csv', 'TEST57.csv', 'TEST58.csv', 'TEST59.csv', 'TEST60.csv', 'TEST61.csv', 'TEST62.csv', 'TEST63.csv', 'TEST64.csv', 'TEST65.csv', 'TEST66.csv', 'TEST67.csv', 'TEST68.csv', 'TEST69.csv', 'TEST70.csv', 'TEST71.csv', 'TEST72.csv', 'TEST73.csv', 'TEST74.csv', 'TEST75.csv', 'TEST76.csv', 'TEST77.csv', 'TEST78.csv', 'TEST79.csv', 'TEST80.csv', 'TEST81.csv', 'TEST82.csv', 'TEST83.csv', 'TEST84.csv', 'TEST85.csv', 'TEST86.csv', 'TEST87.csv', 'TEST88.csv', 'TEST89.csv', 'TEST90.csv', 'TEST91.csv', 'TEST92.csv', 'TEST93.csv', 'TEST94.csv', 'TEST95.csv', 'TEST96.csv', 'TEST97.csv', 'TEST98.csv', 'TEST99.csv', 'TEST100.csv', 'TEST101.csv', 'TEST102.csv', 'TEST103.csv', 'TEST104.csv', 'TEST105.csv', 'TEST106.csv', 'TEST107.csv', 'TEST108.csv', 'TEST109.csv', 'TEST110.csv', 'TEST111.csv', 'TEST112.csv', 'TEST113.csv', 'TEST114.csv', 'TEST115.csv', 'TEST116.csv', 'TEST117.csv', 'TEST118.csv', 'TEST119.csv', 'TEST120.csv', 'TEST121.csv', 'TEST122.csv', 'TEST123.csv', 'TEST124.csv', 'TEST125.csv', 'TEST126.csv', 'TEST127.csv', 'TEST128.csv', 'TEST129.csv', 'TEST130.csv', 'TEST131.csv', 'TEST132.csv', 'TEST133.csv', 'TEST134.csv', 'TEST135.csv', 'TEST136.csv', 'TEST137.csv', 'TEST138.csv', 'TEST139.csv', 'TEST140.csv', 'TEST141.csv', 'TEST142.csv']
