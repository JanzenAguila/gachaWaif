from commands.base_command  import BaseCommand
from utils                  import get_emoji


rarities = ["1-star", "2-star", "3-star", "4-star", "5-star"]

# This is a convenient command that automatically generates a helpful
# message showing all available commands
class Spawn(BaseCommand):

    def __init__(self): 
        description = "Bot creator spawns a character of your choice."
        params = ["name", "rarity"]
        super().__init__(description, params)

    async def handle(self, *params):
        message = params[1]
        client = params[2]
        from message_handler import COMMAND_HANDLERS

        try:
            name = ""
            i = 0
            # print(params)
            while(params[0][i] not in rarities):
                name += params[0][i] + " "
                i += 1
            rarity = params[0][i]
        except ValueError:
            await message.channel.send("Missing name or rarity!")
            return
        except IndexError:
            await message.channel.send(f"{message.author.mention} Missing rarity!")
            return

        msg = get_emoji(":crown:") + f"You spawned a {rarity} {name}!"
        await message.channel.send(msg)
