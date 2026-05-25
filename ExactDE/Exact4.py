%%manim -qm IntegratingFactorTheoryScene

from manim import *

class IntegratingFactorTheoryScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Method of Integrating Factors", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Consider the Non-Exact Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider a non-exact differential equation:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("M(x, y)dx + N(x, y)dy = 0 \\quad \\text{where} \\quad \\frac{\\partial M}{\\partial y} \\neq \\frac{\\partial N}{\\partial x}")
        eq_orig.next_to(step1_text, DOWN, buff=0.4).scale(0.85)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Initial Equation to history
        hist_1 = eq_orig.copy().scale(0.5).to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        self.play(
            FadeOut(step1_text), 
            FadeOut(eq_orig), 
            FadeIn(hist_1, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 2: Introduce Integrating Factor
        # ----------------------------------------------------------------
        step2_text = Tex("Multiply by an integrating factor $\\mu$ to make it exact:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_mu = MathTex("\\mu M\\,dx + \\mu N\\,dy = 0")
        eq_mu.set_color(COLOR_SUBST)
        eq_mu.next_to(step2_text, DOWN, buff=0.4)
        
        self.play(Write(step2_text))
        self.play(FadeIn(eq_mu, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 2 to history
        hist_2 = eq_mu.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.2).align_to(hist_1, LEFT)
        history.add(hist_2)

        self.play(FadeOut(step2_text), FadeOut(eq_mu), FadeIn(hist_2, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 3: New Exactness Condition
        # ----------------------------------------------------------------
        step3_text = Tex("The new exactness condition requires:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_condition = MathTex("\\frac{\\partial}{\\partial y}(\\mu M) = \\frac{\\partial}{\\partial x}(\\mu N)")
        eq_condition.set_color(COLOR_HIGHLIGHT)
        eq_condition.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_condition, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 3 to history
        hist_3 = eq_condition.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.2).align_to(hist_2, LEFT)
        history.add(hist_3)

        self.play(FadeOut(step3_text), FadeOut(eq_condition), FadeIn(hist_3, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 4: Case 1 - μ depends only on x
        # ----------------------------------------------------------------
        step4_text = Tex("If $\\mu = \\mu(x)$, the condition simplifies to a separable ODE:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_case_x = MathTex("\\frac{1}{\\mu} \\frac{d\\mu}{dx} = \\frac{\\frac{\\partial M}{\\partial y} - \\frac{\\partial N}{\\partial x}}{N}")
        eq_case_x.next_to(step4_text, DOWN, buff=0.4)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_case_x, shift=DOWN * 0.2))
        self.wait(3.0)

        # Move Step 4 to history
        hist_4 = eq_case_x.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.2).align_to(hist_3, LEFT)
        history.add(hist_4)

        self.play(FadeOut(step4_text), FadeOut(eq_case_x), FadeIn(hist_4, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 5: Formula for μ(x)
        # ----------------------------------------------------------------
        conclusion_text = Tex("Integrating yields the formula for the \\textbf{integrating factor}:", font_size=40)
        conclusion_text.set_color_by_tex("integrating factor", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("\\mu(x) = e^{\\int \\frac{M_y - N_x}{N}\\,dx}")
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