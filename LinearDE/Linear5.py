%%manim -qm LinearVerificationScene

from manim import *

class LinearVerificationScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_CHECK = GREEN
        COLOR_HISTORY = GRAY_C
        COLOR_RESULT = GREEN

        # Title
        title = Text("Verifying First-Order Linear Equations", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Standard template info shown at top right to guide the viewer
        std_form = MathTex("y' + P(x)y = Q(x)", font_size=40, color=BLUE_A)
        std_form.to_edge(UR).shift(DOWN * 0.5)
        self.play(FadeIn(std_form))

        # Container for the history elements in the top-left corner
        history = VGroup()

        # Equations list to process with altered coefficients and functional forms
        # Every single equation remains perfectly first-order linear.
        equations = [
            {"orig": "3xy' + x^3y = 5x - 4", "std": "y' + \\frac{x^2}{3}y = \\frac{5x-4}{3x}"},
            {"orig": "y' - 4y = 0", "std": "y' - 4y = 0"},
            {"orig": "3y - y' + 2x = 0", "std": "y' - 3y = 2x"},
            {"orig": "y'\\sin x + 2xy = e^x", "std": "y' + \\frac{2x}{\\sin x}y = \\frac{e^x}{\\sin x}"},
            {"orig": "5x^3\\frac{dy}{dx} - 2x^2 = y", "std": "y' - \\frac{1}{5x^3}y = \\frac{2}{5x}"}
        ]

        for i, eq_data in enumerate(equations):
            step_num = i + 1
            
            # ----------------------------------------------------------------
            # PHASE 1: Consider the Equation
            # ----------------------------------------------------------------
            step_text = Tex(f"Equation {step_num}: Consider the equation:", font_size=40)
            step_text.move_to(UP * 1.8)
            
            eq_orig = MathTex(eq_data["orig"])
            eq_orig.next_to(step_text, DOWN, buff=0.4)
            
            self.play(Write(step_text))
            self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
            self.wait(1.5)

            # ----------------------------------------------------------------
            # PHASE 2: Rewrite to Standard Form
            # ----------------------------------------------------------------
            step_text_std = Tex(f"Equation {step_num}: Convert to canonical form $y' + P(x)y = Q(x)$:", font_size=40)
            step_text_std.move_to(UP * 1.8)
            
            eq_std = MathTex(eq_data["std"])
            eq_std.set_color(COLOR_HIGHLIGHT)
            eq_std.next_to(step_text_std, DOWN, buff=0.4)

            self.play(
                Transform(step_text, step_text_std),
                TransformMatchingShapes(eq_orig, eq_std)
            )
            self.wait(1.5)

            # ----------------------------------------------------------------
            # PHASE 3: Text Validation
            # ----------------------------------------------------------------
            check_text = Tex("Matches standard form perfectly!", font_size=40, color=COLOR_CHECK)
            check_text.move_to(DOWN * 1.2)
            
            # Display text label instead of a check mark graphic
            linear_label = Tex("It's linear!", font_size=40, color=COLOR_CHECK)
            linear_label.next_to(eq_std, RIGHT, buff=0.6)

            self.play(Write(check_text))
            self.play(FadeIn(linear_label, shift=RIGHT * 0.2))
            self.wait(2.0)

            # ----------------------------------------------------------------
            # PHASE 4: Move to Corner History
            # ----------------------------------------------------------------
            # Create a small compact record showing [Original Equation] ✓
            hist_item = MathTex(eq_data["orig"]).scale(0.5).set_color(COLOR_HISTORY)
            hist_check = Tex("$\\checkmark$", color=COLOR_CHECK).scale(0.7)
            hist_check.next_to(hist_item, RIGHT, buff=0.15)
            
            hist_group = VGroup(hist_item, hist_check)
            
            if len(history) == 0:
                hist_group.to_corner(UL).shift(DOWN * 1.2)
            else:
                hist_group.next_to(history[-1], DOWN, buff=0.2).align_to(history[-1], LEFT)
                
            history.add(hist_group)

            # Wipe the center completely clean to avoid any overlaps
            self.play(
                FadeOut(step_text),
                FadeOut(eq_std),
                FadeOut(check_text),
                FadeOut(linear_label),
                FadeIn(hist_group, shift=UP * 0.2)
            )
            self.wait(0.5)

        # Final Wrap-Up Screen
        final_text = Tex("All equations are confirmed to be \\textbf{Linear First-Order ODEs}!", font_size=40, color=COLOR_RESULT)
        final_text.move_to(ORIGIN)
        self.play(Write(final_text))
        self.wait(3.5)

        # Smooth terminal clean up
        self.play(
            FadeOut(title),
            FadeOut(std_form),
            FadeOut(final_text),
            FadeOut(history)
        )
        self.wait(1)
