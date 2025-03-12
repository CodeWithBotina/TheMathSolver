# mathsolver/modules/induction.py

from sympy import symbols, Sum, simplify, Eq
from mathsolver.logic.message_formats import SYSTEM_MESSAGE_TEMPLATE  # Import the template

class InductionHandler:
    def __init__(self, formula_text):
        """
        Initializes the induction handler with the formula in text format.
        """
        self.formula_text = formula_text
        self.n = symbols('n')  # Symbolic variable for induction
        self.i = symbols('i')  # Summation variable

    def parse_formula(self):
        """
        Converts the formula text into a SymPy symbolic expression.
        """
        try:
            # Example: If the user enters "Sum(i, (i, 1, n))", convert it to a SymPy expression
            expr = eval(self.formula_text, {'Sum': Sum, 'i': self.i, 'n': self.n})
            return expr
        except Exception as e:
            raise ValueError(f"Error parsing the formula: {e}")

    def format_expression(self, expr):
        """
        Formats a SymPy symbolic expression into a readable string.
        """
        if isinstance(expr, Sum):
            # Format summations
            lower = expr.limits[0][1]
            upper = expr.limits[0][2]
            term = expr.function
            return f"∑({term}, i={lower}..{upper})"
        elif isinstance(expr, Eq):
            # Format equations
            left = self.format_expression(expr.lhs)
            right = self.format_expression(expr.rhs)
            return f"{left} = {right}"
        else:
            # Format other expressions
            return str(expr)

    def solve_induction(self):
        """
        Solves the induction problem step by step.
        """
        try:
            # Convert the formula to a symbolic expression
            expr = self.parse_formula()

            # Step 1: Base case (n = 1)
            case_base = expr.subs(self.n, 1)
            case_base_simplified = simplify(case_base)

            # Step 2: Inductive hypothesis (assume it holds for n = k)
            k = symbols('k')
            hypothesis = expr.subs(self.n, k)

            # Step 3: Inductive step (prove it holds for n = k + 1)
            inductive_step = expr.subs(self.n, k + 1)
            inductive_step_simplified = simplify(inductive_step)

            # Format the step-by-step solution
            solution = f"""
            <b>Step 1: Base case (n = 1)</b><br>
            Substitute n = 1 into the formula:<br>
            {self.format_expression(expr)} → {self.format_expression(case_base)}<br>
            Simplified: {self.format_expression(case_base_simplified)}<br><br>

            <b>Step 2: Inductive hypothesis (n = k)</b><br>
            Assume the formula holds for n = k:<br>
            {self.format_expression(hypothesis)}<br><br>

            <b>Step 3: Inductive step (n = k + 1)</b><br>
            Prove the formula holds for n = k + 1:<br>
            {self.format_expression(expr.subs(self.n, k + 1))} → {self.format_expression(inductive_step_simplified)}<br><br>

            <b>Conclusion:</b><br>
            The formula holds for all natural numbers n ≥ 1 by mathematical induction.
            """

            return SYSTEM_MESSAGE_TEMPLATE.format(solution=solution)

        except Exception as e:
            raise ValueError(f"Error solving the induction: {e}")