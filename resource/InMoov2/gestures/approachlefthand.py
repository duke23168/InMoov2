def approachlefthand():
  i01.startedGesture()
  i01.setHandSpeed("right", 31.0, 31.0, 31.0, 31.0, 31.0, 22.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 6.0, 6.0, 6.0, 6.0)
  i01.setHeadSpeed(22.0, 22.0)
  i01.setTorsoSpeed(31.0, 13.0, 100.0)
  i01.moveHead(20,84)
  i01.moveArm("left",67,52,62,23)
  i01.moveArm("right",55,61,45,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,85,90)
  sleep(4)
  i01.finishedGesture()

