#!/user/bin python
# -*- coding:utf-8 -*- 
def main():
	content = []
	for y in range(30,-30,-1):
		for x in range(-30,30):
			subcontent = []
			if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0:
				subcontent.append('Love'[(x-y)%4])
			else:
				subcontent.append(' ')
			content.append(''.join(subcontent))
		content.append('\n')
	print(''.join(content))

if __name__ == '__main__':
	main()

