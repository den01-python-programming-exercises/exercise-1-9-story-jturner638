def main():
    #write your code below this line
    print("I will tell you a story, but I need some information first.")
    name = input("What is the main character called?")
    job = input("What is their job?")

    print("Here is the story:")
    print("Once upon a time there was {}, who was {}.".format(name, job))
    print("On the way to work, {} reflected on life.".format(name))
    print("Perhaps {} will not be {} forever.".format(name, job))

if __name__ == '__main__':
    main()
