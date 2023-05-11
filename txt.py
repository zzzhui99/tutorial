
'''
处理ESP工具输出，txt改变格式用excel打开
'''

#读写txt
filename=r'D:\0\eCognition\add\2019\cover\t4.Hierarchy_BU.txt'
with open(filename,encoding='utf-8') as file:
     content=file.read()
     print(content.rstrip())     ##rstrip()删除字符串末尾的空行
print(content.replace(',', '\n')) #将','换为'\n'

out_filename='D:\\0\\eCognition\\add\\2019\\cover\\t4.Hierarchy_BU_pro.txt'
with open(out_filename,'w') as f:
	f.write(content.replace(',', '\n'))
