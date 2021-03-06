import pygame
import sys
import random

pygame.init()
pygame.font.init()

pygame.display.set_caption('LifeBox')

graph_mode = 0
real_mode = 1
gradient_mode = 1

if graph_mode == 1:
	screen = pygame.display.set_mode((1000,600))
	x_array = 32
	y_array = 32
	circle_size = 5
else:
	# size for full HD screen
	screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	x_array = 95
	y_array = 55
	circle_size = 9

textfont = pygame.font.SysFont('arial',30)

# colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
magenta = (255,0,255)
white = (255,255,255)
black = (0,0,0)
darkgrey = (30,30,30)
lightgrey = (200,200,200)

# fps management
clock = pygame.time.Clock()

# species matrix
t, w, h = 3,x_array, y_array
# age 0 at z
# energy 1 at z
specie1 = [[[0 for x in range(t)] for y in range(h)] for z in range(w)]
specie2 = [[[0 for x in range(t)] for y in range(h)] for z in range(w)]
plants = [[[0 for x in range(t)] for y in range(h)] for z in range(w)]

# mask
for x in range(0,10):
	for y in range(0,10):
		specie1[x][y][2] = 1
		specie2[x][y][2] = 1
		plants[x][y][2] = 1


# [x][y] [0]:age [1]:energy [2]:mask

# graph arrays

specie1_Iarray = [0 for x in range(200)]
specie2_Iarray = [0 for x in range(200)]
plants_Iarray = [0 for x in range(200)]
specie1_Earray = [0 for x in range(200)]
specie2_Earray = [0 for x in range(200)]
plants_Earray = [0 for x in range(200)]

# species variables

PLANTS_LIFE_EXPECTANCY = 100
PLANTS_RANDOM_BORN_CHANCES = 1000 # high is less chances
PLANTS_NEARBORN_CHANCES = 100
PLANTS_RANDOM_DIE_CHANCES = 2
PLANTS_ENERGY_BASE_PER_CYCLE = 5

#yellow
SPECIE1_LIFE_EXPECTANCY = 200
SPECIE1_RANDOM_BORN_CHANCES = 5000
SPECIE1_NEARBORN_CHANCES = 12
SPECIE1_RANDOM_DIE_CHANCES = 2
SPECIE1_ENERGY_BASE = 20
SPECIE1_ENERGY_NEEDED_PER_CYCLE = 5
SPECIE1_MAX_ENERGY_RECOLECTED_PER_CYCLE = 7
SPECIE1_ENERGY_TO_REPLICATE = 5

#blue
SPECIE2_LIFE_EXPECTANCY = 200
SPECIE2_RANDOM_BORN_CHANCES = 5000
SPECIE2_NEARBORN_CHANCES = 12
SPECIE2_RANDOM_DIE_CHANCES = 2
SPECIE2_ENERGY_BASE = 20
SPECIE2_ENERGY_NEEDED_PER_CYCLE = 5
SPECIE2_MAX_ENERGY_RECOLECTED_PER_CYCLE = 7
SPECIE2_ENERGY_TO_REPLICATE = 5

specie2_individuals = 0
specie1_individuals = 0
plants_individuals = 0

while (True):
	msElapsed = clock.tick(20)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
        		pygame.quit()
	 		sys.exit()

	# init totals
	plants_last_individuals = plants_individuals
        specie2_last_individuals = specie2_individuals
        specie1_last_individuals = specie1_individuals
	specie2_individuals = 0
	specie1_individuals = 0
	plants_individuals = 0
	specie2_energy = 0
	specie1_energy = 0
	plants_energy = 0

	screen.fill(black)

	for x in range(0,x_array):
		# adjacent coordinates
		xp = (x+1)
		if xp >= x_array:
			xp = x_array - 1
		xm = (x-1)
		if xm < 0:
			xm = 0
		for y in range(0,y_array):
			# calculations
			# adjacent coordinates
			yp = (y+1)
			if yp >= y_array:
				yp = y_array - 1
			ym = (y-1)
			if ym < 0:
				ym = 0
			# count the number of currently live neighbouring cells
  			plants_neighbours = 0
  			specie1_neighbours = 0
  			specie2_neighbours = 0
  			# [Plants]

  			if plants[x][y][0] == 0 and plants[xm][y][0] > 0:
				plants_neighbours += 1
  			if plants[x][y][0] == 0 and plants[xp][y][0] > 0:
				plants_neighbours += 1
  			if plants[x][y][0] == 0 and plants[xm][ym][0] > 0:
				plants_neighbours += 1
  			if plants[x][y][0] == 0 and plants[x][ym][0] > 0:
				plants_neighbours += 1
  			if plants[x][y][0] == 0 and plants[xp][ym][0] > 0:
				plants_neighbours += 1
  			if plants[x][y][0] == 0 and plants[xm][yp][0] > 0:
				plants_neighbours += 1
  			if plants[x][y][0] == 0 and plants[x][yp][0] > 0:
				plants_neighbours += 1
  			if plants[x][y][0] == 0 and plants[xp][yp][0] > 0:
				plants_neighbours += 1
  			# [Specie1]
  			if specie1[x][y][0] == 0 and specie1[xm][y][0] > 0:
				specie1_neighbours += 1
  			if specie1[x][y][0] == 0 and specie1[xp][y][0] > 0:
				specie1_neighbours += 1
  			if specie1[x][y][0] == 0 and specie1[xm][ym][0] > 0:
				specie1_neighbours += 1
  			if specie1[x][y][0] == 0 and specie1[x][ym][0] > 0:
				specie1_neighbours += 1
  			if specie1[x][y][0] == 0 and specie1[xp][ym][0] > 0:
				specie1_neighbours += 1
  			if specie1[x][y][0] == 0 and specie1[xm][yp][0] > 0:
				specie1_neighbours += 1
  			if specie1[x][y][0] == 0 and specie1[x][yp][0] > 0:
				specie1_neighbours += 1
  			if specie1[x][y][0] == 0 and specie1[xp][yp][0] > 0:
				specie1_neighbours += 1
  			# [Specie2]
  			if specie2[x][y][0] == 0 and specie2[xm][y][0] > 0:
				specie2_neighbours += 1
  			if specie2[x][y][0] == 0 and specie2[xp][y][0] > 0:
				specie2_neighbours += 1
  			if specie2[x][y][0] == 0 and specie2[xm][ym][0] > 0:
				specie2_neighbours += 1
  			if specie2[x][y][0] == 0 and specie2[x][ym][0] > 0:
				specie2_neighbours += 1
  			if specie2[x][y][0] == 0 and specie2[xp][ym][0] > 0:
				specie2_neighbours += 1
  			if specie2[x][y][0] == 0 and specie2[xm][yp][0] > 0:
				specie2_neighbours += 1
  			if specie2[x][y][0] == 0 and specie2[x][yp][0] > 0:
				specie2_neighbours += 1
  			if specie2[x][y][0] == 0 and specie2[xp][yp][0] > 0:
				specie2_neighbours += 1

			# [plants logic]

			# if old, plant dies
			if plants[x][y][0] >= PLANTS_LIFE_EXPECTANCY:
				plants[x][y][0] = 0
				plants[x][y][1] = 0
			# if no energy, plant dies
			if plants[x][y][0] > 0 and plants[x][y][0] < PLANTS_LIFE_EXPECTANCY and plants[x][y][1] <= 0:
 				plants[x][y][0] = 0
				plants[x][y][1] = 0
			# plant grows
			if plants[x][y][0]>0 and plants[x][y][0] < PLANTS_LIFE_EXPECTANCY:
 				plants[x][y][0] += 1
				plants[x][y][1] = plants[x][y][1]+PLANTS_ENERGY_BASE_PER_CYCLE
				plants_individuals += 1
				plants_energy += plants[x][y][1]
			# plant reproduction
                        if plants[x][y][0] == 0 and plants_neighbours > 0 and plants[x][y][2] == 0:
                                random_number = random.randint(1,PLANTS_NEARBORN_CHANCES)
                                if random_number == 1:
                                        plants[x][y][0] = 1
                                        plants[x][y][1] = PLANTS_ENERGY_BASE_PER_CYCLE
                                        plants_individuals += 1
                                        plants_energy += plants[x][y][1]
			# spontaneous generation
			if plants[x][y][0] == 0 and plants_neighbours == 0 and plants[x][y][2] == 0 and ((plants_last_individuals == 0 and plants_individuals == 0 and real_mode == 1) or real_mode == 0):
				random_number = random.randint(1,PLANTS_RANDOM_BORN_CHANCES)
				if random_number == 1:
					plants[x][y][0] = 1
					plants[x][y][1] = PLANTS_ENERGY_BASE_PER_CYCLE
					plants_individuals += 1
					plants_energy += plants[x][y][1]

			# [specie1 logic]

			# individual alive
			if specie1[x][y][0] > 0:
				#print "("+str(x)+","+str(y)+") is alive"
				# try to eat
  				if plants[x][y][1] > 0:
  					total_energy=0
  					if plants[x][y][1] > SPECIE1_MAX_ENERGY_RECOLECTED_PER_CYCLE:
						total_energy = SPECIE1_MAX_ENERGY_RECOLECTED_PER_CYCLE
						plants[x][y][1] = plants[x][y][1] - SPECIE1_MAX_ENERGY_RECOLECTED_PER_CYCLE
  					else:
						total_energy = plants[x][y][1]
						plants[x][y][1] = 0
  					specie1[x][y][1] = specie1[x][y][1] + total_energy
					#print "("+str(x)+","+str(y)+") eats"
  				# grow and decrease energy
  				specie1[x][y][0] += 1
  				specie1[x][y][1] = specie1[x][y][1] - SPECIE1_ENERGY_NEEDED_PER_CYCLE
				#print "("+str(x)+","+str(y)+") grows"
 				# die if no energy
				if specie1[x][y][1] < 0:
					specie1[x][y][1] = 0
					specie1[x][y][0] = 0
					#print "("+str(x)+","+str(y)+") dies"
  				# try to replicate
  				if specie1[x][y][1] > SPECIE1_ENERGY_TO_REPLICATE and specie1[x][y][2] == 0:
  					available_spots = [0 for numspots in range(8)]
  					pos=0
  					random_number = random.randint(1,SPECIE1_NEARBORN_CHANCES)
  					if specie1[xm][y][0] == 0:
						available_spots[pos] = 1
						pos += 1
  					if specie1[xp][y][0] == 0:
						available_spots[pos] = 2
						pos += 1
  					if specie1[xm][ym][0] == 0:
						available_spots[pos] = 3
						pos += 1
  					if specie1[x][ym][0] == 0:
						available_spots[pos] = 4
						pos += 1
  					if specie1[xp][ym][0] == 0:
						available_spots[pos] = 5
						pos += 1
  					if specie1[xm][yp][0] == 0:
						available_spots[pos] = 6
						pos += 1
  					if specie1[x][yp][0] == 0:
						available_spots[pos] = 7
						pos += 1
 					if specie1[xp][yp][0] == 0:
						available_spots[pos] = 8
						pos += 1
  					if pos > 0:
  						rand_pos=random.randint(0,pos-1)
						if random_number == 1:
							#print "ready to reproduce at ("+str(xm)+","+str(ym)+") - ("+str(xp)+","+str(yp)+") - center ("+str(x)+","+str(y)+")"
							if available_spots[rand_pos] == 1:
								specie1[xm][y][0] = 1
								specie1[xm][y][1] = SPECIE1_ENERGY_BASE
								#print "("+str(xm)+","+str(y)+") born"
							if available_spots[rand_pos] == 2:
                                                                specie1[xp][y][0] = 1
                                                                specie1[xp][y][1] = SPECIE1_ENERGY_BASE
								#print "("+str(xp)+","+str(y)+") born"
							if available_spots[rand_pos] == 3:
                                                                specie1[xm][ym][0] = 1
                                                                specie1[xm][ym][1] = SPECIE1_ENERGY_BASE
								#print "("+str(xm)+","+str(ym)+") born"
							if available_spots[rand_pos] == 4:
                                                                specie1[x][ym][0] = 1
                                                                specie1[x][ym][1] = SPECIE1_ENERGY_BASE
								#print "("+str(x)+","+str(ym)+") born"
							if available_spots[rand_pos] == 5:
                                                                specie1[xp][ym][0] = 1
                                                                specie1[xp][ym][1] = SPECIE1_ENERGY_BASE
								#print "("+str(xp)+","+str(ym)+") born"
							if available_spots[rand_pos] == 6:
                                                                specie1[xm][yp][0] = 1
                                                                specie1[xm][yp][1] = SPECIE1_ENERGY_BASE
								#print "("+str(xm)+","+str(yp)+") born"
							if available_spots[rand_pos] == 7:
                                                                specie1[x][yp][0] = 1
                                                                specie1[x][yp][1] = SPECIE1_ENERGY_BASE
								#print "("+str(x)+","+str(yp)+") born"
							if available_spots[rand_pos] == 8:
                                                                specie1[xp][yp][0] = 1
                                                                specie1[xp][yp][1] = SPECIE1_ENERGY_BASE
								#print "("+str(xp)+","+str(yp)+") born"
							#print "end of reproduction"
  				# die if too old
  				if specie1[x][y][0] > SPECIE1_LIFE_EXPECTANCY:
					specie1[x][y][1] = 0
					specie1[x][y][0] = 0
					#print "("+str(x)+","+str(y)+") dies"
				specie1_individuals += 1
				specie1_energy += specie1[x][y][1]
			# if no individual is alive, random born to avoid extintion
  			if specie1[x][y][0] == 0 and specie1_neighbours==0 and specie1[x][y][2] == 0 and ((specie1_last_individuals == 0 and specie1_individuals == 0 and real_mode == 1) or real_mode == 0):
  				random_number = random.randint(1,SPECIE1_RANDOM_BORN_CHANCES)
  				if random_number==1:
					specie1[x][y][0] = 1
					specie1[x][y][1] = SPECIE1_ENERGY_BASE
					#print "("+str(x)+","+str(y)+") random born"
					specie1_individuals += 1
					specie1_energy += specie1[x][y][1]

			# [species 2 logic]

			# individual alive
                        if specie2[x][y][0] > 0:
                                # try to eat
                                if plants[x][y][1] > 0:
                                        total_energy=0
                                        if plants[x][y][1] > SPECIE2_MAX_ENERGY_RECOLECTED_PER_CYCLE:
                                                total_energy = SPECIE2_MAX_ENERGY_RECOLECTED_PER_CYCLE
                                                plants[x][y][1] = plants[x][y][1] - SPECIE2_MAX_ENERGY_RECOLECTED_PER_CYCLE
                                        else:
                                                total_energy = plants[x][y][1]
                                                plants[x][y][1] = 0
                                        specie2[x][y][1] = specie2[x][y][1] + total_energy
                                # grow and decrease energy
                                specie2[x][y][0] += 1
                                specie2[x][y][1] = specie2[x][y][1] - SPECIE2_ENERGY_NEEDED_PER_CYCLE
                                # die if no energy
                                if specie2[x][y][1] < 0:
                                         specie2[x][y][1] = 0
                                         specie2[x][y][0] = 0
				# try to replicate
                                if specie2[x][y][1] > SPECIE2_ENERGY_TO_REPLICATE and specie2[x][y][2] == 0:
                                        available_spots = [0 for numspots in range(8)]
                                        pos=0
                                        random_number = random.randint(1,SPECIE2_NEARBORN_CHANCES)
                                        if specie2[xm][y][0] == 0:
                                                available_spots[pos] = 1
                                                pos += 1
                                        if specie2[xp][y][0] == 0:
                                                available_spots[pos] = 2
                                                pos += 1
                                        if specie2[xm][ym][0] == 0:
                                                available_spots[pos] = 3
                                                pos += 1
                                        if specie2[x][ym][0] == 0:
                                                available_spots[pos] = 4
                                                pos += 1
                                        if specie2[xp][ym][0] == 0:
                                                available_spots[pos] = 5
                                                pos += 1
                                        if specie2[xm][yp][0] == 0:
                                                available_spots[pos] = 6
                                                pos += 1
                                        if specie2[x][yp][0] == 0:
                                                available_spots[pos] = 7
                                                pos += 1
                                        if specie2[xp][yp][0] == 0:
                                                available_spots[pos] = 8
                                                pos += 1
					if pos > 0:
                                                rand_pos=random.randint(0,pos-1)
                                                if random_number == 1:
                                                        if available_spots[rand_pos] == 1:
                                                                specie2[xm][y][0] = 1
                                                                specie2[xm][y][1] = SPECIE2_ENERGY_BASE
                                                        if available_spots[rand_pos] == 2:
                                                                specie2[xp][y][0] = 1
                                                                specie2[xp][y][1] = SPECIE2_ENERGY_BASE
                                                        if available_spots[rand_pos] == 3:
                                                                specie2[xm][ym][0] = 1
                                                                specie2[xm][ym][1] = SPECIE2_ENERGY_BASE
                                                        if available_spots[rand_pos] == 4:
                                                                specie2[x][ym][0] = 1
                                                                specie2[x][ym][1] = SPECIE2_ENERGY_BASE
                                                        if available_spots[rand_pos] == 5:
                                                                specie2[xp][ym][0] = 1
                                                                specie2[xp][ym][1] = SPECIE2_ENERGY_BASE
                                                        if available_spots[rand_pos] == 6:
                                                                specie2[xm][yp][0] = 1
                                                                specie2[xm][yp][1] = SPECIE2_ENERGY_BASE
                                                        if available_spots[rand_pos] == 7:
                                                                specie2[x][yp][0] = 1
                                                                specie2[x][yp][1] = SPECIE2_ENERGY_BASE
                                                        if available_spots[rand_pos] == 8:
                                                                specie2[xp][yp][0] = 1
                                                                specie2[xp][yp][1] = SPECIE2_ENERGY_BASE
				# die if too old
                                if specie2[x][y][0] > SPECIE2_LIFE_EXPECTANCY:
                                        specie2[x][y][1] = 0
                                        specie2[x][y][0] = 0
                        	specie2_individuals += 1
				specie2_energy += specie2[x][y][1]
			# if no individual is alive, random born to avoid extintion
                        if specie2[x][y][0] == 0 and specie2_neighbours == 0 and specie2[x][y][2] == 0 and ((specie2_last_individuals == 0 and specie2_individuals == 0 and real_mode == 1) or real_mode == 0):
                                random_number = random.randint(1,SPECIE2_RANDOM_BORN_CHANCES)
                                if random_number==1:
                                        specie2[x][y][0] = 1
                                        specie2[x][y][1] = SPECIE2_ENERGY_BASE
					specie2_individuals +=1
					specie2_energy += specie2[x][y][1]


			# draw
			if gradient_mode ==1:
				if plants[x][y][1]>255:
					white = (255,255,255)
				else:
					white = (plants[x][y][1],plants[x][y][1],plants[x][y][1])
				if specie1[x][y][1]>255:
					yellow = (255,255,0)
				else:
					yellow = (specie1[x][y][1],specie1[x][y][1],0)
				if specie2[x][y][1]>255:
					blue = (0,0,255)
				else:
					blue = (0,0,specie2[x][y][1])
				if specie1[x][y][1]+specie2[x][y][1]>255:
					magenta = (255,0,255)
				else:
					magenta = (specie1[x][y][1]+specie2[x][y][1],0,specie1[x][y][1]+specie2[x][y][1])

			if specie1[x][y][0] > 0 and specie2[x][y][0] > 0:
				pygame.draw.circle(screen,magenta,(((x*2*circle_size)+circle_size)+40,((y*2*circle_size)+circle_size)+40),circle_size,0)
			if specie1[x][y][0] > 0 and specie2[x][y][0] == 0:
                                pygame.draw.circle(screen,yellow,(((x*2*circle_size)+circle_size)+40,((y*2*circle_size)+circle_size)+40),circle_size,0)
			if specie1[x][y][0] == 0 and specie2[x][y][0] > 0:
                                pygame.draw.circle(screen,blue,(((x*2*circle_size)+circle_size)+40,((y*2*circle_size)+circle_size)+40),circle_size,0)
			if specie1[x][y][0] == 0 and specie2[x][y][0] == 0 and plants[x][y][0] > 0:
                                pygame.draw.circle(screen,white,(((x*2*circle_size)+circle_size)+40,((y*2*circle_size)+circle_size)+40),circle_size,0)
			if specie1[x][y][0] == 0 and specie2[x][y][0] == 0 and plants[x][y][0] == 0:
                                pygame.draw.circle(screen,darkgrey,(((x*2*circle_size)+circle_size)+40,((y*2*circle_size)+circle_size)+40),circle_size,0)

	if graph_mode == 1:
		# generate graphs
		for x in range(1,200):
			specie1_Iarray[x-1] = specie1_Iarray[x]
			specie2_Iarray[x-1] = specie2_Iarray[x]
			plants_Iarray[x-1] = plants_Iarray[x]
			specie1_Earray[x-1] = specie1_Earray[x]
			specie2_Earray[x-1] = specie2_Earray[x]
			plants_Earray[x-1] = plants_Earray[x]
		specie1_Iarray[199] = specie1_individuals
		specie2_Iarray[199] = specie2_individuals
		plants_Iarray[199] = plants_individuals
		specie1_Earray[199] = specie1_energy
		specie2_Earray[199] = specie2_energy
		plants_Earray[199] = plants_energy

		# draw graphs
		pygame.draw.line(screen,white,(450,350),(650,350))
		pygame.draw.line(screen,white,(650,350),(650,20))
		pygame.draw.line(screen,white,(700,350),(900,350))
		pygame.draw.line(screen,white,(900,350),(900,20))
		text_individuals = textfont.render("Individuals",False, lightgrey, black)
		text_energy = textfont.render("Energy",False, lightgrey, black)
		screen.blit(text_individuals,(480,400))
		screen.blit(text_energy,(740,400))

		for x in range(0,200):
			pygame.draw.line(screen,yellow,(450+x,350-int(specie1_Iarray[x]/3)),(450+x,350-int(specie1_Iarray[x]/3)))
			pygame.draw.line(screen,blue,(450+x,350-int(specie2_Iarray[x]/3)),(450+x,350-int(specie2_Iarray[x]/3)))
			pygame.draw.line(screen,white,(450+x,350-int(plants_Iarray[x]/3)),(450+x,350-int(plants_Iarray[x]/3)))
			pygame.draw.line(screen,yellow,(700+x,350-int(specie1_Earray[x]/500)),(700+x,350-int(specie1_Earray[x]/500)))
	        	pygame.draw.line(screen,blue,(700+x,350-int(specie2_Earray[x]/500)),(700+x,350-int(specie2_Earray[x]/500)))
	        	pygame.draw.line(screen,white,(700+x,350-int(plants_Earray[x]/500)),(700+x,350-int(plants_Earray[x]/500)))

	if graph_mode == 1:
		pygame.draw.rect(screen,lightgrey,(40,40,320,320),1)
	pygame.display.update()
