
from __future__ import annotations

from crypthub.components.CryptUI.cryptui.src.app.config.config import get_settings
from litestar import Litestar
from litestar.static_files.config import StaticFilesConfig
from typing import TYPE_CHECKING
from pathlib import Path

if TYPE_CHECKING:
    from litestar import Litestar
    


def create_app() -> Litestar:
    """_summary_
    
    Load Configuration
    Create Litestar App
    
    Returns:
        Litestar: _description_
    """
    
    
    settings = get_settings()
    
    app = Litestar(
        static_files_config=[
            StaticFilesConfig(
                directories=[
                    "css",
                    "js",
                    "images",
                ],
                path="/static",
                name="static",
            )
        ],
        route_handlers=[

            ],
        plugins=[
            
            ],
        **settings
    )
    
    return app