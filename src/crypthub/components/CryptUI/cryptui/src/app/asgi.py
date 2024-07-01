
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from litestar import Litestar
    from litestar.contrib.jinja import JinjaTemplateEngine
    from litestar.template.config import TemplateConfig
    
def create_app() -> Litestar:
    """Create CryptUI Application"""
    
    from litestar import Litestar
    
    
    settings
    
    from pathlib import Path



    app = Litestar(
        route_handlers=[],
        template_config=TemplateConfig(
            directory=Path("templates"),
            engine=JinjaTemplateEngine,
        )
        
    return app 
)