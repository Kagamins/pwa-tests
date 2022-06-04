import os
from pathlib import Path 
import openpyxl
import shutil
from shutil import ignore_patterns ,copytree
n = 0
s = 0
S = 0
a = 0
A = 0
v = 0
wb = openpyxl.load_workbook('test-n.xlsx')
src_a_10_a = r"A-group/10 A/"
src_a_10_b = r"A-group/10 B/"
src_b_10_a = r"B-group/10 A/"
src_b_10_b = r"B-group/10 A/"
src_a_12_a = r"A-group/12 A/"
src_a_12_b = r"A-group/12 B/"
src_b_12_a = r"B-group/12 A/"
src_b_12_b = r"B-group/12 B/"
src_a_11_a = r"A-group/11 A/"
src_a_11_b = r"A-group/11 B/"
src_b_11_a = r"B-group/11 A/"
src_b_11_b = r"B-group/11 B/"
worksheets = wb.worksheets
for sheet in worksheets:
    rows = [tuple(cell.value for cell in row if cell.value is not None) for row in sheet] # convert the cells to text

    dirnames = list()
    

    for row in rows[5:]: # [5:], ignore column headers for better looping 
        dirnames.append(''.join(str(row[:6]))) # joins the Brand, Family, and Ref columns

    while("()" in dirnames):
        dirnames.remove('()')
    
    dirnames.remove("('عــــــــدد الغياب : ',)")
    dirnames.remove("('عــــــدد الحضور : ',)")    
    dirnames.remove("('العدد الإجمالي :',)")  
    dirnames.remove("('توقيع المعلم',)")

    for i in range(len(dirnames)):
        
        dir = dirnames[i].strip()
        dir = dir.replace(":",'')
        dir = dir.replace("(",'')
        dir = dir.replace(")",'')
        dir = dir.replace(",",'')
        dir = dir.replace("'",'')
        dir = dir.replace(".0",'')
        dir = dir.strip()
        grp = dir[-1]
        test = dir[0]
        print('Group is  : '+grp+' Test match : '+test)
        sub = dir[-4:]
        dir = dir.replace('a','')
        dir = dir.replace('b','')
        
       
        if "علمي"in dir:
            dir = dir.replace(dir[-11:],'')
        if "أدبي"in dir:
            dir = dir.replace(dir[-12:],'')
        if '10' in dir:
            dir = dir.replace(dir[-7:],'')
        dir = dir.replace(sub,'')
        #if not(os.path.exists(sheet.title+'/'+sub+'/'+dir)):
        #os.makedirs(sheet.title+'/'+sub+'/'+dir) # create the dir
        #os.chdir(sheet.title+'/'+sub) # enter the dir
        print('creating', sheet.title+'/'+sub+'/'+dir)

        dst_path = sheet.title+'/'+sub+'/'+dir+'/'
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
        if sheet.title == 'الحادي عشر ادبي':
            a = a+1
            if test == 'a' and grp=='أ':
                shutil.copytree(src_a_11_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))                
            elif test == 'b' and grp=='أ' :
                shutil.copytree(src_a_11_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'a' and grp=='ب' :
                shutil.copytree(src_b_11_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'b' and grp=='ب' :
                shutil.copytree(src_b_11_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))

        if sheet.title == 'الثاني عشر ادبي':
            A = A+1
            if test == 'a' and grp=='أ':
                shutil.copytree(src_a_12_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))                
            elif test == 'b' and grp=='أ' :
                shutil.copytree(src_a_12_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'a' and grp=='ب' :
                shutil.copytree(src_b_12_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'b' and grp=='ب' :
                shutil.copytree(src_b_12_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
                
        if sheet.title == 'الحادي عشر علمي':
            s = s+1
            if test == 'a' and grp=='أ':
                shutil.copytree(src_a_11_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))                
            elif test == 'b' and grp=='أ' :
                shutil.copytree(src_a_11_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'a' and grp=='ب' :
                shutil.copytree(src_b_11_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'b' and grp=='ب' :
                shutil.copytree(src_b_11_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))

        if sheet.title == 'الثاني عشر علمي':
            S = S+1
            if test == 'a' and grp=='أ':
                shutil.copytree(src_a_12_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))                
            elif test == 'b' and grp=='أ' :
                shutil.copytree(src_a_12_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'a' and grp=='ب' :
                shutil.copytree(src_b_12_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'b' and grp=='ب' :
                shutil.copytree(src_b_12_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
        if sheet.title =='العاشر':
            v =v+1
            if test == 'a' and grp=='أ':
                shutil.copytree(src_a_10_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))                
            elif test == 'b' and grp=='أ' :
                shutil.copytree(src_a_10_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'a' and grp=='ب' :
                shutil.copytree(src_b_10_a,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
            elif test == 'b' and grp=='ب' :
                shutil.copytree(src_b_10_b,dst_path,ignore=ignore_patterns('_derived', 'tmp*'))
        n=n+1
   

        

        print(str(n),'folders created')
    print (str(n),'إجمالي الطلبه')
    print(str(v),'الصف العاشر :')
    print(str(s),' الصف الحادي عشر  علمي : ')
    print(str(S),'الصف الثاني عشر علمي : ')
    print(str(a),' الصف الحادي عشر  أدبي : ')
    print(str(A),'الصف الثاني عشر أدبي : ')
        #os.chdir('..') # back out of the dir