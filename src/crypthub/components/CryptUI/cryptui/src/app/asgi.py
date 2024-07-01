
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from litestar import Litestar
    
    
def create_app() -> Litestar:
    """Create CryptUI Application"""
    