import pickle
favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "save.pkl", "wb" ) )
favorite_color_load = pickle.load( open( "save.pkl", "rb" ) )
favorite_color_load