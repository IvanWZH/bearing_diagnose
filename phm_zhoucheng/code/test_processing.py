import pandas as pd
import os

def print_label(inputfile,outputfile,label):
    df = pd.read_csv(inputfile)
    df['label'] = label
    df.to_csv(outputfile,index=False)

dirs_test = os.listdir(r'D:\py-program\phm_zhoucheng\test_set\test')

inputfile_path = [os.path.join(r'D:\py-program\phm_zhoucheng\test_set\test', name) for name in dirs_test]

outputfile_path = [os.path.join(r'D:\py-program\phm_zhoucheng\test_set\test_with_label',name) for name in dirs_test]

print_label(inputfile_path[0],outputfile_path[0],1)
print_label(inputfile_path[1],outputfile_path[1],1)
print_label(inputfile_path[2],outputfile_path[2],1)
print_label(inputfile_path[3],outputfile_path[3],2)
print_label(inputfile_path[4],outputfile_path[4],3)
print_label(inputfile_path[5],outputfile_path[5],2)
print_label(inputfile_path[6],outputfile_path[6],2)
print_label(inputfile_path[7],outputfile_path[7],0)
print_label(inputfile_path[8],outputfile_path[8],2)
print_label(inputfile_path[9],outputfile_path[9],1)
print_label(inputfile_path[10],outputfile_path[10],2)
print_label(inputfile_path[11],outputfile_path[11],3)
print_label(inputfile_path[12],outputfile_path[12],3)
print_label(inputfile_path[13],outputfile_path[13],1)