from beanie import Document

from .player import PlayerTelegramCode
from app.handler import exceptions

class Item(Document):
    telegram_code: str
    item_id: int
    usage_limit: int = 1
    usage: int = 0
    quantity: int = 1
    async def use_item(self):
        if self.usage < self.usage_limit:
            self.usage += 1
        elif self.quantity > 0:
            self.quantity -= 1
            self.usage = 0
        else:
            raise exceptions.BrokenItemException()
        await self.save()
        return self        

    
class QueryItem(PlayerTelegramCode):
    item_id: int
    