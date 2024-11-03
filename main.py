from nav_template import create_navbar

try:
    demo = create_navbar() 
    demo.launch()
except Exception as e:
    print(f"Error launching the navbar: {str(e)}")  