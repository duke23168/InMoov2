def gestureforlondon4():
  if i01.isNeopixelActivated():
    i01.setNeopixelAnimation("Color Wipe", 0, 20, 0, 1)
    sleep(2)
    i01.setNeopixelAnimation("Ironman", 0, 0, 255, 1)
  i01.startedGesture()
#welcome  
  i01.setHandVelocity("left", 19, 19, 19, 19, 19, 19)
  i01.setHandVelocity("right", 19, 36, 19, 19, 19, 19)
  i01.setArmVelocity("left", 19, 19, 19, 19)
  i01.setArmVelocity("right", 19, 19, 19, 19)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(0,90,90,50,65)
  i01.moveHead(0,90)
  i01.head.rollNeck.moveTo(90)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  sleep(5)
#welcome close hand
  i01.setHandVelocity("left", 59, 59, 59, 59, 59, -1)
  i01.setHandVelocity("right", 59, 59, 59, 59, 59, -1)
  i01.setArmVelocity("left", 19, 19, 19, 19)
  i01.setArmVelocity("right", 19, 19, 19, 19)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(0,40,25,40,65)
  i01.moveHead(0,40)
  i01.head.rollNeck.moveTo(50)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,180,180,180,180,90)
  sleep(3)
#welcome close hand 2
  i01.setHandVelocity("left", 59, 59, 59, 59, 59, -1)
  i01.setHandVelocity("right", 59, 59, 59, 59, 59, -1)
  i01.setArmVelocity("left", 19, 19, 19, 19)
  i01.setArmVelocity("right", 19, 19, 19, 19)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(0,40,25,40,65)
  i01.moveHead(0,120)
  i01.head.rollNeck.moveTo(120)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,180,180,180,180,90)
  sleep(3)
#welcome close hand3
  i01.setHandVelocity("left", 59, 59, 59, 59, 59, -1)
  i01.setHandVelocity("right", 59, 59, 59, 59, 59, -1)
  i01.setArmVelocity("left", 19, 19, 19, 19)
  i01.setArmVelocity("right", 19, 19, 19, 19)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(0,40,25,40,65)
  i01.moveHead(0,90)
  i01.head.rollNeck.moveTo(90)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,180,180,180,180,90)
  sleep(3)  
#davinci  
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  i01.head.rollNeck.moveTo(50)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(2)
#davinci turn wrist 1 
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  i01.head.rollNeck.moveTo(50)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",0,24,54,50,82,10)
  i01.moveTorso(95,90,90)
  sleep(1) 
#davinci turn wrist 2  
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",180,180,180,180,180,180)
  i01.moveTorso(95,90,90)
  sleep(2) 
#davinci turn wrist 3 
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",0,24,54,50,82,10)
  i01.moveTorso(95,90,90)
  sleep(1) 
#davinci  
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  i01.head.rollNeck.moveTo(90)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(1)
#davinci turn head close hand 1   
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(-1, -1)
  #i01.moveHead(46,160,130,40,65)
  i01.moveHead(46,160)
  i01.head.rollNeck.moveTo(120)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",180,180,180,180,180,10)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(2)
#davinci turn head close hand 2   
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(50, 50)
  i01.moveHead(46,160)
  #i01.moveHead(46,160,130,40,65)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",0,0,0,0,0,180)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(2)
#davinci turn head close hand 3   
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(50, 50)
  #i01.moveHead(46,160,130,40,65)
  i01.moveHead(46,160)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",180,180,180,180,180,10)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(2)         
#close hands and turn both wrist 
  #i01.moveHead(50,50,60,90,65)
  i01.moveHead(50,50)
  i01.head.rollNeck.moveTo(90)
  i01.moveArm("left",88,103,75,28)
  i01.moveArm("right",80,97,76,21)
  i01.moveHand("left",180,180,180,180,180,170)
  i01.moveHand("right",180,180,180,180,180,10)
  i01.moveTorso(90,90,90)   
  sleep(3)
#dab left  
  i01.setHandVelocity("left", 50.0, 50.0, 50.0, 50.0, 50.0, -1)
  i01.setHandVelocity("right", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(50.0, 50.0)
  i01.setTorsoVelocity(31.0, 31.0, -1)
  #i01.moveHead(79,160,120,90,65)
  i01.moveHead(79,160)
  i01.moveArm("left",5,84,32,78)
  i01.moveArm("right",87,82,123,74)
  i01.moveHand("left",0,0,0,0,0,25)
  i01.moveHand("right",0,0,0,0,0,113)
  i01.moveTorso(170,120,90)
  sleep(6)
#arms up and centered  
  i01.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  i01.setHandVelocity("right", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  i01.setArmVelocity("left", 50.0, 50.0, 50.0, 50.0)
  i01.setArmVelocity("right", 50.0, 50.0, 50.0, 50.0)
  i01.setHeadVelocity(36.0, 36.0)
  i01.setTorsoVelocity(31.0, 31.0, -1)
  #i01.moveHead(60,50,70,90,65)
  i01.moveHead(60,50)
  i01.moveArm("left",75,90,120,10)
  i01.moveArm("right",75,90,120,10)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",180,180,180,180,180,113)
  i01.moveTorso(90,90,90) 
  sleep(3)
#dab right
  i01.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  i01.setHandVelocity("right", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  i01.setArmVelocity("left", 50.0, 50.0, 50.0, 50.0)
  i01.setArmVelocity("right", 50.0, 50.0, 50.0, 50.0)
  i01.setHeadVelocity(36.0, 36.0)
  i01.setTorsoVelocity(31.0, 31.0, -1)  
  i01.moveHead(60,20)
  i01.moveArm("left",87,90,123,74)
  i01.moveArm("right",5,84,32,80)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(40,70,90)
  sleep(6)
#welcome  
  i01.setHandVelocity("left", 36, 36, 36, 36, 36, 36)
  i01.setHandVelocity("right", 36, 36, 36, 36, 36, 36)
  i01.setArmVelocity("left", 36, 36, 36, 36)
  i01.setArmVelocity("right", 36, 36, 36, 36)
  i01.setHeadVelocity(50, 50)
  i01.setTorsoVelocity(31.0, 31.0, -1)  
  #i01.moveHead(0,90,90,50,65)
  i01.moveHead(0,90)
  i01.moveArm("left",15,105,30,20)
  i01.moveArm("right",25,124,30,20)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  i01.moveTorso(90,90,90)
  sleep(5)
  i01.finishedGesture()
