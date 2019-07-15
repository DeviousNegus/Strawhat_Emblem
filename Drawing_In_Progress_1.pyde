size(1000,1000)
background(255,180,15)



ellipse(500, 430, 600, 600) # Top Half of Skull
fill(0,0,0)
ellipse(500, 550, 70, 70) # Nose
arc(350, 390, 200, 200, 0, PI+QUARTER_PI, OPEN) #L EYE
translate(650, 390)
rotate(-PI/4)
translate(-650, -390)
arc(650, 390, 200, 200, 0, PI+QUARTER_PI, OPEN)  #R EYE
translate(650, 390)
rotate(PI/4)
translate(-650, -390)


line(990, 290, 10, 290) # Hat Brim
fill(255,0,0)
rect(200,230,600,60) # Red-Stripe
fill(212,177,4)
rect(10,250,190,40)# L. Side Brim
rect(800,250,190,40)# R. Side Brim
rect(200,100,600,130)# Top of Strawhat

fill(255,255,255)
arc(500, 630, 450, 450, 0, PI) # Bottom Half of Skull

arc(500, 625, 340, 340, 0, PI, CHORD)
