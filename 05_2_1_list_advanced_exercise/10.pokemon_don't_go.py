def increase_decrease(pokemon_distances, removed_pokemon):
    # increasing value of the elements <= of the removed element
    for indx in range(len(pokemon_distances)):
        if pokemon_distances[indx] <= removed_pokemon:
            pokemon_distances[indx] += removed_pokemon
        elif pokemon_distances[indx] > removed_pokemon:
            pokemon_distances[indx] -= removed_pokemon

    return pokemon_distances


pokemon_distances = input().split()
removed_pokemon_counter = 0

while len(pokemon_distances) > 0:
    pokemon_index = int(input())
    # from list of strings to list of integers
    pokemon_distances = [int(ch) for ch in pokemon_distances]

    if pokemon_index > len(pokemon_distances) -1:
        # removing the last element of the list and copying the 1st one on it's place
        removed_pokemon = pokemon_distances.pop(-1)
        pokemon_distances.append(pokemon_distances[0])
        increase_decrease(pokemon_distances, removed_pokemon)
        removed_pokemon_counter += removed_pokemon

    elif pokemon_index < 0:
        # removing 1st element and copy last one to his place
        removed_pokemon = pokemon_distances.pop(0)
        pokemon_distances.insert(0, pokemon_distances[-1])
        increase_decrease(pokemon_distances, removed_pokemon)
        removed_pokemon_counter += removed_pokemon

    elif pokemon_index >= 0:
        # removing element on the given index
        removed_pokemon = pokemon_distances.pop(pokemon_index)
        increase_decrease(pokemon_distances, removed_pokemon)
        removed_pokemon_counter += removed_pokemon

print(removed_pokemon_counter)