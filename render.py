import pygame, os, random, time, finnhub

os.environ['SDL_VIDEO_WINDOW_POS'] = f"-2720,0" # REMOVE FOR SERVICE
fh_client = finnhub.Client(api_key="cvsppl9r01qhup0sap60cvsppl9r01qhup0sap6g")
pygame.font.init()
font = pygame.font.Font('SpaceMonoReg.ttf', 24)
window = pygame.display.set_mode((800,480), pygame.FULLSCREEN)

GREEN = (0, 255, 0)
RED = (255, 0, 0)

stocks = [
    "NVDA",  # NVIDIA Corporation
    "TSLA",  # Tesla Inc.
    "AAPL",  # Apple Inc.
    "AMZN",  # Amazon.com Inc.
    "MSFT",  # Microsoft Corporation
    "META",  # Meta Platforms Inc.
    "GOOG",  # Alphabet Inc. Class C
    "IMMR",  # Immersion Corporation
    "TSM",  # Taiwan Semiconductor Manufacturing
    "NFLX",  # Netflix Inc.
    "BAC",   # Bank of America Corporation
    "F",     # Ford Motor Company
    "INTC",  # Intel Corporation
    "JPM",   # JPMorgan Chase & Co.
    "UNH",   # UnitedHealth Group Incorporated
    "BTC",   # Bitcoin
    "ETH",   # Etherium
    "BA",    # Boeing Company
    "DIS",   # The Walt Disney Company
    "BABA",  # Alibaba Group Holding Limited
    "LVMUY"  # Sephora
]

names = [
    "NVIDIA",
    "Tesla",
    "Apple",
    "Amazon",
    "Microsoft",
    "Meta",
    "Google",
    "Immersion",
    "Taiwan Semi.",
    "Netflix",
    "BofA",
    "Ford",
    "Intel",
    "JPMorgan",
    "UnitedHealth",
    "Bitcoin",
    "Etherium",
    "Boeing",
    "Disney",
    "Alibaba",
    "Sephora"
]

    
RUN = False
def text(text, color, pos):
    window.blit(font.render(text, False, color), pos)


while True:
    window.fill((0,0,0))
    pygame.draw.line(window, (255,255,255), (0, 44), (800, 44), 4)
    text('Symbol', (255, 255, 255), (8, 8))
    text('Price', (255, 255, 255), (120, 8))
    text('Change', (255,255,255), (240, 8))
    text('Name', (255,255,255), (380, 8))
    for index, stock in enumerate(stocks):

        quote = fh_client.quote(stock)
    
        price = str(round(quote['c'],2)).zfill(5)
        change = '{:01.2f}'.format(round(quote['dp'],2))
        name = names[index]

        
        text(stock, (255, 255, 0), (8, (index * 20)+44))
        text(price, (255, 255, 255), (120, (index * 20)+44))
        text((' ' if not '-' in change else '') + change, RED if '-' in change else GREEN, (240, (index * 20)+44))
        text(name, (255, 255, 0), (380, (index * 20)+44))
    status = fh_client.market_status('US')
    is_open = status['isOpen']

    
    text(F'[Market is {"OPEN" if is_open else "CLOSED]"}', GREEN if is_open else RED, (532, 6))
    
    pygame.display.flip()
    time.sleep(30)
