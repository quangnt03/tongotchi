from beanie import Document
from pydantic import BaseModel
from app.handler import exceptions

class Item(Document):
    telegram_code: str
    item_id: int
    usage_limit: int = 1
    usage: int = 0
    quantity: int
    category: int
    specific_category: int
    def use_item(self):
        if self.usage < self.usage_limit:
            self.usage += 1
        elif self.quantity > 0:
            self.quantity -= 1
            self.usage = 0
        return self        

    
class QueryItem(BaseModel):
    telegram_code: str
    item_id: int
    pet_id: int | None = None

class QueryOnlyItem(BaseModel):
    telegram_code: str
    item_id: int
    quantity: int = 1
    