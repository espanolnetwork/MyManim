%%manim -qm IntegratingFactorExampleScene

from manim import *

class IntegratingFactorExampleScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Solving via Integrating Factor", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Consider the Initial Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the given differential equation:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("(3xy + y^2)dx + (x^2 + xy)dy = 0")
        eq_orig.next_to(step1_text, DOWN, buff=0.4)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2.0)

        # Move Initial Equation to history
        hist_1 = eq_orig.copy().scale(0.5).to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        self.play(FadeOut(step1_text), FadeOut(eq_orig), FadeIn(hist_1, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 2: Verify Non-Exactness
        # ----------------------------------------------------------------
        step2_text = Tex("Check partial derivatives to verify exactness:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_check = MathTex(
            "\\frac{\\partial M}{\\partial y} = 3x + 2y",
            "\\quad \\neq \\quad",
            "\\frac{\\partial N}{\\partial x} = 2x + y"
        )
        eq_check.set_color(COLOR_HIGHLIGHT)
        eq_check.next_to(step2_text, DOWN, buff=0.4)
        
        self.play(Write(step2_text))
        self.play(FadeIn(eq_check, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 2 to history
        hist_2 = eq_check.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.2).align_to(hist_1, LEFT)
        history.add(hist_2)

        self.play(FadeOut(step2_text), FadeOut(eq_check), FadeIn(hist_2, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 3: Calculate the Integrating Factor μ(x)
        # ----------------------------------------------------------------
        step3_text = Tex("Find $\\mu(x)$ since $\\frac{M_y - N_x}{N}$ depends only on $x$:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_find_mu = MathTex(
            "\\frac{M_y - N_x}{N} = \\frac{(3x+2y) - (2x+y)}{x(x+y)} = \\frac{1}{x}",
            "\\implies \\mu(x) = e^{\\int \\frac{1}{x}dx} = x"
        )
        eq_find_mu.set_color(COLOR_SUBST)
        eq_find_mu.next_to(step3_text, DOWN, buff=0.4).scale(0.85)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_find_mu, shift=DOWN * 0.2))
        self.wait(3.0)

        # Move Step 3 to history
        hist_3 = eq_find_mu.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.2).align_to(hist_2, LEFT)
        history.add(hist_3)

        self.play(FadeOut(step3_text), FadeOut(eq_find_mu), FadeIn(hist_3, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 4: Multiply by μ(x) = x
        # ----------------------------------------------------------------
        step4_text = Tex("Multiply the original ODE by $\\mu(x) = x$ to make it exact:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_exact = MathTex("(3x^2y + xy^2)dx + (x^3 + x^2y)dy = 0")
        eq_exact.next_to(step4_text, DOWN, buff=0.4)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_exact, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 4 to history
        hist_4 = eq_exact.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.2).align_to(hist_3, LEFT)
        history.add(hist_4)

        self.play(FadeOut(step4_text), FadeOut(eq_exact), FadeIn(hist_4, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 5: Integrate New M with respect to x
        # ----------------------------------------------------------------
        step5_text = Tex("Integrate new $M(x,y)$ by $x$ to find potential function $U$:", font_size=40)
        step5_text.move_to(UP * 1.8)

        eq_integrate = MathTex("U(x,y) = \\int (3x^2y + xy^2)dx = x^3y + \\frac{1}{2}x^2y^2 + h(y)")
        eq_integrate.set_color(COLOR_HIGHLIGHT)
        eq_integrate.next_to(step5_text, DOWN, buff=0.4).scale(0.85)
        
        self.play(Write(step5_text))
        self.play(FadeIn(eq_integrate, shift=DOWN * 0.2))
        self.wait(3.0)

        # Move Step 5 to history
        hist_5 = eq_integrate.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_5.next_to(hist_4, DOWN, buff=0.2).align_to(hist_4, LEFT)
        history.add(hist_5)

        self.play(FadeOut(step5_text), FadeOut(eq_integrate), FadeIn(hist_5, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 6: Differentiate U by y to find h(y)
        # ----------------------------------------------------------------
        step6_text = Tex("Differentiate $U$ by $y$ and match with new $N(x,y)$:", font_size=40)
        step6_text.move_to(UP * 1.8)

        eq_find_h = MathTex(
            "\\frac{\\partial U}{\\partial y} = x^3 + x^2y + h'(y) = x^3 + x^2y",
            "\\implies h'(y) = 0 \\implies h(y) = 0"
        )
        eq_find_h.next_to(step6_text, DOWN, buff=0.4).scale(0.85)

        self.play(Write(step6_text))
        self.play(FadeIn(eq_find_h, shift=DOWN * 0.2))
        self.wait(3.0)

        # Move Step 6 to history
        hist_6 = eq_find_h.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_6.next_to(hist_5, DOWN, buff=0.2).align_to(hist_5, LEFT)
        history.add(hist_6)

        self.play(FadeOut(step6_text), FadeOut(eq_find_h), FadeIn(hist_6, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # FINAL STEP: Conclusion
        # ----------------------------------------------------------------
        conclusion_text = Tex("Set $U(x,y) = C$ to write the implicit \\textbf{general solution}:", font_size=40)
        conclusion_text.set_color_by_tex("general solution", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("x^3y + \\frac{1}{2}x^2y^2 = C")
        eq_final.set_color(COLOR_RESULT)
        eq_final.next_to(conclusion_text, DOWN, buff=0.4)
        
        box = SurroundingRectangle(eq_final, color=COLOR_RESULT, buff=0.2)
        
        self.play(Write(conclusion_text))
        self.play(FadeIn(eq_final, shift=DOWN * 0.2))
        self.play(Create(box))
        self.wait(4.0)

        # Final clean up
        self.play(
            FadeOut(title), FadeOut(conclusion_text), FadeOut(eq_final),
            box.animate.scale(0).move_to(eq_final.get_center()), FadeOut(history)
        )
        self.wait(1)