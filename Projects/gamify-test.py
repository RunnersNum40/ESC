import gamify

#test 1
print("test 1 : 2")
gamify1.initialize()
gamify1.perform_activity("running", 1)
print(gamify1.get_cur_hedons())
print("**")

#test 2
print("test 2 : 0")
gamify1.initialize()
gamify1.perform_activity("running", 20)
print(gamify1.get_cur_hedons())
print("**")

#test 3
print("test 3 : 0")
gamify1.initialize()
gamify1.perform_activity("resting", 1)
print(gamify1.get_cur_hedons())
print("**")

#test 4
print("test 4 : 1")
gamify1.initialize()
gamify1.perform_activity("textbooks", 1)
print(gamify1.get_cur_hedons())
print("**")

#test 5
print("test 5 : 20")
gamify1.initialize()
gamify1.perform_activity("textbooks", 20)
print(gamify1.get_cur_hedons())
print("**")

#test 6
print("test 6 : 10")
gamify1.initialize()
gamify1.perform_activity("textbooks", 30)
print(gamify1.get_cur_hedons())
print("**")

#test 7
print("test 7 : 2,0")
gamify1.initialize()
gamify1.perform_activity("running", 1)
print(gamify1.get_cur_hedons())
gamify1.perform_activity("running", 1)
print(gamify1.get_cur_hedons())
print("**")

#test 8
print("test 8 : 2,2")
gamify1.initialize()
gamify1.perform_activity("running", 1)
print(gamify1.get_cur_hedons())
gamify1.perform_activity("resting", 1)
print(gamify1.get_cur_hedons())
print("**")


#test 9
print("test 9 : 150")
gamify1.initialize()
gamify1.perform_activity("running", 50)
print(gamify1.get_cur_health())
print("**")

#test 10
print("test 10 : 240")
gamify1.perform_activity("running", 30)
print(gamify1.get_cur_health())
print("**")

#test 11
print("test 11 : 540")
gamify1.perform_activity("running", 100)
print(gamify1.get_cur_health())
print("**")

#test 12
print("test 12 : 620")
gamify1.perform_activity("running", 80)
print(gamify1.get_cur_health())
print("**")

#test 13
print("test 13 : 810")
gamify1.perform_activity("running", 190)
print(gamify1.get_cur_health())
print("**")

#test 14
print("test 14 : 400")
gamify1.initialize()
gamify1.perform_activity("textbooks", 200)
print(gamify1.get_cur_health())
print("**")