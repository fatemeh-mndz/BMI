def bmi(height,weight):
    x=round(weight/(height**2),2)
    return x
def main():
    height=float(input("Enter your height: "))
    weight=float(input("Enter your weight: "))
    x=bmi(height,weight)
    print(f"BMI:{x}")
    
    if x<18.5:
        result="You're skinny "
    elif x>=18.5:
        result="you're normal"
    elif x>=25 and x<30:
        result="You're overweight "
    else:
        return "you're fat"
    print(result)
if __name__=="__main__":
    main()