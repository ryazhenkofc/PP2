# Made by Ten Dmitriy
from scipy.integrate import quad
import sympy as sp

def main():
    n = 4
    a, b = map( float, input("Enter the values for a and b: ").split())
    func_str = input("Please input the function as f(x)= ")
    
    x = sp.symbols('x')
    f = sp.sympify(func_str)
    
    step_size = (b - a) / n

    step_values = [a + i * step_size for i in range(n + 1)]
    func_values = [f.subs(x, step) for step in step_values]
    # I
    # A
    T = (step_size/2)*(func_values[0] + 2*sum(func_values[1:-1]) + func_values[-1])

    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)
    
    if f_double_prime.is_constant():
        M = f_double_prime.evalf()
    else:
        M = abs(f_double_prime.evalf(subs={x: a}) if f.subs(x, a) > f.subs(x, b) else f_double_prime.evalf(subs={x: b}))

    
    Et = (M * pow((b - a), 3))/(12 * pow(n, 2))
    # B
    f_lambda = sp.lambdify(x, f, modules=['numpy'])
    true_value, _ = quad(f_lambda, a, b) 
    
    # C
    C = (abs(true_value-T) / (true_value)) * 100
    
    # II
    S = (step_size/3)*(func_values[0] + 4*sum(func_values[1::2]) + 2*(sum(func_values[2::2])-func_values[-1]) + func_values[-1])

    f_third_prime = sp.diff(f_double_prime, x)
    f_fourth_prime = sp.diff(f_third_prime, x)
    if f_fourth_prime.is_constant():
        N = f_fourth_prime.evalf()
    else:
        N = abs(f_fourth_prime.evalf(subs={x: a}) if f.subs(x, a) > f.subs(x, b) else f_fourth_prime.evalf(subs={x: b}))
    Es = ((N*pow((b-a), 5))/(180*pow(n, 4)))
    D = (abs(true_value-S) / (true_value))*100

    print("n, a, b =", float(n), float(a), float(b))
    print("f(x) =", f)
    print("Step size =", float(step_size))
    print("I")
    print("---------------------")
    print("T =", float(T))    
    print("M =", float(M))
    print("Et =", float(Et))
    print("True value =", float(true_value))
    print("C =", float(C))
    print("II")
    print("---------------------")
    print("S =", float(S))
    print("M =", float(N))
    print("Es =", float(Es))
    print("True value =", float(true_value))
    print("C =", float(D))

if __name__ == "__main__":
    main()