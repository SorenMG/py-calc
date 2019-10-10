# Shell calculator
Have your own CAS-tool in your terminal!

# Features
- Integration
    - Indefinite integrals
    - Definite integrals
    - Partial integrals
    - Mixed partial integrals
    - Integral of n'th order
- Derivatives
    - Partial derivatives
    - Critical values
    - Derivative of n'th order
- Solving in an equation
- Support for trigonometric functions, pi and square root
- Equation evaluation

# Docs
The commands are structured, so you type a command and then the equation

```
COMMAND EQUATION
```

If you want to extract as much information out of your input, type in
```
wolf EQUATION
```
This will spit out everything it can find about your equation

## Integral
To find an indefinite integral simply put in
```
int EQUATION
```
And then it will find the indefinite integral among other things.

To find a definite integral simply type in
```
int EQUATION from START to END
```

Or to find an integral of a given order
```
int EQUATION order ORDER
```

## Derivative
To find the derivative and partial derivatives
```
diff EQUATION
```

To find a derivative of order
```
diff EQUATION order ORDER
```

## Solve
To solve for all given variables simply put int
```
solve EQUATION
```

## Evaluate
To evaluate simply put in your equation
```
eval EQUATION
```

# TODO
- Add support for linreg
- Add support for limit

# Contribution
To contribute, please submit a pull request 👏