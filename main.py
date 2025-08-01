import argparse
from core.pipeline import Pipeline

def main():
    parser = argparse.ArgumentParser()
    
    # Add args in here
    parser.add_argument("--path", "-p", help="Enter your pipeline path here")
    
    # Take args
    path = parser.parse_args().path
        
    # Create pipeline class
    Pipeline(path)

if __name__ == "__main__":
    main()