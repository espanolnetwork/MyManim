%%manim -qm NonLinearVerificationScene

from manim import *

class NonLinearVerificationScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_CROSS = RED
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Verifying Non-Linear Equations", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Standard template info shown at top right to guide the viewer
        std_form = MathTex("y' + P(x)y = Q(x)", font_size=40, color=BLUE_A)
        std_form.to_edge(UR).shift(DOWN * 0.5)
        self.play(FadeIn(std_form))

        # Container for the history elements in the top-left corner
        history = VGroup()

        # Modified equations list with altered coefficients and functional forms
        # Every single equation remains strictly non-linear.
        equations = [
            {"orig": "5xy' - 3x^3y^4 = e^x", "reason": "Contains $y^4$ term (degree $> 1$)"},
            {"orig": "y' + \\ln(y) = 2x", "reason": "Contains non-linear function $\\ln(y)$"},
            {"orig": "y^2 \\cdot y' + 4y = 9", "reason": "Contains product of $y^2$ and $y'$"},
            {"orig": "\\sqrt{y'} \\cos x - 2xy = 5", "reason": "Derivative is inside a non-linear square root"},
            {"orig": "3x^2\\frac{dy}{dx} + 7 = 8y^{-2}", "reason": "Contains negative power $y^{-2}$ (degree $\\neq 1$)"}
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
            # PHASE 2: Identify Non-Linear Component
            # ----------------------------------------------------------------
            step_text_reason = Tex(f"Equation {step_num}: Check against $y' + P(x)y = Q(x)$:", font_size=40)
            step_text_reason.move_to(UP * 1.8)
            
            reason_text = Tex(eq_data["reason"], font_size=36, color=COLOR_HIGHLIGHT)
            reason_text.next_to(eq_orig, DOWN, buff=0.4)

            self.play(Transform(step_text, step_text_reason))
            self.play(Write(reason_text))
            self.wait(1.5)

            # ----------------------------------------------------------------
            # PHASE 3: Cross Mark Validation (Not Linear)
            # ----------------------------------------------------------------
            fail_text = Tex("Violates standard linear structure!", font_size=40, color=COLOR_CROSS)
            fail_text.move_to(DOWN * 1.6)
            
            # Vector shape for a cross mark (X)
            crossmark = VGroup(
                Line(UP*0.3 + LEFT*0.3, DOWN*0.3 + RIGHT*0.3, stroke_width=6),
                Line(DOWN*0.3 + LEFT*0.3, UP*0.3 + RIGHT*0.3, stroke_width=6)
            ).set_color(COLOR_CROSS)
            crossmark.next_to(eq_orig, RIGHT, buff=0.6)

            self.play(Write(fail_text))
            self.play(FadeIn(crossmark, scale=0.5))
            self.wait(2.0)

            # ----------------------------------------------------------------
            # PHASE 4: Move to Corner History
            # ----------------------------------------------------------------
            # Create a small compact record showing [Equation] ✗
            hist_item = MathTex(eq_data["orig"]).scale(0.45).set_color(COLOR_HISTORY)
            hist_cross = Tex("$\\mathbf{\\times}$", color=COLOR_CROSS).scale(0.7)
            hist_cross.next_to(hist_item, RIGHT, buff=0.15)
            
            hist_group = VGroup(hist_item, hist_cross)
            
            if len(history) == 0:
                hist_group.to_corner(UL).shift(DOWN * 1.2)
            else:
                hist_group.next_to(history[-1], DOWN, buff=0.2).align_to(history[-1], LEFT)
                
            history.add(hist_group)

            # Wipe the center completely clean to avoid any overlaps
            self.play(
                FadeOut(step_text),
                FadeOut(eq_orig),
                FadeOut(reason_text),
                FadeOut(fail_text),
                FadeOut(crossmark),
                FadeIn(hist_group, shift=UP * 0.2)
            )
            self.wait(0.5)

        # Final Wrap-Up Screen
        final_text = Tex("All equations are confirmed to be \\textbf{Non-Linear}!", font_size=40, color=COLOR_CROSS)
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