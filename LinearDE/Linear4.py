%%manim -qm LagrangeMethodScene

from manim import *

class LagrangeMethodScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Solving via Lagrange Method (Variation of Parameters)", font_size=28, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Standard Form
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the standard linear ODE:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("y' + P(x)y = Q(x)")
        eq_orig.next_to(step1_text, DOWN, buff=0.4)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for the history corner
        hist_1 = eq_orig.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_1.to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        # Erase the center and show it in the corner simultaneously
        self.play(
            FadeOut(step1_text),
            FadeOut(eq_orig),
            FadeIn(hist_1, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 2: Associated Homogeneous Equation
        # ----------------------------------------------------------------
        step2_text = Tex("First, solve the complementary homogeneous equation ($Q(x)=0$):", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_homog = MathTex("y' + P(x)y = 0 \\implies y_h = C \\cdot e^{-\\int P(x)dx}")
        eq_homog.set_color(COLOR_HIGHLIGHT)
        eq_homog.next_to(step2_text, DOWN, buff=0.4).scale(0.9)

        self.play(Write(step2_text))
        self.play(FadeIn(eq_homog, shift=DOWN * 0.2))
        self.wait(2.5)

        # Create a scaled-down copy for history
        hist_2 = eq_homog.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.25).align_to(hist_1, LEFT)
        history.add(hist_2)

        self.play(
            FadeOut(step2_text),
            FadeOut(eq_homog),
            FadeIn(hist_2, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 3: Variation of Parameter
        # ----------------------------------------------------------------
        step3_text = Tex("Vary the constant: Replace $C$ with a function $C(x)$:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_vary = MathTex("y = C(x) \\cdot e^{-\\int P(x)dx}")
        eq_vary.set_color(COLOR_SUBST)
        eq_vary.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_vary, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_3 = eq_vary.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.25).align_to(hist_2, LEFT)
        history.add(hist_3)

        self.play(
            FadeOut(step3_text),
            FadeOut(eq_vary),
            FadeIn(hist_3, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 4: Differentiate and Substitute
        # ----------------------------------------------------------------
        step4_text = Tex("Differentiate $y$ and substitute back into the original ODE:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_sub_back = MathTex("C'(x)e^{-\\int Pdx} - C(x)P(x)e^{-\\int Pdx} + P(x)C(x)e^{-\\int Pdx} = Q(x)")
        eq_sub_back.next_to(step4_text, DOWN, buff=0.4).scale(0.7)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_sub_back, shift=DOWN * 0.2))
        self.wait(3)

        # Create a scaled-down copy for history
        hist_4 = eq_sub_back.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.25).align_to(hist_3, LEFT)
        history.add(hist_4)

        self.play(
            FadeOut(step4_text),
            FadeOut(eq_sub_back),
            FadeIn(hist_4, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 5: Find C'(x)
        # ----------------------------------------------------------------
        step5_text = Tex("Simplify (the terms with $C(x)$ always cancel out):", font_size=40)
        step5_text.move_to(UP * 1.8)

        eq_find_c = MathTex("C'(x)e^{-\\int P(x)dx} = Q(x) \\implies C'(x) = Q(x)e^{\\int P(x)dx}")
        eq_find_c.set_color(COLOR_HIGHLIGHT)
        eq_find_c.next_to(step5_text, DOWN, buff=0.4).scale(0.85)
        
        self.play(Write(step5_text))
        self.play(FadeIn(eq_find_c, shift=DOWN * 0.2))
        self.wait(2.5)

        # Create a scaled-down copy for history
        hist_5 = eq_find_c.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_5.next_to(hist_4, DOWN, buff=0.25).align_to(hist_4, LEFT)
        history.add(hist_5)

        self.play(
            FadeOut(step5_text),
            FadeOut(eq_find_c),
            FadeIn(hist_5, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 6: Conclusion
        # ----------------------------------------------------------------
        conclusion_text = Tex("Integrate $C'(x)$ to find $C(x)$ and write the final solution:", font_size=40)
        conclusion_text.set_color_by_tex("final solution", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("y = \\left( \\int Q(x)e^{\\int P(x)dx}dx + K \\right) e^{-\\int P(x)dx}")
        eq_final.set_color(COLOR_RESULT)
        eq_final.next_to(conclusion_text, DOWN, buff=0.4).scale(0.9)
        
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
