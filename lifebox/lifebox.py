import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640,480))

# colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
magenta = (255,0,255)
white = (255,255,255)
black = (0,0,0)

# fps management
clock = pygame.time.Clock()

# species matrix
t, w, h= 2,32, 32
# age 0 at z
# energy 1 at z
specie1 = [[[0 for x in range(t)] for y in range(h)] for z in range(w)]
specie2 = [[[0 for x in range(t)] for y in range(h)] for z in range(w)]
plants = [[[0 for x in range(t)] for y in range(h)] for z in range(w)]

# species variables

PLANTS_LIFE_EXPECTANCY = 100
PLANTS_RANDOM_BORN_CHANCES = 1000 # high is less chances
PLANTS_NEARBORN_CHANCES = 100
PLANTS_RANDOM_DIE_CHANCES = 2
PLANTS_ENERGY_BASE_PER_CYCLE = 5

#yellow
SPECIE1_LIFE_EXPECTANCY = 200
SPECIE1_RANDOM_BORN_CHANCES = 5000
SPECIE1_NEARBORN_CHANCES = 20
SPECIE1_RANDOM_DIE_CHANCES = 2
SPECIE1_ENERGY_BASE = 20
SPECIE1_ENERGY_NEEDED_PER_CYCLE = 2
SPECIE1_MAX_ENERGY_RECOLECTED_PER_CYCLE = 20
SPECIE1_ENERGY_TO_REPLICATE = 5

#blue
SPECIE2_LIFE_EXPECTANCY = 280
SPECIE2_RANDOM_BORN_CHANCES = 5000
SPECIE2_NEARBORN_CHANCES = 18
SPECIE2_RANDOM_DIE_CHANCES = 2
SPECIE2_ENERGY_BASE = 20
SPECIE2_ENERGY_NEEDED_PER_CYCLE = 2
SPECIE2_MAX_ENERGY_RECOLECTED_PER_CYCLE = 20
SPECIE2_ENERGY_TO_REPLICATE = 6

while (True):
	msElapsed = clock.tick(20)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
        		pygame.quit()
	 		sys.exit()

	for x in range(0,32):
		# adjacent coordinates
		xp = (x+1) & 31
		xm = (x-1) & 31
		for y in range(0,32):
			# calculations
			# adjacent coordinates
			yp = (y+1) & 31
			ym = (y-1) & 31
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
			# spontaneous generation
			if plants[x][y][0] == 0 and plants_neighbours == 0:
				random_number = random.randint(1,PLANTS_RANDOM_BORN_CHANCES)
				if random_number == 1:
					plants[x][y][0] = 1
					plants[x][y][1] = PLANTS_ENERGY_BASE_PER_CYCLE
			# plant reproduction
			if plants[x][y][0] == 0 and plants_neighbours > 0:
				random_number = random.randint(1,PLANTS_NEARBORN_CHANCES)
				if random_number == 1:
					plants[x][y][0] = 1
					plants[x][y][1] = PLANTS_ENERGY_BASE_PER_CYCLE

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
  				if specie1[x][y][1] > SPECIE1_ENERGY_TO_REPLICATE:
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
			# if no individual is alive, random born to avoid extintion
  			if specie1[x][y][0] == 0 and specie1_neighbours==0:
  				random_number = random.randint(1,SPECIE1_RANDOM_BORN_CHANCES)
  				if random_number==1:
					specie1[x][y][0] = 1
					specie1[x][y][1] = SPECIE1_ENERGY_BASE
					#print "("+str(x)+","+str(y)+") random born"

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
                                if specie2[x][y][1] > SPECIE2_ENERGY_TO_REPLICATE:
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
                        # if no individual is alive, random born to avoid extintion
                        if specie2[x][y][0] == 0 and specie2_neighbours == 0:
                                random_number = random.randint(1,SPECIE2_RANDOM_BORN_CHANCES)
                                if random_number==1:
                                        specie2[x][y][0] = 1
                                        specie2[x][y][1] = SPECIE2_ENERGY_BASE


			# draw
			if specie1[x][y][0] > 0 and specie2[x][y][0] > 0:
				pygame.draw.rect(screen,magenta,(x*10+10,y*10+10,10,10),0)
			if specie1[x][y][0] > 0 and specie2[x][y][0] == 0:
                                pygame.draw.rect(screen,yellow,(x*10+10,y*10+10,10,10),0)
			if specie1[x][y][0] == 0 and specie2[x][y][0] > 0:
                                pygame.draw.rect(screen,blue,(x*10+10,y*10+10,10,10),0)
			if specie1[x][y][0] == 0 and specie2[x][y][0] == 0 and plants[x][y][0] > 0:
                                pygame.draw.rect(screen,white,(x*10+10,y*10+10,10,10),0)
			if specie1[x][y][0] == 0 and specie2[x][y][0] == 0 and plants[x][y][0] == 0:
                                pygame.draw.rect(screen,black,(x*10+10,y*10+10,10,10),0)

	pygame.draw.rect(screen,white,(10,10,320,320),1)
	pygame.display.update()