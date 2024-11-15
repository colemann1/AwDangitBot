from easy_pil import Editor, Canvas, Font

pic = Editor(Canvas((710,890),color="#964B00")).rounded_corners(radius=40)
pic.paste(Editor(Canvas((690,870),color="#35654d")).rounded_corners(radius=30),(10,10))
pic.rectangle((40,40),630,310,outline="#ffffff")
pic.rectangle((45,45),620,300,outline="#ffffff")
#bottom rectangle
pic.rectangle((40,540),630,310,outline="#ffffff")
pic.rectangle((45,545),620,300,outline="#ffffff")
#cards = 190x270
#white ring 1 = 200x280
#white ring 2 = 210x290 
#Spacing = 40px                 290x370
#Border = 10px                  310x390
##20px-border,80px-spacing,10px-rings,card

pic.text(position=(355,360),text="Dealer's Value: 1/11+",align="center",color="#ffffff",font=Font.poppins(size=50))
pic.text(position=(355,480),text="Moore's Value: 13",align="center",color="#ffffff",font=Font.poppins(size=50))


# 1 card: 200
# 2 cards: 150 250
# 3 cards: 100 200 300
# 4 cards: 50 150 250 350
# 5 cards: 0 100 200 300 400
# plus 60 for offset

# #Tops


# pic.paste(Editor("imgs/K-H.png"), (60,60))
# pic.paste(Editor("imgs/Q-H.png"), (160,60))
# pic.paste(Editor("imgs/J-H.png"), (260,60))
# pic.paste(Editor("imgs/10-H.png"), (360,60))
# pic.paste(Editor("imgs/A-H.png"), (460,60))

# #Bottom
# pic.paste(Editor("imgs/K-H.png"), (60,560))
# pic.paste(Editor("imgs/Q-H.png"), (160,560))
# pic.paste(Editor("imgs/J-H.png"), (260,560))
# pic.paste(Editor("imgs/10-H.png"), (360,560))
# pic.paste(Editor("imgs/A-H.png"), (460,560))


pic.show()
#pic.save(fp="Background.png")