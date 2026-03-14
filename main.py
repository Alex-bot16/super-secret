"""Entry point – works both locally (python main.py) and in pygbag (browser)."""
import asyncio
import pygame
from game import Game
 
 
async def main():
    game = Game()
    await game.run()
 
 
asyncio.run(main())
 