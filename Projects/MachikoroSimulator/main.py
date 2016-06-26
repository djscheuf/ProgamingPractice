"""
Purpose: Main interaction point for User

Responsibilities:
+ Collect User input
+ Route to Simulator
+ Present Results
"""

#import tkinter as tk
import Infra.Simulator as Simulator
#import AiReader from Infra.AiReader

def routine():
    print("Machikoro Simulator v0.0")
    # Collect user input
    #aiFilename = tk.askopenfilename()
    gameCnt = 100#input("Please enter desired number of games > ")

    if(gameCnt < 0):
        print("Invalid number of games. Exiting.")
        return

    # Route to Simulator
    #aiList = AiReader(aifilename);
    aiList = {}
    simulation = Simulator.Simulator(aiList,gameCnt)

    print("Run Simulator")
    simulation.Run()

    results = simulation.Results
    # Present Results


if __name__ == "__main__":
    routine()
