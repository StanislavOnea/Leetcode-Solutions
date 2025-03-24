# Intuition
Intuition was to take one recipe and check if we can make it, if not try to run recursively the same logic on the igredient thant shoulb be assambled if all igredients arr in suply or can be made from supply then we can make this recipe.

# Approach
For each recipe check if the ingredients are available if not and the igredient is another recipe try to run the same recursive function and check if we can make it. Store the new recepies that can be made in a supply set so it will optimez future search if we will need it as ingredient. Also store the recepies that cannot be made to not try to process them again. Run this dfs on each recipe in the inpout array.

# Complexity
- Time complexity:
$$O(n + m)$$ - n nr of recepies, m ingredients.

- Space complexity:
$$O(n + m + k)$$ - n set of recepies, m set ofingredients, set of supplies.

# Code
```python3 []
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

```