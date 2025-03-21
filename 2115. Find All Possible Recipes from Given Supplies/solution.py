from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_set = set(recipes)
        supplies_set = set(supplies)
        ingredients_dict = {recipes[i]: ingredients[i] for i in range(len(ingredients))}

        imposible_make = set()

        def dfs(recipe, visited):
            if recipe in supplies_set:
                return True
            if recipe in visited:
                return False
            if recipe not in recipes_set and recipe not in supplies_set:
                return False
            
            visited.add(recipe)
            for ingredient in ingredients_dict[recipe]:
                if ingredient not in supplies_set:
                    if not dfs(ingredient, visited):
                        imposible_make.add(recipe)
                        return False

            supplies_set.add(recipe)
            return True

        res = []
        for recipe in recipes:
            if recipe in supplies_set:
                res.append(recipe)
            elif recipe in imposible_make:
                continue
            else:
                if dfs(recipe, set()):
                    res.append(recipe)

        return res
