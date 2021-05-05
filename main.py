from recommender import Recommender

system_constructor = Recommender()
system_constructor.fit_transform('data/RAW_interactions.csv', 'data/RAW_recipes.csv')
recipe_recommender = system_constructor.generator(50)

print(recipe_recommender.head(10))
