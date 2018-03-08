class person:
	#人类
	def __init__(self,name):
		self.name=name
		self.gun=None		#人手里的枪

	def putBullToClip(self,clip,bullet):
		#老王将子弹保存到弹夹
		clip.baocunBullet(bullet)

	def putClipToGun(self,clip,gun):
		#保存弹夹到枪中
		gun.baocunClip(clip)

	def naqiang(self,gun):
		self.gun=gun

	def koubanji(self,diren):
		#枪开火
		self.gun.fire(diren)
		
class Gun:
	#枪类
	def __init__(self,name):
		self.name=name 			#name  哪种枪
		self.baocun1=None		#弹夹
	#保存弹夹
	def baocunClip(self,clip):
		if not self.baocun1:
			self.baocun1=clip 			#只存一份

	def __str__(self):
		if not self.baocun1:
			return '当前枪的信息为%s,当前有弹夹'%(self.name)
		else:
			return '当前枪的信息为%s,当前没有弹夹'%(self.name)

	def fire(self,diren):

class Clip:
	#弹夹类
	def __init__(self,maxnum):
		self.maxnum=maxnum 
		self.baocun=[]		#保存子弹的容器
	def baocunBullet(self,bullet):
		self.baocun.append(bullet)	#往容器中追加子弹

	def __str__(self):
		return '当前弹夹的状态是%d/%s'%(len(self.baocun),self.maxnum)
class Bullet:
	#子弹类
	def __init__(self,typeBull):	#typeBull 代表子弹的杀伤力	
		self.typeBull=typeBull 

#-----------------------------------------------------------------------

def main():
	#1.有老王这个对象
	laowang=person('老王')
	#2.枪对象
	ak47=Gun('AK47')
	#3.弹夹对象
	clip=Clip(30)
	for i in range(10):
		#4.一堆子弹
		bullet=Bullet(10)
		#5.老王将子弹放到弹夹中
		laowang.putBullToClip(clip,bullet)
	#6.将弹夹放到枪里
	laowang.putClipToGun(clip,ak47)
	#7.有敌人
	gebilaowang=person('隔壁老王')
	#8.老王拿枪
	laowang.naqiang(ak47)
	
	#9.打敌人（扣扳机）
	laowang.koubanji(gebilaowang)

main()