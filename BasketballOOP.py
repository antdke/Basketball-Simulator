class Player:

	def __init__(self, first, last, height, weight, agility, strength):
		self.first = first
		self.last = last
		self.height = height # min 185cm:6ft - mid 200cm:6'6ft - max 220cm:7'2ft
		self.weight = weight # min 175lbs:80kg - mid 220lbs:100kg - max 320lbs:145kg
		self.agility = agility
		self.strength = strength
		# height, strength, weight, agility = numbers, for easy comparison

	def fullname(self):
		self.name = "{} {}".format(self.first, self.last)


	def off_rating(self, dribble, jumpshot, layup, assist): 
		# right now itll be a static method cuz idk how to incorporate 
		# info with rating; but rating will be average of skill points.
		# Rating will be 1 - 10 for simplicity right now
		self.dribble = dribble
		self.jumpshot = jumpshot
		self.layup = layup
		self.assist = assist
		total_off_rating = dribble + jumpshot + layup + assist
		avg_off_rating = (total_off_rating / 4.0)
		return avg_off_rating 

	def def_rating(self, steal, block):
		self.steal = steal
		self.block = block
		total_def_rating = steal + block
		avg_def_rating = total_def_rating / 2.0
		return avg_def_rating



#I am creating six players to try 3-on-3

#player 1
player_1 = Player('Tony', 'Douglass', 205, 100, 6, 6) # average player (sf) ht: 6'6 wt: 220
player_1.off_rating(6, 7, 7, 6) # avg off
player_1.def_rating(5, 5) # avg def 

#player 2
player_2 = Player('Greg', 'Johnson', 208, 125, 4, 8) # strong player (pf)
player_2.off_rating(4, 5, 8, 4)
player_2.def_rating(3, 7)

#player 3
player_3 = Player('Jack', 'Heckler', 185, 90, 10, 2) # quick player (pg)
player_3.off_rating(8, 8, 3, 8)
player_3.def_rating(9, 2)

#player 4
player_4 = Player('Fred', 'Ottoman', 215, 300, 2, 10) # physical player (c)
player_4.off_rating(2, 4, 9, 3)
player_4.def_rating(2, 9)

#player 5
player_5 = Player('Anthony', 'Dike', 200, 105, 9, 8) # all star player (sg)
player_5.off_rating(9, 8, 9, 8)
player_5.def_rating(9, 6)

#player 6
player_6 = Player('Kipp', 'Anderson', 205, 110, 4, 4) # ok player (sf)
player_6.off_rating(6, 6, 5, 5)
player_6.def_rating(3, 3)
