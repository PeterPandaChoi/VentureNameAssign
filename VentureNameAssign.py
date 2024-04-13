import os
import shutil
import fnmatch

#현재 폴더의 경로
filePath = os.getcwd()
#현재 프로그램의 이름(사용자가 이름을 바꿨을 경우를 위한)
thisProgramName=os.path.basename(__file__)
#현재 폴더에 있는 파일들을 리스트로 저장
file_names = os.listdir(filePath)
#그 리스트에서 현재 프로그램을 뺌
file_names.remove(thisProgramName)

#'정리'라는 폴더가 없으면 만들고, 있다면 리스트에서 '정리'를 빼서 버그 제거
if not (os.path.isdir('.\정리')):
  os.makedirs('정리') 
else:
  file_names.remove('정리')
category=''


print("\n____________________파일을 아래와 같이 변경____________________\n")
for file in file_names:
  #파일의 이름을 출력해주고
  print(file)

  #해당하는 경우에 변경을 해주도록 카테고리를 설정
  if fnmatch.fnmatch(file,'*중소기업*'):
    category='[필수] 1.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*사업자*'):
    category='[필수] 2.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*법인등기*'):
    category='[필수] 3.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*과세표준*'):
    category='[필수] 4.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*재무제표*'):
    category='[필수] 5.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*고용보험*'):
    category='[필수] 6.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*4대*'):
    category='[필수] 7.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*사대보험*'):
    category='[필수] 7.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*자격득실*'):
    category='[추가] 1.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*주주명부*'):
    category='[추가] 2.'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*연구*'):
    category='[추가] 3.'
    print('변경->'+category+file+'\n')
  else:
    category=''
    print(' ---> 변경되지않음')

    #마지막으로 정리 폴더에 파일을 카피해주면 끝!
  shutil.copyfile(filePath+'/'+file, filePath+'/정리/'+category+file)


print("\n____________________파일을 위 와 같 이 변경____________________\n")