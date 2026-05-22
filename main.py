import random
from fastmcp import FastMCP
mcp = FastMCP("expense tracker")

@mcp.tool
def rool_dice(n_dice : int=1)-> list[int]:
    """Roll n_dice 6-sided dice and return the results"""
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.tool
def add(a: float, b: float)->float:
    """adding two numbers a and b"""
    return a+b

if __name__ == "__main__":
    mcp.run()