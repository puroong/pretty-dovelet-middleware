from app import app
from app.utils.dove_request import DoveRequest

a=DoveRequest()

print(a.login('joon', 'joon0202'))
#print(a.login('puroong','karkar55@'))
print(a.get_stair(1))
print(a.get_stair(1)[10]['title'])
#print(a.get_problem('/30stair/op/op.php?pname=op'))
print(a.submit(a.get_stair(0)[1]['title'], 1, '#include<stdio.h>\r\n\r\nint main(){\r\n printf("234");\r\n return 0;\r\n}'))
