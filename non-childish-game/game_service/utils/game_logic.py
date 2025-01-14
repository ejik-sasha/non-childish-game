import random
def level_up(character, experience_points):
    character.experience += experience_points
    required_exp = character.level * 100  # Пример: для каждого уровня требуется 100 * уровень опыта
    if character.experience >= required_exp:
        character.level += 1
        character.experience -= required_exp
        return True
    return False

def gather_resources(character, resource_type, base_amount):
    total_amount = base_amount + (character.gathering * 0.1)
    return total_amount

def build_base(resources, cost):
    for resource, amount in cost.items():
        if resources.get(resource, 0) < amount:
            return False 
    for resource, amount in cost.items():
        resources[resource] -= amount
    return True



def fight(player, opponent):
    while player.health > 0 and opponent.health > 0:
        # Атака игрока
        damage = player.level + player.agility + player.gathering + player.inlligence + random.randint(-5, 5)
        opponent.health -= damage

        if opponent.health <= 0:
            return "Player wins!"

        # Атака противника
        damage = opponent.level + opponent.agility + opponent.gathering + opponent.inlligence + random.randint(-5, 5)
        player.health -= damage

        if player.health <= 0:
            return "Opponent wins!"

