dict = ('omg':'oh my gawd',
         'l8r':'later',
         'ttyl':'talk to you later',
         'g9' : 'good night',
         'gtg': 'got to go',
         'ty': 'thank you',
         'smh': 'shaking my head'
         'lol': 'laughing out loud'
         'rofl': 'rolling on floor'
         'smol': 'small'
         'wow' : 'world of warcraft')

         translate_shorthand(phrases)

         story = """
         Stacy was texting. She said lol noobs suck smh. imo wow is better. are you going to gwcsip?
         """

         story_list = story.split(".")

         new_story_list = []
         # Go through each word of our story
         for word in story_list:
             if word in phrases.keys():
                 new_story_list.append(phrases[word])
                 # The word is NOT a shorthand
             else:
                 new_story_list.append(word)
            print(new_story_list)
            print(" ".join(new_story_list))
