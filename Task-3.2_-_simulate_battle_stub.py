"""
Exercise 3.2: Simulate a Turn-Based Battle (Class-Based)

In this exercise, you will create a Pokemon class and use it to simulate battles.
This demonstrates object-oriented programming principles: encapsulation, methods, and clear responsibilities.
"""


'''Student Name: Hashim Ali
Student ID: 201967833'''


import httpx, json


class Pokemon:
    """
    Represents a Pokemon with stats fetched from the PokeAPI.
    """

    def __init__(self, name):
        """
        Initialise a Pokemon by fetching its data from the API and calculating its stats.

        Args:
            name (str): The name of the Pokemon (e.g., "pikachu")
        """
        # TODO: Store the Pokemon's name (lowercase)
        self.name = name.lower()
        # TODO: Fetch Pokemon data from PokeAPI
        # - Create the URL: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

        # - Make GET request
        # - Check response status code (raise error if not 200)
        # - Store the JSON data
        url =  f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        
        response = httpx.get(url)

        if response.status_code == 200:
            data = response.json()


            self.stats = {"attack":0, "defense":0, "speed": 0}
            self.max_hp = 0

            for stat in data['stats']:
                if stat['stat']['name'] == 'attack':
                    self.stats['attack'] = self._calculate_stat(stat['base_stat'])
                if stat['stat']['name'] == 'defense':
                    self.stats['defense'] = self._calculate_stat(stat['base_stat'])
                if stat['stat']['name'] == 'speed':
                    self.stats['speed'] = self._calculate_stat(stat['base_stat'])
                if stat['stat']['name'] == 'hp':
                    self.max_hp = self._calculate_hp(stat['base_stat'])    
            

            self.current_hp = self.max_hp

        else:
            return f"{self.name} is not a Pokemon!"

        # TODO: Calculate and store stats
        # - Use _calculate_stat() for attack, defense, speed
        # - Use _calculate_hp() for max HP
        # - Store stats in a dictionary
        # - Set current_hp = max_hp

    def _calculate_stat(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's stat at a given level.
        Helper method (note the underscore prefix).

        Args:
            base_stat (int): The base stat value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated stat        """
        # TODO: Implement the stat calculation formula
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

    def _calculate_hp(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's HP at a given level.
        HP uses a different formula than other stats.

        Args:
            base_stat (int): The base HP value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated HP
        """
        # TODO: Implement the HP calculation formula
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

    def attack(self, defender):
        """
        Attack another Pokemon, dealing damage based on stats.

        Args:
            defender (Pokemon): The Pokemon being attacked

        Returns:
            int: The amount of damage dealt
        """
        # TODO: Calculate damage using the damage formula
        damage = int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defender.stats['defense'] * 50)) + 2)
        # Where 50 is level and 60 is base_power

        # TODO: Make the defender take damage
        # Call defender.take_damage(damage)
        defender.take_damage(damage)
        # TODO: Return the damage amount
        return damage

    def take_damage(self, amount):
        """
        Reduce this Pokemon's HP by the damage amount.

        Args:
            amount (int): The damage to take
        """
        # TODO: Reduce current_hp by amount
        self.current_hp -= amount
        # Make sure HP doesn't go below 0
        if self.current_hp <= 0:
            self.current_hp = 0


    def is_fainted(self):
        """
        Check if this Pokemon has fainted (HP <= 0).

        Returns:
            bool: True if fainted, False otherwise
        """
        # TODO: Return True if current_hp <= 0, False otherwise
        if self.current_hp <= 0:
            return True
        else:
            return False

    def __str__(self):
        """
        String representation of the Pokemon for printing.

        Returns:
            str: A nice display of the Pokemon's name and HP
        """
        # TODO: Return a string like "Pikachu (HP: 95/120)"
        return f"{self.name.title()} (HP: {self.current_hp}/{self.max_hp})"



def simulate_battle(pokemon1_name, pokemon2_name):
    """
    Simulate a turn-based battle between two Pokemon.

    Args:
        pokemon1_name (str): Name of the first Pokemon
        pokemon2_name (str): Name of the second Pokemon
    """
    # TODO: Create two Pokemon objects
    pokemon1_name = Pokemon(pokemon1_name)
    pokemon2_name = Pokemon(pokemon2_name)
    # TODO: Display battle start message
    # Show both Pokemon names and initial HP
    print(f"""
Pokemon Battle
          
{pokemon1_name.name} V {pokemon2_name.name}  """)
    # TODO: Determine who attacks first based on speed
    # The Pokemon with higher speed goes first
    # Hint: Compare pokemon1.stats['speed'] with pokemon2.stats['speed']
    pokemon1_next = None
    pokemon2_next = None

    

    pokemon1_name_fainted = False
    pokemon2_name_fainted = False

    if pokemon1_name.stats['speed'] > pokemon2_name.stats['speed']:
        pokemon1_next = True
    else:
        pokemon2_next = True

    round = 1

    while pokemon1_name_fainted != True and pokemon2_name_fainted != True:
        
        print(f"Round {round}")

        if pokemon1_next == True:
            damage = pokemon1_name.attack(pokemon2_name)
            print(f"{pokemon2_name.name} took {damage}. Has {pokemon2_name.current_hp} left")
            pokemon2_name_fainted = pokemon2_name.is_fainted()
            round += 1
            pokemon2_next = True
            pokemon1_next = False
        elif pokemon2_next == True:
            damage = pokemon2_name.attack(pokemon1_name)
            print(f"{pokemon1_name.name} took {damage}. Has {pokemon1_name.current_hp} left")
            pokemon1_name_fainted = pokemon1_name.is_fainted()
            pokemon1_next = True
            pokemon2_next = False
            round += 1
    
    if pokemon2_name_fainted == True:
        print(f"""
{pokemon1_name.name} WON
Has {pokemon1_name.current_hp} left""")
    elif pokemon1_name_fainted == True:
        print(f"""
{pokemon2_name.name} WON
Has {pokemon2_name.current_hp} left""")

        

    # TODO: Battle loop
    # - Keep track of round number
    # - While neither Pokemon is fainted:
    #   - Display round number
    #   - Attacker attacks defender
    #   - Display damage and remaining HP
    #   - Check if defender fainted
    #   - If not, swap attacker and defender
    #   - Increment round number

    # TODO: Display battle result
    # Show which Pokemon won and their remaining HP


if __name__ == "__main__":
    # Test your battle simulator

    # Uncomment to test other battles:
    simulate_battle("eevee", "jigglypuff")