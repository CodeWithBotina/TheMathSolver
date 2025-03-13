from mathsolver.modules.induction import InductionHandler

class FormulaHandler:
    def process_formula(self, operation_type, formula):
        """Process the formula based on the selected operation."""
        if operation_type == "Induction":
            try:
                induction_handler = InductionHandler(formula)
                solution = induction_handler.solve_induction()
                return f"""
                <div class="system-message">
                    <b>MathSolver:</b> Here's the step-by-step solution:<br><br>
                    {solution}
                </div>
                """
            except Exception as e:
                return f"""
                <div class="system-message">
                    <b>MathSolver:</b> Error processing the formula: {e}
                </div>
                """
        else:
            return f"""
            <div class="system-message">
                <b>MathSolver:</b> Operation not supported yet.
            </div>
            """