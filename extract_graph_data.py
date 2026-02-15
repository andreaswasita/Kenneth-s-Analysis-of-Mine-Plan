"""
Graph Data Extraction Tool
This script helps extract data points from graphs in the IGO Limited Annual Report
(Page 28) and export them to CSV/Excel format.

Usage: python extract_graph_data.py
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import sys


class GraphDataExtractor:
    def __init__(self):
        self.graphs = {
            '1': 'Nickel Production (tonnes)',
            '2': 'Copper Production (tonnes)',
            '3': 'Ore Processing (tonnes)',
            '4': 'Recovery Rate (%)'
        }
        self.data = {graph: [] for graph in self.graphs.values()}
    
    def display_menu(self):
        print("\n" + "="*60)
        print("Graph Data Extraction Tool")
        print("="*60)
        print("\nAvailable Graphs:")
        for key, value in self.graphs.items():
            print(f"{key}. {value}")
        print("\nOptions:")
        print("A. Add data point")
        print("D. Display current data")
        print("E. Export to CSV")
        print("X. Export to Excel")
        print("R. Remove data point")
        print("Q. Quit")
        print("="*60)
    
    def add_data_point(self):
        print("\nSelect graph (1-4):")
        graph_choice = input("Graph number: ").strip()
        
        if graph_choice not in self.graphs:
            print("Invalid graph selection!")
            return
        
        graph_name = self.graphs[graph_choice]
        
        try:
            year = input("Enter year (e.g., 2024): ").strip()
            value = float(input(f"Enter value for {graph_name}: ").strip())
            
            self.data[graph_name].append({
                'Year': year,
                'Value': value
            })
            print(f"✓ Data point added to {graph_name}")
        except ValueError:
            print("Invalid value entered! Please enter a numeric value.")
    
    def display_data(self):
        print("\n" + "="*60)
        print("Current Data")
        print("="*60)
        
        for graph_name, points in self.data.items():
            if points:
                print(f"\n{graph_name}:")
                df = pd.DataFrame(points)
                print(df.to_string(index=False))
            else:
                print(f"\n{graph_name}: No data points yet")
    
    def export_to_csv(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for graph_name, points in self.data.items():
            if points:
                df = pd.DataFrame(points)
                filename = f"{graph_name.replace(' ', '_').replace('(', '').replace(')', '')}_{timestamp}.csv"
                df.to_csv(filename, index=False)
                print(f"✓ Exported {graph_name} to {filename}")
        
        print("\n✓ All data exported to CSV files!")
    
    def export_to_excel(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"mine_plan_data_{timestamp}.xlsx"
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            for graph_name, points in self.data.items():
                if points:
                    df = pd.DataFrame(points)
                    sheet_name = graph_name[:31]  # Excel sheet name limit
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"\n✓ All data exported to {filename}!")
    
    def remove_data_point(self):
        self.display_data()
        
        print("\nSelect graph (1-4):")
        graph_choice = input("Graph number: ").strip()
        
        if graph_choice not in self.graphs:
            print("Invalid graph selection!")
            return
        
        graph_name = self.graphs[graph_choice]
        
        if not self.data[graph_name]:
            print("No data points to remove!")
            return
        
        try:
            index = int(input(f"Enter index to remove (0-{len(self.data[graph_name])-1}): "))
            if 0 <= index < len(self.data[graph_name]):
                removed = self.data[graph_name].pop(index)
                print(f"✓ Removed: {removed}")
            else:
                print("Invalid index!")
        except (ValueError, IndexError):
            print("Invalid input!")
    
    def run(self):
        print("\nWelcome to the Graph Data Extraction Tool!")
        print("This tool helps you extract data from the IGO Limited Annual Report graphs.")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip().upper()
            
            if choice == 'A':
                self.add_data_point()
            elif choice == 'D':
                self.display_data()
            elif choice == 'E':
                self.export_to_csv()
            elif choice == 'X':
                self.export_to_excel()
            elif choice == 'R':
                self.remove_data_point()
            elif choice == 'Q':
                print("\nThank you for using the Graph Data Extraction Tool!")
                sys.exit(0)
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    extractor = GraphDataExtractor()
    extractor.run()