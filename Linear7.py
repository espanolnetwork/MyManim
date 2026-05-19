%%manim -qm BernoulliExampleSolutionScene

from manim import *

class BernoulliExampleSolutionScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Solving linear equation via Bernoulli Method", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Consider the Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the given linear ODE:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("y' - 2xy = e^{x^2}")
        eq_orig.next_to(step1_text, DOWN, buff=0.4)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2)

        # Move to history
        hist_1 = eq_orig.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_1.to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        self.play(FadeOut(step1_text), FadeOut(eq_orig), FadeIn(hist_1, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 2: Substitution
        # ----------------------------------------------------------------
        step2_text = Tex("Substitute $y = uv \\Rightarrow y' = u'v + uv'$:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_subst = MathTex("u'v + uv' - 2x(uv) = e^{x^2}")
        eq_subst.set_color_by_tex("uv", COLOR_SUBST)
        eq_subst.next_to(step2_text, DOWN, buff=0.4)

        self.play(Write(step2_text))
        self.play(FadeIn(eq_subst, shift=DOWN * 0.2))
        self.wait(2)

        # Move to history
        hist_2 = eq_subst.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.25).align_to(hist_1, LEFT)
        history.add(hist_2)

        self.play(FadeOut(step2_text), FadeOut(eq_subst), FadeIn(hist_2, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 3: Factoring Group
        # ----------------------------------------------------------------
        step3_text = Tex("Group terms containing the function $u$:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_factored = MathTex("u'v + u(v' - 2xv) = e^{x^2}")
        eq_factored.set_color_by_tex("v' - 2xv", COLOR_HIGHLIGHT)
        eq_factored.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_factored, shift=DOWN * 0.2))
        self.wait(2)

        # Move to history
        hist_3 = eq_factored.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.25).align_to(hist_2, LEFT)
        history.add(hist_3)

        self.play(FadeOut(step3_text), FadeOut(eq_factored), FadeIn(hist_3, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 4: Finding v
        # ----------------------------------------------------------------
        step4_text = Tex("Let $v' - 2xv = 0$ to find $v(x)$:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_find_v = MathTex("\\frac{dv}{v} = 2xdx \\implies \\ln|v| = x^2 \\implies v = e^{x^2}")
        eq_find_v.set_color(COLOR_HIGHLIGHT)
        eq_find_v.next_to(step4_text, DOWN, buff=0.4).scale(0.85)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_find_v, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move to history
        hist_4 = eq_find_v.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.25).align_to(hist_3, LEFT)
        history.add(hist_4)

        self.play(FadeOut(step4_text), FadeOut(eq_find_v), FadeIn(hist_4, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 5: Finding u
        # ----------------------------------------------------------------
        step5_text = Tex("Substitute $v = e^{x^2}$ back to solve for $u(x)$:", font_size=40)
        step5_text.move_to(UP * 1.8)

        eq_find_u = MathTex("u'(e^{x^2}) = e^{x^2} \\implies u' = 1 \\implies u = x + C")
        eq_find_u.set_color(COLOR_HIGHLIGHT)
        eq_find_u.next_to(step5_text, DOWN, buff=0.4).scale(0.85)
        
        self.play(Write(step5_text))
        self.play(FadeIn(eq_find_u, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move to history
        hist_5 = eq_find_u.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_5.next_to(hist_4, DOWN, buff=0.25).align_to(hist_4, LEFT)
        history.add(hist_5)

        self.play(FadeOut(step5_text), FadeOut(eq_find_u), FadeIn(hist_5, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 6: Conclusion
        # ----------------------------------------------------------------
        conclusion_text = Tex("Combine $u$ and $v$ for the general solution:", font_size=40)
        conclusion_text.set_color_by_tex("general solution", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("y = (x + C)e^{x^2}")
        eq_final.set_color(COLOR_RESULT)
        eq_final.next_to(conclusion_text, DOWN, buff=0.4)
        
        box = SurroundingRectangle(eq_final, color=COLOR_RESULT, buff=0.2)
        
        self.play(Write(conclusion_text))
        self.play(FadeIn(eq_final, shift=DOWN * 0.2))
        self.play(Create(box))
        self.wait(4)

        # Clean up
        self.play(
            FadeOut(title), FadeOut(conclusion_text), FadeOut(eq_final),
            box.animate.scale(0).move_to(eq_final.get_center()), FadeOut(history)
        )
        self.wait(1)
