def primo(n):
    for i in range(1, n):
        div=n/i
        if div == 0:
            print("nao é primo")
            break
        elif i == n-1 and div!=0:
            print(" é primo")
            
def main():
    nun = int(input("numero: "))
    primo(nun)

if(__name__ == "__main__"):
    main()