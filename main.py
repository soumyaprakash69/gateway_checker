# main.py - Entry point for Pella.app deployment
# This file imports and runs the gateway_checker bot

# Import the necessary components from your existing bot file
from gateway_checker import app

# This is the standard entry point that Pella.app will look for
if __name__ == "__main__":
    # Run the Pyrogram client
    app.run()