import sys
def default():
    print("Hello")
def main():
    if sys.argv[1]=="wolf":
        print("wolf")
    elif sys.argv[1]=="cat":
        print("cat")
    else:
        default()
if __name__=="__main__":
    main()

