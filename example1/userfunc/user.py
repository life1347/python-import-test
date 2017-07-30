import sys
sys.path.append('.')
import yaml

document = """
  a: 1
  b:
    c: 3
    d: 4
"""

def main():
    return yaml.dump(yaml.load(document))

if __name__ == "__main__":
    print(main())
